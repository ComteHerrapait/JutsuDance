# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:16:11 2020

@author: jbapt
"""
import cv2
import numpy as np
import classification as cl
import matplotlib.pyplot as plt
import sys


# img1=cv2.imread('1.jpg')
# img1=cl.segmenatationMain(img1)
# #sklt=cl.find_skeleton2(img1.astype(np.uint8))
# #plt.imshow(sklt[0])
# print(cl.orientation(img1))
# sys.exit()







# img1=cv2.cvtColor(cv2.imread('1.jpg'), cv2.COLOR_BGR2LAB)
# img2=cv2.cvtColor(cv2.imread('2.jpg'), cv2.COLOR_BGR2LAB)
# img3=cv2.cvtColor(cv2.imread('3.jpg'), cv2.COLOR_BGR2LAB)
# img4=cv2.cvtColor(cv2.imread('4.jpg'), cv2.COLOR_BGR2LAB)
# img5=cv2.cvtColor(cv2.imread('5.jpg'), cv2.COLOR_BGR2LAB)
# img6=cv2.cvtColor(cv2.imread('6.jpg'), cv2.COLOR_BGR2LAB)
# img7=cv2.cvtColor(cv2.imread('7.jpg'), cv2.COLOR_BGR2LAB)
# img8=cv2.cvtColor(cv2.imread('8.jpg'), cv2.COLOR_BGR2LAB)
# img9=cv2.cvtColor(cv2.imread('9.jpg'), cv2.COLOR_BGR2LAB)
# img10=cv2.cvtColor(cv2.imread('10.jpg'), cv2.COLOR_BGR2LAB)
# img11=cv2.cvtColor(cv2.imread('11.jpg'), cv2.COLOR_BGR2LAB)
# img12=cv2.cvtColor(cv2.imread('12.jpg'), cv2.COLOR_BGR2LAB)
# img13=cv2.cvtColor(cv2.imread('13.jpg'), cv2.COLOR_BGR2LAB)
# img14=cv2.cvtColor(cv2.imread('14.jpg'), cv2.COLOR_BGR2LAB)
# img15=cv2.cvtColor(cv2.imread('15.jpg'), cv2.COLOR_BGR2LAB)
# img16=cv2.cvtColor(cv2.imread('16.jpg'), cv2.COLOR_BGR2LAB)
# img17=cv2.cvtColor(cv2.imread('17.jpg'), cv2.COLOR_BGR2LAB)
# img18=cv2.cvtColor(cv2.imread('18.jpg'), cv2.COLOR_BGR2LAB)
# img19=cv2.cvtColor(cv2.imread('19.jpg'), cv2.COLOR_BGR2LAB)
# img20=cv2.cvtColor(cv2.imread('20.jpg'), cv2.COLOR_BGR2LAB)
# img21=cv2.cvtColor(cv2.imread('21.jpg'), cv2.COLOR_BGR2LAB)

img1=cv2.imread('1.jpg')
img2=cv2.imread('2.jpg')
img3=cv2.imread('3.jpg')
img4=cv2.imread('4.jpg')
img5=cv2.imread('5.jpg')
img6=cv2.imread('6.jpg')
img7=cv2.imread('7.jpg')
img8=cv2.imread('8.jpg')
img9=cv2.imread('9.jpg')
img10=cv2.imread('10.jpg')
img11=cv2.imread('11.jpg')
img12=cv2.imread('12.jpg')
img13=cv2.imread('13.jpg')
img14=cv2.imread('14.jpg')
img15=cv2.imread('15.jpg')
img16=cv2.imread('16.jpg')
img17=cv2.imread('17.jpg')
img18=cv2.imread('18.jpg')
img19=cv2.imread('19.jpg')
img20=cv2.imread('20.jpg')
img21=cv2.imread('21.jpg')

h1=cl.createFeatureVector(img1)    
h2=cl.createFeatureVector(img2)
h3=cl.createFeatureVector(img3)
h4=cl.createFeatureVector(img4)
h5=cl.createFeatureVector(img5)
h6=cl.createFeatureVector(img6)
h7=cl.createFeatureVector(img7)    
h8=cl.createFeatureVector(img8)
h9=cl.createFeatureVector(img9)
h10=cl.createFeatureVector(img10)
h11=cl.createFeatureVector(img11)
h12=cl.createFeatureVector(img12)
h13=cl.createFeatureVector(img13)    
h14=cl.createFeatureVector(img14)
h15=cl.createFeatureVector(img15)
h16=cl.createFeatureVector(img16)
h17=cl.createFeatureVector(img17)
h18=cl.createFeatureVector(img18)
h19=cl.createFeatureVector(img19)    
h20=cl.createFeatureVector(img20)
h21=cl.createFeatureVector(img21)

dataset1=np.concatenate((h1.T, h4.T,h7.T,h10.T,h13.T,h16.T,h19.T),axis=0)
dataset2=np.concatenate((h2.T, h5.T,h8.T,h11.T,h14.T,h17.T,h20.T),axis=0)
dataset3=np.concatenate((h3.T, h6.T,h9.T,h12.T,h15.T,h18.T,h21.T),axis=0)

cluster1=cl.createCluster(np.concatenate((dataset1, dataset2),axis=0))
cluster2=cl.createCluster(np.concatenate((dataset2, dataset3),axis=0))
cluster3=cl.createCluster(np.concatenate((dataset1, dataset3),axis=0))
print('k=1')
print(cl.findcluster(h1.T,cluster1))
print(cl.findcluster(h2.T,cluster1))
print(cl.findcluster(h3.T,cluster1))

print(cl.findcluster(h4.T,cluster1))
print(cl.findcluster(h5.T,cluster1))
print(cl.findcluster(h6.T,cluster1))

print(cl.findcluster(h7.T,cluster1))
print(cl.findcluster(h8.T,cluster1))
print(cl.findcluster(h9.T,cluster1))

print(cl.findcluster(h10.T,cluster1))
print(cl.findcluster(h11.T,cluster1))
print(cl.findcluster(h12.T,cluster1))

print(cl.findcluster(h13.T,cluster1))
print(cl.findcluster(h14.T,cluster1))
print(cl.findcluster(h15.T,cluster1))

print(cl.findcluster(h16.T,cluster1))
print(cl.findcluster(h17.T,cluster1))
print(cl.findcluster(h18.T,cluster1))

print(cl.findcluster(h19.T,cluster1))
print(cl.findcluster(h20.T,cluster1))
print(cl.findcluster(h21.T,cluster1))


print('k=2')

print(cl.findcluster(h1.T,cluster2))
print(cl.findcluster(h2.T,cluster2))
print(cl.findcluster(h3.T,cluster2))

print(cl.findcluster(h4.T,cluster2))
print(cl.findcluster(h5.T,cluster2))
print(cl.findcluster(h6.T,cluster2))

print(cl.findcluster(h7.T,cluster2))
print(cl.findcluster(h8.T,cluster2))
print(cl.findcluster(h9.T,cluster2))

print(cl.findcluster(h10.T,cluster2))
print(cl.findcluster(h11.T,cluster2))
print(cl.findcluster(h12.T,cluster2))

print(cl.findcluster(h13.T,cluster2))
print(cl.findcluster(h14.T,cluster2))
print(cl.findcluster(h15.T,cluster2))

print(cl.findcluster(h16.T,cluster2))
print(cl.findcluster(h17.T,cluster2))
print(cl.findcluster(h18.T,cluster2))

print(cl.findcluster(h19.T,cluster2))
print(cl.findcluster(h20.T,cluster2))
print(cl.findcluster(h21.T,cluster2))

print('k=3')

print(cl.findcluster(h1.T,cluster3))
print(cl.findcluster(h2.T,cluster3))
print(cl.findcluster(h3.T,cluster3))

print(cl.findcluster(h4.T,cluster3))
print(cl.findcluster(h5.T,cluster3))
print(cl.findcluster(h6.T,cluster3))

print(cl.findcluster(h7.T,cluster3))
print(cl.findcluster(h8.T,cluster3))
print(cl.findcluster(h9.T,cluster3))

print(cl.findcluster(h10.T,cluster3))
print(cl.findcluster(h11.T,cluster3))
print(cl.findcluster(h12.T,cluster3))

print(cl.findcluster(h13.T,cluster3))
print(cl.findcluster(h14.T,cluster3))
print(cl.findcluster(h15.T,cluster3))

print(cl.findcluster(h16.T,cluster3))
print(cl.findcluster(h17.T,cluster3))
print(cl.findcluster(h18.T,cluster3))

print(cl.findcluster(h19.T,cluster3))
print(cl.findcluster(h20.T,cluster3))
print(cl.findcluster(h21.T,cluster3))