import random

x = random.randint(1, 100)
num = 0
count = 0
print('I made a number from 1 to 100, try to guess it with 7 attempts')
while True:
    num = int(input('Enter a number!\n'))
    count += 1
    if count == 7:
        print("You're out of luck! All attempts are over!")
        break
    elif num == x:
        print(f'You were lucky you guessed the number with {count} attempts!')
        if input('Do you want to play again? "y|n"\n') == 'y':
            x = random.randint(1, 100)
            count = 0
        else:
            print('Thank you for playing!')
            break
    elif num > x:
        print('My number is less than!')
    else:
        print('My number is higher!')
