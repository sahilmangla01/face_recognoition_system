from tkinter import*
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from dev import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognition_system")

        # Background image
        img4 = Image.open(r"Images\bg-image.jpg")
        img4 = img4.resize((1540,800),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img= Label(self.root ,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1540,height=800)

        title_lbl = Label(bg_img,text="BIOMETRIC ATTENDANCE SYSTEM SOFTWARE" , font=("times new roman" , 35 , "bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=180,width=1530,height=50)

        # ==================time============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl=Label(title_lbl,font=("times new roman" , 14 , "bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # FirstImage
        img1 = Image.open(r"Images\image-1.jpg")
        img1 = img1.resize((500,180),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image = self.photoimg1)
        f_lbl.place(x=0 , y=0 , width=500 , height=180)

        # SecondImage
        img2 = Image.open(r"Images\image-2.png")
        img2 = img2.resize((500,180),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl= Label(self.root ,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=500,height=180)

        # ThirdImage
        img3 = Image.open(r"Images\image-3.jpg")
        img3 = img3.resize((500,180),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl= Label(self.root ,image=self.photoimg3)
        f_lbl.place(x=1020,y=0,width=500,height=180)

        # StudentButton
        img5 = Image.open(r"Images\student.png")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=250 , width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor ="hand2",font=("times new roman" , 15 , "bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=450 , width=220,height=40)


        # DetectButton
        img6= Image.open(r"Images\face-detector.png")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2=Button(bg_img,command=self.face_data,image=self.photoimg6,cursor="hand2")
        b2.place(x=500,y=250 , width=220,height=220)

        b2_1=Button(bg_img,command=self.face_data,text="Face Detection",cursor="hand2",font=("times new roman" , 15 , "bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=450 , width=220,height=40)

        # Attendance
        img7= Image.open(r"Images\attendance.jpg")
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b2=Button(bg_img,command=self.attendance_data,image=self.photoimg7,cursor="hand2")
        b2.place(x=800,y=250 , width=220,height=220)

        b2_1=Button(bg_img,command=self.attendance_data,text="Attendance",cursor="hand2",font=("times new roman" , 15 , "bold"),bg="darkblue",fg="white")
        b2_1.place(x=800,y=450 , width=220,height=40)

        # Help Desk
        img8= Image.open(r"Images\Service-Help-Desk.png")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b2=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_desk)
        b2.place(x=1100,y=250 , width=220,height=220)

        b2_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_desk,font=("times new roman" , 15 , "bold"),bg="darkblue",fg="white")
        b2_1.place(x=1100,y=450 , width=220,height=40)

         # Train data
        img9= Image.open(r"Images\train.jpg")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b2=Button(bg_img,command=self.train_data,image=self.photoimg9,cursor="hand2")
        b2.place(x=200,y=520 , width=220,height=220)

        b2_1=Button(bg_img,command=self.train_data,text="Train Data",cursor="hand2",font=("times new roman" , 15 , "bold"),bg="darkblue",fg="white")
        b2_1.place(x=200,y=720 , width=220,height=40)

        # Image Collection
        img910= Image.open(r"Images\photo.jpg")
        img910 = img910.resize((220,220),Image.ANTIALIAS)
        self.photoimg910 = ImageTk.PhotoImage(img910)

        b2=Button(bg_img,command=self.open_img,image=self.photoimg910,cursor="hand2")
        b2.place(x=500,y=520 , width=220,height=220)

        b2_1=Button(bg_img,command=self.open_img,text="Images",cursor="hand2",font=("times new roman" , 15 , "bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=720 , width=220,height=40)

        # Developer
        img11= Image.open(r"Images\developer.jpg")
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b2=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b2.place(x=800,y=520 , width=220,height=220)

        b2_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman" , 15 , "bold"),bg="darkblue",fg="white")
        b2_1.place(x=800,y=720 , width=220,height=40)

        # Exit
        img12= Image.open(r"Images\exit.jpg")
        img12 = img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b2=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit)
        b2.place(x=1100,y=520 , width=220,height=220)

        b2_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman" , 15 , "bold"),bg="darkblue",fg="white")
        b2_1.place(x=1100,y=720 , width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

     # =====================Function Buttons====================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student( self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Train( self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Face_Recognition( self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Attendance( self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Developer( self.new_window)

    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app = Help( self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj= Face_Recognition_System(root)
    root.mainloop()      