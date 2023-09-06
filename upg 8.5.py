todos = [
    'Städa',
    'Handla',
    'Plugga',
    'Ge blod'
]
print(todos)
while True:
    try:
        HämtadInfo = input('Lägg till todo: ')
        if HämtadInfo.strip() == '':
            raise ValueError('FEL: Mata in minst ett tecken')
        todos.append(HämtadInfo)
        sorted_todos = sorted(todos, key=str.lower)
        print(sorted_todos)
        break
    except ValueError as error:
        print(error)
