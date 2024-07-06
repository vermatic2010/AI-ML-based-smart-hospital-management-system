git clone https://github.com/vermatic2010/AI-ML-based-smart-hospital-management-system.git<br />
Make 2 folders - dataSet & recognizer
<br /><br />
<br /><br />

A smart hospital management system built using a pre-trained Haar Cascade classifier for detecting frontal faces in images. It includes tables of patient, doctor, and medicine. A patient registers to see a doctor and uses a contactless method to enter the hospital. The admin or nurse verifies the patient's details using the hospital's installed cameras, which displays the patient's Aadhar ID, name, age, and gender on the hospital computer screens. The patient receives information about the consultation fees to be paid & OPD details where their registered doctor is located, also displayed beside their face upon arrival at the hospital & have to pay the consultation fees to the hospital staff. The doctor prescribes medicines to the patient and the face recognition algorithm displays these details along with the total bill to the patient & pharmacist.
<br /><br />
<br /><br />

1. Make a facedb with Doctor, Medicine & Patient tables.
2. Enter values in Doctor & Medicine tables.<br />
<img width="548" alt="Screenshot 2024-07-06 120715" src="https://github.com/vermatic2010/AI-ML-based-smart-hospital-management-system/assets/127281006/89bd6c5d-e677-4efc-8ba2-57b875163e82"><br />
<img width="238" alt="Screenshot 2024-07-06 120732" src="https://github.com/vermatic2010/AI-ML-based-smart-hospital-management-system/assets/127281006/c4dcf194-550e-4504-bb1d-8033654d54a6"><br />
<img width="394" alt="Screenshot 2024-07-06 120813" src="https://github.com/vermatic2010/AI-ML-based-smart-hospital-management-system/assets/127281006/19e85491-23de-4c0c-976b-e11d646193a6"><br />
<img width="104" alt="Screenshot 2024-07-06 120845" src="https://github.com/vermatic2010/AI-ML-based-smart-hospital-management-system/assets/127281006/a5a8a2c5-2a42-4828-bae0-6200c7d84e42"><br /><br />

3. Patients register for appointment via RegisterAppointment.py<br />
<img width="887" alt="Screenshot 2024-07-06 112519" src="https://github.com/vermatic2010/AI-ML-based-smart-hospital-management-system/assets/127281006/8c1f9555-febb-4226-80cd-f1d155f8e464"><br />
<img width="960" alt="Screenshot 2024-07-06 112449" src="https://github.com/vermatic2010/AI-ML-based-smart-hospital-management-system/assets/127281006/d296e1b8-e1e6-44cc-85b3-2c8fb214d2ac"><br />
<br />
4. Run TrainFace.py<br />
5. Run PatientFaceRecogniser.py - When patient goes to the hospital, he gets the details of the OPD & has to pay total consultation fees to the hospital staff.<br />
<img width="960" alt="Screenshot 2024-07-06 122515" src="https://github.com/vermatic2010/AI-ML-based-smart-hospital-management-system/assets/127281006/2eef5285-be79-48d3-b785-2c5d2e90e542"><br /><br />
6. Run DoctorGivesPrescription.py - Doctor enters the medicine id & medicine quantities details.<br />
<img width="907" alt="Screenshot 2024-07-06 113128" src="https://github.com/vermatic2010/AI-ML-based-smart-hospital-management-system/assets/127281006/c3724aee-4e7d-45a9-b0e5-c14986bee23e"><br /><br />
7. Run MedicinesBill.py<br />
<img width="960" alt="Screenshot 2024-07-06 113315" src="https://github.com/vermatic2010/AI-ML-based-smart-hospital-management-system/assets/127281006/3c83ac05-bd64-410b-8bfd-9447b91b3643">
