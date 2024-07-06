import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0)
def display_medicine():
    conn=sqlite3.connect("facedb.db")
    print(conn)
    cmd="SELECT * FROM Medicine"
    medicine_id_list=conn.execute(cmd)
    print(medicine_id_list)
    for medicine_id in medicine_id_list:
        print(medicine_id)

def update(aadhar_id,medicine_id_list,medicine_units_list):
    conn=sqlite3.connect("facedb.db")
    print(conn)
    cmd="SELECT * FROM Patient WHERE AadharNo="+str(aadhar_id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cursor.execute("UPDATE Patient SET MedicineIdList = '" + str(medicine_id_list) + "' WHERE AadharNo=" + str(aadhar_id))
        cursor.execute("UPDATE Patient SET MedicineUnits = '" + str(medicine_units_list) + "' WHERE AadharNo=" + str(aadhar_id))
    conn.commit()
    conn.close()

#print medicine table
print("Available medicine details: Medicine ID, Medicine Name, Medicine Cost: ")
display_medicine()
aadhar_id=input('Enter the Patient Aadhar Id: ')
medicine_id_list=input('Enter the Medicine Id List to be prescribed: ')
medicine_units_list=input('Enter the Medicine Units List to be prescribed: ')
update(aadhar_id,medicine_id_list,medicine_units_list)
