import asyncio


# принимает на вход текст поста и имитирует публикацию нового поста на блоге Васи
async def publish_post(text):
    await asyncio.sleep(1)
    print(f"Пост опубликован: {text}")
    return text


# принимает на вход список подписчиков и имитирует отправку уведомления каждому подписчику
async def notify_subscribers(subscribers):
    tasks = []
    for subscriber in subscribers:
        task = asyncio.create_task(asyncio.sleep(1), name=subscriber)
        task.add_done_callback(callback(subscriber))
        tasks.append(task)
    await asyncio.gather(*tasks)


def callback(subscriber):
    print(f"Уведомление отправлено {subscriber}")
    return subscriber


async def main():
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    task1 = asyncio.create_task(publish_post(post_text))
    task2 = asyncio.create_task(notify_subscribers(subscribers))
    await task1
    await task2


asyncio.run(main())
