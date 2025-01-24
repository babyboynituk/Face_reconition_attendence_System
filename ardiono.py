import serial
import time
from tkinter import *
from TEST import Face_Recgnition_System
class  detector:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("800x600")
        
        # Initialize Serial  with Arduino
        try:
            self.arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # Update 'COM3' as per your setup
            print("Connected to Arduino")
        except serial.SerialException:
            print("Could not connect to Arduino. Please check the port.")
            self.arduino = None

        # Create a button to simulate recognition and attendance marking
        self.recog_button = Button(self.root,  command=self.test,text="Simulate Recognition" )
        self.recog_button.pack(pady=20)

    def mark_attendance(self, name):
        """Send the recognized name to Arduino to mark attendance."""
        if self.arduino and self.arduino.is_open:
            self.arduino.write(f"{name}\n".encode())  # Send name followed by a newline
            print(f"Attendance marked for: {name}")
        else:
            print("Arduino is not connected. Unable to mark attendance.")

    def recogni(self):
        """Simulate the face recognition and mark attendance for the recognized person."""
        # Simulate recognition; replace with actual recognition logic
        recognized_name = "John Doe"  # Replace with actual recognized name from face recognition
        print(f"Recognized: {recognized_name}")
        
        # Mark attendance by sending name to Arduino
        self.mark_attendance(recognized_name)


    def test(self):
        self.new_window=Toplevel(self.root)
        self.apppp=Face_Recgnition_System(self.new_window)
    
    






if __name__ == '__main__':
    root = Tk()
    app =  detector(root)
    root.mainloop()
