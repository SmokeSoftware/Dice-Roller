import tkinter as tk
import random
from tkinter import *
from PIL import Image,ImageTk

dice_1 = None
dice_2 = None

BG_COLOR = random.choice(["green","blue","salmon","lime","black","red"])

DİCE_ROLLİNG_APP = tk.Tk()
DİCE_ROLLİNG_APP.title("DİCE ROLLİNG APPLİCATİON")
DİCE_ROLLİNG_APP.minsize(350,300)
DİCE_ROLLİNG_APP.maxsize(350,300)

DİCE_ROLLİNG_APP.config(bg = BG_COLOR)

dice1_pic = ImageTk.PhotoImage(Image.open("dice1.png"))
dice2_pic = ImageTk.PhotoImage(Image.open("dice2.png"))
dice3_pic = ImageTk.PhotoImage(Image.open("dice3.png"))
dice4_pic = ImageTk.PhotoImage(Image.open("dice4.png"))
dice5_pic = ImageTk.PhotoImage(Image.open("dice5.png"))
dice6_pic = ImageTk.PhotoImage(Image.open("dice6.png"))

def DİCE():
    global dice_1
    global dice_2
    dice_1 = random.choice(["1","2","3","4","5","6"])
    dice_2 = random.choice(["1","2","3","4","5","6"])
    
    if dice_1 == "1" and dice_2 == "1":
        DİCE_1_1.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_1.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        

    elif dice_1 == "1" and dice_2 == "2":
        DİCE_1_1.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_2.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        

    elif dice_1 == "1" and dice_2 == "3":
        DİCE_1_1.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_3.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "1" and dice_2 == "4":
        DİCE_1_1.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_4.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "1" and dice_2 == "5":
        DİCE_1_1.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_5.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "1" and dice_2 == "6":
        DİCE_1_1.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_6.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "2" and dice_2 == "1":
        DİCE_1_2.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_1.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "2" and dice_2 == "2":
        DİCE_1_2.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_2.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "2" and dice_2 == "3":
        DİCE_1_2.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_3.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "2" and dice_2 == "4":
        DİCE_1_2.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_4.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "2" and dice_2 == "5":
        DİCE_1_2.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_5.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "2" and dice_2 == "6":
        DİCE_1_2.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_6.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "3" and dice_2 == "1":
        DİCE_1_3.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_1.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "3" and dice_2 == "2":
        DİCE_1_3.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_2.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "3" and dice_2 == "3":
        DİCE_1_3.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_3.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "3" and dice_2 == "4":
        DİCE_1_3.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_4.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
  
    elif dice_1 == "3" and dice_2 == "5":
        DİCE_1_3.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_5.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "3" and dice_2 == "6":
        DİCE_1_3.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_6.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "4" and dice_2 == "1":
        DİCE_1_4.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_1.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "4" and dice_2 == "2":
        DİCE_1_4.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_2.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "4" and dice_2 == "3":
        DİCE_1_4.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_3.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "4" and dice_2 == "4":
        DİCE_1_4.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_4.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "4" and dice_2 == "5":
        DİCE_1_4.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_5.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "4" and dice_2 == "6":
        DİCE_1_4.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_6.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "5" and dice_2 == "1":
        DİCE_1_5.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_1.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
       
    elif dice_1 == "5" and dice_2 == "2":
        DİCE_1_5.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_2.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "5" and dice_2 == "3":
        DİCE_1_5.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_3.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "5" and dice_2 == "4":
        DİCE_1_5.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_4.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "5" and dice_2 == "5":
        DİCE_1_5.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_5.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "5" and dice_2 == "6":
        DİCE_1_5.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_6.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        
    elif dice_1 == "6" and dice_2 == "1":
        DİCE_1_6.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_1.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "6" and dice_2 == "2":
        DİCE_1_6.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_2.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)

    elif dice_1 == "6" and dice_2 == "3":
        DİCE_1_6.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_3.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
       
    elif dice_1 == "6" and dice_2 == "4":
        DİCE_1_6.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_4.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
      
    elif dice_1 == "6" and dice_2 == "5":
        DİCE_1_6.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_5.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)
      
    elif dice_1 == "6" and dice_2 == "6":
        DİCE_1_6.place(width = 80,height = 80,x = 50,y = 50)
        DİCE_2_6.place(width = 80,height = 80,x = 220,y = 50)
        DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)
        DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)

DİCE_BUTTON = tk.Button(DİCE_ROLLİNG_APP,text = "DİCE",fg = "lime",bg = "black",activebackground = "lime",activeforeground = "black",font = "Arial 70",command = DİCE)
DİCE_BUTTON.place(width = 350,height = 100,x = 0,y = 200)

DİCE_1_1 = tk.Label(DİCE_ROLLİNG_APP,image = dice1_pic,bg = "red")
DİCE_1_1.place(width = 80,height = 80,x = -500,y = 0)

DİCE_1_2 = tk.Label(DİCE_ROLLİNG_APP,image = dice2_pic,bg = "red")
DİCE_1_2.place(width = 80,height = 80,x = -500,y = 0)

DİCE_1_3 = tk.Label(DİCE_ROLLİNG_APP,image = dice3_pic,bg = "red")
DİCE_1_3.place(width = 80,height = 80,x = -500,y = 0)

DİCE_1_4 = tk.Label(DİCE_ROLLİNG_APP,image = dice4_pic,bg = "red")
DİCE_1_4.place(width = 80,height = 80,x = -500,y = 0)

DİCE_1_5 = tk.Label(DİCE_ROLLİNG_APP,image = dice5_pic,bg = "red")
DİCE_1_5.place(width = 80,height = 80,x = -500,y = 0)

DİCE_1_6 = tk.Label(DİCE_ROLLİNG_APP,image = dice6_pic,bg = "red")
DİCE_1_6.place(width = 80,height = 80,x = -500,y = 0)

DİCE_2_1 = tk.Label(DİCE_ROLLİNG_APP,image = dice1_pic,bg = "red")
DİCE_2_1.place(width = 80,height = 80,x = -500,y = 0)

DİCE_2_2 = tk.Label(DİCE_ROLLİNG_APP,image = dice2_pic,bg = "red")
DİCE_2_2.place(width = 80,height = 80,x = -500,y = 0)

DİCE_2_3 = tk.Label(DİCE_ROLLİNG_APP,image = dice3_pic,bg = "red")
DİCE_2_3.place(width = 80,height = 80,x = -500,y = 0)

DİCE_2_4 = tk.Label(DİCE_ROLLİNG_APP,image = dice4_pic,bg = "red")
DİCE_2_4.place(width = 80,height = 80,x = -500,y = 0)

DİCE_2_5 = tk.Label(DİCE_ROLLİNG_APP,image = dice5_pic,bg = "red")
DİCE_2_5.place(width = 80,height = 80,x = -500,y = 0)

DİCE_2_6 = tk.Label(DİCE_ROLLİNG_APP,image = dice6_pic,bg = "red")
DİCE_2_6.place(width = 80,height = 80,x = -500,y = 0)

DİCE_ROLLİNG_APP.mainloop()
