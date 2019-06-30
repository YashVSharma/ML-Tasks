import cv2
cap=cv2.VideoCapture(0)
# first camera

#to check camera is on or not
while cap.isOpened():
 status,img=cap.read()
 cv2.imshow('liveimage',img)
 if cv2.waitKey(10) & 0xff == ord('q'):
   break
cv2.destroyWindow('liveimage')
cv.release()
