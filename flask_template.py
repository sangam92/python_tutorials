#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 08:44:03 2019

@author: sangam
"""

from flask import Flask, render_template

app =Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run()