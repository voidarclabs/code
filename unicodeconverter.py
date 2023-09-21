
while True:
    choice = input('char or num: ')
    if choice == 'exit':
        break
    else:
        pass
    char = input('input number: ')

    if choice == 'char':
        char = ord(char)
        print('unicode number is: ' + str(char))
    elif choice == 'num':
        char = chr(int(char))
        print('character is:' + str(char))
    elif choice == 'exit':
        break
    else:
        print('incorrect input')