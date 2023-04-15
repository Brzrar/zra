glas = "ауоыиэяюёеaeiouy"
while True:
    gls = 0
    sgl = 0
    kol = 0
    lang = input('\nВведите слово: (exit: выход)').strip().lower()
    if lang == 'exit':
        print('Программа завершена')
        break
    for i in lang:
        if i.isalpha():
            kol += 1
            if i in glas:
                gls += 1
            else:
                sgl += 1
    s = round((gls * 100) / kol, 2)
    a = round((sgl * 100) / kol, 2)
    print('Количество букв:', kol)
    print(f'Согласных букв: {sgl}')
    print(f'Гласных букв: {gls}')
    print(f'Гласные/Согласные {s}% / {a}%')








