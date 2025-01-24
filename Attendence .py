from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector  
import cv2
import os
 






class Attendence_manager:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title(" Attendence Manager")
        #for title in bg_img 
        title_lbl=Label(self.root,text=" Student Management System",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        
        #background image
        bg_img=Image.open(r"C:\Users\kumar\Desktop\college_images\wp2551980.jpg  " )# for calling the images fromfolder to window
        bg_img=bg_img.resize((1530,730)  )# fro resizing the image
        self.bg_photoimg=ImageTk.PhotoImage(bg_img) 
        bg_lbl=Label(self.root,image=self.bg_photoimg)# ye label self ke andar banega
        bg_lbl.place(x=0, y=45,width=1530, height=750) # it is for decide the position of image in window by using place method()
         
        # #face_recogniton Button
        # face_recogniton_btn=Button(  bg_lbl,width=250,text=" Check Attendence", command= , font=("times new roman",18,"bold"),bg="red",fg="white")
        # face_recogniton_btn.place(x=275 ,y=695,width=250, height=30) #
    
        # Button to open CSV file
        b5 = Button(bg_lbl, text="Open sahil.csv", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5.place(x=800, y=620, width=220, height=35)

        
        
        
        
        
        
        
    # def open_csv(self):
        
    #     try:
            
    #     # Get the full path to sahil.csv (assuming it's in the same directory as this script)
    #         csv_file_path = os.path.join(os.path.dirname(__file__), "sahil.csv")
        
    #     # Check if the file exists
    #         if not os.path.isfile("sahil.csv" ):
                
    #             print("Error: sahil.csv file not found!")
    #             return
        
    #     # Open the file with the default application
    #         os.startfile( "sahil.csv")  # This works on Windows
        
    #     # For non-Windows systems, use appropriate methods
    #     # Example for Linux/macOS:
    #     # subprocess.call(('xdg-open', csv_file_path))
    #     except Exception as e:
            
            
    #         print(f"An error occurred while trying to  sahil.csv: {e}")

        
 
    # Your existing code...

    def open_img(self):
        try:
            # Construct the path to the 'sahil.csv' file in the same directory as the script
            file_path = os.path.join(os.path.dirname(__file__), "sahil.csv")
            
            # Check if the file exists
            if os.path.exists("sahil.csv"):
                os.startfile("sahil.csv")  # This will open the file with the default CSV viewer
                print(f"Opening file: {" sahil.csv"}")
            else:
                print(f"File 'sahil.csv' not found in the current directory.")
        except Exception as e:
            print(f"Error while opening the file: {e}")
     
        
        
        
        
        
        
        
        
        
        
if __name__ =='__main__':
    root=Tk() #calling of root
    obj= Attendence_manager(root)  # for connecting the object with root
    root.mainloop() # close the main      
        