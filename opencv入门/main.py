import cv2
import matplotlib
import numpy
"""
img = cv2.imread('test.png', 1)#参数2  -1 不变  0 为灰度  1为彩色
img2 = cv2.imread('test.png',-1)
cv2.imshow("PNG", img)
cv2.imshow("PNG2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
cap = cv2.VideoCapture(0)

while True:
    ret ,frame =cap.read()
    #ret --布尔值
    #fream --帧
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #bgr blue green red
    cv2.imshow('frame',gray)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(0) & 0xFF == ord('a'):
        img_line=cv2.line(gray,(0,0),(170,290),(255,200,200),20)
        cv2.imshow('a',img_line)

cap.release()
cv2.destroyAllWindows()