# Programmer: Benjamin Wilkinson
# Date: 09/02/2024
# Description: Temperature Conversion GUI Program

import PySimpleGUI as sg

# calculation function
def ftoc(f):
ennfwnfwofn = ((f - 32) * 5/9)
newcalcf = str(round(ennfwnfwofn))
return newcalcf

def ctof(c):
firstnewcalcc = c * 1.8
finalnewcalcc = str(round(firstnewcalcc + 32))
return finalnewcalcc

# set the theme
sg.theme("wdasdaca")

# laid out elements
layout = [[sg.Combo(['°C','°F'], key="tester",default_value="°C")],
[sg.Text("Enter in temperatures"), sg.Push()],
[sg.Input(key="txt_temp1", size=(7,20)), sg.Text("Temp: ", key="1"),],
[sg.Input(key="txt_temp2",size=(7,20)), sg.Text("Temp: ", key="2"),],
[sg.Input(key="txt_temp3",size=(7,20)),sg.Text("Temp: ", key="3"),],
[sg.Input(key="txt_temp4",size=(7,20)),sg.Text("Temp: ", key="4"),],
[sg.Input(key="txt_temp5",size=(7,20)),sg.Text("Temp: ", key="5"),],
[sg.Input(key="txt_temp6",size=(7,20)),sg.Text("Temp: ", key="6"),],
[sg.Input(key="txt_temp7",size=(7,20)),sg.Text("Temp: ", key="7"),],
[sg.Input(key="txt_temp8",size=(7,20)),sg.Text("Temp: ", key="8"),],
[sg.Input(key="txt_temp9",size=(7,20)),sg.Text("Temp: ", key="9"),],
[sg.Input(key="txt_temp10",size=(7,20)),sg.Text("Temp: ", key="10"),],
[sg.Button("Ok"), sg.Button("Close"), sg.Push()],]


# name and create window
window = sg.Window("Average Temp Calculator", layout, icon='', size=(250,400))

# predefine datatypes
f = 0
# window while loop
while True:
event, values = window.read()

if event in (None, "Close"):
break

if event == "Ok":
try:
Temp1 = float(values["txt_temp1"])
Temp2 = float(values["txt_temp2"])
Temp3 = float(values["txt_temp3"])
Temp4 = float(values["txt_temp4"])
Temp5 = float(values["txt_temp5"])
Temp6 = float(values["txt_temp6"])
Temp7 = float(values["txt_temp7"])
Temp8 = float(values["txt_temp8"])
Temp9 = float(values["txt_temp9"])
Temp10 = float(values["txt_temp10"])

if str(values["tester"]) == "°F":
window["1"].update(f"Temp in C: {ftoc(Temp1)} °C")
window["2"].update(f"Temp in C: {ftoc(Temp2)} °C")
window["3"].update(f"Temp in C: {ftoc(Temp3)} °C")
window["4"].update(f"Temp in C: {ftoc(Temp4)} °C")
window["5"].update(f"Temp in C: {ftoc(Temp5)} °C")
window["6"].update(f"Temp in C: {ftoc(Temp6)} °C")
window["7"].update(f"Temp in C: {ftoc(Temp7)} °C")
window["8"].update(f"Temp in C: {ftoc(Temp8)} °C")
window["9"].update(f"Temp in C: {ftoc(Temp9)} °C")
window["10"].update(f"Temp in C: {ftoc(Temp10)} °C")

if str(values["tester"]) == "°C":
window["1"].update(f"Temp in F: {ctof(Temp1)} °F")
window["2"].update(f"Temp in F: {ctof(Temp2)} °F")
window["3"].update(f"Temp in F: {ctof(Temp3)} °F")
window["4"].update(f"Temp in F: {ctof(Temp4)} °F")
window["5"].update(f"Temp in F: {ctof(Temp5)} °F")
window["6"].update(f"Temp in F: {ctof(Temp6)} °F")
window["7"].update(f"Temp in F: {ctof(Temp7)} °F")
window["8"].update(f"Temp in F: {ctof(Temp8)} °F")
window["9"].update(f"Temp in F: {ctof(Temp9)} °F")
window["10"].update(f"Temp in F: {ctof(Temp10)} °F")
except:
sg.popup_error("Nope")

window.close()
