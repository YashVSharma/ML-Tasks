import cv2

casclf=cv2.CascadeClassifier('face.xml')
#load face data
cap=cv2.VideoCapture(0)

while cap.isOpened():
  status,frame=cap.read()
  face=casclf.detectMultiScale(frame,1.13,5)
  #print(face)
  for x,y,h,w in face:
    cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
    facedata=frame[x:x+h,y:y+w]  
    #cv2.imshow('f',facedata)   
  cv2.imshow('face',frame) 
  if cv2.waitKey(10) & 0xff==ord('q'):
    break
cv2.destroyAllWindows()
cap.release()