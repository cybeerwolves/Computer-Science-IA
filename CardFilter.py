import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import os

from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import cv2
import extcolors
from colormap import rgb2hex
CardCounter = 0
pixels = 0
yellow = 0
counter = 0
Newcounter = 0
Greencounter = 0
BoldSplit = 0

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
    # Find the color name with the closest RGB values to the provided values
    closest_color = None
    closest_distance = float('inf')
    for name, values in color_names.items():
        distance = sum([(v - c) ** 2 for v, c in zip(values, (r, g, b))])
        if distance < closest_distance:
            closest_distance = distance
            closest_color = name
    return closest_color

Card_paths = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCards/'
Cards = os.listdir(Card_paths)
for image in Cards:
    Colors = []
    if image.endswith(".jpg"):
        CardCounter = CardCounter + 1
        CardPath = os.path.join(Card_paths, f'card_{CardCounter}.jpg')
        Clocation = CardPath.split('/')
        Card_output = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Cards/'+Clocation[len(Clocation) - 1]
        card = cv2.imread(CardPath)
        colors_x = extcolors.extract_from_path(CardPath, tolerance = 30, limit = 9)
        Color_D = color_to_df(colors_x)


        #Filter out the string
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
            output_path = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCardsFiltered/'
            image = Image.open(CardPath)
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            #new_filename = os.path.join(output_path, f'Filteredcard_{counter}.jpg')
            new_filename = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCardsFiltered/'+Clocation[len(Clocation) - 1]
            image.save(new_filename)
            #counter = counter + 1
        elif len(Colors) == 4 and Colors.count('white') > 0 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0:
            output_path = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/NeedSplit/'
            image = Image.open(CardPath)
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            #new_filename = os.path.join(output_path, f'Filteredcard_{Newcounter}.jpg')
            new_filename = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/NeedSplit/'+Clocation[len(Clocation) - 1]
            image.save(new_filename)
            #Newcounter = Newcounter + 1
        elif len(Colors) == 4 and Colors.count('green') > 0 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0:
            output_path = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/NeedBold/'
            image = Image.open(CardPath)
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            #new_filename = os.path.join(output_path, f'Filteredcard_{Greencounter}.jpg')
            new_filename = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/NeedBold/'+Clocation[len(Clocation) - 1]
            image.save(new_filename)
        elif len(Colors) > 4 and Colors.count('green') > 0 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0 and Colors.count('white') > 0:
            output_path = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/NeedBoldSplit/'
            image = Image.open(CardPath)
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            #new_filename = os.path.join(output_path, f'Filteredcard_{BoldSplit}.jpg')
            new_filename = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/NeedBoldSplit/'+Clocation[len(Clocation) - 1]
            image.save(new_filename)
            #BoldSplit = BoldSplit + 1
        #else:
            #print("abnormal", CardPath)
            



#normal: 1, 8, 
#Bold text: 208, 209
#Abnormal: 41, 42, 45, 46, 69, 66, 178, 195, 124
#No text: 84, 87, 88, 105

#Normal sequence of colors: ['#FFFF00', '#0C0900', '#EF0900', '#F5F734', '#EAED58']