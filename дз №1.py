# Шаг 1 загадать случайное число +
import random

number = random.randint(1, 100)
# print(number)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выберите уровень сложности: '))
max_count = levels[level]

user_count = int(input('Введите кол пользоват: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя: {i}: ')
    users.append(user_name)

print(users)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Все проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        # шаг 2 предложить пользователю ввести число
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        # Шаг 3   сравнение результатов и ввывод числа
        elif number < user_number:
            print('ваше число больше загадонного')
        else:
            print('Ваше число меньше загадонного')

else:
    print(f'Победа ползьзователя: {winner_name}')
