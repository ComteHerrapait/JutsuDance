import cv2
import os

def acq(space): #'HSV' pour le format HSV et 'LAB' pour le format LAB
    webcam = cv2.VideoCapture(0) 
    check, frame = webcam.read()
    cv2.imwrite(filename='saved_img.jpg', img=frame)
    webcam.release()
    img = cv2.imread('saved_img.jpg', cv2.IMREAD_COLOR)
    os.remove('saved_img.jpg') 
    if space=='HSV':
        imgHSV=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        return(imgHSV)
    if space=='LAB':
        imgLAB=cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        return(imgLAB)
    return()

def save(rep,image):
    cv2.imwrite(filename=(rep+'.jpg'), img=image)
    return()

