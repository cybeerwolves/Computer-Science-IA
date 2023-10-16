import cv2
import numpy as np
from PIL import Image
import extcolors
import os
import shutil

# Load the image
def color_to_df(input):
    
    colors_pre_list = str(input).replace('([(','').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')','') for i in colors_pre_list]
    
    #convert RGB to HEX code
    df = [df_rgb, df_percent]
    return df

def identify_color(r, g, b):
    # Define a list of color names and their corresponding RGB values
    color_names = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'yellow': (240, 240, 70),
        'cyan': (0, 255, 255),
        # Add more color names and RGB values as needed
    }
    closest_color = None
    closest_distance = float('inf')
    for name, values in color_names.items():
        distance = sum([(v - c) ** 2 for v, c in zip(values, (r, g, b))])
        if distance < closest_distance:
            closest_distance = distance
            closest_color = name
    return closest_color
    # Find the color name with the closest RGB values to the provided values

cage = 0
counter = 0


pathsss = 'C:/Users/5amue1/Desktop/Code/IA for Computer Science/Computer-Science-IA/Samples/'

Card_paths = 'C:/Users/5amue1/Desktop/Code/IA for Computer Science/Computer-Science-IA/NeedSplit/'
Cards = os.listdir(Card_paths)
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

        # Initialize the list of detected rectangles
        rectangles = []

        # Loop through all the contours and find the rectangles of the appropriate size
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if min_length <= w <= max_length and min_width <= h <= max_width:
                print(x, y, w, h)
                # Check if the rectangle is not too small and not too large
                # and does not intersect with any other rectangles
                y = int(y)
                x = int(x)    
                w = int(w + x)
                h = int(h + y)
                imge = cv2.imread(img)
                imge = imge[y:h, x:w]
                cage = cage + 1
                filename = os.path.join(pathsss, f'nominal{cage}.jpg')
                if not os.path.exists(pathsss):
                    os.makedirs(pathsss)
                cv2.imwrite(filename, imge)
                colors_x = extcolors.extract_from_path(filename, tolerance = 30, limit = 9)
                Color_D = color_to_df(colors_x)
                Colors = []
                for i in range(0, len(Color_D[0])):
                    Contain = False
                    Color_D[0][i] = Color_D[0][i][1:len(Color_D[0][i]) - 1]
                    Color_D[0][i] = Color_D[0][i].split(", ")
                    Color_D[0][i] = [int(x) for x in Color_D[0][i]]
                    Color = identify_color(Color_D[0][i][0], Color_D[0][i][1], Color_D[0][i][2])
                    for u in range(0, len(Colors)):
                        if Color == Colors[u]:
                            Contain = True
                    if Contain == False:
                        Colors.append(Color)
                if len(Colors) == 3 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0:
                    output_path = 'C:/Users/5amue1/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCardsFiltered/'
                    image = Image.open(filename)
                    counter = counter + 1
                    if not os.path.exists(output_path):
                        os.makedirs(output_path)
                        #new_filename = os.path.join(output_path, f'Filteredcard_{counter}.jpg')
                    new_filename = os.path.join(output_path, f'Filtered{counter}.jpg')
                    image.save(new_filename)
                    # Check if all pixels within the rectangle are yellow
                elif len(Colors) == 4 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0 and Colors.count('green') > 0:
                    output_path = 'C:/Users/5amue1/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCardsFiltered/'
                    image = Image.open(filename)
                    counter = counter + 1
                    if not os.path.exists(output_path):
                        os.makedirs(output_path)
                        #new_filename = os.path.join(output_path, f'Filteredcard_{counter}.jpg')
                    new_filename = os.path.join(output_path, f'Filtered{counter}.jpg')
                    image.save(new_filename)
                    # Check if all pixels within the rectangle are yellow
shutil.rmtree(pathsss)

#Note: need change with the file output