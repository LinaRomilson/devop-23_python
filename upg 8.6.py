todos = [
    'Städa',
    'Handla',
    'Plugga',
    'Ge blod'
]
print(todos)
while True:
    try:
        AngivenTodo = input('Ange todo: ')
        if AngivenTodo.strip() == '':
            raise ValueError()
        if AngivenTodo in todos:
            print(f"'{AngivenTodo}' finns i listan.")
        else:
            print(f"{AngivenTodo} finns inte i listan.")
            Svar = input('Vill du lägga till denna (J/N)? ')
            if Svar == 'J':
                todos.append(AngivenTodo)
                print('Todo tillagd!')
                print(todos)
                break
            elif Svar == 'N':
                print(todos)
                break
            else:
                print("FEL: ange ett svar (J/N)")

    except ValueError:
        print("FEL: Ange en todo")