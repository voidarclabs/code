def choice1func():
    choice1 = input('bin, den or hex? ')
    if choice1 == 'exit':
        exit()
    else:
        choice2(choice1)

def choice2(choice1):
    choice2 = input('bin, den or hex? ')
    if choice2 == 'exit':
        exit()
    elif choice1 == 'bin':
        if choice2 == 'bin':
            num1 = input('input number: ')
            same(num1)
        elif choice2 == 'den':
            num1 = input('Input number: ')
            bintoden(num1)
        elif choice2 == 'hex':
            num1 = input('input number: ')
            bintohex(num1)
        else:
            print('invalid unit.')
    elif choice1 == 'den':
        if choice2 == 'bin':
            num1 = input('input number: ')
            dentobin(num1)
        elif choice2 == 'den':
            num1 = input('Input number: ')
            same(num1)
        elif choice2 == 'hex':
            num1 = input('input number: ')
            dentohex(num1)
    elif choice1 == 'hex':
        if choice2 == 'bin':
            num1 = input('input number: ')
            hextobin(num1)
        elif choice2 == 'den':
            num1 = input('Input number: ')
            hextoden(num1)
        elif choice2 == 'hex':
            num1 = input('input number: ')
            same(num1)
    else:
        print('invalid choice...')
        choice1func()
    
def dentobin(num1):
    num = bin(int(num1))
    num = num.split('b')
    print(num[1])

def bintoden(num1):
    num = int(num1, 2)
    print('\nConverted number: ' + str(num))

def dentohex(num1):
    num = hex(int(num1))
    num = num.split('x')
    print('\nConverted number: ' + str(num[1]))

def hextoden(num1):
    num = int(num1, 16)
    print(num)

def bintohex(num1):
    num = int(num1, 2)
    num = hex(num)
    num = num.split('x')
    print('\nConverted number: ' + str(num[1]))
    
def hextobin(num1):
    num = int(num1, 16)
    num = bin(num)
    num = num.split('b')
    print(num[1])
    
def same(num1):
    print('\nConverted number: ' + num1)


def main():
    while True:
        choice1func()
        exit = input('exit? (y/n): ')
        if exit == 'y':
            print('exiting...')
            break
        else:
            pass