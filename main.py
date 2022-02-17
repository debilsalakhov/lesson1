name = input('VVEdite imadthyh: ')
age = int(input("Введите возраст: "))
name_letters = list(name)
not_space = True
for i in range(len(name_letters)):                  # задание 9, проверка на наличие пробелов в имени
    if name_letters[i] == ' ':
        not_space = False
if not_space and 0 <= int(age) <= 150:              # проверка на диапазон возраста, проверка на соответствие условиям
    if age < 18:
        print("Маловат еще;)")
    elif age < 30:
        print("Идеальный возраст")
    else:
        print("Старикашка")
    print('Меняем местами буквы в имени:', name[-2:0:-1] + name[-3:] + name[:5])  # задание 6
    print('Длина имени:', len(name))
    age = str(age)
    age = list(age)  # разделяем число на цифры (пока тип строки), задание 7
    for i in range(len(age)):  # меняем тип на целые числа
        age[i] = int(age[i])
    print('Сумма цифр:', sum(age))
    age_mult = 1
    for i in range(len(age)):  # перемножаем все цифры
        age_mult *= age[i]
    print("Произведение цифр возраста: ", age_mult)
    print('Меняем регистры букв в имени:', '\nЗаглавные:', name.upper(), '\nМаленькие:', name.lower(),
          '\nПервая большая:', name.capitalize(), '\nНаоборот:', name.capitalize().swapcase())  # задание 8
else:
    print('Введенные данные не соответствуют условиям!')
print('Решите выражение 8 * 9 + 94 / 2')
answer = int(input('Ответ: '))
if answer == 119:
    print('Абсолютно верно!')
else:
    print('Неверно, подумайте еще.')
