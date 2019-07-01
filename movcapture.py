import cv2

cap=cv2.VideoCapture(0)

tp1=cap.read()[1]  #take1
tp2=cap.read()[1]  #take2 
tp3=cap.read()[1]  #take3

g1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY) 
g2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
g3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

def img_diff(x,y,z):
  #diff g1-g2
  d1=cv2.absdiff(x,y)
  #diff g2-g3
  d2=cv2.absdiff(y,z)
  #diff g3-g1
  d3=cv2.bitwise_and(d1,d2)
  return d3

#now apply function
while cap.isOpened():
  status,frame=cap.read()
  motion=img_diff(g1,g2,g3)
  #replacing image frame
  g1=g2
  g2=g3
  g3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  cv2.imshow('motion',frame)
  cv2.imshow('motion',motion)
  if cv2.waitKey(10)  & 0xff == ord('q'):
    break
cv2.destroyAllWindows()
cap.release()