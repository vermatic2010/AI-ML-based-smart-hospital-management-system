import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer/trainningData.yml")

fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 0.5
fontcolor = (0, 0, 255)

def getProfile(id):
    conn=sqlite3.connect("facedb.db")
    cmd="SELECT * FROM Patient WHERE AadharNo="+str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    conn = sqlite3.connect("facedb.db")
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        print(profile)

        dr_id_list=profile[4].split(" ")
        print(dr_id_list)
        total_cost = 0
        doctor_opd_list = {}
        for dr_id in dr_id_list:
            cmd = "SELECT OPD FROM Doctor WHERE DoctorId=" + str(dr_id)
            opd = conn.execute(cmd)
            opd = opd.fetchone()
            print(opd[0])

            cmd = "SELECT DoctorName FROM Doctor WHERE DoctorId=" + str(dr_id)
            doctor_name = conn.execute(cmd)
            doctor_name = doctor_name.fetchone()

            doctor_opd_list[doctor_name] = opd

            cmd = "SELECT ConsultationFees FROM Doctor WHERE DoctorId=" + str(dr_id)
            consultation_fees = conn.execute(cmd)
            consultation_fees = consultation_fees.fetchone()
            print(consultation_fees)
            total_cost = total_cost + int(consultation_fees[0])

        if(profile!=None):
            cv2.putText(img,"Name : "+str(profile[1]),(x,y+h+20),fontface, fontscale, fontcolor)
            cv2.putText(img,"Age: "+str(profile[2]),(x,y+h+60),fontface, fontscale, fontcolor)
            cv2.putText(img,"Gender: "+str(profile[3]),(x,y+h+100),fontface, fontscale, fontcolor)
            cv2.putText(img,"OPD: "+str(doctor_opd_list),(x,y+h+140),fontface, fontscale, fontcolor)
            cv2.putText(img,"Consultation fees: "+str(total_cost),(x,y+h+180),fontface, fontscale, fontcolor)
    cv2.imshow("Face",img)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()