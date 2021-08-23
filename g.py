'''import pandas as pd
import cv2
covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')
covid_data['Active'] = covid_data['Confirmed'] - covid_data['Deaths'] - covid_data['Recovered']
#result = covid_data.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
print(covid_data)'''
import cv2
import numpy as np
face_classifier = cv2.CascadeClassifier('F:/mypython/facial_recognisation/haarcacade_frontlace_default.xml')

def face_extractor(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return  None
    for(x,y,w,h) in faces:
        cropped_faces=img[y:y+h,x:x+w]
    return cropped_faces







cap =cv2.VideoCapture(0)
count=0

while True:
    ret, frame=cap.read()
    print(frame)
    if face_extractor(frame) is not None:

        count+=1
        face=cv2.resize(face_extractor(frame),(200,200))
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

        file_name_path='C:/Users/ASUS/Downloads/images/user'+ str(count) + '.jpg'
        cv2.imwrite(file_name_path,face)

        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('face cropper',face)
    else:
        print('face not found')
        
    #if cv2.waitkey(1)==13:
     #   cv2.destroyAllWindows()
      #  break

cap.release()
cap.deleteAllWindows()
print('collecting samples complete')





