import cv2.py

cap=cv2.VideoCapture(0)

tp1=cap.read()[1]  #take1
tp2=cap.read()[1]  #take2 
tp3=cap.read()[1]  #take3

g1=cv2.cvtColor(tp1,cv2.COLOR_BG2GRAY) 
g2=cv2.cvtColor(tp2,cv2.COLOR_BG2GRAY)
g3=cv2.cvtColor(tp3,cv2.COLOR_BG2GRAY)