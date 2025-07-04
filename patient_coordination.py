import asyncio

async def producer(queues, patient_info):
    for patient in patient_info:
        await asyncio.sleep(0.1)  # Имитация различной задержки регистрации
        if patient['direction'] == 'Терапевт':
            await queues['therapist'].put(patient)
        elif patient['direction'] == 'Хирург':
            await queues['surgeon'].put(patient)
        elif patient['direction'] == 'ЛОР':
            await queues['ent'].put(patient)
       
        print(f"Регистратор добавил в очередь: {patient['name']}, направление: {patient['direction']}, процедура: {patient['procedure']}")

async def consumer(queue, doctor_type):
    while True:
        patient = await queue.get()
        print(f"{doctor_type} принял пациента: {patient['name']}, процедура: {patient['procedure']}")
        await asyncio.sleep(0.5)  # Имитация времени на обслуживание пациента
        queue.task_done()

async def main():
    queues = {
        'therapist': asyncio.Queue(),
        'surgeon': asyncio.Queue(),
        'ent': asyncio.Queue()
    }

    patient_info = [
        {'name': 'Алексей Иванов', 'direction': 'Терапевт', 'procedure': 'Прием для общего осмотра'},
        {'name': 'Мария Петрова', 'direction': 'Хирург', 'procedure': 'Малая операция'},
        {'name': 'Ирина Сидорова', 'direction': 'ЛОР', 'procedure': 'Осмотр уха'},
        {'name': 'Владимир Кузнецов', 'direction': 'Терапевт', 'procedure': 'Консультация'},
        {'name': 'Елена Васильева', 'direction': 'Хирург', 'procedure': 'Хирургическая процедура'},
        {'name': 'Дмитрий Николаев', 'direction': 'ЛОР', 'procedure': 'Промывание носа'},
        {'name': 'Светлана Михайлова', 'direction': 'Терапевт', 'procedure': 'Рутинный осмотр'},
        {'name': 'Никита Алексеев', 'direction': 'Хирург', 'procedure': 'Операция на колене'},
        {'name': 'Ольга Сергеева', 'direction': 'ЛОР', 'procedure': 'Лечение ангины'},
        {'name': 'Анна Жукова', 'direction': 'Терапевт', 'procedure': 'Вакцинация'}
    ]

    # Запускаем потребителей для каждого типа врача
    consumers = [
        asyncio.create_task(consumer(queues['therapist'], 'Терапевт')),
        asyncio.create_task(consumer(queues['surgeon'], 'Хирург')),
        asyncio.create_task(consumer(queues['ent'], 'ЛОР'))
    ]

    # Запускаем производителя
    await producer(queues, patient_info)

    # Ожидаем обработки всех элементов в очередях
    for queue in queues.values():
        await queue.join()

    # Отменяем задачи потребителей
    for consumer_task in consumers:
        consumer_task.cancel()

asyncio.run(main())
