# Programmer: Benjamin
# Date: 08/02/2024
# Description: Temperature Calculation GUI Program

import PySimpleGUI as sg

# calculation function
def calTemp(Value1,Value2):
addTemp = Value1 + Value2
finalTemp = str(round(addTemp / 2, 2))
return finalTemp

# set the theme
sg.theme("BrightColors")

# laid out elements
layout = [[sg.Combo(['°C','°F'], key='tester',default_value="°C")],
[sg.Text("Enter Miniumum Temperature Value"), sg.Push()],
[sg.Input(key="txt_temp1"), sg.Push()],
[sg.Text("Enter Maximum Temperature Value"), sg.Push()],
[sg.Input(key="txt_temp2"), sg.Push()],
[sg.Button("Ok"), sg.Button("Close"), sg.Push()],
[sg.Text("Average Temp: ", key="score"),],]

# name and create window
window = sg.Window("Average Temp Calculator", layout, icon='', size=(400,300))

# predefine datatypes
counter = 0
temperatures = ['C', 'F']
FirstTemp = 0
SecondTemp = 0

# window while loop
while True:
event, values = window.read()

if event in (None, "Close"):
break

if event == "Ok":
try:
FirstTemp = float(values["txt_temp1"])
SecondTemp = float(values["txt_temp2"])

if str(values["tester"]) == "°C":
window["score"].update(f"Average Temp: {calTemp(FirstTemp, SecondTemp)} °C")

if str(values["tester"]) == "°F":
window["score"].update(f"Average Temp: {calTemp(FirstTemp, SecondTemp)} °F")

if FirstTemp > SecondTemp:
window["score"].update("Minimum temp must be smaller than maximum temp")



except ValueError:
window["score"].update("Please enter integers")


window.close()
