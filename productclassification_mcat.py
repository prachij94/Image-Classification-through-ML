#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:29:49 2018

@author: imart
"""
# Importing the essential libraries
import pandas as pd
import os
import urllib.request


#Reading the data from csv file
file1 = pd.read_excel('productClassificationfullmcats final list.xlsx',sheet_name='Final Sheet')


# Fetching the unique MCAT ID's from the above data
uniqMCAT = list(file1['Current MCAT'].unique())



##classification of images on basis of MCAT Id


for x1 in range(0,len(uniqMCAT)):
    
    
    # creating the folder by the name of the MCAT
    newMCATpath = str(uniqMCAT[x1])
    if not os.path.exists(newMCATpath):
        os.makedirs(newMCATpath)
        
    b = ""
    
    #Retrieving the unique PCID's corresponding to these MCAT's
    uniqPCID1 = list(file1.loc[file1['PMCAT ID'] == uniqMCAT[x1]]['PC_ITEM_ID'].unique())
    
    
    
    #Renaming as PCID and storing the images in the PMCAt folder
    for i in range(0,len(uniqPCID1)):
        newPCIDpath1 = os.path.join(newMCATpath,str(uniqPCID1[i])+'.jpg')
        
        
        
        b = str(file1.loc[file1['PC_ITEM_ID'] == uniqPCID1[i]]['PC_ITEM_IMG_ORIGINAL'].unique())[2:-2]
         
        
        if b!= 'a':
            urllib.request.urlretrieve(b, newPCIDpath1)
    