#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 09:23:26 2018

@author: prachi
"""

#Importing the required libraries for enhancing images

import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import imageio
import os

ia.seed(1)


#Set the path of the directory having the multiple directories with name as MCATID's and having images for that MCAT inside each of them
directory ="/home/imart/Downloads/mcatimagestest/train"


#Iterating over the above path to get inside each MCATID folder and perform the required enhancement operation on each image 
#(here, we are doing flipping left-right, rotation 15 degree clockwise and 15 degree anti-clockwise and mking the image grainy)

for directories in os.listdir(directory):
    for files in os.listdir((os.path.join(directory,str(directories)))):
        print(files)

        img = imageio.imread(os.path.join(directory,str(directories),str(files))) #read your image
        
        
        imagefliplr = np.array([img for _ in range(2)], dtype=np.uint8)  # 2 means create 2-1 i.e. 1 enhanced image using following methods.
        imagerotate = np.array([img for _ in range(2)], dtype=np.uint8)
        imagegrain = np.array([img for _ in range(2)], dtype=np.uint8)
        
        
        #Perform the image augmentations
        fliplr = iaa.Fliplr(0.5)   #create an object with 0.5 flipping i.e. left-right
        images1 = fliplr.augment_image(imagefliplr[0]) #Performing the augmentation
        
        imageio.imwrite(os.path.join(directory,str(directories),str(files)[:-4]+'_fliplr.jpg'), images1) #Writing the file to the required directory
        
        
        rotated = iaa.Affine(rotate=15,mode="symmetric")  #create an object with +15 degree rotation i.e. clockwise using Affine method which uses symmetric mode
        images3 = rotated.augment_image(imagerotate[0]) #Performing the augmentation
        imageio.imwrite(os.path.join(directory,str(directories),str(files)[:-4]+'_rotateclock.jpg'), images3) #Writing the file to the required directory
        
        
        rotated = iaa.Affine(rotate=-15,mode="symmetric") #create an object with -15 degree rotation i.e. anti-clockwise using Affine method which uses symmetric mode
        images2 = rotated.augment_image(imagerotate[0]) #Performing the augmentation
        imageio.imwrite(os.path.join(directory,str(directories),str(files)[:-4]+'_rotateanticlock.jpg'), images2) #Writing the file to the required directory
        
        
        grainy = iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05 * 255), per_channel=0.5)
        images4 = grainy.augment_image(imagegrain[0])
        imageio.imwrite(os.path.join(directory,str(directories),str(files)[:-4]+'_grainy.jpg'), images4)