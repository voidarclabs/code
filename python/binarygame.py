import random

score = 0

while True:
    number = random.randint(0, 7)
    binnumber = bin(number)
    print(binnumber)
    answer = input('In denary: ')
    if answer == 'exit':
        print('Your score was: ' + str(score))
        break
    elif int(answer) == number:
        print("That's right!")
        score = score + 1
    else:
        print('Oops! Better luck next time!')