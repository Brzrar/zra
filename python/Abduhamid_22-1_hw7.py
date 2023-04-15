# 1 "Ближайшее Число"
# def nearest_num(num, n_num=600):
#     return n_num, sorted(num, key=lambda x: abs(x - n_num))
# print(nearest_num([312, 996, 31, 1991], 1000))

# 2
# def iterable(x):
#     while True:
#         ind = input('Введите индекс: ').lower()
#         if ind == 'exit':
#             print('Функция завершена!')
#             break
#         try:
#             print(x[int(ind)])
#         except ValueError:
#                 print('только целые числа!')
#         except IndexError:
#                 print('Индекс может быть только от len(x) до len(x) -1')
# iterable(['hello', 'python', 18, 'Hallo_sir', 'java', 20])

# 3
# player = [{'name': 'Hamid', 'growth': 170, 'age': 17}, {'name': 'Sam', 'growth': 180, 'age': 20}]
#
# filter(lambda x: x['name'] == 'Hamid', player)  # Вернёт: [{'name': 'Hamid', 'growth': 170, 'age': 17}]


# player = [{'name': 'Hamid', 'growth': 170, 'age': 17}, {'name': 'Sam', 'growth': 180, 'age': 20}]
#
# map(lambda x: x['name'], player)  # Вернёт: ['Hamid', 'Sam']
