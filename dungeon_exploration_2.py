import asyncio


players = {
    'DragonSlayer': 0.2,
    'ShadowHunter': 0.6,
    'MagicWizard': 0.8,
    'ElfArcher': 2.0,
    'DarkMage': 1.4,
    'SteelWarrior': 1.6,
    'ThunderBolt': 3.0}


async def enter_dungeon(player, time, barrier):
    await asyncio.sleep(time)
    print(f"{player} готов войти в подземелье")
    try:
        async with barrier:
            print(f"{player} вошел в подземелье")
    except asyncio.BrokenBarrierError:
        print(f"{player} не смог попасть в подземелье. Группа не собрана")


async def aborting_task(barrier):
    await asyncio.sleep(5)
    await barrier.reset()


async def main():
    barrier = asyncio.Barrier(5)
    tasks = [asyncio.create_task(enter_dungeon(player, time, barrier)) for player, time in players.items()] + [asyncio.create_task(aborting_task(barrier))]
    await asyncio.gather(*tasks)


asyncio.run(main())
