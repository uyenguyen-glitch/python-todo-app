import PySimpleGUI as sg
from converters import convert

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert", key="convert")
output = sg.Text(key="output")


window = sg.Window("Convertor", layout=[[feet_label, feet_input],
                                        [inches_label, inches_input],
                                        [convert_button, output]])
while True:
    events, values = window.read()
    feet = values["feet"]
    inches = values["inches"]

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")



window.close()