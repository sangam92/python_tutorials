#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 23:11:30 2019

@author: sangam
"""
import pickle

data_to_be_pickle = ['tad','five','kyle','Ram']

dump_filename = 'file_pickle'

outfile = open(dump_filename,'wb')

data_to_be_dumped = pickle.dump(data_to_be_pickle,outfile)

outfile.close()

infile = open(dump_filename,'rb')



data_to_be_unpickle = pickle.load(infile)

print(data_to_be_unpickle)