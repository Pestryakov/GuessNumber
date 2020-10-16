import random

x = random.randint(1, 100)
num = 0
count = 0

while True:
    num = int(input('Я загадал число от 1 до 100, попробуй угадай его c 7 попыток!\n'))
    count += 1
    if count == 7:
        print('Тебе не повезло! Все попытки закончились!')
        break
    elif num == x:
        print(f'Тебе повезло ты угадал число с {count} попытки!')
        if input('Не хочешь сыграть еще? "y|n"\n') == 'y':
            x = random.randint(1, 100)
            count = 0
        else:
            print('Спасибо за игру!')
            break
    elif num > x:
        print('Мое число меньше')
    else:
        print('Мое число больше!')
