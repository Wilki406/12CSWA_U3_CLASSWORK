# Programmer: Benjamin Wilkinson
# Date: 01/02/2024
# Description: Starter GUI Program

import PySimpleGUI as sg

sg.theme("GreenTan")

layout = [[sg.Push(), sg.Text("Enter Text"), sg.Push()],
[sg.Push(), sg.Input(key="txt_input"), sg.Push()],
[sg.Push(), sg.Button("Ok"), sg.Button("Close"), sg.Push()],
[sg.Push(), sg.Text(key="counter"), sg.Push()]]

window = sg.Window("My First GUI", layout, icon='images/Limav-Flat-Gradient-Social-Twitter.512 (1).ico', size=(500,120))
counter = 0

while True:
event, values = window.read()
if event in (None, "Close"):
break
if event == "Ok":
counter += 1
print(f"Ok button clicker {counter} times.")
print("User typed in: " + values["txt_input"])
window["counter"].update(counter)

window.close()
