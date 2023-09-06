todos = [
    'Städa',
    'Handla',
    'Plugga',
    'Ge blod'
]
print(todos)
while True:
    try:
        HämtadInfo = int(input('Ta bort todo (index):'))
        del todos[HämtadInfo]
        print(todos)
        break
    except ValueError:
        print("FEL: Mata in ett heltal")
    except IndexError:
        print("FEL: Ange ett befintligt index")