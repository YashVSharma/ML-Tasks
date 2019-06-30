import cv2
cap=cv2.VideoCapture(0)
# first camera

#to check camera is on or not
while cap.isOpened():
 status,img=cap.read()
 greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 cv2.line(img,(0,0),(300,300),(0,255,0),6)
 cv2.rectangle(img,(80,90),(190,190),(0,255,0),10)
 font=cv2.FONT_HERSHEY_SIMPLEX #this is font supported by numpy
 cv2.putText(img,'Chakk De Phatte',(30,50),font,2,(0,2,55),3,cv2.LINE_AA)
 cv2.imshow('liveimage',img)

 #cv2.imshow('b/w',greyimg)
 if cv2.waitKey(10) & 0xff == ord('q'):
   break
cv2.destroyWindow('liveimage')
cap.release()
