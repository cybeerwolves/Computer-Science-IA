import tkinter as tk
import time

class ImageTextChanger:
    def __init__(self, controller):
        self.controller = controller
        self.interval = 2000
        self.current_index = 0
        self.current_text = 1
        self.G = False
        self.text_list = ["Processing step 1/5", "Processing step 2/5", "Processing step 3/5", "Processing step 4/5", "Processing step 5/5", "Finnished"]
        self.image_paths = ["C:/Users/samue/Downloads/compressed/Progress1.png", "C:/Users/samue/Downloads/compressed/Progress2.png", "C:/Users/samue/Downloads/compressed/Progress3.png", "C:/Users/samue/Downloads/compressed/Progress4.png", "C:/Users/samue/Downloads/compressed/Progress5.png", "C:/Users/samue/Downloads/compressed/Progress6.png"]

        # Create a label to display the image
        self.image_label = tk.Label(self.controller)
        self.image_label.pack()

        # Create a label to display the text
        self.text_label = tk.Label(self.controller, font=("Helvetica", 16), text=self.text_list[0])
        self.text_label.pack()

        # Load the first image and display it
        self.load_image()
        # Start the timer to change the image and text
        self.controller.after(self.interval, self.change_image_text)
        self.yoo_button = tk.Button(self.controller, text="YOOO", command=self.yoo_button, state=tk.DISABLED)
        self.yoo_button.pack()

    def load_image(self):
        self.image = tk.PhotoImage(file=self.image_paths[self.current_index])
        self.image_label.config(image=self.image)

    def change_image_text(self):
        self.text_label.config(text=self.text_list[self.current_text])
        # Increment the index to get the next image and text
        self.current_index = (self.current_index + 1) % 6
        self.current_text = (self.current_text + 1)  % 6
        # Load the next image and display it
        self.load_image()

        if self.current_text == 0:
            self.yoo_button.config(state=tk.NORMAL)
            self.G = True
        elif self.G == True: 
            print("Process is done")
        else:
            self.controller.after(self.interval, self.change_image_text)
            self.yoo_button.config(state=tk.DISABLED)

    
    def yoo_button(self):
        # Create a label to display "YOOO"
        yoo_label = tk.Label(self.controller, text="YOOO", font=("Helvetica", 24))
        yoo_label.pack()

# Create the main window
root = tk.Tk()
root.title("Image and Text Changer")

# Set the window size
root.geometry("400x400")

# Define the image paths, text list, and interval


# Create the ImageTextChanger object
itc = ImageTextChanger(root)

# Start the main loop
root.mainloop()







