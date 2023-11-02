import subprocess
import time

def execute_python_program(program_path):
    try:
        subprocess.run(['python', program_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the program: {e}")
    except FileNotFoundError:
        print("The 'python' command was not found. Make sure Python is installed and added to the system's PATH.")

# Example usage
SlidestoImages = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Seperator.py'
ImagetoCards = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/ImageRecogniser.py'
CardsFilter = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/CardFilter.py'
CardSplitter = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Splitter2.py'
Textoutput = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Test.py'
print("Started")

execute_python_program(SlidestoImages)
print("SlidestoImage running")
Run = True

execute_python_program(ImagetoCards)
print("ImagetoCards running")

execute_python_program(CardsFilter)
print("CardsFilter")

execute_python_program(CardSplitter)
print("CardSplitter")

execute_python_program(Textoutput)
print("Textoutput finnished")