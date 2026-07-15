# lab_sequential.py
import asyncio
import time
from time import ctime
from lab_utils import control_light

async def main():
    STUDENT_ID = "6720301004"
    lights = ["light_1", "light_2", "light_3", "light_4"]

    print(f"{ctime()} | --- Turning on lights sequentially (left to right) ---")
    start = time.perf_counter()

    for light_id in lights:
        # await ทีละดวง -> ดวงถัดไปจะเริ่มก็ต่อเมื่อดวงก่อนหน้าทำเสร็จแล้วเท่านั้น
        result = await control_light(STUDENT_ID, light_id, "ON")
        print(f"{ctime()} | [{light_id}] -> {result}")

    elapsed = time.perf_counter() - start
    print(f"{ctime()} | Total time: {elapsed:.2f} seconds (should equal sum of all delays: 0.5+1.2+2.0+0.8 = 4.5s)")


if __name__ == "__main__":
    asyncio.run(main())