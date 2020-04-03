import cv2
import os

def acquisition():
    webcam = cv2.VideoCapture(0) 
    check, frame = webcam.read()
    webcam.release()
    cv2.imwrite(filename='saved_img.jpg', img=frame)
    img = cv2.imread('saved_img.jpg', cv2.COLOR_BGR2HSV)
    os.remove('saved_img.jpg')
    return(img)


def save(rep,frame):
    cv2.imwrite(filename=rep+'.jpg', img=frame)
    return()

a=acquisition()
cv2.imshow('test',a)