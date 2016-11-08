#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image
import scipy
import numpy as np
import cv2
import os

nomeImagem="muitas_crateras.jpg"

def medianBlur(img):
    img_blur=cv2.medianBlur(img,7);
    return img_blur

def averageBlur(img):
    kernel = np.ones((5,5),np.float32)/25
    img_blur=cv2.filter2D(img,-1,kernel);
    return img_blur

def highBoostBlur(img, img_blur, c):
    print(type(img))
    mag = cv2.Laplacian(img, cv2.CV_16S, ksize=int(c*2))
    mag = cv2.convertScaleAbs(mag)
    print(type(mag))
    return mag#np.subtract(img, img_blur)

def noFiltro(img):
    pixels=np.array(img.getdata())
    ii,jj=img.size
    pixels=pixels.reshape(jj,ii)
    dx=ndimage.sobel(img,0) #Ox
    dy=ndimage.sobel(img,1) #Oy
    mag=np.hypot(dx,dy)#magnetude
    #mag*=255.0/np.max(mag) #normalização
    np.place(dx,dx==0,1)
    divided=np.divide(dy,dx)
    direc=np.arctan(divided)*180/np.pi
    for i in range(len(direc)):
        for j in range(len(direc[i])):
            if(direc[i][j]<=30):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and  mag[i][j]>mag[i][j-1]+mag[i][j+1]):
                    pixels[i][j]=mag[i][j]
                else:
                    pixels[i][j]=0
            elif(direc[i][j]>30 and direc[i][j]<=60):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j+1]+mag[i-1][j-1]):
                    pixels[i][j]=mag[i][j]
                else:
                    pixels[i][j]=0
            elif(direc[i][j]>60 and direc[i][j]<=90):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j]+mag[i-1][j]):
                    pixels[i][j]=mag[i][j]
                else:
                    pixels[i][j]=0
            elif(direc[i][j]>90 and direc[i][j]<=120):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j-1]+mag[i-1][j+1]):
                    pixels[i][j]=mag[i][j]
                else:
                    pixels[i][j]=0
    pixels=pixels.astype(np.uint8)
    result=Image.fromarray(pixels)
    result.save('results/semFiltro.png')

def media(img):
    pixels=np.array(img.getdata())
    ii,jj=img.size
    pixels=pixels.astype(np.uint8)
    pixels=averageBlur(pixels)
    pixels=pixels.reshape(jj,ii)
    result=Image.fromarray(pixels)
    dx=ndimage.sobel(img,0) #Ox
    dy=ndimage.sobel(img,1) #Oy
    mag=np.hypot(dx,dy)#magnetude
    #mag*=255.0/np.max(mag) #normalização
    np.place(dx,dx==0,1)
    divided=np.divide(dy,dx)
    direc=np.arctan(divided)*180/np.pi
    pixels2=np.zeros((jj,ii))
    for i in range(len(direc)):
        for j in range(len(direc[i])):
            if(direc[i][j]<=30):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and  mag[i][j]>mag[i][j-1]+mag[i][j+1]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
            elif(direc[i][j]>30 and direc[i][j]<=60):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j+1]+mag[i-1][j-1]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
            elif(direc[i][j]>60 and direc[i][j]<=90):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j]+mag[i-1][j]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
            elif(direc[i][j]>90 and direc[i][j]<=120):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j-1]+mag[i-1][j+1]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
    pixels2=pixels2.astype(np.uint8)
    result=Image.fromarray(pixels2)
    result.save('results/media.png')

def mediana(img):
    pixels=np.array(img.getdata())
    ii,jj=img.size
    pixels=pixels.astype(np.uint8)
    pixels=medianBlur(pixels)
    pixels=pixels.reshape(jj,ii)
    result=Image.fromarray(pixels)
    dx=ndimage.sobel(img,0) #Ox
    dy=ndimage.sobel(img,1) #Oy
    mag=np.hypot(dx,dy)#magnetude
    #mag*=255.0/np.max(mag) #normalização
    np.place(dx,dx==0,1)
    divided=np.divide(dy,dx)
    direc=np.arctan(divided)*180/np.pi
    pixels2=np.zeros((jj,ii))
    for i in range(len(direc)):
        for j in range(len(direc[i])):
            if(direc[i][j]<=30):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and  mag[i][j]>mag[i][j-1]+mag[i][j+1]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
            elif(direc[i][j]>30 and direc[i][j]<=60):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j+1]+mag[i-1][j-1]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
            elif(direc[i][j]>60 and direc[i][j]<=90):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j]+mag[i-1][j]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
            elif(direc[i][j]>90 and direc[i][j]<=120):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j-1]+mag[i-1][j+1]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
    pixels2=pixels2.astype(np.uint8)
    result=Image.fromarray(pixels2)
    result.save('results/mediana.png')

def passaAlta(img):
    pixels=np.array(img.getdata())
    ii,jj=img.size
    pixels=pixels.astype(np.uint8)
    mpixels=medianBlur(pixels)
    mpixels=mpixels.astype(np.uint8)
    pixels=highBoostBlur(pixels,mpixels,1.5)
    pixels=pixels.reshape(jj,ii)
    result=Image.fromarray(pixels)
    result.save('results/passaaltaBlur1.5.png')
    dx=ndimage.sobel(img,0) #Ox
    dy=ndimage.sobel(img,1) #Oy
    mag=np.hypot(dx,dy)#magnetude
    mag*=255.0/np.max(mag) #normalização
    np.place(dx,dx==0,1)
    divided=np.divide(dy,dx)
    direc=np.arctan(divided)*180/np.pi
    pixels2=np.zeros((jj,ii))
    
    for i in range(len(direc)):
        for j in range(len(direc[i])):
            if(direc[i][j]<=30):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and  mag[i][j]>mag[i][j-1]+mag[i][j+1]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
            elif(direc[i][j]>30 and direc[i][j]<=60):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j+1]+mag[i-1][j-1]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
            elif(direc[i][j]>60 and direc[i][j]<=90):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j]+mag[i-1][j]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
            elif(direc[i][j]>90 and direc[i][j]<=120):
                if(j-1>=0 and i-1>=0 and i+1<jj and j+1 <ii and mag[i][j]>mag[i+1][j-1]+mag[i-1][j+1]):
                    pixels2[i][j]=pixels[i][j]
                else:
                    pixels2[i][j]=0
    
    pixels2=pixels2.astype(np.uint8)
    result=Image.fromarray(pixels2)
    result.save('results/passaAlta1.5.png')

if __name__=="__main__":
    img=Image.open(nomeImagem).convert(mode="L")
    '''print "Imagem sem filtro"
    noFiltro(img)
    print "Media"
    media(img)
    print "Mediana"
    mediana(img)
    print "High pass"'''
    passaAlta(img)
