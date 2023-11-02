import numpy as np
import cv2
from PIL import Image
import os

lower = (0, 254, 255)
upper = (2, 255, 255)
counter = 0
#zoom the image out for showing the output
def zoom(img, zoom_factor=0.66):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)

PDFcounter = 0
paths = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlidesImage/'
notice = os.listdir(paths)
for fil in notice:
    if fil.endswith(".pdf"):
        path = os.path.join(paths, f'{notice[PDFcounter]}')
        PDFcounter = PDFcounter + 1
        files = os.listdir(path)
        ImageCounter = 0
        for file in files:
            if file.endswith(".jpg"):
                ImageCounter = ImageCounter + 1
                ImagePath = os.path.join(path, f'page{ImageCounter}.jpg')
                image = cv2.imread(ImagePath)
                #create numpy array from boundaries
                #lower = np.array(lower, dtype = "uint8")
                #upper = np.array(upper, dtype = "uint8")
                #find colors within specified boundaries and apply the mask (to filter the colours out)
                image = zoom(image)
                mask = cv2.inRange(image, lower, upper)
                output = cv2.bitwise_and(image, image, mask = mask)
                #zoomed_output = zoom(output)
                point1 = False
                point2 = False
                #find the coordinate grid of the image that is zoomed
                coord=cv2.findNonZero(mask)
                try:
                    while len(coord) > 0: #there is a card within the image
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
                        #need a loop to find max and min
                        counter = counter + 1
                        crop_img = image[min_y:max_y, min_x:max_x]
                        output_path = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCards/'
                        if not os.path.exists(output_path):
                            os.makedirs(output_path)
                        new_filename = os.path.join(output_path, f'card_{counter}.jpg')
                        cv2.imwrite(new_filename, crop_img)
                        break
                    


                        #crop_img = image[289:432, 30:935] #y, x format


                    #point1 = False
                        #point2 = False
                        #for i in range(0, len(coord) - 1):
                        #   if coord[i][0][0] + 4 > max_x:
                        #        if coord[i][0][1] - 1 < min_y:
                    #             point1 = True
                    #      elif coord[i][0][0] - 4 < min_x:
                    #           if coord[i][0][1] + 1 < max_y:
                                # point2 = True
                except:
                    u = 0
                    u = u + 1
