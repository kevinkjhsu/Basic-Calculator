import PySimpleGUI as sg

# Calculator GUI layout
button_size = (4, 2)
theme = ["Menu", ["random", "GrayGrayGray", "LightBlue"]]


def create_window(theme_item):
    layout = [
        [sg.Text("", tooltip="Right click to change theme", key="DISPLAY", expand_x=True,
                 justification="right", pad=(10, 20), font=("Arial", 30),
                 right_click_menu=theme)],
        [sg.Button("Clear", key="CLEAR", size=button_size, expand_x=True),
         sg.Button("Enter", key="ENTER", size=button_size, expand_x=True)],
        [sg.Button(7, size=button_size), sg.Button(8, size=button_size),
         sg.Button(9, size=button_size), sg.Button("*", size=button_size)],
        [sg.Button(4, size=button_size), sg.Button(5, size=button_size),
         sg.Button(6, size=button_size), sg.Button("/", size=button_size)],
        [sg.Button(1, size=button_size), sg.Button(2, size=button_size),
         sg.Button(3, size=button_size), sg.Button("-", size=button_size)],
        [sg.Button(0, size=button_size, expand_x=True), sg.Button(".", size=button_size),
         sg.Button("+", size=button_size)]
    ]
    sg.theme(theme_item)
    return sg.Window("Calculator", layout=layout, font=("calibri", 20))


window = create_window("dark")
num_entered = []
complete_action = []
deci_entered = False
while True:
    event, value = window.read()
    if event in theme[1]:
        window.close()
        window = create_window(event)
    if event == sg.WIN_CLOSED:
        break
    if event in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        num_entered.append(event)
        if num_entered[0] == "0":
            num_entered.pop()
        complete_action.append(event)
        complete_text = ''.join(complete_action)
        window["DISPLAY"].update(complete_text)
    if event == ".":
        if deci_entered:
            pass
        else:
            deci_entered = True
            complete_action.append(event)
            complete_text = ''.join(complete_action)
            window["DISPLAY"].update(complete_text)
    if event in ["*", "/", "-", "+"]:
        deci_entered = False
        complete_action.append(event)
        complete_cal = ''.join(complete_action)
        window["DISPLAY"].update(complete_cal)
    if event == "CLEAR":
        deci_entered = False
        window["DISPLAY"].update("")
        complete_action = []
    if event == "ENTER":
        deci_entered = False
        result = str(eval(''.join(complete_action)))
        if len(result) > 10:
            result = f"{float(result):e}"
        window["DISPLAY"].update(result)
        complete_action = []
