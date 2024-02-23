import cv2
import numpy as np
from PIL import Image
import extcolors
import os
import shutil
import time


def color_to_df(input):
    
    input = str(input)
    #Remove the bulky formatting at start
    colors_pre_list = input.replace('([(','')

    #Split the different colours to objects in arrays
    colors_pre_list = colors_pre_list.split(', (')[0:-1]

    # Seperate into parallel arrays of amount of pixels and colour
    df_rgb = []
    df_percent = []
    for i in range(0, len(colors_pre_list) - 1):
        #Splits String then append to array
        df_rgb.append(colors_pre_list[i].split('), ')[0] + ')')
        df_percent.append(colors_pre_list[i].split('), ')[1].replace(')',''))
    
    #Combine arrays to 2 dimensional arrays
    df = [df_rgb, df_percent]
    return df

def identify_color(r, g, b):
    # Define a list of color names and their corresponding RGB values, dictionary array
    color_names = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'yellow': (255, 255, 0),
        'yellow': (240, 240, 70),
        'cyan': (0, 255, 255),
    }
    # Find the color name with the closest RGB values to the provided values
    closest_color = None
    closest_distance = float('inf')
    #Loop throgh each colour, with the colour name and the value assigned to it 
    for name, values in color_names.items():
        #Finding closest distance using pythagorean theorem
        
        distance = sum([(v - c) ** 2 for v, c in zip(values, (r, g, b))])
        #Find minimum distance
        if distance < closest_distance:
            closest_distance = distance
            closest_color = name
    return closest_color

def Splitter(Cards, Card_paths, pathsss):
    cage = 0
    counter = 0
    for img in Cards:
        if img.endswith(".jpg"):
            img = os.path.join(Card_paths, img)
            modified_img = cv2.imread(img)
            hsv = cv2.cvtColor(modified_img, cv2.COLOR_BGR2HSV)

            # Define the range of yellow color in HSV
            lower_yellow = np.array([20, 100, 100])
            upper_yellow = np.array([30, 255, 255])
            mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
            # Find contours in the binary image
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # Define the minimum and maximum size of the rectangles you want to detect
            min_length = 100
            max_length = 999999999999999999999
            min_width = 10
            max_width = 999999999999999999999
            rectangles = []

            # Loop through all the contours and find the rectangles of the appropriate size
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                if min_length <= w <= max_length and min_width <= h <= max_width:
                    print(x, y, w, h)
                    # Check if the rectangle is not too small and not too large
                    # and does not intersect with any other rectangles
                    #Converting format
                    y = int(y)
                    x = int(x)    
                    w = int(w + x)
                    h = int(h + y)
                    imge = cv2.imread(img)
                    #Crop out the image
                    imge = imge[y:h, x:w]
                    cage = cage + 1
                    #Make the folder / check existence and store the image 
                    filename = os.path.join(pathsss, f'nominal{cage}.jpg')
                    if not os.path.exists(pathsss):
                        os.makedirs(pathsss)
                    cv2.imwrite(filename, imge)
                    #Extract colours from image of the top 9 shades, with the number of pixels and shade
                    colors_x = extcolors.extract_from_path(filename, tolerance = 30, limit = 9)
                    #Convert to viewable format
                    Color_D = color_to_df(colors_x)
                    Colors = []
                    #Loop through all the colours
                    for i in range(0, len(Color_D[0])):
                        Contain = False
                        #Change colours to integers
                        Color_D[0][i] = Color_D[0][i][1:len(Color_D[0][i]) - 1]
                        Color_D[0][i] = Color_D[0][i].split(", ")
                        Color_D[0][i] = [int(x) for x in Color_D[0][i]]
                        #Identify the colours and the colour contained in the filtered image
                        Color = identify_color(Color_D[0][i][0], Color_D[0][i][1], Color_D[0][i][2]) 
                        for u in range(0, len(Colors)):
                            if Color == Colors[u]:
                                Contain = True
                        if Contain == False:
                            Colors.append(Color)
                    
                    #For non-bolded texts
                    if len(Colors) == 3 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0:
                        #Set output name and path
                        output_path = 'C:/Users/samue/OneDrive/Desktop/Ankify/SlideCardsFiltered/'
                        image = Image.open(filename)
                        counter = counter + 1
                        if not os.path.exists(output_path):
                            os.makedirs(output_path)
                        new_filename = os.path.join(output_path, f'Filtered{counter}.jpg')
                        image.save(new_filename)
                        # Check if all pixels within the rectangle are yellow
                    #For bolded text
                    elif len(Colors) == 4 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0 and Colors.count('green') > 0:
                        #Set output name and path, storing it
                        output_path = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedBold/'
                        image = Image.open(filename)
                        counter = counter + 1
                        if not os.path.exists(output_path):
                            os.makedirs(output_path)
                            #new_filename = os.path.join(output_path, f'Filteredcard_{counter}.jpg')
                        new_filename = os.path.join(output_path, f'Bold{counter}.jpg')
                        image.save(new_filename)
                        shutil.rmtree(pathsss)
                        # Check if all pixels within the rectangle are yellow


def run():
    
    time.sleep(50)
    pathsss = 'C:/Users/samue/OneDrive/Desktop/Ankify/Computer-Science-IA/Samples/'
    Card_paths = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedSplit/'
    BoldSplit = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedBoldSplit/'
    #Running this for both NeedSplit and BoldSplit Folders
    Cards = os.listdir(Card_paths)
    BoldSplits = os.listdir(BoldSplit)
    Splitter(Cards, Card_paths, pathsss)
    Splitter(BoldSplits,BoldSplit, pathsss)
run()


