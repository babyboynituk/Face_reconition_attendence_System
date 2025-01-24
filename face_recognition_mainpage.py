from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk ##for style the image
from tkinter import messagebox ### for show all prompt
import mysql.connector  
# from time import strftime
# from datetime import datetime
import cv2  ## f
import os ##for make file with collection of image and open folder from the pc
import numpy as np   ##for convertig image in array
import serial
import datetime
import time
import threading
import pygame 
# New import for sound playback
from datetime import datetime
# Ensure proper import


# Initialize pygame mixer for sound playback
pygame.mixer.init()





class face:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title(" Face recognition main")
         
        self.arduino = None

#     def connect_to_arduino(self, port='COM4', baudrate=9600):
#         try:
#             self.arduino = serial.Serial(port, baudrate, timeout=1)
#             print(f"Connected to Arduino on {port}")
#         except Exception as e:
#             print(f"Failed to connect to Arduino: {e}")

           
   
            
#         #  
#         #     
                
#     #      
            
#     #      
#     def send_to_arduino(self, text):
        
#        if self.arduino and self.arduino.is_open:
           
#             try:
#                 self.arduino.write(f"{text}\n".encode())
#                 print(f"Sent to Arduino: {text}")
#             except serial.SerialException as e:
#                print(f"Error sending data to Arduino: {e}")
#        else:
#             print("Arduin o not connected or not open.")
#     def disconnect_arduino(self):
#         if self.arduino and self.arduino.is_open:
#             self.arduino.close()
#             print("Disconnected from Arduino")
#    # Rest of your code (face_recog, draw_boundary, etc.)
          
          
          
         #for title in bg_img 
        title_lbl=Label( self.root,text="FACE RECOGNITION",font=("times new roman",40,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        # topright_side_img 
        right_side_img=Image.open(r"C:\Users\kumar\Desktop\college_images\face_detector1.jpg " )# for calling the images fromfolder to window
        right_side_img=right_side_img.resize((690,790)  )# fro resizing the image
        self.phototopimg=ImageTk.PhotoImage(right_side_img) 
        
        f1_lbl=Label( self.root,image=self.phototopimg)# ye label self ke andar banega
        f1_lbl.place(x=0, y=55,width=690, height=790) # it is for decide the position of image in window by using place method

         # big_side_img 
        big_side_img=Image.open(r"C:\Users\kumar\Desktop\college_images\4.jpg " )# for calling the images fromfolder to window
        big_side_img=big_side_img.resize((810,790)  )# fro resizing the image
        self.photoimg=ImageTk.PhotoImage(big_side_img) 
        
        f2_lbl=Label( self.root,image=self.photoimg)# ye label self ke andar banega
        f2_lbl.place(x=690, y=55,width=810, height=790) # it is for decide the position of image in window by using place method

         #face_recogniton Button
        face_recogniton_btn=Button(f2_lbl ,width=250,text="Face Recogniton Button", command=self.face_recog, font=("times new roman",18,"bold"),bg="red",fg="white")
        face_recogniton_btn.place(x=275 ,y=695,width=250, height=30) #
    
    ####################################### attendence Manager########################################
    def connect_to_arduino(self, port='COM4', baudrate=9600):
        try:
            self.arduino = serial.Serial(port, baudrate, timeout=1)
            print(f"Connected to Arduino on {port}")
        except Exception as e:
            print(f"Failed to connect to Arduino: {e}")

           
   
            
        #  
        #     
                
    #      
            
    #      
    def send_to_arduino(self, text):
        
       if self.arduino and self.arduino.is_open:
           
            try:
                self.arduino.write(f"{text}\n".encode())
                print(f"Sent to Arduino: {text}")
            except serial.SerialException as e:
               print(f"Error sending data to Arduino: {e}")
       else:
            print("Arduin o not connected or not open.")
    def disconnect_arduino(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
            print("Disconnected from Arduino")   
                    
         
    def mark_Attendence(self, fetched_rollno_data, fetched_name_data, fetched_department_data, fetched_course_data):
        
    # File name for attendance records
        filename = "sahil.csv"
    
    # Ensure file exists; create it with headers if not
        try:
            open(filename, "r").close()
        except FileNotFoundError:
            with open(filename, "w", newline="") as f:
               f.write("Roll Number,Name,Department,Course,Date,Time,Status\n")
    
    # Open the file in append mode
        with open(filename, "r+", newline="") as f:
           reader = f.readlines()
           name_list = []

        # Collect roll numbers already marked as present
           for line in reader:
                entry = line.strip().split(",")
                if entry:
                    name_list.append(entry[0])  # Only check roll number for uniqueness

        # Write attendance only if roll number not found
           if fetched_rollno_data not in name_list:
                now = datetime.now()
                date_string = now.strftime("%d/%m/%Y")
                time_string = now.strftime("%H:%M:%S")
                f.write(f"{fetched_rollno_data},{fetched_name_data},{fetched_department_data},{fetched_course_data},{date_string},{time_string},Present\n")
                print(f"Attendance marked for: {fetched_name_data}")
           else:
                print(f"Attendance already marked for: {fetched_name_data}")

   
   
   
   
   
   
 
   
   
   
   
   
     
 #################################### faceRecognition function ################################### 
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf, sent_names):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
         
            coordinates = []
            for (x, y, w, h) in features:
                fetched_name_data = "Unknown"  # Default value
                fetched_rollno_data = ""
                fetched_department_data = ""
                fetched_course_data = ""
                fetched_group_data = ""

                try:
                    
                
                
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    id,predict = clf.predict(gray_img[y:y + h, x:x + w])
                    confidence = int((100 * (1 - predict / 300)))
                
                # def fetch_student_details(id):
                    
                 # Establishing database connection
                    
                    id = int(id)
                        
                        
                        
                    connection=mysql.connector.connect(host="localhost",username="root",password="W7301@jqir#",database="face_recogntion") # required all four variable for connect mysql to python
                    my_cursor=connection.cursor()
                        #  # Query to fetch the data
                        # query = """SELECT StudentRollNo, StudentName, Deparment, Course, StudentGroup FROM student
                        #                 """
                 
                        # # my_cursor.execute("SELECT StudentRollNO, StudentName, Deparment, Course, StudentGroup FROM student WHERE StudentID = %s", (id,))
                        # print(f"Querying database with StudentID: {id}")  # Debug log
                        # my_cursor.execute(query, (id,))

                        # result = my_cursor.fetchone()
                        # if result:
                            
                        #     (fetched_rollno_data,fetched_name_data,fetched_department_data,fetched_course_data, fetched_group_data) = result
                        #     print(f"Fetched data: {result}")  # Debug log
                            
                           
                        
                        # else:
                        #     # Handle case when no data is found
                        #     print(f"No data found for StudentID: {id}")
                        #     fetched_rollno_data = "Unknown"
                        #     fetched_name_data = "Unknown"
                        #     fetched_department_data = "Unknown"
                        #     fetched_course_data = "Unknown"
                        #     fetched_group_data = "Unknown"
                            
    
                            
                        #     fetched_rollno_data, fetched_name_data, fetched_department_data, fetched_course_data, fetched_group_data = result
                        # else:
                        #     fetched_rollno_data = fetched_name_data = fetched_department_data = fetched_course_data = fetched_group_data = ""

                    
                    my_cursor.execute("SELECT StudentRollNO FROM datastudent WHERE StudentID=  %s", (id,)  )
                    result = my_cursor.fetchone()
                    fetched_rollno_data = "+".join(result) if result else ""  # Safe handling of None

                    my_cursor.execute("SELECT StudentName FROM  datastudent WHERE StudentID=%s", (id,)      )
                    result = my_cursor.fetchone()
                    fetched_name_data = "+".join(result) if result else ""
                    self.send_to_arduino(str(fetched_name_data))
                    
                    
          

                    my_cursor.execute("SELECT Deparment FROM datastudent WHERE StudentID= %s", (id,)  )
                    result = my_cursor.fetchone()
                    fetched_department_data = "+".join(result) if result else ""

                    my_cursor.execute("SELECT Course FROM  datastudent WHERE StudentID=   %s", (id,)  )
                    result = my_cursor.fetchone()
                    fetched_course_data = "+".join(result) if result else ""

                    my_cursor.execute("SELECT StudentGroup FROM  datastudent WHERE StudentID=  %s", (id,)    )
                    result = my_cursor.fetchone()
                    fetched_group_data = "+".join(result) if result else ""
                    
               
                
                   
                    
                   
                    
                except mysql.connector.Error as e:
                    
                        
                        
                    print(f"Database error: {e}")
                        # fetched_rollno_data = "Error"
                        # fetched_name_data = "Error"
                        # fetched_department_data = "Error"
                        # fetched_course_data = "Error"
                        # fetched_group_data = "Error"


                finally:
                    
                        
            # Close the cursor and connection
                    if my_cursor:
                            my_cursor.close()
                    if connection and connection.is_connected():
                            connection.close()
                # result = fetch_student_details(id)
                # fetched_rollno_data, fetched_name_data, fetched_department_data, fetched_course_data, fetched_group_data = result
 
    
                

                if confidence > 70 :
                    
                    #and fetched_name_data not in sent_names:  
                     
                     # Lowered confidence threshold
                  # Displaying the student's information on the image
                  
                       # Update last sent ID and confidence
                        # self.last_id_sent = id
                        # self.last_confidence_sent = confidence

                        
                            
                            # sent_names.add(fetched_name_data)
                            # self.send_to_arduino(fetched_name_data)
                            # self.mark_Attendence(fetched_rollno_data, fetched_name_data, fetched_department_data, fetched_course_data)
                    
                        
                        sent_names.add(fetched_name_data)
                        self.send_to_arduino(fetched_name_data)
                        #self.disconnect_arduino()
          
     
                     
                        self.mark_Attendence(fetched_rollno_data, fetched_name_data, fetched_department_data, fetched_course_data)
                        cv2.putText(img,f"RollNO:{fetched_rollno_data}", (x, y - 100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                       
                        
                        cv2.putText(img, f"Name:{fetched_name_data}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.send_to_arduino(fetched_name_data)
                        cv2.putText(img, f"Deparment:{fetched_department_data}", (x, y -45 ), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img,f"Group:{fetched_group_data}", (x, y -15 ), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Course:{fetched_course_data}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        # self.mark_Attendence(fetched_rollno_data,fetched_name_data,fetched_department_data,fetched_course_data)
                        # return fetched_name_data  # Return the recognized name
                         # Load and play the sound
#                         # Play sound using pygame
#                         def play_sound():
                            
                            
#                             pygame.mixer.music.load("Attendence.mp3")  # Replace with your sound file
#                             pygame.mixer.music.play()
#                             while pygame.mixer.music.get_busy():
#                                 continue
# # w
# #                     # Use threading to avoid blocking
#                         threading.Thread(target=play_sound, daemon=True).start()

# # #                     # Display success message
#                         messagebox.showinfo("Success", f"Attendance marked for {fetched_name_data}!")

#                     # Close the camera





                        return  True

                
                else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)  # Red color for unknown face
                        cv2.putText(img, "Unknown Face", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        # return None

                coordinates = [x, y, w, h]
             

            #      finally:
            # # Close the cursor and connection
            #         if my_cursor:
            #             my_cursor.close()
            #          if connection and connection.is_connected():
            #           connection.close()
            return  False
             
                
        def recognizer(img, clf, face_cascade,sent_names):
            
            coordinates= draw_boundary(img, face_cascade, 1.1, 10, (255, 25, 255), "face", clf,sent_names)
            return img,coordinates
    
    # Load face cascade and recognizer model
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
    
    # # Capture video from webcam
        video_cap = cv2.VideoCapture(0)
        sent_names=set()
        attendance_data = [] 
    
        while True:
            
            
            ret, img = video_cap.read()
            img ,coordinates =recognizer(img, clf, face_cascade,  sent_names)
            cv2.imshow("Welcome to face recognizer", img)
        
    #     # Break the loop when 'Enter' key is pressed
            if cv2.waitKey(1) == 13  :
                break
            for data in attendance_data:
            
              fetched_rollno_data, fetched_name_data, fetched_department_data, fetched_course_data = data
              self.mark_Attendence(fetched_rollno_data, fetched_name_data, fetched_department_data, fetched_course_data)

    
        video_cap.release()
        cv2.destroyAllWindows()
        # Handle attendance marking and sound playback after loop
        # 
        # Play sound
        # def play_sound():
        #     pygame.mixer.music.load("Attendence.mp3")  # Replace with your sound file
        #     pygame.mixer.music.play()
        #     while pygame.mixer.music.get_busy():
        #         continue

        # threading.Thread(target=play_sound, daemon=True).start()

        # Disconnect Arduino after closing the camera
        # Display success message
        # messagebox.showinfo("Success", f"Attendance marked for ")

        self.disconnect_arduino()
          
     
        
    
 
    # 
    #     

 


    
    
    
    
    
    
    
    
if __name__ =='__main__':
    root=Tk() #calling of root
    obj= face(root)  # for connecting the object with root
    # Detected name (for testing purposes)
    #obj.face_recog() # Replace with the name of the detected person
    
    # Call the send_to_arduino method on the instance of the class
    # Initialize Arduino
    face_recog_system = face(root)
    face_recog_system.connect_to_arduino()
    face_recog_system.face_recog()

     
    root.mainloop() # close the main
        