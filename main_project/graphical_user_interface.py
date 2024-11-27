import functions
import FreeSimpleGUI as sg


label = sg.Text("Type a to-do: ")
input_box = sg.InputText(tooltip = "to-do")
add_button = sg.Button("ADD")

window = sg.Window('My to-do app', layout = [[label],[input_box, add_button]])
window.read()
window.close()