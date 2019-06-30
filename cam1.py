import cv2
cap=cv2.VideoCapture(0)
# first camera

#to check camera is on or not
print(cap.isOpened())

#now we can take read input from camera
print(cap.read())
#it wil take first pic

status,img=cap.read()

cv2.imshow('liveimage',img)
cv2.waitKey(0)