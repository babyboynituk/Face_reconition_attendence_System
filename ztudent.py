from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector  
import cv2
 






class Student_Details:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title(" Student Details")
        
        
        ##### decalrartin of Variable for table store data
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stdID=StringVar()
        self.var_stdName=StringVar()
        self.var_stdrollno=StringVar()
        self.var_stdgroup=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_coordinator=StringVar()
        self.var_mobileNo=StringVar()
        self.var_Address=StringVar()
         
         


        #first image1
        img1=Image.open(r"C:\Users\kumar\Desktop\college_images\face-recognition.png" )# for calling the images fromfolder to window
        img1=img1.resize((500,130)  )# for resizing the image
        self.photoimg1=ImageTk.PhotoImage(img1) 
        f1_lbl=Label(self.root,image=self.photoimg1)# ye label self ke andar banega
        f1_lbl.place(x=0, y=0,width=500, height=130) # decide the position of image in window by using place method
        
        
        #second image
        img2=Image.open(r"C:\Users\kumar\Desktop\college_images\smart-attendance.jpg" )# for calling the images fromfolder to window
        img2=img2.resize((500,130)  )# fro resizing the image
        self.photoimg2=ImageTk.PhotoImage(img2) 
        f1_lbl=Label(self.root,image=self.photoimg2)# ye label self ke andar banega
        f1_lbl.place(x=500, y=0,width=500, height=130) # it is for decide the position of image in window by using place method
        
        
        #third image
        img3=Image.open(r"C:\Users\kumar\Desktop\college_images\photo.jpg" )# for calling the images fromfolder to window
        img3=img3.resize((500,130)  )# fro resizing the image
        self.photoimg3=ImageTk.PhotoImage(img3) 
        f1_lbl=Label(self.root,image=self.photoimg3)# ye label self ke andar banega
        f1_lbl.place(x=1000, y=0,width=550, height=130) # it is for decide the position of image in window by using place method
        
        
         #background image
        bg_img=Image.open(r"C:\Users\kumar\Desktop\college_images\wp2551980.jpg  " )# for calling the images fromfolder to window
        bg_img=bg_img.resize((1530,730)  )# fro resizing the image
        self.bg_photoimg=ImageTk.PhotoImage(bg_img) 
        bg_lbl=Label(self.root,image=self.bg_photoimg)# ye label self ke andar banega
        bg_lbl.place(x=0, y=130,width=1530, height=710) # it is for decide the position of image in window by using place method()
         #for title in bg_img 
        title_lbl=Label(bg_lbl,text=" Student Management System",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
         
        
        
        #main frame on background image,bd means border of frame
        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=60,width=1455,height=640)
        
        
        
        # left Side label frame 
        label_frameleft=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Details",font=("tomes new roman",12,"bold"))#relief is used for border size
        label_frameleft.place(x=10,y=5,width=720,height=620)
        
        
        #left frame image 
        left_img=Image.open(r"C:\Users\kumar\Desktop\college_images\thirds.jpg " )# for calling the images fromfolder to window
        left_img=left_img.resize((710,130)  )# fro resizing the image
        self.photoleftimg=ImageTk.PhotoImage(left_img) 
        
        f1_lbl=Label( label_frameleft,image=self.photoleftimg)# ye label self ke andar banega
        f1_lbl.place(x=5, y=0,width=708, height=130) # it is for decide the position of image in window by using place method
        
        #label frame inside left label frame and current course
        current_frame=LabelFrame( label_frameleft,bd=2,bg="white",relief=RIDGE,text="Current Course Informations",font=("times new roman",12,"bold"))#relief is used for border size
        current_frame.place(x=5,y=130,width=708,height=130)
        
        
        #department label
        dep_label=Label(current_frame,text="Deparment",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)#here grid property is used
        
        
        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dept,font=("times new roman",12,"bold"),width=25,state='readonly')
        #Here with help of tuple we dedign select box 
        dep_combo["values"]=("Select Department","Civil Engineering","Computer Science Engineering","Electronic and Communication Engineering","Electrical and Electronics Engineering","Other")
        dep_combo.current(0)# initily select deparment
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
          
          # course label
        course_label=Label(current_frame, text="Course",font=("times new roman",12,"bold"),bg='white')
        course_label.grid(row=0,column=2,padx=10,sticky=W)#here grid property is used
        
        #combo label
        course_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=25,state='readonly')
        #Here with help of tuple we dedign select box 
        course_combo["values"]=("Select Course"," Digital Electronics"," Signal and System"," BAsic Electrical Engineering"," Solid State Devices","Electromagnetism","other")
        course_combo.current(0)# initily select deparment
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        
        # year
        year_label=Label(current_frame,text=" Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0, padx=10,sticky=W)#here grid property is used
        
        
        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=25,state='readonly')
        #Here with help of tuple we dedign select box 
        year_combo["values"]=("Select Year", "2018","2019", "2020"," 2021"," 2022"," 2023"," 2024")
        year_combo.current(0)# initily select deparment
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        
        # semester
        semester_label=Label(current_frame,text=" Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2, padx=10,sticky=W)#here grid property is used
        
        
        semester_combo=ttk.Combobox(current_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=25,state='readonly')
        #Here with help of tuple we dedign select box 
        semester_combo["values"]=("Select the semester ", "first","second", "third"," fourth"," fifth"," six"," seventh","eight","other")
        semester_combo.current(0)# initily select deparment
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        
        #label frame inside left label frame and class  student information frame
        class_Student_Information_frame=LabelFrame( label_frameleft,bd=2,bg="white",relief=RIDGE,text=" Student Class Information",font=("times new roman",12,"bold"))#relief is used for border size)
        class_Student_Information_frame.place(x=5,y=265,width=708,height=325)
        
        
        # StudentId
        studentId_label=Label( class_Student_Information_frame,text="ID",font=("times new roman",12,"bold"))
        studentId_label.grid(row=0,column=0, padx=10,sticky=W)#here grid property is used
        
        #entry box
        studentID_entryBox=ttk.Entry( class_Student_Information_frame,textvariable=self.var_stdID,width=27,font=("times new roman",12,"bold"))
        studentID_entryBox.grid(row=0,column=1,padx=2,pady=10,sticky=W )
        
        
        # StudentName
        studentName_label=Label( class_Student_Information_frame,text="Name",font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2, padx=10,sticky=W)#here grid property is used
        
        #entry box
        studentName_entryBox=ttk.Entry( class_Student_Information_frame,textvariable=self.var_stdName,width=27,font=("times new roman",12,"bold"))
        studentName_entryBox.grid(row=0,column=3,padx=2,pady=10,sticky=W )
        
        # Student Roll Number
        Roll_No_label=Label( class_Student_Information_frame,text="Roll_No",font=("times new roman",12,"bold"))
        Roll_No_label.grid(row=1,column=0, padx=10,sticky=W)#here grid property is used
        
        #entry box
        Roll_No_entryBox=ttk.Entry( class_Student_Information_frame,textvariable=self.var_stdrollno,width=27,font=("times new roman",12,"bold"))
        Roll_No_entryBox.grid(row=1,column=1,padx=2,pady=10,sticky=W )
        
        
         # Student Group
        studentGroup_label=Label( class_Student_Information_frame,text="Group",font=("times new roman",12,"bold"))
        studentGroup_label.grid(row=1,column=2, padx=10,sticky=W)#here grid property is used
        
         
        group_combo=ttk.Combobox( class_Student_Information_frame,textvariable=self.var_stdgroup ,font=("times new roman",12,"bold"),width=25,state='readonly')
        #Here with help of tuple we dedign select box 
        group_combo["values"]=("select group","G1", "G2","G3","G4","other" )
        group_combo.current(0)# initily select deparment
        group_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        
        
        
        #  Gender
        gender_label=Label( class_Student_Information_frame,text="Gender",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0, padx=10,sticky=W)#here grid property is used
        
         
        gneder_combo=ttk.Combobox( class_Student_Information_frame,textvariable=self.var_gender ,font=("times new roman",12,"bold"),width=25,state='readonly')
        #Here with help of tuple we dedign select box 
        gneder_combo["values"]=(" Male", "Female","Other" )
        gneder_combo.current(0)# initily select deparment
        gneder_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
        
        #  Mobile Number
        mobileNumber_label=Label( class_Student_Information_frame,text="MobileNO",font=("times new roman",12,"bold"))
        mobileNumber_label.grid(row=2,column=2, padx=10,sticky=W)#here grid property is used
        
        #entry box
        mobileNumber_entryBox=ttk.Entry( class_Student_Information_frame,textvariable=self.var_mobileNo,width=27,font=("times new roman",12,"bold"))
        mobileNumber_entryBox.grid(row=2,column=3,padx=2,pady=10,sticky=W )
        
        # DOB
        DOB_label=Label( class_Student_Information_frame,text="DOB",font=("times new roman",12,"bold"))
        DOB_label.grid(row=3,column=0, padx=10,sticky=W)#here grid property is used
        
        #entry box
        DOB_entryBox=ttk.Entry( class_Student_Information_frame,textvariable=self.var_dob,width=27,font=("times new roman",12,"bold"))
        DOB_entryBox.grid(row=3,column=1,padx=2,pady=10,sticky=W )
        
         #  Email
        Email_label=Label( class_Student_Information_frame,text="EmailID",font=("times new roman",12,"bold"))
        Email_label.grid(row=3,column=2, padx=10,sticky=W)#here grid property is used
        
        #entry box
        Email_entryBox=ttk.Entry( class_Student_Information_frame,textvariable=self.var_email,width=27,font=("times new roman",12,"bold"))
        Email_entryBox.grid(row=3,column=3,padx=2,pady=10,sticky=W )
        
        
        
         #  Course_Cordinator
        Course_Cordinator_label=Label( class_Student_Information_frame,text="coordinator",font=("times new roman",12,"bold"))
        Course_Cordinator_label.grid(row=4,column=0, padx=10,sticky=W)#here grid property is used
        
        #entry box
        Course_Cordinator_entryBox=ttk.Entry( class_Student_Information_frame,textvariable=self.var_coordinator,width=27,font=("times new roman",12,"bold"))
        Course_Cordinator_entryBox.grid(row=4,column=1,padx=2,pady=10,sticky=W )
        
         #  Address
        Address_label=Label( class_Student_Information_frame,text="Address",font=("times new roman",12,"bold"))
        Address_label.grid(row=4,column=2, padx=10,sticky=W)#here grid property is used
        
        #entry box
        Address_entryBox=ttk.Entry( class_Student_Information_frame,textvariable=self.var_Address,width=27,font=("times new roman",12,"bold"))
        Address_entryBox.grid(row=4,column=3,padx=2,pady=10,sticky=W )
        
        
        #radio1 Box 
        self.var_radio1=StringVar()
        radio1_Button=ttk.Radiobutton(class_Student_Information_frame,variable=self.var_radio1,text="Take A Photo Sample", value="yes")
         # variable assign
        
        radio1_Button.grid(row=5,column=0 )
         #radio2 Box
         
        radio2_Button=ttk.Radiobutton(class_Student_Information_frame,variable=self.var_radio1,text="NO Photo Sample", value="No")
           # variable assign
        
        radio2_Button.grid(row=5,column=1 )
         
        
        
        #button frame
        btn_frame=Frame(class_Student_Information_frame,bd=2,relief=RIDGE )
        btn_frame.place(x=0,y=260,width=700,height=37) 
        
        #save Button
        Save_btn=Button(btn_frame,width=12,text="Save",command=self.add_data, font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        Save_btn.grid(row=0,column=0)
        #Update Button
        Update_btn=Button(btn_frame,width=12,text=" Update",command=self.Update,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        Update_btn.grid(row=0,column=1)
        #delete Button
        delete_btn=Button(btn_frame,width=12,text="Delete", command=self.delete_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)
        #Reset Button
        Reset_btn=Button(btn_frame,width=12,text="Reset",command=self.Reset_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        Reset_btn.grid(row=0,column=3)
        #Take photo Button
        photo_btn=Button(btn_frame,width=12,text="Take photo", command=self.generate_dataset,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        photo_btn.grid(row=0,column=4)
        #Upadate photo Button
        update_photo_btn=Button(btn_frame,width=12,text="update photo",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        update_photo_btn.grid(row=0,column=5)# CALLmain
        
        
    # right Side label frame 
        label_frameright=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Details",font=("tomes new roman",12,"bold"))#relief is used for border size
        label_frameright.place(x=740,y=5,width=715,height=620)
          
          
          #right frame image 
        right_img=Image.open(r"C:\Users\kumar\Desktop\college_images\student.jpeg " )# for calling the images fromfolder to window
        right_img=right_img.resize((710,130)  )# fro resizing the image
        self.photorightimg=ImageTk.PhotoImage(right_img) 
        
        f2_lbl=Label( label_frameright,image=self.photorightimg)# ye label self ke andar banega
        f2_lbl.place(x=5, y=0,width=708, height=130) # it is for decide the position of image in window by using place method
        
        
        
        #label frame inside right label frame
        search_frame=LabelFrame( label_frameright,bd=2,bg="white",relief=RIDGE,text="Search System ",font=("times new roman",12,"bold"))#relief is used for border size
        search_frame.place(x=5,y=130,width=703,height=65)
        
        #search label
        search_label=Label( search_frame,text=" Search By",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)#here grid property is used
        
        
        search_combo=ttk.Combobox(search_frame ,font=("times new roman",15,"bold"),width=16,state='readonly')
        #Here with he .p of tuple we dedign select box 
        search_combo["values"]=("Select "," Roll No","Moble No ","StudentID ", "Other")
        search_combo.current(0)# initily select deparment
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
          
        _entryBox=ttk.Entry(  search_frame ,width=19,font=("times new roman",15,"bold"))
        _entryBox.grid(row=0,column=2,padx=2,pady=10,sticky=W )
         #save Button
        search_btn=Button( search_frame,width=10,text="  Search",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)
        #Update Button
        ShowAll_btn=Button( search_frame,width=10,text="  ShowAll ",font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        ShowAll_btn.grid(row=0,column=4)
        
        
        # table  frame inright label frame
        table_frame=Frame( label_frameright,bd=2,bg="white",relief=RIDGE )#relief is used for border size
        table_frame.place(x=5,y=200,width=703,height=380)
        #scrollBar in x and y axisin table Frame
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        
        # after creating hte scroll bar  make the table using treeview properties of ttk table should be in self
        self.student_table=ttk.Treeview(table_frame,column=("Department","Course","Year","Semester","StudentID","StudentName","StudentRollNo","StudentGroup","Gender","MobileNo","DOB","Email","coordinator", "Address","PhotoSample"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side= RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview) # config it for  view
        
        scroll_y.config(command=self.student_table.yview) #config it for view
        
        #for adding column in table student table
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course" ,text="Course")
        self.student_table.heading("Year",text="Year" )
        self.student_table.heading("Semester",text= "Semester")
        self.student_table.heading("StudentID",text="StudentID" )
        self.student_table.heading("StudentName",text="StudentName" )
        self.student_table.heading("StudentRollNo",text="StudentRollNo" )
        self.student_table.heading("StudentGroup",text= "StudentGroup")
        self.student_table.heading("Gender",text="Gender" )
        
        self.student_table.heading( "MobileNo",text="MobileNo" ) 
        self.student_table.heading("DOB",text= "DOB")
        self.student_table.heading("Email" ,text="Email" )
        self.student_table.heading("coordinator" ,text="coordinator" )
         
        self.student_table.heading( "Address",text="Address" )
        self.student_table.heading( "PhotoSample",text="PhotoSample" )
        
        self.student_table["show"]="headings"
        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("StudentID",width=100)
        self.student_table.column("StudentName",width=100)
        self.student_table.heading("StudentGroup",text= "StudentGroup")
        self.student_table.heading("Gender",text="Gender" )
        self.student_table.column("MobileNo",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("coordinator",width=100)
         
        self.student_table.column("Address",width=100)
        self.student_table.column("PhotoSample",width=150)
         
         
        self.student_table.pack(fill=BOTH,expand=1) #for pack the all heading in table
        self.student_table.bind("<ButtonRelease>",self.get_cursor) ######line for focus the cursor requiered  for bnd the table button thre aremay type of button one is ButtonRelase
        self.fetch_data()##calling of fetch data function for printing the data into table shown in window or above
       
      
        
        
        
     #######function declaration for store data in table
    def add_data(self):
      if self.var_dept.get()=="Select Department" or  self.var_course.get()=="" or self.var_stdID.get()=="":
        messagebox.showerror("Error","All field are required")
      else:
          try:
                
                connection=mysql.connector.connect(host="localhost",username="root",password="W7301@jqir#",database="face_recogntion") # required all four variable for connect mysql to python
                my_cursor=connection.cursor() 
                my_cursor.execute(" INSERT INTO  datastudent VALUES ( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                  self.var_dept.get(),
                                                                                                                  self.var_course.get(), 
                                                                                                                  self.var_year.get(),
                                                                                                                  self.var_semester.get(),
                                                                                                                  self.var_stdID.get(),
                                                                                                                  self.var_stdName.get(),
                                                                                                                  self.var_stdrollno.get(),
                                                                                                                  self.var_stdgroup.get(),
                                                                                                                  self.var_gender.get(),
                                                                                                                  self.var_mobileNo.get(),
                                                                                                                   
                                                                                                                  self.var_dob.get(),
                                                                                                                  self.var_email.get(),
                                                                                                                  self.var_coordinator.get(),
                                                                                                                   
                                                                                                                  self.var_Address.get(),
                                                                                                                  self.var_radio1.get(),
                                                                                                                )) 
                                                                                                                  
                                                                                                            
                                                                                                                  #for geting all data form the user into mysql table
            
             
                connection.commit()# for update the data in mysql table
                self.fetch_data()
                 
                connection.close()
                messagebox.showinfo("Success","All Student Details added Sucessfully",parent=self.root)
          except Exception as es:
                messagebox.showerror("Error",f"Due TO :{str(es)}",parent=self.root)
     
     
     
     
     
     #####################################fetch data#################################################
        
         
            
           
           
         
          
         
        
             
    def fetch_data(self):
          connection=mysql.connector.connect(host="localhost",username="root",password="W7301@jqir#",database="face_recogntion") # required all four variable for connect mysql to python
          my_cursor=connection.cursor()
          my_cursor.execute("Select * from datastudent") 
          data=my_cursor.fetchall()
          if len(data)!=0:
                self.student_table .delete(*self.student_table.get_children())
         
                for i in data:
                      self.student_table.insert("",END,values=i)
          connection.commit()
          connection.close()   
       
       
       ######################### get cursor###########################################
    def get_cursor(self, event=""):# by default put Event
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)  # for getteing the variable data from the student tabel andfocusit
      data=content["values"]
      self.var_dept.set(data[0]),
      self.var_course.set(data[1]),
      
      self.var_year.set(data[2]),
      
      self.var_semester.set(data[3]),
      
      self.var_stdID.set(data[4]),
      
      self.var_stdName.set(data[5]),
      
      self.var_stdrollno.set(data[6]),
      
      self.var_stdgroup.set(data[7]),
      self.var_gender.set(data[8])
      
      self.var_dob.set(data[10]),
      
      self.var_email.set(data[11]),
      
      self.var_coordinator.set(data[12]),
      
      self.var_mobileNo.set(data[9]),
      
      self.var_Address.set(data[13]),
      
      self.var_radio1.set(data[14])
      
    ########  update the student details###################                                                                                                                                                                                                                                                    
    def Update(self):
       if self.var_dept.get() == "Select Department" or self.var_course.get() == "" or self.var_stdID.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
       else:
        try:
            update = messagebox.askyesno("Update", "Do you want to update the student details?", parent=self.root)
            if update:
                connection = mysql.connector.connect(
                    host="localhost", username="root", password="W7301@jqir#", database="face_recogntion"
                )
                my_cursor = connection.cursor()
                my_cursor.execute(
                    "UPDATE  datastudent SET Deparment=%s, Course=%s, Year=%s, Semester=%s, StudentName=%s, "
                    "StudentRollNo=%s, StudentGroup=%s, Gender=%s, MobileNo=%s, DOB=%s, Email=%s,coordinator=%s, "
                    "Address=%s, PhotoSample=%s WHERE StudentID=%s",
                    (
                        self.var_dept.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_stdName.get(),
                        self.var_stdrollno.get(),
                        self.var_stdgroup.get(),
                        self.var_gender.get(),
                        self.var_mobileNo.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_coordinator.get(),
                        self.var_Address.get(),
                        self.var_radio1.get(),
                        self.var_stdID.get(),
                    )
                )
                connection.commit()
                connection.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Student Details updated successfully", parent=self.root)
            else:
                return
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    # delete Function####
    def delete_data(self):
      if self.var_stdID=="" :
        messagebox.showerror("Error","Field is mandatory for delete data",parent=self.root) 
      else:
        try:
          delete=messagebox.askyesno("student delete ","Do you want to delete the data",parent=self.root)
          if delete>0: 
              connection = mysql.connector.connect(
                    host="localhost", username="root", password="W7301@jqir#", database="face_recogntion"
                )
              my_cursor = connection.cursor()
              sql="DELETE FROM  datastudent WHERE StudentID=%s"
              val=(self.var_stdID.get(),)
              my_cursor.execute(sql,val)
          else:
            if not delete:
              return
          connection.commit()
          self.fetch_data() 
          connection.close()
          messagebox.showinfo("Delete","Successfully deleted",parent=self.root)     
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)        
    # Reset function #######
    def Reset_data(self):
       self.var_dept.set("Select Department" )
       self.var_course.set("Select Course")
      
       self.var_year.set("Select Year")
      
       self.var_semester.set("Select the semester ")
      
       self.var_stdID.set("")
      
       self.var_stdName.set("")
      
       self.var_stdrollno.set("")
      
       self.var_stdgroup.set("select group")
       self.var_gender.set("Male")
       self.var_mobileNo.set("")
      
       self.var_dob.set("")
      
       self.var_email.set("")
      
       self.var_coordinator.set("")
      
        
      
       self.var_Address.set("")
      
       self.var_radio1.set("")
                   

#### generate dataset and take photo samples ############################
    def generate_dataset(self):
      if self.var_dept.get() == "Select Department" or self.var_course.get() == "" or self.var_stdID.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try:
          connection = mysql.connector.connect(
                    host="localhost", username="root", password="W7301@jqir#", database="face_recogntion"
                )
          my_cursor = connection.cursor()
          my_cursor.execute("SELECT * FROM datastudent")
          my_result=my_cursor.fetchall()
          id=0
          for x in my_result:
            id+=1
          my_cursor.execute(
                    "UPDATE  datastudent SET Deparment=%s, Course=%s, Year=%s, Semester=%s, StudentName=%s, "
                    "StudentRollNo=%s, StudentGroup=%s, Gender=%s, MobileNo=%s, DOB=%s, Email=%s,coordinator=%s, "
                    "Address=%s, PhotoSample=%s WHERE StudentID=%s",
                    (
                        self.var_dept.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_stdName.get(),
                        self.var_stdrollno.get(),
                        self.var_stdgroup.get(),
                        self.var_gender.get(),
                        self.var_mobileNo.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_coordinator.get(),
                        self.var_Address.get(),
                        self.var_radio1.get(),
                        self.var_stdID.get()==id+1
                        
                    )
                )
          connection.commit()
          self.fetch_data()
          self.Reset_data()
          connection.close()
           
               ################### Load predefined data on face frontals from opencv  
          face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #froload haar cascade xml file here
          
          def face_cropped(img) :
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
            faces=face_classifier.detectMultiScale(gray,1.3,5)      # for detect scale
            #scaling factor 1.3
            #minimum Neighour 5
            for(x,y,w,h) in faces:     ##for making reactangle around image
              face_cropped=img[y:y+h,x:x+w]
              return face_cropped
          cap=cv2.VideoCapture(0) # for capcuture the image using camara
          img_id=0
          while True:
            ret,my_frame=cap.read() # for read the imagethat is cpcuture by camera
            if  face_cropped(my_frame) is not None:
              img_id+=1
              face=cv2.resize(face_cropped(my_frame),(450,450)) ###for cropped the imge
              face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)### for converting again image into  gray
            
              File_For_storing_capcropped_img="DATAIMG/user."+str(id)+"."+str(img_id)+".jpg"  #### for storing the capcuture image in folder name DATAIMG with all image name user 
              cv2.imwrite(File_For_storing_capcropped_img,face)
              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
              cv2.imshow("Crooped Face",face)
            if cv2.waitKey(1)==13 or int(img_id)==100:
              break
          cap.release()
          cv2.destroyAllWindows()
          messagebox.showinfo("Result","Generating all dataset completed!!!!")
        except Exception as es:
          messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)






























































































































   
 
          
        
        
        
if __name__ =='__main__':
    root=Tk() #calling of root
    obj= Student_Details(root)  # for connecting the object with root
    root.mainloop() # close the main      
        
           
         
        
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
 


  