import numpy as np
import cv2
from PIL import Image

#zoom the image out for showing the output
def zoom(img, zoom_factor=0.66):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)

image = cv2.imread('SlidesImage/3.7 Supply-side Policies.pdf/page2.jpg')

lower = (0, 254, 255)
upper = (2, 255, 255)
#create numpy array from boundaries
#lower = np.array(lower, dtype = "uint8")
#upper = np.array(upper, dtype = "uint8")
#find colors within specified boundaries and apply the mask (to filter the colours out)
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)
zoomed_output = zoom(output)

#find the coordinate grid of the image that is zoomed
coord=cv2.findNonZero(mask)
print(coord[0][0][0])
print(coord[len(coord) - 1][0][0])
crop_img = image[coord[0][0][0]:coord[len(coord) - 1][0][0], coord[0][0][1]:coord[len(coord) - 1][0][0]]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)

#display the image
#cv2.imshow('images', np.hstack([output]))
cv2.imshow('images', zoomed_output)
cv2.waitKey(0)