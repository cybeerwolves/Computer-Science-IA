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

def color_to_df(input):
    
    colors_pre_list = str(input).replace('([(','').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')','') for i in colors_pre_list]
    
    #convert RGB to HEX code
    df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(","")),
                          int(i.split(", ")[1]),
                          int(i.split(", ")[2].replace(")",""))) for i in df_rgb]
    df = [df_color_up, df_percent]
    return df


Card_paths = 'C:/Users/5amue1/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCards/'
Cards = os.listdir(Card_paths)
for image in Cards:
    if image.endswith(".jpg"):
        CardCounter = CardCounter + 1
        CardPath = os.path.join(Card_paths, f'card_{CardCounter}.jpg')
        Clocation = CardPath.split('/')
        Card_output = 'C:/Users/5amue1/Desktop/Code/IA for Computer Science/Computer-Science-IA/Cards/'+Clocation[len(Clocation) - 1]
        card = cv2.imread(CardPath)
        colors_x = extcolors.extract_from_path(CardPath, tolerance = 6, limit = 6)
        Color_D = color_to_df(colors_x)
        pixels = 0
        yellow = 0
        for counter in range(0, len(Color_D[1])):
            pixels = pixels + int(Color_D[1][counter])
        for color in range(0, len(Color_D[0])):
            if Color_D[0][color] == "#FFFF00":
                yellow = int(Color_D[1][color])
                break
            elif color == len(Color_D[0]) - 1:
                print(CardPath)
                

0  #FFFF00    100584
1  #0C0900      7060
2  #F8F824      4625
3  #EF0900      3345
4  #F6F63E      1671 