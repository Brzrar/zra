num, num1, guess = 0, 101, 50
i = 0
user = input("Загадайте число (от 0 до 100): ")
while not(user.isdigit()):
 user = input("Загаданное вами число должно состоять из целых чисел: ")
with open('resultss.txt', 'w') as file:
 file.write(f"Попытки: ")
 while True:
  print(f"Загаданное вами число равно: {guess}?")
  file.write(f"{guess} ")
  otvet = input()
  i += 1
  if otvet == '>':
   num = guess
   guess = (num + num1) // 2
  elif otvet == '<':
   num1 = guess
   guess = (num + num1) // 2
  elif otvet.lower() == 'да':
   print('Я его угадал, ураааа!')
   file.write(f"\nКоличество попыток: {i}")
   break
  else:
   print(f"Если:\n\tЗагаданное число меньше {guess}, введите '<'"
     f"\n\tЗагаданное число больше {guess}, введите '>'"
     f"\n\tЗагаданное число равно {guess}, введите 'Да'")

 file.write(f"\nЗагаданное число: {guess}")