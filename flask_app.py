#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 23:23:59 2020

@author: sangam
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')