
'''
Experimenting with creating GUI's in Python

I am using PySimpleGUI it seems to be a package of tools that make it easier to create GUIs. We shall see


Getting information from;
    https://realpython.com/pysimplegui-python/#getting-started-with-pysimplegui
    http://www.PySimpleGUI.org

    

'''

# # hello_world.py

# import PySimpleGUI as sg  # imports the needed libraries

# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read() # sg.Window() Starts the GUI



# hello_psg.py

import PySimpleGUI as sg
import subprocess
import sys

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")], [sg.Button("Run PowerShell Script")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

# while True:
    event, values = window.read()
    if event == "Run PowerShell Script" or event == sg.WIN_CLOSED:
        p = subprocess.Popen(["powershell.exe",
        "C:/Users/simpl/OneDrive/Documents/GitHub/PyShell/powershell/main.ps1"],
        stdout=sys.stdout)
        p.communicate()
        break

window.close()


