from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognition_system")

        title_lbl = Label(self.root,text="DEVELOPER" , font=("times new roman" , 35 , "bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"Images\dev.jpg")
        img_top = img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
       
        f_lbl=Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0 , y=55 , width=1530 , height=720)

        # Frame
        main_frame = Frame( f_lbl,bd=2,bg="darkblue")
        main_frame.place(x=10,y=30,width=1500,height=630)

        # 1st
        Left_frame1 = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE, font=("times new roman",12,"bold"))
        Left_frame1.place(x=0 , y=0 , width=350 , height=610)
        
        img_top1 = Image.open(r"Images\MY.jpg")
        img_top1 = img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
       
        f_lbl=Label(Left_frame1,image = self.photoimg_top1)
        f_lbl.place(x=70 , y=0 , width=200 , height=200)

        dev_label1 = Label(Left_frame1 , text="Hello My Name is Naman Sharma",bg="white", font=("times new roman",12,"bold"))
        dev_label1.place(x=0 , y=210 )

        # 2ND
        
        Left_frame2 = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE, font=("times new roman",12,"bold"))
        Left_frame2.place(x=370 , y=0 , width=350 , height=610)
      
        img_top2 = Image.open(r"Images\MY.jpg")
        img_top2 = img_top2.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
       
        f_lbl=Label(Left_frame2,image = self.photoimg_top2)
        f_lbl.place(x=70 , y=0 , width=200 , height=200)

        dev_label2 = Label(Left_frame2 , text="Hello My Name is Sahil",bg="white", font=("times new roman",12,"bold"))
        dev_label2.place(x=0 , y=210 )

        # 3rd
        Left_frame3 = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE, font=("times new roman",12,"bold"))
        Left_frame3.place(x=740 , y=0 , width=350 , height=610)
      
        img_top3 = Image.open(r"Images\MY.jpg")
        img_top3 = img_top3.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top3 = ImageTk.PhotoImage(img_top3)
       
        f_lbl=Label(Left_frame3,image = self.photoimg_top3)
        f_lbl.place(x=70 , y=0 , width=200 , height=200)

        dev_label3 = Label(Left_frame3 , text="Hello My Name is Kishore Kant tiwari",bg="white", font=("times new roman",12,"bold"))
        dev_label3.place(x=0 , y=210 )

        # 4th
        Left_frame4 = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE, font=("times new roman",12,"bold"))
        Left_frame4.place(x=1110 , y=0 , width=350 , height=610)
      
        img_top4 = Image.open(r"Images\MY.jpg")
        img_top4 = img_top4.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top4 = ImageTk.PhotoImage(img_top4)
       
        f_lbl=Label(Left_frame4,image = self.photoimg_top4)
        f_lbl.place(x=70 , y=0 , width=200 , height=200)

        dev_label4 = Label(Left_frame4 , text="Hello My Name is Ravi Pratap",bg="white", font=("times new roman",12,"bold"))
        dev_label4.place(x=0 , y=210 )





if __name__ == "__main__":
    root = Tk()
    obj= Developer(root)
    root.mainloop()     