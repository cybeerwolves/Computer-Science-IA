import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# open the image file using the PIL module
img = cv2.imread('C:/Users/samue/OneDrive/Desktop/Ankify/SlideCardsFiltered/card_3.jpg')

def yellowFilter(img):
   lower_yellow = (0, 200, 250)
   upper_yellow = (120, 255, 255)
   hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
   img[mask > 0] = (255, 255, 255)
   #for i in range(len(mask)):
   #   if mask[i][0] == True:
    #     img[i][0] = (255, 255, 255)

yellowFilter(img)
#blue, green, red
lower_red = (0, 180, 170)
upper_red = (100, 255, 255)
hs = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)    # Create a mask for the yellow color
mask = cv2.inRange(hs, lower_red, upper_red)
img[mask == 0] = (255, 255, 255)
redtext = pytesseract.image_to_string(img)
cv2.imshow('Result', img)

print("Red text: ", redtext)
cv2.waitKey(0)
cv2.destroyAllWindows()