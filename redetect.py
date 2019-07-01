import cv2
cap=cv2.VideoCapture(0)

while cap.isOpened():
  stats,frame=cap.read()
  red=cv2.inRange(frame,(0,0,0),(150,65,255))
  cv2.imshow('live',red)
  if cv2.waitKey(10) & 0xff == ord('q'):
     break
cv2.destroyAllWindows()
cap.release()