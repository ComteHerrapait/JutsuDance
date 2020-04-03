import cv2
import os

def acquisition():
    webcam = cv2.VideoCapture(0)
    check, frame = webcam.read()
    webcam.release()
    cv2.imwrite(filename='saved_img.jpg', img=frame)
    img = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('testrgb',img)
    cv2.waitKey(0)
    cv2.imshow('testhsv',imghsv)
    cv2.waitKey(0)
    os.remove('saved_img.jpg')
    return(img,imghsv)


def save(rep,frame):
    cv2.imwrite(filename=rep+'.jpg', img=frame)
    return()


a=acquisition()