#This document filters out and seperates out the different images onto individual cards of which can be used to have the recognition method applied
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
Colors = []
def color_to_df(input):
    
    colors_pre_list = str(input).replace('([(','').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')','') for i in colors_pre_list]
    #convert RGB to HEX code
    df = [df_rgb, df_percent]
    print(df)
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
        #print(name, distance)
        if distance < closest_distance:
            closest_distance = distance
            closest_color = name
    return closest_color

CardPath = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCardsFiltered/card_1.jpg'
card = cv2.imread(CardPath)
colors_x = extcolors.extract_from_path(CardPath, tolerance = 30, limit = 9)
Color_D = color_to_df(colors_x)
for i in range(0, len(Color_D[0])):
    Contain = False
    Color_D[0][i] = Color_D[0][i][1:len(Color_D[0][i]) - 1]
    Color_D[0][i] = Color_D[0][i].split(", ")
    print(Color_D[0][i])
    Color_D[0][i] = [int(x) for x in Color_D[0][i]]
    Color = identify_color(Color_D[0][i][0], Color_D[0][i][1], Color_D[0][i][2])
    print(Color)
    for u in range(0, len(Colors)):
        if Color == Colors[u]:
            Contain = True
    if Contain == False:
        Colors.append(Color)
print(Colors)
                

0  #FFFF00    100584
1  #0C0900      7060
2  #F8F824      4625
3  #EF0900      3345
4  #F6F63E      1671 