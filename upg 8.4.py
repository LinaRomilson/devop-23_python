todos = [
    'Städa',
    'Handla',
    'Plugga',
    'Ge blod'
]
print(todos)
while True:
    try:
        HämtadInfo = input('Ta bort todo (värde): ')
        todos.remove(HämtadInfo)
        print(todos)
        break
    except ValueError:
        print("FEL: Ange en befintlig todo\nINFO: Tänk på att todos är känsliga för stora och små bokstäver")
