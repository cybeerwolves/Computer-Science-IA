import tkinter as tk
from tkinter import *
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

def open_window():
    read=easygui.fileopenbox(default="C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Slides/")
    return read

def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")

def DEL_files(folderList):
    sortlist=sorted(os.listdir(folderList))       
    i=0
    while(i<len(sortlist)):
        delete_file(folderList+sortlist[i])
        i+=1

def delete_file(del_file):
    if os.path.exists(del_file):
        os.remove(del_file)

def copy_file(destination1, source1):
    shutil.copy(source1,destination1)

def RunTheProgram():
    source = open_window()
    copy_file("C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Slides/", source)
    


class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def show(self):
        self.lift()

class MainPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        label = tk.Label(self, text="Main Page")
        label.pack(pady=10, padx=10)

        secondary_button = tk.Button(self, text="View Past Slides", width=20, height=2, command=lambda: open_file()) 
        secondary_button.pack()

        tertiary_button = tk.Button(self, text="Input new Slides", width=20, height=2, command=lambda: controller.show_page(InputPage))
        tertiary_button.pack()

#class SecondaryPage(Page):
 #   def __init__(self, parent, controller):
  #      Page.__init__(self, parent, controller)
#
 #       label = tk.Label(self, text="View Past Slides")
  #      label.pack(pady=10, padx=10)

   #     button = tk.Button(self, text="Go back to Main Page", width=20, height=2, command=lambda: controller.show_page(MainPage))
    #    button.pack()

class InputPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        label = tk.Label(self, text="Input New Slide")
        label.pack(pady=10, padx=10)
        button3 = tk.Button(self, text="Select PDF", width=20, height=2, command= lambda: RunTheProgram())
        button3.pack()

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("500x500")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for PageClass in (MainPage, InputPage):
            page = PageClass(container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(MainPage)

    def show_page(self, page_class):
        page = self.pages[page_class]
        page.show()

if __name__ == "__main__":
    app = Application()
    app.mainloop()