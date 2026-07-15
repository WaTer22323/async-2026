# lab_utils.py
import httpx

BASE_URL = "http://172.16.2.117:8088"

async def control_light(student_id: str, light_id: str, status: str) -> dict:
    """เปิด/ปิดไฟดวงเดียว (status = 'ON' หรือ 'OFF')"""
    url = f"{BASE_URL}/api/{student_id}/lights/{light_id}"
    payload = {"status": status}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, timeout=10.0)
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "ERROR", "detail": f"HTTP Error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"status": "ERROR", "detail": f"Connection failed: {e}"}
    
async def reset_all_lights(student_id: str) -> dict:
    """รีเซ็ตไฟทั้งหมดของ student_id นี้กลับเป็น OFF (เหมือนกดปุ่ม Reset บนเว็บ)"""
    url = f"{BASE_URL}/api/{student_id}/lights/reset"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, timeout=10.0)
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "ERROR", "detail": f"HTTP Error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"status": "ERROR", "detail": f"Connection failed: {e}"}