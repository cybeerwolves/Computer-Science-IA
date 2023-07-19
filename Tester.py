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

def color_to_df(input):
    
    colors_pre_list = str(input).replace('([(','').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')','') for i in colors_pre_list]
    
    #convert RGB to HEX code
    #df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(","")),
    #                      int(i.split(", ")[1]),
     #                     int(i.split(", ")[2].replace(")",""))) for i in df_rgb]
    #df = [df_color_up, df_percent]
    df = df_rgb
    return df

CardPath = 'C:/Users/5amue1/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCards/card_124.jpg'
colors_x = extcolors.extract_from_path(CardPath, tolerance = 10, limit = 5)
Color_D = color_to_df(colors_x)
print(Color_D)
#normal: 1, 8, 
#Bold text: 208, 209
#Abnormal: 41, 42, 45, 46, 69, 66, 178, 195, 124
#No text: 84, 87, 88, 105

#Normal sequence of colors: ['#FFFF00', '#0C0900', '#EF0900', '#F5F734', '#EAED58']