# Programmer: Benjamin Wilkinson
# Date: 02/02/2024
# Description: AFL Calculation GUI Program

import PySimpleGUI as sg

def calculateTotalScore(goals, behinds):
goalScore = goals * 6 + behinds
return goalScore

sg.theme("Topanga")

layout = [[sg.Text("Enter Goals"), sg.Push()],
[sg.Input(key="txt_goals"), sg.Push()],
[sg.Text("Enter Behinds"), sg.Push()],
[sg.Input(key="txt_behinds"), sg.Push()],
[sg.Button("Ok"), sg.Button("Close"), sg.Push()],
[sg.Text("Score:", key="score"),]]

window = sg.Window("AFL SCORE CALCULATOR", layout, icon='images/Australian_Football_League.svg.ico', size=(320,300))
counter = 0

goals = 0
behinds = 0

goalScore = 0
while True:
event, values = window.read()

if event in (None, "Close"):
break

if event == "Ok":
try:
goals = int(values["txt_goals"])
behinds = int(values["txt_behinds"])
if goals < 0 or behinds < 0:
print("Invalid input: Please enter a positive integer")
else:
print(f"Your total score is {calculateTotalScore(goals, behinds)}")

window["score"].update(f"Score: {calculateTotalScore(goals, behinds)}")
if goals < 0 or behinds < 0:
window["score"].update("Dont enter negatives")

except ValueError:
print("Invalid input: Please enter an integer.")
window["score"].update("Please enter integers")
