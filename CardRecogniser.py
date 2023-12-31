import pytesseract
from PIL import Image
import cv2
import numpy as np
import os
import datetime
import time
import shutil

def yellowFilter(img):
    lower_yellow = np.array([0, 200, 250])
    upper_yellow = np.array([120, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    img[mask > 0] = (255, 255, 255)
    
def run():
    time.sleep(120)
    deck_name = "C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Variable/Deckname.txt"
    with open(deck_name, 'r') as file:
        Deck = str(file)
    # Load the image
    Inputpath = "C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCardsFiltered/"
    Boldpath = "C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/NeedBold/"
    BoldFile = os.listdir(Boldpath)
    for item in BoldFile:
        Path = item.split('/')
        shutil.copy(Boldpath+Path[len(Path) - 1], Inputpath)
    noted = os.listdir(Inputpath)
    Slocation = []
    Reds = []
    card = []
    for itg in noted:
        Slocation = itg.split('/')
        img = cv2.imread('C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCardsFiltered/'+Slocation[len(Slocation) - 1])
        img2 = cv2.imread('C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCardsFiltered/'+Slocation[len(Slocation) - 1])
        img3 = cv2.imread('C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCardsFiltered/'+Slocation[len(Slocation) - 1])
        img4 = cv2.imread('C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/SlideCardsFiltered/'+Slocation[len(Slocation) - 1])
        # SUccessful black filter
        #lower_yellow = (0, 130, 130)
        #upper_yellow = (120, 255, 255)

        #normal filtering, would filter out yellow 

        yellowFilter(img)
        yellowFilter(img2)
        yellowFilter(img3)
        yellowFilter(img4)
        Output = "#separator:tab\n#html:true\n#deck column:1\n#tags column:4\n"

        #lower_black = np.array([0, 160, 0])
        #upper_black = np.arr ay([80, 255, 80])
        #hv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
        #mas = cv2.inRange(hv, lower_black, upper_black)
        #img2[mas == 0] = (255, 255, 255)
        #Blacktext = pytesseract.image_to_string(img2)
        #print("blackText: ", Blacktext)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for red color in HSV
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])

        # Create a mask for red text
        mask = cv2.inRange(hsv, lower_red, upper_red)

    # Apply the mask to the image
        red_text_image = cv2.bitwise_and(img, img, mask=mask)

    # Convert the red text image to grayscale
        gray = cv2.cvtColor(red_text_image, cv2.COLOR_BGR2GRAY)

    # Perform OCR using pytesseract
        redtext = pytesseract.image_to_string(gray)

        lower_Green = np.array([40, 135, 40])
        upper_Green = np.array([200, 255, 200])
        hv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
        GreenMask = cv2.inRange(hv, lower_Green, upper_Green)
        img3[GreenMask == 0] = (255, 255, 255)
        Greentext = pytesseract.image_to_string(img3)
        #print("GreenText: ", Greentext)

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
        for u in range(len(line)):
            Alltext = Alltext[:line[u]+1]+"<br>"+Alltext[line[u]+1:]

        Greentext = Greentext[:len(Greentext) - 1]
        if len(Greentext) > 0:
            for y in range(len(Alltext) - len(Greentext)):
                if Alltext[y:y+len(Greentext)] == Greentext:
                    Alltext = Alltext[:y]+"<b>"+Alltext[y:y+ len(Greentext)]+"</b>"+Alltext[y+ len(Greentext):]
                    break

        redtext = redtext[:len(redtext) - 1]
        for g in range(len(Alltext)):
            if Alltext[g:g+len(redtext)] == redtext:
                Alltext = Alltext[:g]+Alltext[g+ len(redtext):]
                break
        
        #Duplicates detector
        Detected = False
        
        for o in range(len(Reds)):
            if redtext == Reds[o]:
                Detected = True
        if Detected == False:
            Reds.append(redtext)
            card.append(Deck+"\t"+redtext+"\t"+Alltext+"\n")

    for f in range(len(card)):
        Output = Output + card[f]
    print(Output)
    now = datetime.datetime.now() # gets the time in string format
    times = now.strftime("%Y%m%H%M")
    #print(time)
    file_name = "C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Output/"+times+".txt"
    folder_name = 'C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/Output/'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(file_name, "w") as file:
        # Write the content to the file
        print(Output)
        file.write(Output)
    print("finnished")

run()

        #Will need to find the location of the Redtext and exclude it from the final product

        #need to learn how to bold in anki card
        #if both not red and not black then green

        # Replace the yellow pixels with white pixels


        # Save the modified image
        # open the image file using the PIL module

        # display the result
        #cv2.imshow('Result', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #text = pytesseract.image_to_string(img)
        #print(text)