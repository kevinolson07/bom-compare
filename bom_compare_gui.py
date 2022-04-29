import PySimpleGUI as sg
import os.path
from bom_compare import *
import subprocess
import sys


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Browse for Bom 1'), sg.FileBrowse()],
            [sg.Text('Browse for Bom 2'), sg.FileBrowse()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs

# def runCommand(cmd, timeout=None, window=None):
#     p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     output = ''
#     for line in p.stdout:
#         line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
#         output += line
#         print(line)
#         window.Refresh() if window else None        # yes, a 1-line if, so shoot me
#     retval = p.wait(timeout)
#     return (retval, output)







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
            # runCommand(cmd=values['_IN_'], window=window)
            old_bom, new_bom = selectBom(bom1, bom2)
            descChange(old_bom, new_bom)
            qtyChange(old_bom, new_bom)
            revChange(old_bom, new_bom)
            # print("here")
            # print(output)
            # for i in output:
            #     [sg.Text(i)]
            removeParts(old_bom, new_bom)
            addParts(old_bom, new_bom)