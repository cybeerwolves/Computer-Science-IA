import subprocess
import tkinter as tk

def run_program():
    subprocess.Popen(["python", "C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/RANNNN.py"])

root = tk.Tk()
button = tk.Button(root, text="Run Program", command=run_program)
button.pack()
root.mainloop()