from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk ##for style the image
from tkinter import messagebox ### for show all prompt
import mysql.connector  
import cv2  ## for all image operation
import os ##for make file with collection of image and open folder from the pc
import numpy as np   ##for convertig image in 
 






class Train_dataset:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title(" Train Dataset")
        
        
        
         #for title in bg_img 
        title_lbl=Label( self.root,text=" Train Data Set",font=("times new roman",40,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        # top  image 
        top_img=Image.open(r"C:\Users\kumar\Desktop\college_images\facialrecognition.png " )# for calling the images fromfolder to window
        top_img=top_img.resize((1500,350)  )# fro resizing the image
        self.phototopimg=ImageTk.PhotoImage(top_img) 
        
        f1_lbl=Label( self.root,image=self.phototopimg)# ye label self ke andar banega
        f1_lbl.place(x=0, y=55,width=1500, height=350) # it is for decide the position of image in window by using place method
        
         #Trainig Button
        Traing_btn=Button(self.root,width=1500,text="Train DataSet ", command=self.train_clessifier, font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        Traing_btn.place(x=0, y=410,width=1500, height=82) #
    
        
        
         # bottom image 
        bottom_img=Image.open(r"C:\Users\kumar\Desktop\college_images\bottomtrain.jpg" )# for calling the images fromfolder to window
        bottom_img=bottom_img.resize((1500,350)  )# fro resizing the image
        self.photobottomimg=ImageTk.PhotoImage(bottom_img) 
        
        f1_lbl=Label( self.root,image=self.photobottomimg)# ye label self ke andar banega
        f1_lbl.place(x=0, y=500,width=1500, height=350) # it is for decide the position of image in window by using place method
    
    
    def train_clessifier(self):
        data_dir=("DATAIMG")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)] ###it is a list comprihension way for using loop and list
        
        
        
        faces=[]
        ids=[]
        
        for image in path:
            
            img =Image.open(image).convert('L') ###another way for converting image into gray 
            imageNp=np.array(img,'uint8')  ####uint8 is only datatype
            id=int(os.path.split(image)[1].split('.')[1])
           
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("traing",imageNp)
            cv2.waitKey(1)==13  ### press enter for closing the window
        ids=np.array(ids)
        ###### train The classifier and save
        classifir=cv2.face.LBPHFaceRecognizer_create()
        classifir.train(faces,ids)
        classifir.write("classifier.xml")### inside bracket write the file name by which you want to save the file
        cv2.destroyAllWindows()
        messagebox.showinfo("result","Traing the faces in dataset is completed")
           
           
            
         
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ =='__main__':
    root=Tk() #calling of root
    obj= Train_dataset(root)  # for connecting the object with root
    root.mainloop() # close the main      
        