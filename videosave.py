import cv2
cap=cv2.VideoCapture(0)

plugin=cv2.VideoWriter_fourcc(*'XVID')  #XVID is a plugin to suppoert MP4, AVi
output=cv2.VideoWriter('trial.mp4',plugin,90,(640,480)) #to save the video
while cap.isOpened():
 status,img=cap.read()
 cv2.imshow('liveimage',img)
 output.write(img)
 if cv2.waitKey(10) & 0xff == ord('q'):
   break
cv2.destroyWindow('liveimage')
cap.release()
