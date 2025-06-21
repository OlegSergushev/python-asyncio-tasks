from random import randint
from itertools import product
import asyncio


shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]


async def launch_firework(color, shape, action):
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")


async def main():
    combinations = list(product(colors, shapes, actions))
    tasks = [asyncio.create_task(launch_firework(firework[0], firework[1], firework[2])) for firework in combinations]
    await asyncio.gather(*tasks)


asyncio.run(main())
