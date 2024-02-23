import tkinter as tk
from tkinter import *
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import subprocess

# Pre-define some defaults
FONT_LARGE = ("Arial", 20)
FONT_SMALL = ("Arial", 10)
ALLOWED_SLIDE_FILES = (("PDF files","*.pdf"), ("PDF files","*.pdf"))
ALLOWED_OUTPUT_FILES = (("Text files","*.txt"), ("Text files","*.txt"))

class General():
    #Opens file manager menu
    def open_window(Default, ALLOWED_FILES):
        filename = filedialog.askopenfilename(initialdir=Default, title="Select file", filetypes=ALLOWED_FILES)
        return filename

    #Opens a file for user to view
    def open_file(Default, ALLOWED_FILES):
        string = General.open_window(Default, ALLOWED_FILES)
        try:
            os.startfile(string)
        except:
            mb.showinfo('confirmation', "File not found!")

    #Copies a file to another location
    def copy_file(destination1, source1):
        if not os.path.exists(destination1):
            os.makedirs(destination1)
        Filename = os.path.basename(source1)
        destinationlist = []
        destinationlist = sorted(os.listdir(destination1))
        for file in range(len(destinationlist)):
            if destinationlist[file] == Filename:
                return None 
        shutil.copy(source1,destination1)

#Basic class used, inherited by other pages
class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def show(self):
        self.lift()

#First page user views
class MainPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        #title
        label = tk.Label(self, text="Ankify Main Page", font=FONT_LARGE)
        label.place(x=100, y=20)
        #Image logo
        imag = Image.open("C:/Users/samue/OneDrive/Desktop/Ankify/UI images/ANKIABLE.jpg")
        photo = ImageTk.PhotoImage(imag)
        self.photo = photo
        image_label = tk.Label(self, image=photo)
        image_label.place(x=316, y=10)

        #Button 1
        primary_button = tk.Button(self, text="Input new Slides", font=FONT_SMALL, width=20, height=2, command=lambda: controller.show_page(InputPage))
        primary_button.place(x=150, y=70)

        #button 2
        secondary_button = tk.Button(self, text="View Past Slides", font=FONT_SMALL, width=20, height=2, command=lambda: General.open_file("C:/Users/samue/OneDrive/Desktop/Ankify/PastSlides/", ALLOWED_SLIDE_FILES)) 
        secondary_button.place(x=150, y=120)
        
        #Button 3
        tertiary_button = tk.Button(self, text="View Past Decks", font=FONT_SMALL, width=20, height=2, command=lambda: General.open_file("C:/Users/samue/OneDrive/Desktop/Ankify/Output/", ALLOWED_OUTPUT_FILES)) 
        tertiary_button.place(x=150, y=170)

#The loading page with the progress bars
class LoadingPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        self.controller = controller
        #The different loading screens
        self.Loading_list = ["Loading...", "Loading...", "Loading...", "Loading...", "Loading...", "Finished"]
        self.text_list = ["Processing step 1/5", "Processing step 2/5", "Processing step 3/5", "Processing step 4/5", "Processing step 5/5", "Finished"]
        self.image_paths = ["C:/Users/samue/OneDrive/Desktop/Ankify/UI images/Progressbars/Progress1.png", "C:/Users/samue/OneDrive/Desktop/Ankify/UI images/Progressbars/Progress2.png", "C:/Users/samue/OneDrive/Desktop/Ankify/UI images/Progressbars/Progress3.png", "C:/Users/samue/OneDrive/Desktop/Ankify/UI images/Progressbars/Progress4.png", "C:/Users/samue/OneDrive/Desktop/Ankify/UI images/Progressbars/Progress5.png", "C:/Users/samue/OneDrive/Desktop/Ankify/UI images/Progressbars/Progress6.png"]
        self.current_index = 0
        self.current_text = 1
        self.G = False

        LoadingPage.label6 = Label(self, text=self.Loading_list[0], font=FONT_LARGE)
        LoadingPage.label6.place(x=180, y=20)
        LoadingPage.label7 = Label(self, text=self.text_list[0], font=FONT_SMALL)
        LoadingPage.label7.place(x=170, y=60)

        LoadingPage.progress_label = tk.Label(self)
        LoadingPage.progress_label.place(x=120, y=80)
        LoadingPage.FinishButton = Button(self, text="Finish", font=FONT_SMALL, state=tk.DISABLED,width=20, height=2, command=lambda: controller.show_page(FinishPage))
        LoadingPage.FinishButton.place(x=300, y=400)
        self.load_image()
        self.controller.after(self.interval, self.change_image_text)

    def load_image(self):
        self.image = tk.PhotoImage(file=self.image_paths[self.current_index])
        self.progress_label.config(image=self.image)    

    def change_image_text(self):
        LoadingPage.label6.config(text=self.Loading_list[self.current_text])
        LoadingPage.label7.config(text=self.text_list[self.current_text])
        # Increment the index to get the next image and text
        self.current_index = (self.current_index + 1) % 6
        self.current_text = (self.current_text + 1)  % 6
        # Load the next image and display it
        self.load_image()

        if self.current_text == 0:
            LoadingPage.FinishButton.config(state=tk.NORMAL)
            self.G = True
        elif self.G == True: 
            print("Process is done")
        else:
            self.controller.after(self.interval, self.change_image_text)
            LoadingPage.FinishButton.config(state=tk.DISABLED)

    def RunTheProgram(controller):
        print("Started")
        LoadingPage.CopytheFiles(controller)
        controller.show_page(LoadingPage)
        Program_list = ["C:/Users/samue/OneDrive/Desktop/Ankify/Seperator.py",
                         "C:/Users/samue/OneDrive/Desktop/Ankify/ImageRecogniser.py", 
                         "C:/Users/samue/OneDrive/Desktop/Ankify/CardFilter.py", 
                         "C:/Users/samue/OneDrive/Desktop/Ankify/Splitter2.py", 
                         "C:/Users/samue/OneDrive/Desktop/Ankify/CardRecogniser.py"]
        for i in range(0,5):
            LoadingPage.RunPythonProgram(Program_list[i])
            LoadingPage.change_image_text(controller)
    
    def CopytheFiles(controller):
        source = General.open_window("C:/Users/samue/OneDrive/Desktop/", ALLOWED_SLIDE_FILES)
        General.copy_file("C:/Users/samue/OneDrive/Desktop/Ankify/PastSlides/", source)
        General.copy_file("C:/Users/samue/OneDrive/Desktop/Ankify/Slides/", source)


    def RunPythonProgram(Program):
        r = subprocess.Popen(["python", Program])
        return r
        

class FinishPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        #Title
        DownloadLabel = Label(self, text="Download Cards", font=FONT_LARGE)
        DownloadLabel.place(x=165, y=20)
        #button
        DownloadButton = Button(self, text="Download Cards", font=FONT_SMALL,width=20, height=2, command=lambda: FinishPage.openFolder())
        DownloadButton.place(x=180, y=80)
    
    def openFolder():
        folderList = filedialog.askdirectory()
        #List of directories for the folder
        Items = os.listdir("C:/Users/samue/OneDrive/Desktop/Ankify/Output/")
        minNum = 0
        #Loop through all items
        for item in Items:
            item = os.path.basename(item)
            intitem = item[:-4]
            intitem = int(intitem)
            if intitem > minNum:
                minNum = intitem
        minNum = str(minNum)
        print("C:/Users/samue/OneDrive/Desktop/Ankify/Output/"+minNum+".txt")
        General.copy_file(folderList+"/", "C:/Users/samue/OneDrive/Desktop/Ankify/Output/"+minNum+".txt")

class InputPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        self.confirm_pressed = False

        label = Label(self, text="Input New Slide", font=FONT_LARGE)
        label.place(x=150, y=30)

        label0 = Label(self, text="Please input only letters / numbers (space is allowed)")
        label0.place(x=150, y=60)

        entry = Entry(self, state="normal")
        entry.place(x=150, y=90)

        button3 = Button(self, text="Confirm", font=FONT_SMALL, state="disabled",width=20, height=2, command=lambda: create_label())
        button3.place(x=150, y=140)

        #button4 = tk.Button(self, text="Select PDF", width=20, height=2, command=lambda: LoadingPage.RunTheProgram(controller), state="disabled")
        button4 = Button(self, text="Select PDF", font=FONT_SMALL, width=20, height=2, command=lambda: LoadingPage.RunTheProgram(controller), state="disabled")
        button4.place(x=150, y=200)



        def create_label():
            self.confirm_pressed_func(entry, button3, button4)
            text = entry.get()
            #Place deckname label
            label = tk.Label(entry, text="Deck name: "+text, font=FONT_SMALL)
            button3.config(state="disabled")
            label.place(x=150, y=300)
            label.pack()
            file_name = "C:/Users/samue/OneDrive/Desktop/Ankify/Variable/Deckname.txt"
            folder_name = 'C:/Users/samue/OneDrive/Desktop/Ankify/Variable/'
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            #Store in variable
            with open(file_name, "w") as file:
                # Write the content to the file
                print(text)
                file.write(text)

        def enable_confirm_button(event):
            #remove the spaces from the testing text
            test = entry.get()
            i = 0
            while i < len(test) - 1:  
                if test[i] == " ":
                    test = test[0:i]+test[i+1:len(test)]
                i = i+ 1
            #Validate the button
            if entry.get() and test.isalnum():
                button3.config(state="normal")
            else:
                button3.config(state="disabled")

        entry.bind("<KeyRelease>", enable_confirm_button)

    def confirm_pressed_func(self, entry, button3, button4):
        #Reconfigure buttons
        self.confirm_pressed = True
        entry.config(state="disabled")
        button3.config(state="disabled")
        button4.config(state="normal")


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #Basic frame
        self.geometry("500x500")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Instantiate the pages
        self.pages = {}
        for PageClass in (MainPage, InputPage, LoadingPage, FinishPage):
            page = PageClass(container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(MainPage)
    #Display the pages
    def show_page(self, page_class):
        page = self.pages[page_class]
        page.show()
   #     if page_class == LoadingPage and Application.Loading1Ran == False:
    #        RANNNN.run()
    #        Application.Loading1Ran = True
            

app = Application()
app.title("Ankify")
app.mainloop()
