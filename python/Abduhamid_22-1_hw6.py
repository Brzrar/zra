
# 1 "Чётное-Нечётное"
# def even_odd(a):
#     if type(a) == int:
#         if a % 2 == 0:
#             return True
#         else:
#             return False
#     else:
#         return None
# print(even_odd(2))

# 2 "Правописание на минималках."
# def  is_right_sentence(x: str):
#      if x[0].istitle() and x[-1] == '.':
#           return x
#      else:
#           return ('Введите корректно! Пример:(Привет.) (Начинается с заглавной буквы и заканчивается точкой))')
# print(is_right_sentence('Hello.'))

# 3 "Среднее арифметическое"
# def arifmetic_mean(*n: int):
#      sum(n)
#      return sum(n)//len(n)
# print(arifmetic_mean(76, 95, 130))

# 4 "Ближайшее Число"
# def nearest_num(num, n_num):
#     found = num[0]
#     for item in num:
#         if abs(item - n_num) < abs(found - n_num):
#             found = item
#     return found
#
# print(nearest_num([5, 20.18, 103, 4], 27))