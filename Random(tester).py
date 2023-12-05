import PySimpleGUI as sg
import webbrowser

# Define the URL
url1 = "https://th.bing.com/th/id/R.ba39022002c667d7127b0395386f1ec7?rik=cLmXqPvORDkpqQ&pid=ImgRaw&r=0"
url2 = "https://media.tenor.com/8tgG_KyJqqwAAAAi/happy-happy-happy-happy.gif"
url3 = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8c327453-d068-47ab-b450-6958dda97075/dd48m6p-6e7abb7d-0665-40d6-b0e2-689eb838304c.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzhjMzI3NDUzLWQwNjgtNDdhYi1iNDUwLTY5NThkZGE5NzA3NVwvZGQ0OG02cC02ZTdhYmI3ZC0wNjY1LTQwZDYtYjBlMi02ODllYjgzODMwNGMuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.XgyiNqZ61FtlUgsyR3DbIy_hx3pnhoXiqzwnXMEKKL4"
url4 = "https://i.pinimg.com/originals/1e/53/f4/1e53f4e398a2c278f4f560ff37b3473d.jpg"

# Define the layout of the window
layout = [
    [sg.Text('Meme Page', size=(30, 1), justification='center', font=('Helvetica', 20), relief=sg.RELIEF_RIDGE)],
    [sg.Button('Totally not rickroll', button_color=('white', 'black'), size=(50, 3), key='Button1', pad=((100, 100), (10, 20)))],
    [sg.Button('Happy Cat', button_color=('white', 'black'), size=(50, 3), key='Button2', pad=((100, 100), (10, 20)))],
    [sg.Button('sussy Button', button_color=('white', 'black'), size=(50, 3), key='Button3', pad=((100, 100), (10, 20)))],
    [sg.Button('Cat V2', button_color=('white', 'black'), size=(50, 3), key='Button4', pad=((100, 100), (10, 20)))],
    [sg.Button('Quit', button_color=('white', 'black'), size=(50, 3), key='Button5', pad=((100, 100), (10, 20)))]
]


# Create the window
window = sg.Window('Button Screen', layout, size=(500, 500))

# Event loop to process events and button clicks
while True:
    event, values = window.read()

    # Handle button clicks
    if event == sg.WINDOW_CLOSED:
        break  # Exit the program if the window is closed
    elif event == 'Button1':
        webbrowser.open(url1)  # Open the URL in the default web browser
    elif event == 'Button2':
        webbrowser.open(url2)
    elif event == 'Button3':
        webbrowser.open(url3)
        print("Are you regretting it?")
    elif event == 'Button4':
        webbrowser.open(url4)
    elif event == 'Button5':
        break
# Close the window
window.close()