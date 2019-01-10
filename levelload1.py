#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:08:22 2018

@author: prachi
"""

#Importing the required libraries

import os
import operator
import math
import pandas as pd
import shutil

#Set the path of the directory having the multiple directories with name as MCATID's and having images for that MCAT inside each of them
directory = "/home/imart/Downloads/mcatimagestest/train"

#Finding the names of MCATID's and storing into a list
numoffolders=os.listdir(directory)
        
#Initialising the counter variable and a list for number of files 
count=0
numoffiles=[]


#Finding the number of files in each MCATID folder and store in a list
for directories in os.listdir(directory):
    count=0
    for files in os.listdir((os.path.join(directory,str(directories)))):
        
        count+=1
    numoffiles.append(count)
 
 
#Create a dictionary which stores the mapping of MCATID name to the number of images it contains   
numberdict=dict(zip(numoffolders,numoffiles))   

#Finding the maximum number of files out of all the file counts
maxfiles=max(numoffiles)   

#sorting the dictionary according to file count (for analysis purpose)
sorted_x = sorted(numberdict.items(), key=operator.itemgetter(1))

#Finding the mean of all the file counts (for analysis purpose)
avg=math.floor(pd.Series(numoffiles).mean())


#Taking the 0.98 quantile for the file counts
quantrange = math.floor(pd.Series(numoffiles).quantile(q=0.98))


#Iterating over the directory path to find the folders where the number of files is less than the quantile range, and if found, copy the files to level load the images upto 'factor' times(where factor is the remainder of quantile range by the number of files in that directory) 
for directories in os.listdir(directory):
    factor = math.floor(quantrange/numberdict[directories])
    for files in os.listdir((os.path.join(directory,str(directories)))):
        
        if(numberdict[directories]<=quantrange):
            for c in range(1,factor+1):
                shutil.copy(directory+'/'+directories+'/'+files,directory+'/'+directories+'/'+files[:-4]+'copy'+str(c)+'.jpg')
