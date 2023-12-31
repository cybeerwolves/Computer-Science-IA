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
Textoutput = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/CardRecogniser.py'

Program_order = [SlidestoImages, ImagetoCards, CardsFilter, CardSplitter, Textoutput]
print("Started")

for i in range(0, len(Program_order)):
    execute_python_program(Program_order[i])