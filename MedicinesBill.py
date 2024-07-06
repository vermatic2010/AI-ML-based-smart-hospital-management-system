import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer/trainningData.yml")

fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
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
        medicine_id_list=profile[5].split(" ")
        medicine_units_list=profile[6].split(" ")
        total_cost=0
        medicine_name_list = []
        print("medicine_units_list %s", medicine_units_list)
        print("medicine_id_list %s", medicine_id_list)

        for medicine_id_count in range(0, len(medicine_id_list)):
            cmd = "SELECT MedicineName FROM Medicine WHERE MedicineId=" + str(medicine_id_list[medicine_id_count])
            medicine_name = conn.execute(cmd)
            medicine_name = medicine_name.fetchall()
            medicine_name_list.append(medicine_name[0][0])

            cmd = "SELECT MedicineCostPerUnit FROM Medicine WHERE MedicineId=" + str(medicine_id_list[medicine_id_count])
            medicine_cost = conn.execute(cmd)
            medicine_cost = medicine_cost.fetchall()
            medicine_cost = medicine_cost[0][0]

            total_cost = total_cost + int(medicine_units_list[medicine_id_count]) * int(medicine_cost)

        print("total_cost %s", total_cost)
        print(medicine_name_list)

        if(profile!=None):
            cv2.putText(img,"Name: "+str(profile[1]),(x,y+h+20),fontface, fontscale, fontcolor)
            cv2.putText(img,"Medicines: "+str(medicine_name_list),(x,y+h+85),fontface, fontscale, fontcolor)
            cv2.putText(img,"Bill: "+str(total_cost),(x,y+h+155),fontface, fontscale, fontcolor)
    cv2.imshow("Face",img)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()