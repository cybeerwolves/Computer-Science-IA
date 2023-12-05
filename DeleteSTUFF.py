import tkinter as tk
from tkinter import *
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

def DEL_files(folderList):
    sortlist=sorted(os.listdir(folderList))       
    i=0
    while(i<len(sortlist)):
        delete_file(folderList+sortlist[i])
        i+=1

def delete_file(del_file):
    if os.path.exists(del_file):
        os.remove(del_file)            

DEL_files("C:/Users/samue/OneDrive/Desktop/Code/IA for Computer Science/Computer-Science-IA/GOOFY AHH FOLDER/")