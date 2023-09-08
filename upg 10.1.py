import os

if os.path.exists('sign.txt'):
    f = open('sign.txt', 'a')
else:
    f = open('sign.txt', 'x')

textskylt = ''
while True:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    try:
        print('`\n|-----------------------------------------|')
        print('|  #  -----------------------       #     |')
        print('| ### | ', textskylt.center(18), '|  #   ###    |')
        print('| ### ----------------------- ###  ###    |')
        print('|   |        |        |        |    |   # |')
        print('|-----------------------------------------|')
        print('| C | Change sign message')
        print('| E | Exit program')
        print('|-------------------------')

        menu = input('| > ')
        print('|-------------------------')
        if menu == 'C':
            textskylt = input('| Enter new message: \n| > ')
            f.write(textskylt + '\n')
        elif menu == 'E':
            break
        else:
            raise Exception('| ERROR: Enter a valid command')
        if textskylt.strip() == "":
            raise ValueError('| ERROR: Unknown command')
    except ValueError as d:
        print(d)
        input('| Press enter to continue...')
    except Exception as e:
        print(e)
        input('| Press enter to continue...')

f.close()
