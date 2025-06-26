import asyncio
import random

# Асинхронная функция для сканирования одного порта
async def scan_port(address, port):
    await asyncio.sleep(1)  # Имитация задержки для сетевого запроса
    if random.random() < 0.5:  # 50% шанс, что порт будет считаться открытым
        print(f"Порт {port} на адресе {address} открыт")  # Выводим сообщение о том, что порт открыт
        return port  # Возвращаем номер открытого порта
    else:
        return None  # Возвращаем None, если порт закрыт

# Асинхронная функция для сканирования диапазона портов
async def scan_range(address, start_port, end_port):
    print(f"Сканирование портов с {start_port} по {end_port} на адресе {address}")  # Информация о диапазоне сканирования
    tasks = []  # Список для хранения задач сканирования
    for port in range(start_port, end_port + 1):
        task = asyncio.create_task(scan_port(address, port))  # Создаем задачу для сканирования порта
        tasks.append(task)  # Добавляем задачу в список

    open_ports = []  # Список для хранения открытых портов
    results = await asyncio.gather(*tasks)  # Дожидаемся выполнения всех задач

    for port in results:
        if port is not None:  # Если порт открыт
            open_ports.append(port)  # Добавляем его в список открытых портов

    if len(open_ports) > 0:  # Если найдены открытые порты
        print(f"Открытые порты на адресе {address}: {open_ports}")  # Выводим их
    else:
        print(f"Открытых портов на адресе {address} не найдено")  # Иначе выводим, что открытых портов нет

# Основная асинхронная функция
async def main():
    address = "192.168.0.1"  # IP-адрес для сканирования
    start_port = 80  # Начальный порт диапазона
    end_port = 85  # Конечный порт диапазона
    await scan_range(address, start_port, end_port)  # Запуск функции сканирования

# Запуск асинхронного сканирования
asyncio.run(main())
