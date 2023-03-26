from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recognition_system")

        self.var_atten_id =StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        img1 = Image.open(r"Images\sms-1.png")
        img1 = img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image = self.photoimg1)
        f_lbl.place(x=0 , y=0 , width=800 , height=200)


        img2 = Image.open(r"Images\attendance02.jpg")
        img2 = img2.resize((800,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl= Label(self.root ,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=800,height=200)

        title_lbl = Label(self.root,text="ATTENDANCE SYSTEM" , font=("times new roman" , 35 , "bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=200,width=1530,height=40)

        main_frame = Frame(self.root,bd=2,bg="white")
        main_frame.place(x=10,y=250,width=1500,height=630)
        
        Left_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Attendance Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=5 , y=0 , width=720 , height=610)

        img_left = Image.open(r"Images\attendance03.jpeg")
        img_left = img_left.resize((400,150),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=150,y=0,width=400, height=150)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=155,width=715,height=370)

        # attendanceid
        attendanceID_label = Label(left_inside_frame,text ="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0)

        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,pady=8,sticky=W)

        # Roll
        roll_label = Label(left_inside_frame,text ="Roll:",font=("comicsansns",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2)
        roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("comicsansns",12,"bold"))
        roll_entry.grid(row=0,column=3,pady=8,sticky=W)

        # Name
        name_label = Label(left_inside_frame,text ="Name:",font=("comicsansns",12,"bold"),bg="white")
        name_label.grid(row=1,column=0)
        name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("comicsansns",12,"bold"))
        name_entry.grid(row=1,column=1,pady=8,sticky=W)

        # Department
        department_label = Label(left_inside_frame,text ="Department:",font=("comicsansns",12,"bold"),bg="white")
        department_label.grid(row=1,column=2)
        department_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("comicsansns",12,"bold"))
        department_entry.grid(row=1,column=3,pady=8,sticky=W)

        # time
        time_label = Label(left_inside_frame,text ="Time:",font=("comicsansns",12,"bold"),bg="white")
        time_label.grid(row=2,column=0)
        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("comicsansns",12,"bold"))
        time_entry.grid(row=2,column=1,pady=8,sticky=W)

        # Date
        Date_label = Label(left_inside_frame,text ="Date:",font=("comicsansns",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2)
        Date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("comicsansns",12,"bold"))
        Date_entry.grid(row=2,column=3,pady=8,sticky=W)

    # attendance
        attendance_label = Label(left_inside_frame,text ="Attendance Status:",font=("comicsansns",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=20,font=("comicsansns",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

         # Button Frame1
        button_frame1 = Frame(left_inside_frame,bd=2,relief=RIDGE, bg="white")
        button_frame1.place(x=5,y=300, width=680 , height=35)

        # Import button
        savebtn = Button(button_frame1,command=self.importCsv,text="Import csv",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        savebtn.grid(row=0, column=0)

        # Export
        updatebtn = Button(button_frame1,command=self.exportCsv,text="Export csv",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        updatebtn.grid(row=0, column=1)

        # Update
        deletebtn = Button(button_frame1,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        deletebtn.grid(row=0, column=2)

        # Reset
        resetbtn = Button(button_frame1,command=self.reset_data,text="Reset",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        resetbtn.grid(row=0, column=3)


        Right_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Attendance Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=740 , y=0 , width=740 , height=610)
        
        table_frame = Frame(Right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5 , y=5 , width=726 , height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendanceReportTable = ttk.Treeview(table_frame, columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("id",text="Attendance ID")
        self.attendanceReportTable.heading("roll",text="Roll")
        self.attendanceReportTable.heading("name",text="Name")
        self.attendanceReportTable.heading("department",text="Department")
        self.attendanceReportTable.heading("time",text="Time")
        self.attendanceReportTable.heading("date",text="Date")
        self.attendanceReportTable.heading("attendance",text="Attendance")

        self.attendanceReportTable["show"]="headings"

        self.attendanceReportTable.column("id",width=100)
        self.attendanceReportTable.column("roll",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=100)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendance",width=100)


        self.attendanceReportTable.pack(fill=BOTH,expand=1)
        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("", END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln)as myFile:
            csvRead = csv.reader(myFile,delimiter=",")
            for i in csvRead:
                mydata.append(i)
            self.fetchData(mydata)  

    
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w") as myFile:
                export=csv.writer(myFile,lineterminator='\n',delimiter=",")
                for i in mydata:
                    export.writerow(i)
                messagebox.showinfo("Data Export","Your data Exported to"+os.path.basename(fln)+"successfully",parent=self.root)    
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)

    def get_cursor(self,event=""):
        cursor_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



if __name__ == "__main__":
    root = Tk()
    obj= Attendance(root)
    root.mainloop() 