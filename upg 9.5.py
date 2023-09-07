import os
ui_width = 30
anslagstavla = ''
while True:
    try:
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')

        print('.:STACKMASTER:. v1.33.7'.center(ui_width))
        print('-' * ui_width)

        lista =[]

        print(anslagstavla)
        print('-' * ui_width)
        print('| MENU |'.center(ui_width))
        print('-' * ui_width)
        print('push | Push element to stack\npull | Pull element from stack\nexit | Exit program')
        print('-' * ui_width)

        menu = input('MENU > ')
        if menu == 'push':
            print('-' * ui_width)
            item = input('ITEM > ')
            lista.append(item)
            for element in range(len(lista)):
                anslagstavla = lista[element]
            continue
        elif menu == 'pull':
            lista.pop()
        elif menu == 'exit':
            break
        else:
            raise Exception('FEL: Ange en korrekt input')
    except IndexError:
        print('FEL: Listan är tom, du kan inte använda pull på en tom lista.')
        input('tryck på enter för att fortsätta...')
    except Exception as e:
        print(e)
        input('tryck på enter för att fortsätta...')
