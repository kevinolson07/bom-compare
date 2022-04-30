import PySimpleGUI as sg
from bom_compare import *
import sys


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Browse for Bom 1'), sg.FileBrowse()],
            [sg.Text('Browse for Bom 2'), sg.FileBrowse()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)







if __name__ ==   "__main__":    
    while True:
        event, values = window.read()
        bom1 = values["Browse"]
        bom2 = values["Browse0"]
        # print(values["Browse"], values["Browse0"])
        # print()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        elif event == "Ok":
            old_bom, new_bom = selectBom(bom1, bom2)
            desc = descChange(old_bom, new_bom)
            qty = qtyChange(old_bom, new_bom)
            rev = revChange(old_bom, new_bom)
            rmPart = removeParts(old_bom, new_bom)
            addPart = addParts(old_bom, new_bom)
            # runCommand(cmd=values['_IN_'], window=window)
            sg.theme('DarkAmber')   # Add a touch of color
            # All the stuff inside your window.
            print(desc)
            layout = [  [sg.Text(desc)],
            [sg.Text(qty)],
            [sg.Text(rev)],
            [sg.Text(rmPart)]
             ]
            window = sg.Window('Window Title', layout)