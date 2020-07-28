name = input('Имя: ')
surname = input('Фамилия: ')
age = int(input('Сколько вам лет: '))
weight = int(input('Какой ваш вес: '))

if age <= 30 and weight >= 50 and weight <= 120:
    print(name, surname, age, 'год', 'вес', weight, '- хорошее состояние')
elif age > 30 and age <= 40 and (weight < 50 or weight > 120):
    print(name, surname, age, 'год', 'вес', weight, '- необходимо вести прпавельный образ жизни')
elif age > 40 and (weight < 50 or weight > 120):
    print(name, surname, age, 'год', 'вес', weight, '- требуеться врчебный осмотр')
