# import asyncio
# import time
#
#
# async def async_func():
#     print('Старт....')
#     await asyncio.sleep(3)
#     print('Готово....')
#
#
# async def main():
#     task = asyncio.create_task(async_func())
#     await task
#
# asyncio.run(main())




# import asyncio
#
#
# async def async_func(task_no):
#     print(f'...start {task_no}')
#     await asyncio.sleep(3)
#     print(f'...end {task_no}')
#
#
# async def main():
#     task1 = asyncio.create_task(async_func('A'))
#     task2 = asyncio.create_task(async_func('B'))
#     task3 = asyncio.create_task(async_func('C'))
#     await asyncio.wait([task1, task2, task3])
#
# if __name__ == '__main__':
#     asyncio.run(main())









# import time
#
# def brewCoffe():
#     print('Start brewCoffe()')
#     time.sleep(3)
#     print('Finish brewCoffe')
#     return 'Coffe is ready'
#
# def toastBage1():
#     print('Start toastBage1()')
#     time.sleep(3)
#     print('Finish toastBage1()')
#     return 'Toast is ready'
#
# def main ():
#     start = time.time()
#     result_coffee = brewCoffe()
#     result_toast = toastBage1()
#     end = time.time()
#
#     print(result_coffee)
#     print(result_toast)
#     print(f'spent time = {end - start:2f} seconds')
#
# main()







# import asyncio
# import http
#
# import httpx
#
#
# async def dowloand(current_activity):
#     url = f'https://reqres.in/api/users/{current_activity}'
#
#     async with httpx.AsyncClient() as client:
#         r = await client.get(url)
#         if r.status_code == 200:
#             _r = r.json()
#             print(_r.get('data'))
#         else:
#             print(r.status_code)
#         print(f'Рекомендую {current_activity}')
#
# async def main():
#     page_count = int(input('Сколько развлечений нужно ? '))
#
#     current_activity = 0
#     while current_activity < page_count:
#         current_activity += 1
#         await dowloand(current_activity)
#     print('Done')
#
#
# asyncio.run(main())








# 1
# import asyncio
# import time
#
# async def Plus(a, b):
#     print('Складывание началось.....')
#     await asyncio.sleep(3)
#     print(f'результат складывание', a + b)
#     return a + b
#
# async def kvadrat(a):
#     print('сложение квадратов началось.......')
#     await asyncio.sleep(4)
#     print('результат сложение квадратов', a**2)
#     return a**2
#
# async def main():
#     count = list()
#
#     task1 = asyncio.create_task(Plus(4,6))
#     task2 = asyncio.create_task(kvadrat(4))
#
#     await asyncio.gather(task1, task2)
#
# asyncio.run(main())










# 2
# import asyncio
#
# async def calls():
#     await asyncio.sleep(1)
#     print(f'Секретарь отвечает на звонки')
#     await asyncio.sleep(1)
#     print(f'Разговаривает по телефону')
#
# async def takes():
#     await asyncio.sleep(1)
#     print(f'Секретарь принимает людей')
#
# async def airlines():
#     await asyncio.sleep(1)
#     print(f'Бронирует билеты')
#
# async def graphics():
#     await asyncio.sleep(1)
#     print(f'контралирует график встреч')
#
# async def doktype():
#     await asyncio.sleep(1)
#     print(f'Запоняет документы')
#
# async def main():
#     task_list = [
#         calls(),
#         takes(),
#         airlines(),
#         graphics(),
#         doktype(),
#     ]
#     await asyncio.gather(*task_list)
#
# asyncio.run(main())