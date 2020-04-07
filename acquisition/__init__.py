import cv2
import os

def acq(space, height=480,width=640): #'HSV' pour le format HSV et 'LAB' pour le format LAB
    webcam = cv2.VideoCapture(0) 
    webcam.set(4,height) # 4 : format de l'image en hauteur
    webcam.set(3,width) # 3 : format de l'image en largeur
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
    if space=='RGB' :
        imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return(imgRGB)
    return(img)


def save(name,image):
    cv2.imwrite(filename=(name+'.jpg'), img=image)
    return()
