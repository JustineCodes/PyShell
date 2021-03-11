
'''
Experimenting with creating GUI's in Python

I am using PySimpleGUI it seems to be a package of tools that make it easier to create GUIs. We shall see


Getting information from;
    https://realpython.com/pysimplegui-python/#getting-started-with-pysimplegui
    http://www.PySimpleGUI.org

    
I can grab an event from the user in a Python GUI and use it to trigger the PowerShell script.
    Nice step in the proccess.

Next up
    How to take stdin from the Python GUI and pass it to the PowerShell script.
    
'''

# # hello_world.py

# import PySimpleGUI as sg  # imports the needed libraries

# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read() # sg.Window() Starts the GUI



# hello_psg.py

import PySimpleGUI as sg
import subprocess
import sys

sg.theme('BrightColors')


layout = [[sg.Text("PyShell")],
         [sg.Button("type Something"), sg.Input(key='-IN-')],
         [sg.Text(size=(12,1), key='-OUTPUT-')],
         [(sg.Button("reset"))],
         [sg.Button("Run PowerShell Script")] ]

# Create the window
window = sg.Window("PyShell", layout)

# Create an event loop
while True:
    event, values = window.read()
    print(event, values)
    # End program if user closes window or
    # presses the OK button

    if event == "Run PowerShell Script": # or event == sg.WIN_CLOSED:
        p = subprocess.run(["powershell.exe",
        "C:/Users/simpl/OneDrive/Documents/GitHub/PyShell/powershell/main.ps1"],
        stdout=sys.stdout)

    if event == "type Something":
        window['-OUTPUT-'].update(values['-IN-'])

    if event == "reset":
        window['-OUTPUT-']('')

    if event == sg.WIN_CLOSED or event == 'Exit': # This closes the GUI. Adding here keeps it open.
        break
 
    




