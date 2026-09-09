import asyncio
import random
import json
import redis.asyncio as redis

# ⚙️ CONFIGURATION
REDIS_HOST = '172.16.46.79'     # IP ของ Redis Server 
GROUP_ID = 'g01'                 # เลขกลุ่ม
STUDENT_ID = '6720301004'        # รหัสนักศึกษาตนเอง

STREAM_KEY = f"f1:telemetry:{GROUP_ID}"
GROUP_NAME = "f1_pitwall"
CONSUMER_NAME = f"engineer_drs_controller_{STUDENT_ID}"
MAIN_DASHBOARD_CHANNEL = f"f1:dashboard:{GROUP_ID}" 

async def init_group(r: redis.Redis):
    try:
        await r.xgroup_create(STREAM_KEY, GROUP_NAME, id="$", mkstream=True)
    except redis.ResponseError as e:
        if "BUSYGROUP" not in str(e): raise e

async def drs_controller_worker():
    # ใช้ socket_keepalive เพื่อให้ส่งข้อมูลผ่าน Network ได้ต่อเนื่องเร็วที่สุด
    r = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True, socket_keepalive=True)
    await init_group(r)
    print(f"⚡ FAST DYNAMIC DRS Controller Ready... [Consumer: {CONSUMER_NAME}]")

    while True:
        try:
            # count=5 เพื่ออ่านข้อความเร็วขึ้น และ block=10 เพื่อให้ลูปทำงานต่อเนื่องทันที[cite: 7]
            entries = await r.xreadgroup(GROUP_NAME, CONSUMER_NAME, {STREAM_KEY: '>'}, count=5, block=10)
            if entries:
                msg_ids_to_ack = []
                for stream, msgs in entries:
                    for msg_id, data in msgs:
                        current_speed = float(data['speed'])
                        gear = int(data['gear'])
                        engine_temp = float(data.get('engine_temp', 100.0))
                        tire_wear = float(data.get('tire_wear', 0.0))
                        rpm = int(data.get('rpm', 10000))
                        distance = float(data.get('distance', 0.0))

                        # ⚡ สุ่มการเปลี่ยนแปลงความเร็วแบบเร่งขึ้น-ลง (-40.0 ถึง +80.0 km/h) ในทุกๆ รอบ
                        speed_change = round(random.uniform(-40.0, 80.0), 1)
                        calculated_speed = current_speed + speed_change
                        
                        # 🛑 คุมช่วงความเร็วให้อยู่ระหว่าง 180.0 - 330.0 km/h ไม่ให้หลุดขอบสนาม
                        final_speed = round(max(180.0, min(calculated_speed, 330.0)), 1)
                        
                        # กำหนดสถานะ DRS ตามการสุ่มเปลี่ยนความเร็ว
                        if speed_change > 0:
                            drs_status = "ENABLED"
                            print(f"🚀 [SPEED UP] {current_speed} -> {final_speed} km/h (+{speed_change})")
                        else:
                            drs_status = "DISABLED"
                            print(f"🔻 [SPEED DOWN] {current_speed} -> {final_speed} km/h ({speed_change})")

                        # แพ็กข้อมูลส่งออกไปยัง Dashboard[cite: 8, 10]
                        dashboard_payload = {
                            "group_id": GROUP_ID,
                            "student_id": STUDENT_ID,
                            "speed": final_speed,
                            "original_speed": current_speed,
                            "drs_status": drs_status,
                            "gear": gear,
                            "rpm": rpm,
                            "engine_temp": engine_temp,
                            "tire_wear": tire_wear,
                            "distance": distance
                        }

                        # 📡 Publish ขึ้น Dashboard ทันที[cite: 8, 10]
                        await r.publish(MAIN_DASHBOARD_CHANNEL, json.dumps(dashboard_payload))
                        msg_ids_to_ack.append(msg_id)

                # ⚡ACK รวดเดียวเพื่อประมวลผลได้ไวที่สุด (Batch ACK)[cite: 7]
                if msg_ids_to_ack:
                    await r.xack(STREAM_KEY, GROUP_NAME, *msg_ids_to_ack)

        except asyncio.CancelledError:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(drs_controller_worker())