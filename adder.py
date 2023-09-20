num1 = input('Number 1: ')
num2 = input('Number 2: ')

num1den = int(num1, 2)
num2den = int(num2, 2)

answer = num1den + num2den

answer = bin(answer)
answersplit = answer.split('x')
answerbin = answersplit[1]

print('\n' + answerbin + '\n')