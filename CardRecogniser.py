import pytesseract
from PIL import Image
import cv2
import numpy as np
import os
import datetime
import shutil
import time

def yellowFilter(img):
    #Mask for yellow image, filter out all these pixels
    lower_yellow = np.array([0, 200, 250])
    upper_yellow = np.array([120, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    img[mask > 0] = (255, 255, 255)
    
def run():
    time.sleep(70)
    #Get the deck name
    #Preset text for output
    Output = "#separator:tab\n#html:false\n#deck column:1\n"
    deck_name = "C:/Users/samue/OneDrive/Desktop/Ankify/Variable/Deckname.txt"
    with open(deck_name, 'r') as file:
        Deck = file.read()
    Deck = str(Deck)
    # Load the image
    Inputpath = "C:/Users/samue/OneDrive/Desktop/Ankify/SlideCardsFiltered/"
    Boldpath = "C:/Users/samue/OneDrive/Desktop/Ankify/NeedBold/"
    #Get items
    BoldFile = os.listdir(Boldpath)
    for item in BoldFile:
        Path = item.split('/')
        #Copy into normal folder for easier processing
        shutil.copy(Boldpath+Path[len(Path) - 1], Inputpath)
    noted = os.listdir(Inputpath)
    Slocation = []
    Reds = []
    card = []
    #Loop through all images
    for itg in noted:
        Slocation = itg.split('/')
        #Find the image 
        img = cv2.imread('C:/Users/samue/OneDrive/Desktop/Ankify/SlideCardsFiltered/'+Slocation[len(Slocation) - 1])
        img2 = cv2.imread('C:/Users/samue/OneDrive/Desktop/Ankify/SlideCardsFiltered/'+Slocation[len(Slocation) - 1])
        img3 = cv2.imread('C:/Users/samue/OneDrive/Desktop/Ankify/SlideCardsFiltered/'+Slocation[len(Slocation) - 1])
        img4 = cv2.imread('C:/Users/samue/OneDrive/Desktop/Ankify/SlideCardsFiltered/'+Slocation[len(Slocation) - 1])

        #Place yellow filter before text recognition
        yellowFilter(img)
        yellowFilter(img2)
        yellowFilter(img3)
        yellowFilter(img4)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for red color in HSV
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        # Create a mask for red text and apply it
        mask = cv2.inRange(hsv, lower_red, upper_red)
        red_text_image = cv2.bitwise_and(img, img, mask=mask)
    # Convert the red text image to grayscale
        gray = cv2.cvtColor(red_text_image, cv2.COLOR_BGR2GRAY)
    # Perform OCR using pytesseract
        redtext = pytesseract.image_to_string(gray)

#Same thing with green text
        
        lower_Green = np.array([40, 135, 40])
        upper_Green = np.array([200, 255, 200])
        # Convert the green text image to grayscale
        hv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
        GreenMask = cv2.inRange(hv, lower_Green, upper_Green)
        img3[GreenMask == 0] = (255, 255, 255)
        # Perform OCR using pytesseract
        Greentext = pytesseract.image_to_string(img3)
        #print("GreenText: ", Greentext)

#Getting the same with all text
        lower_All = (0, 0, 0)
        upper_All = (255, 255, 255)
        height = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)
        AllMask = cv2.inRange(height, lower_All, upper_All)
        img4[AllMask == 0] = (255, 255, 255)
        Alltext = pytesseract.image_to_string(img4)
        line = []

        k = Alltext.split('\n')
        number = []
        for l in range(0, len(k)):
            if k[l] == '':
                number.append(l)
        for j in range(len(number)):
            k.pop(number[j])
            for u in range(len(number)):
                number[u] = number[u] - 1
        for i in range(len(k)):
            if i == 0:
                line.append(len(k[i]))
            else:
                tota = 0
                for n in range(len(line)):
                    tota = line[n] + tota
                line.append(len(k[i]) + tota)
        Alltext = ' '.join(k)
        if len(line) > 0:
            line.pop(len(line) - 1)
        #Place it all in one line
        for u in range(len(line)):
            Alltext = Alltext[:line[u]+1]+Alltext[line[u]+1:]

        #Add in the green formatting
        Greentext = Greentext[:len(Greentext) - 1]
        if len(Greentext) > 0:
            for y in range(len(Alltext) - len(Greentext)):
                if Alltext[y:y+len(Greentext)] == Greentext:
                    Alltext = Alltext[:y]+"<b>"+Alltext[y:y+ len(Greentext)]+"</b>"+Alltext[y+ len(Greentext):]
                    break

        #Removes the red text form the all texrt
        redtext = redtext[:len(redtext) - 1]
        for g in range(len(Alltext)):
            if Alltext[g:g+len(redtext)] == redtext:
                Alltext = Alltext[:g]+Alltext[g+ len(redtext):]
                break
        
        #Duplicates detector, using red text
        Detected = False
        for o in range(len(Reds)):
            if redtext == Reds[o]:
                Detected = True
        if Detected == False:
            Reds.append(redtext)
            card.append(Deck+"\t"+redtext+"\t"+Alltext+"\n")

    for f in range(len(card)):
        Output = Output + card[f]

    now = datetime.datetime.now() # gets the time in string format
    #Set Unique file name
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d" )
    hour = now.strftime("%H")
    min = now.strftime("%M")
    second = now.strftime("%S")
    times = year+month+day+hour+min+second
    #print(time)
    file_name = "C:/Users/samue/OneDrive/Desktop/Ankify/Output/"+times+".txt"
    folder_name = 'C:/Users/samue/OneDrive/Desktop/Ankify/Output/'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    print(Output)
    with open(file_name, "w") as file:
        # Write the content to the file
        
        Output = str(Output)
        file.write(Output)
    print("finnished")

run()