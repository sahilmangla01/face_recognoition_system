from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

        # =====================variables============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        # Background image
        img4 = Image.open(r"C:\Users\magla\OneDrive\Desktop\Face Recognition Attendence System\Images\bg-image.jpg")
        img4 = img4.resize((1540,800),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img= Label(self.root ,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1540,height=800)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM" , font=("times new roman" , 35 , "bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=130,width=1530,height=40)

        # FirstImage
        img1 = Image.open(r"C:\Users\magla\OneDrive\Desktop\Face Recognition Attendence System\Images\sms-1.png")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image = self.photoimg1)
        f_lbl.place(x=0 , y=0 , width=500 , height=130)

        # SecondImage
        img2 = Image.open(r"C:\Users\magla\OneDrive\Desktop\Face Recognition Attendence System\Images\image-2.png")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl= Label(self.root ,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=500,height=130)

        # ThirdImage
        img3 = Image.open(r"C:\Users\magla\OneDrive\Desktop\Face Recognition Attendence System\Images\sms-2.png")
        img3 = img3.resize((520,130),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl= Label(self.root ,image=self.photoimg3)
        f_lbl.place(x=1020,y=0,width=520,height=130)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=175,width=1500,height=630)
        # left label Frame
        Left_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=5 , y=0 , width=720 , height=610)
        
        img_left = Image.open(r"C:\Users\magla\OneDrive\Desktop\Face Recognition Attendence System\Images\sms-detail.png")
        img_left = img_left.resize((400,150),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=150,y=0,width=400, height=150)

        # current course
        current_course_frame = LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Current course information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5 , y=145 , width=700 , height=110)

        # Department
        dep_label = Label(current_course_frame , text="Department",bg="white", font=("times new roman",12,"bold"))
        dep_label.grid(row=0 , column=0 , padx=10 ,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width =20,state="readonly")
        dep_combo["values"]= ("Select Department","Chemical Engineering", "Civil Engineering","Computer and Science","Electrical Engineering","Mechanical Engineering ")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Course
        course_label = Label(current_course_frame,text ="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width =20,state="readonly")
        course_combo["values"]=("Select Course","FE", "SE" , "TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        Year_label = Label(current_course_frame,text ="Year",font=("times new roman",12,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)

        Year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width =20,state="readonly")
        Year_combo["values"]=("Select Year","2019-20", "2020-21" , "2021-22","2022-23","2023-24")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label = Label(current_course_frame,text ="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width =20,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1", "Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

         # Student course
        student_frame = LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Student Information", font=("times new roman",12,"bold"))
        student_frame.place(x=5 , y=255 , width=700 , height=330)

        # StudentID
        studentId_label = Label(student_frame,text ="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student Name
        studentName_label = Label(student_frame,text ="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Class Division
        class_div_label = Label(student_frame,text ="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_combo = ttk.Combobox(student_frame,textvariable=self.var_div,width=18,font=("times new roman",12,"bold"),state="readonly")
        class_div_combo["values"]=("Select Division","A", "B" , "C","D","E","F","G","H")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


         # Roll no.
        Rollno_label = Label(student_frame,text ="Roll No:",font=("times new roman",12,"bold"),bg="white")
        Rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Rollno_entry=ttk.Entry(student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        Rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #Gender
        gender_label = Label(student_frame,text ="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

       
        gender_combo = ttk.Combobox(student_frame,textvariable=self.var_gender,width=18,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select Gender","Male", "Female" , "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

         # Date of birth
        dob_label = Label(student_frame,text ="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)



         #Email
        email_label = Label(student_frame,text ="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         # phone no
        phoneNo_label = Label(student_frame,text ="Phone no:",font=("times new roman",12,"bold"),bg="white")
        phoneNo_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phoneNo_entry=ttk.Entry(student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         #Address
        address_label = Label(student_frame,text ="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

         #Teacher Name
        teacher_label = Label(student_frame,text ="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radioButton
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Photo Sample", value="YES")
        radiobtn1.grid(row=6, column=0)

        
        radiobtn2 = ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No Photo Sample", value="NO")
        radiobtn2.grid(row=6, column=1)

        # Button Frame1
        button_frame1 = Frame(student_frame,bd=2,relief=RIDGE, bg="white")
        button_frame1.place(x=5,y=210, width=680 , height=35)

        # save button
        savebtn = Button(button_frame1,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        savebtn.grid(row=0, column=0)

        # Update
        updatebtn = Button(button_frame1,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        updatebtn.grid(row=0, column=1)

        # Delete
        deletebtn = Button(button_frame1,command=self.delete_data,text="Delete",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        deletebtn.grid(row=0, column=2)

        # Reset
        resetbtn = Button(button_frame1,command=self.reset_data,text="Reset",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        resetbtn.grid(row=0, column=3)

         # Button Frame2
        button_frame2 = Frame(student_frame,bd=2,relief=RIDGE, bg="white")
        button_frame2.place(x=5,y=247, width=680 , height=35)


         # Take a photo sample
        takePhotobtn = Button(button_frame2,command=self.generate_dataset,text="Take Photo Sample",width=37,font=("times new roman",12,"bold"),bg="blue",fg="white")
        takePhotobtn.grid(row=1, column=0)

         #Update Photo Sample
        UpdatePhotobtn = Button(button_frame2,text="Update Photo Sample",width=37,font=("times new roman",12,"bold"),bg="blue",fg="white")
        UpdatePhotobtn.grid(row=1, column=1)


        # Right label Frame
        Right_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student details", font=("times new roman",12,"bold"))
        Right_frame.place(x=740 , y=0 , width=740 , height=610)
         
        #  Image in right frame
        img_right = Image.open(r"C:\Users\magla\OneDrive\Desktop\Face Recognition Attendence System\Images\rightimage.webp")
        img_right = img_right.resize((400,150),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=150,y=0,width=400, height=150)

        # ==================Search System=====================
        search_frame = LabelFrame(Right_frame,bg="white",bd=2,relief=RIDGE,text="Search System", font=("times new roman",12,"bold"))
        search_frame.place(x=5 , y=155 , width=726 , height=80)

        search_label = Label(search_frame,text ="Search By:",font=("times new roman",12,"bold"),bg="red", fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width =15,state="readonly")
        search_combo["values"]=("Select ", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=17,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Search",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame,text="Show All",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # ===========================Table Frame===========================
        table_frame = Frame(Right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5 , y=220 , width=726 , height=365)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course" ,"year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department" )
        self.student_table.heading("course",text="Course" )
        self.student_table.heading("year",text="Year" )
        self.student_table.heading("sem",text="Semester" )
        self.student_table.heading("id",text="StudentId" )
        self.student_table.heading("name",text="Name" )
        self.student_table.heading("div",text="Division" )
        self.student_table.heading("roll",text="RollNo" )
        self.student_table.heading("gender",text="Gender" )
        self.student_table.heading("dob",text="DOB" )
        self.student_table.heading("email",text="Email" )
        self.student_table.heading("phone",text="Phone" )
        self.student_table.heading("address",text="Address" )
        self.student_table.heading("teacher",text="Teacher" )
        self.student_table.heading("photo",text="PhotoSampleStatus" )
        self.student_table["show"]= "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100) 

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # =======================Function Declaration=========================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()== "" or self.var_std_id.get()== "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@#Sahil123456",database="face_recognizor")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()

                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully", parent= self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)

    # ====================fetch data==================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@#Sahil123456",database="face_recognizor")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ===================get cursor==================
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),   
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),    
        self.var_roll.set(data[7]),   
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ===================update Function==============
    def update_data(self):   
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()== "" or self.var_std_id.get()== "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details", parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="@#Sahil123456",database="face_recognizor")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_std_id.get()
                    
                                                                                                                                                                            ))
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # =========================delete function==================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want oto delete this student information",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="@#Sahil123456",database="face_recognizor")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()   
                messagebox.showinfo("Success","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    # ===================reset=============
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),   
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),    
        self.var_roll.set(""),   
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


    # ============================Generate data set or take photo sample===========================
    def generate_dataset(self):  
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()== "" or self.var_std_id.get()== "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@#Sahil123456",database="face_recognizor")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_std_id.get()==id+1
                    
                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ==============load predefined data on face frontols from opencv===============
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap= cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,225,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                        
                


 




       


if __name__ == "__main__":
    root = Tk()
    obj= Student(root)
    root.mainloop()         