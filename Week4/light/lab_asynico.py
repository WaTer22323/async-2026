import asyncio
import time
from time import ctime
from lab_utils import control_light, reset_all_lights



async def main():
    STUDENT_ID = "6720301004"
    lights = ["light_1", "light_2", "light_3", "light_4"]
    reset_task = reset_all_lights(STUDENT_ID)
    reset_result = await reset_task
    print(f"{ctime()} | --- Reset all lights: {reset_result} ---")


    print(f"{ctime()} | --- Turning on lights sequentially (left to right) ---")
    start = time.perf_counter()

    tasks = [control_light(STUDENT_ID, light_id, "ON") for light_id in lights]
    results = await asyncio.gather(*tasks)

    for light_id, result in zip(lights, results):   
        print(f"{ctime()} | [{light_id}] -> {result}")

    end = time.perf_counter()
    print(f"{ctime()} | --- Total time: {end - start:.2f} seconds ---")

if __name__ == "__main__":
    asyncio.run(main())