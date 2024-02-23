import numpy as np
import cv2
from PIL import Image
import os
import time 

def zoom(img, zoom_factor=0.66):
        return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)

def run():
    #Set the path for output and make the folder
    output_path = 'C:/Users/samue/OneDrive/Desktop/Ankify/SlideCards/'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    lower = (0, 254, 255)
    upper = (2, 255, 255)
    counter = 0
    #zoom the image out for showing the output
    

    paths = 'C:/Users/samue/OneDrive/Desktop/Ankify/SlidesImage/'
    files = os.listdir(paths)
    ImageCounter = 0
    #Loop all the JPEG images
    for file in files:
        if file.endswith(".jpg"):
            #Get the image
            ImageCounter = ImageCounter + 1
            ImagePath = os.path.join(paths, f'page{ImageCounter}.jpg')
            image = cv2.imread(ImagePath)
            #find colors within specified boundaries and apply the mask (to filter the colours out)
            image = zoom(image)
            #Filter out the colours
            mask = cv2.inRange(image, lower, upper)
            #find the coordinate grid of the image that is zoomed
            coord=cv2.findNonZero(mask)

            try:
                while len(coord) > 0: #there is a card within the image, finding the max and min coordinate for boundaries of box
                    min_x = 9999
                    max_x = 0
                    min_y = 9999
                    max_y = 0
                    coordinate = [0, 0, 0, 0]
                    for i in range(0, len(coord) - 1):
                        if coord[i][0][0] > max_x:
                            max_x = coord[i][0][0]
                            coordinate[0] = i
                        elif int(coord[i][0][0]) < min_x:
                            min_x = coord[i][0][0]
                            coordinate[1] = i
                        if coord[i][0][1] > max_y:
                            max_y = coord[i][0][1]
                            coordinate[2] = i
                        elif coord[i][0][1] < min_y:
                            min_y = coord[i][0][1]
                            coordinate[3] = i
                    #print(max_x)
                    #print(max_y)
                    #print(min_x)
                    #print(min_y)
                    #Set Unique file name with counter
                    #Crop out image
                    crop_img = image[min_y:max_y, min_x:max_x]
                    counter = counter + 1
                    #Store image in temporary storage, unique file name
                    new_filename = os.path.join(output_path, f'card_{counter}.jpg')
                    cv2.imwrite(new_filename, crop_img)
                    break
            #Exception handling to continue the loop
            except:
                #Random command to fill space 
                u = 0
                u = u + 1
run()
