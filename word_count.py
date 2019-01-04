#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 06:16:23 2019

@author: sangam
"""

words = ['A','boy','is','a','the','boy','is','the','the','india'] 
wordcount = {}


for word in words:
    if word not in wordcount:
        wordcount[word] =1
    else:
        wordcount[word] +=1
    
    
for k,v  in wordcount.items():
    print(k,v)