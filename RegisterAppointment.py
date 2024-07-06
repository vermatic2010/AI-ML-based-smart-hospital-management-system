import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0)
def display_dr():
    conn=sqlite3.connect("facedb.db")
    print(conn)
    cmd="SELECT * FROM Doctor"
    dr_id_list=conn.execute(cmd)
    print(dr_id_list)
    for dr_id in dr_id_list:
        print(dr_id)

def insertOrUpdate(aadhar_id,name,gender,age,dr_id):
    conn=sqlite3.connect("facedb.db")
    print(conn)
    cmd="SELECT * FROM Patient WHERE AadharNo="+str(aadhar_id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE Patient SET PatientName="+str(name)+"WHERE AadharNo="+str(aadhar_id)
        cmd2="UPDATE Patient SET PatientAge="+str(age)+"WHERE AadharNo="+str(aadhar_id)
        cmd3="UPDATE Patient SET PatientGender="+str(gender)+"WHERE AadharNo="+str(aadhar_id)
        conn.execute(cmd)
    else:
        params = (aadhar_id,name,gender,age,dr_id)
        cmd="INSERT INTO Patient(AadharNo,PatientName,PatientAge,PatientGender,DoctorId) Values(?, ?, ?, ?, ?)"
        cmd2=""
        cmd3=""
        cmd4=""
        conn.execute(cmd, params)

    conn.execute(cmd2)
    conn.execute(cmd3)
    conn.execute(cmd4)
    conn.commit()
    conn.close()

aadhar_id=input('Enter your Aadhar Number: ')
name=input('Enter your Name: ')
age=input('Enter your Age: ')
gender=input('Enter your Gender: ')
#print doctor table
print("Available doctor details: Doctor ID, Doctor Name, Doctor Gender, Doctor Age, Doctor Profession, Hospital details, Doctor consultation fees: ")
display_dr()
dr_id=input('Enter the Doctor Ids separated by white spaces with whom you want to meet for consultation: ')
insertOrUpdate(aadhar_id,name,gender,age,dr_id)
sampleNum=0
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1
        cv2.imwrite("dataSet/User."+str(aadhar_id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if(sampleNum>50):
        break
cam.release()
cv2.destroyAllWindows()