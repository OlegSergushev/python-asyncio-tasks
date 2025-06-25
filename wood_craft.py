import asyncio


wood_resources_dict = {
    "Деревянный меч": 6,
    "Деревянный щит": 12,
    "Деревянный стул": 24,
}

storage = 0


async def gather_wood(cond_storage, event_terminate):
    # Код по добыче 2ед древесины в секунду
    global storage
    while True:
        await asyncio.sleep(1)
        if event_terminate.is_set():
            break
        async with cond_storage:
            storage += 2
            print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
            cond_storage.notify()


async def craft_item(cond_storage, event_terminate):
    # Код изготовлению деревянных предметов
    global storage
    for item, resources in wood_resources_dict.items():
        async with cond_storage:
            await cond_storage.wait_for(lambda: resources <= storage)
            storage -= resources
            print(f"Изготовлен {item}.")
    event_terminate.set()


async def main():
    cond_storage = asyncio.Condition()
    event_terminate = asyncio.Event()
    await asyncio.gather(craft_item(cond_storage, event_terminate), gather_wood(cond_storage, event_terminate))
    

asyncio.run(main())
