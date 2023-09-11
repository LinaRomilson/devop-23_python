import json
import os

ui_width = 21

siffror = []

while True:
    #Rensa terminalen
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

    print('.: intMEMORIZER :.'.center(ui_width))
    print('*' * ui_width)
