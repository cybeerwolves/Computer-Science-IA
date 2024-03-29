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

def run():
    #Detect and make folders for card outputs 
    output_path = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedSplit/'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    new_filename = 'C:/Users/samue/OneDrive/Desktop/Ankify/SlideCardsFiltered/'
    if not os.path.exists(new_filename):
        os.makedirs(new_filename)
    Card_paths = 'C:/Users/samue/OneDrive/Desktop/Ankify/SlideCards/'
    
    NeedBold = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedBold/'
    if not os.path.exists(NeedBold):
        os.makedirs(NeedBold)
    NeedBoldSplit = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedBoldSplit/'
    if not os.path.exists(NeedBoldSplit):
        os.makedirs(NeedBoldSplit)
    
    #looping through all the cards
    Cards = os.listdir(Card_paths)
    CardCounter = 0
    for image in Cards:
        Colors = []
        #Check the formatting is correct
        if image.endswith(".jpg") or image.endswith(".jpeg"):
            CardCounter = CardCounter + 1
            CardPath = os.path.join(Card_paths, f'card_{CardCounter}.jpg')
            #Getting file name
            Clocation = CardPath.split('/')
            #Extract colours from image of the top 9 shades, with the number of pixels and shade
            colors_x = extcolors.extract_from_path(CardPath, tolerance = 30, limit = 9)

            #Converting colour to RGB and percentage values
            Color_D = color_to_df(colors_x)


            #Filter out the string
            for i in range(0, len(Color_D[0])):
                Contain = False
                #Obtain colours as coordinates
                Color_D[0][i] = Color_D[0][i][1:len(Color_D[0][i]) - 1]
                Color_D[0][i] = Color_D[0][i].split(", ")
                Color_D[0][i] = [int(x) for x in Color_D[0][i]]
                #Identify colour and find closest distance
                Color = identify_color(Color_D[0][i][0], Color_D[0][i][1], Color_D[0][i][2])
                #Sequential Search and append
                for u in range(0, len(Colors)):
                    if Color == Colors[u]:
                        Contain = True
                if Contain == False:
                    Colors.append(Color)
            if len(Colors) == 3 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0:
                #Set output path
                output_path = 'C:/Users/samue/OneDrive/Desktop/Ankify/SlideCardsFiltered/'
                image = Image.open(CardPath)
                #Store to SlideCards Filtered
                new_filename = 'C:/Users/samue/OneDrive/Desktop/Ankify/SlideCardsFiltered/'+Clocation[len(Clocation) - 1]
                image.save(new_filename)
            elif len(Colors) == 4 and Colors.count('white') > 0 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0:
                #Set output path
                output_path = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedSplit/'
                image = Image.open(CardPath)
                #Store to Need Splits
                new_filename = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedSplit/'+Clocation[len(Clocation) - 1]
                image.save(new_filename)
            elif len(Colors) == 4 and Colors.count('green') > 0 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0:
                #Set output path
                output_path = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedBold/'
                image = Image.open(CardPath)
                #Store to Need Splits
                new_filename = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedBold/'+Clocation[len(Clocation) - 1]
                image.save(new_filename)
            elif len(Colors) > 4 and Colors.count('green') > 0 and Colors.count('yellow') > 0 and Colors.count('red') > 0 and Colors.count('black') > 0 and Colors.count('white') > 0:
                #Set output path
                output_path = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedBoldSplit/'
                image = Image.open(CardPath)
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                #Store to Need boldsplits
                new_filename = 'C:/Users/samue/OneDrive/Desktop/Ankify/NeedBoldSplit/'+Clocation[len(Clocation) - 1]
                image.save(new_filename)
               
run()               

#previous testing notes
    #normal: 1, 8, 
    #Bold text: 208, 209
    #Abnormal: 41, 42, 45, 46, 69, 66, 178, 195, 124
    #No text: 84, 87, 88, 105

    #Normal sequence of colors: ['#FFFF00', '#0C0900', '#EF0900', '#F5F734', '#EAED58']