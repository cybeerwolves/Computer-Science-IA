import subprocess
import time

def execute_python_program(program_path):
    try:
        subprocess.run(['python', program_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the program: {e}")
    except FileNotFoundError:
        print("The 'python' command was not found. Make sure Python is installed and added to the system's PATH.")

#Guide to program run order
SlidestoImages = 'C:/Users/samue/OneDrive/Desktop/Ankify/Seperator.py'
ImagetoCards = 'C:/Users/samue/OneDrive/Desktop/Ankify/ImageRecogniser.py'
CardsFilter = 'C:/Users/samue/OneDrive/Desktop/Ankify/CardFilter.py'
CardSplitter = 'C:/Users/samue/OneDrive/Desktop/Ankify/Splitter2.py'
Textoutput = 'C:/Users/samue/OneDrive/Desktop/Ankify/CardRecogniser.py'

Program_order = [SlidestoImages, ImagetoCards, CardsFilter, CardSplitter, Textoutput]
print("Started")

for i in range(0, len(Program_order)):
    execute_python_program(Program_order[i])
    print("Program"+Program_order[i]+" done, moving onto the next one")