from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognition_system")

        title_lbl = Label(self.root,text="HELP DESK" , font=("times new roman" , 35 , "bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"Images\hlp.webp")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
       
        f_lbl=Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0 , y=55 , width=1530 , height=720)

        dev_label4 = Label(f_lbl , text="Email: Manglasahil9050@gmail.com",fg="blue",bg="white", font=("times new roman",20,"bold"))
        dev_label4.place(x=550 , y=260 )


if __name__ == "__main__":
    root = Tk()
    obj= Help(root)
    root.mainloop()   