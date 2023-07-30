import tkinter as tk
from tkinter import messagebox

def start_button_clicked():
    messagebox.showinfo("Page 2", "Choose your files:")

# Create the main window
window = tk.Tk()
window.title("My Program")

# Create a label for the title
title_label = tk.Label(window, text="Welcome to My Program")
title_label.pack()

# Create a button that triggers the start_button_clicked function
start_button = tk.Button(window, text="Start", command=start_button_clicked)
start_button.pack()

# Run the main event loop
window.mainloop()

#Running the other python programs in order
import subprocess

# Define the command to execute the Python program
command = ['python', 'path/to/your/program.py']
#The order should be:
#Seperator.py
#ImageRecogniser
#Tester
#Splitter2
#test

# Run the Python program as a subprocess
subprocess.run(command)