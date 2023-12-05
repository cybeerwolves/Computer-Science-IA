import PySimpleGUI as sg

# Define the layout of the window
layout1 = [
    [sg.Text('Ankible', size=(30, 1), justification='center', font=('ink draft', 50), pad=((100, 100), (20, 20)) )],
    [sg.Button('View Past Slides', button_color=('white', 'black'), size=(50, 3), key='Button1', pad=((100, 100), (120, 20)))],
    [sg.Button('Input New Slides', button_color=('white', 'black'), size=(50, 3), key='Button2', pad=((100, 100), (5, 20)))],
    [sg.Button('Quit', button_color=('white', 'black'), size=(50, 3), key='Button3', pad=((100, 100), (5, 20)))],
]

layout_new_page = [
    [sg.Text('View Past Slides', size=(30, 1), justification='center', font=('ink draft', 50), pad=((100, 100), (20, 20)))],
    [sg.Button('Back', button_color=('white', 'black'), size=(50, 3), key='Back')],
]

# Create the window
window = sg.Window('Button Screen', layout1, size=(500, 500))

# Event loop to process events and button clicks
while True:
    event, values = window.read()

    # Handle button clicks
    if event == sg.WINDOW_CLOSED:
        break  # Exit the program if the window is closed
    elif event == 'Button1':
        print("Past slides viewed")
        layout = layout_new_page  
    elif event == 'Button2':
        print("Input new slides")
    elif event == 'Button3':
        break
    elif event == 'Back':
        layout = layout1 
    if 'layout' in locals():
        window.close()  # Close the current window
        window = sg.Window('Button Screen', layout, size=(500, 500))

# Close the window
window.close()