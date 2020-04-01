#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:09:17 2020

@author: sangam
"""
from threading import Thread

class Hello(Thread):
    def run(self):
        for _ in range(500):
            print("Hello")

class Hi(Thread):
    def run(self):
        for _ in range(500):
            print("Hi")
   

t1=Hello()
t2=Hi()

t1.start()
t2.start()