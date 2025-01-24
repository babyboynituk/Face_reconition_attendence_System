from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from ztudent import Student_Details
import os
from train import Train_dataset
from face_recognition_mainpage import face
import serial
import time







class Face_Recgnition_System:
    def __init__(self ,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
         # Set up serial connection to Arduino
       # arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)  # Use your Arduino port here
       # time.sleep(2)  # Give some time for the connection to stabilize
       # Initialize Arduino connection
        
        #first image1
        img1=Image.open(r"C:\Users\kumar\Desktop\college_images\Stanford.jpg" )# for calling the images fromfolder to window
        img1=img1.resize((500,130)  )# fro resizing the image
        self.photoimg1=ImageTk.PhotoImage(img1) 
        f1_lbl=Label(self.root,image=self.photoimg1)# ye label self ke andar banega
        f1_lbl.place(x=0, y=0,width=500, height=130) # it is for decide the position of image in window by using place method
        
        
        #second image
        img2=Image.open(r"C:\Users\kumar\Desktop\college_images\facialrecognition.png " )# for calling the images fromfolder to window
        img2=img2.resize((500,130)  )# fro resizing the image
        self.photoimg2=ImageTk.PhotoImage(img2) 
        f1_lbl=Label(self.root,image=self.photoimg2)# ye label self ke andar banega
        f1_lbl.place(x=500, y=0,width=500, height=130) # it is for decide the position of image in window by using place method
        
        
        #third image
        img3=Image.open(r"C:\Users\kumar\Desktop\college_images\u.jpg " )# for calling the images fromfolder to window
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
        title_lbl=Label(bg_lbl,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
         
         #student Button
        #for design image as button on above the background image
        img4=Image.open(r"C:\Users\kumar\Desktop\college_images\har.jpg " )# for calling the images fromfolder to window
        img4=img4.resize((220,220)  )# fro resizing the image
        self.photoimg4=ImageTk.PhotoImage(img4)
         
         #b1means button
        b1=Button(bg_lbl,image= self.photoimg4,cursor="hand2" ,command=self.student_details)
        b1.place(x=400,y=100,width=220,height=220) 
        #b1_1 means button text
        b1_1=Button(bg_lbl, text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=320,width=220,height=35) 
        
        
         # Face detector Button
        #for design image as button on above the background image
        img5=Image.open(r"C:\Users\kumar\Desktop\college_images\face_detector1.jpg " )# for calling the images fromfolder to window
        img5=img5.resize((220,220)  )# fro resizing the image
        self.photoimg5=ImageTk.PhotoImage(img5)
         
         #b1means button
        b2=Button(bg_lbl,image= self.photoimg5,cursor="hand2",command=self.datapic )
        b2.place(x=850,y=100,width=220,height=220) 
        #b1_1 means button text
        b2_2=Button(bg_lbl, text="Face Detector",cursor="hand2",command=self.datapic ,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=850,y=320,width=220,height=35) 
        
        
        # #    Attendence Button
        # #for design image as button on above the background image
        # img6=Image.open(r"C:\Users\kumar\Desktop\college_images\student.jpeg" )# for calling the images fromfolder to window
        # img6=img6.resize((220,220)  )# fro resizing the image
        # self.photoimg6=ImageTk.PhotoImage(img6)
         
        #  #b1means button
        # b3=Button(bg_lbl,image= self.photoimg6,cursor="hand2")
        # b3.place(x= 800,y=100,width=220,height=220) 
        # #b3_3 means button text
        # b3_3=Button(bg_lbl, text="Attendence Manager",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b3_3.place(x=800,y=320,width=220,height=35) 
        
        
        # #     Help Button
        # #for design image as button on above the background image
        # img7=Image.open(r"C:\Users\kumar\Desktop\college_images\help.jpg " )# for calling the images fromfolder to window
        # img7=img7.resize((220,220)  )# fro resizing the image
        # self.photoimg7=ImageTk.PhotoImage(img7)
         
        #  #b1means button
        # b4=Button(bg_lbl,image= self.photoimg7,cursor="hand2")
        # b4.place(x= 1100,y=100,width=220,height=220) 
        # #b3_3 means button text
        # b4_4=Button(bg_lbl, text="  Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b4_4.place(x=1100,y=320,width=220,height=35) 
        
        #     Train  face Button
        #for design image as button on above the background image
        img8=Image.open(r"C:\Users\kumar\Desktop\college_images\Train.jpg " )# for calling the images fromfolder to window
        img8=img8.resize((220,220)  )# fro resizing the image
        self.photoimg8=ImageTk.PhotoImage(img8)
         
         #b 1 means button
        b4=Button(bg_lbl,image= self.photoimg8,cursor="hand2",command=self.trian_file)
        b4.place(x=400,y=400,width=220,height=220) 
        #b3_3 means button text
        b4_4=Button(bg_lbl, text="  Train Face",cursor="hand2",command=self.trian_file,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=400,y=620,width=220,height=35) 
        
        # #    Photos Button
        #for design image as button on above the background image
        img9=Image.open(r"C:\Users\kumar\Desktop\college_images\photo.jpg " )# for calling the images fromfolder to window
        img9=img9.resize((220,220)  )# fro resizing the image
        self.photoimg9=ImageTk.PhotoImage(img9)
         
         #b 1 means button
        b4=Button(bg_lbl,image= self.photoimg9,cursor="hand2", command=self.open_img)
        b4.place(x=850,y=400,width=220,height=220) 
        #b3_3 means button text
        b4_4=Button(bg_lbl, text="  Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=850,y=620,width=220,height=35) 
        
        
        
        # # #    Developer Button
        # #for design image as button on above the background image
        # img10=Image.open(r"C:\Users\kumar\Desktop\college_images\dev.jpg " )# for calling the images fromfolder to window
        # img10=img8.resize((220,220)  )# fro resizing the image
        # self.photoimg10=ImageTk.PhotoImage(img10)
         
        #  #b 1 means button
        # b4=Button(bg_lbl,image= self.photoimg10,cursor="hand2")
        # b4.place(x=800,y=400,width=220,height=220) 
        # #b3_3 means button text
        # b4_4=Button(bg_lbl, text="   Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b4_4.place(x=800,y=620,width=220,height=35) 
        
        
        
        # # #    Exit Button
        # #for design image as button on above the background image
        # img11=Image.open(r"C:\Users\kumar\Desktop\college_images\exit.jpg " )# for calling the images fromfolder to window
        # img11=img11.resize((220,220)  )# fro resizing the image
        # self.photoimg11=ImageTk.PhotoImage(img11)
         
        #  #b 1 means button
        # b4=Button(bg_lbl,image= self.photoimg11,cursor="hand2)
        # b4.place(x=1100,y=400,width=220,height=220) 
        # #b3_3 means button text
        # b4_4=Button(bg_lbl, text="   Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b4_4.place(x=1100,y=620,width=220,height=35) 
        # ######for open images in photo button  from  folder name DATAIMG###############
     
        
        
        
        
        
        
        
        
        
        
        
    
    
    def open_img(self):
        os.startfile("DATAIMG")    
        
        
        
        
        
        
         #function for link the student details page with test page
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.appp=Student_Details(self.new_window)
    
    
    #function for link the  train page with test page
    def  trian_file(self):
        self.new_window=Toplevel(self.root)
        self.appp= Train_dataset(self.new_window)
        
     
        
    ################################################
    # ###############################################        
    def datapic(self):
        self.new_window=Toplevel(self.root)
        self.app=face(self.new_window)
        
    # # # Check if a name was recognized
    # #     if recognized_name:
    # #     # Mark attendance by sending the recognized name to Arduino
    # #             self.mark_attendance(recognized_name)
    # #     else:
    # #             print("No face recognized or face unknown.") 
    # def send_to_arduino(text):
    #    if arduino.is_open:
    #        arduino.write(f"{text}\n".encode())  # Send the text with a newline character
    #        print(f"Sent to Arduino: {text}")

        
        
        
        
        
        
 # CALLmain
       
if __name__ =='__main__':
    root=Tk() #calling of root
    obj=Face_Recgnition_System(root)  # for connecting the object with root
    root.mainloop() # close the main
    
    
    
    
    
   
        
    
    
       