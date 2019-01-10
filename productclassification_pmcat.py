#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:28:46 2018

@author: imart
"""
# Importing the essential libraries
import pandas as pd
import os
import urllib.request

#Reading the data from csv file

file1 = pd.read_excel('productClassificationfullmcats final list.xlsx',sheet_name='Final Sheet')


# Fetching the unique PMCAT ID's from the above data

uniqPMCAT = list(file1['PMCAT ID'].unique())



#classification of images on basis of PMCAT Id

for x in range(0,len(uniqPMCAT)):
    
    # creating the folder by the name of the PMCAT
    newPMCATpath = str(uniqPMCAT[x])
    if not os.path.exists(newPMCATpath):
        os.makedirs(newPMCATpath)
        
    a = ""
    
    #Retrieving the unique PCID's corresponding to these PMCAT's
    uniqPCID = list(file1.loc[file1['PMCAT ID'] == uniqPMCAT[x]]['PC_ITEM_ID'].unique())
    
    
    #Renaming as PCID and storing the images in the PMCAt folder 
    for i in range(0,len(uniqPCID)):
        newPCIDpath = os.path.join(newPMCATpath,str(uniqPCID[i])+'.jpg')
        
        a = str(file1.loc[file1['PC_ITEM_ID'] == uniqPCID[i]]['PC_ITEM_IMG_ORIGINAL'].unique())[2:-2]
         
        
        if a!= 'a':
            urllib.request.urlretrieve(a, newPCIDpath)
        
      