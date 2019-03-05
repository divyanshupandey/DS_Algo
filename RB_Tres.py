#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:29:00 2019

@author: dprasad@ad.msystechnologies.com
"""

with open('/home/ad.msystechnologies.com/dprasad/Downloads/vocab.vi') as f:
    mylist = [line.rstrip('\n') for line in f]

dictOfWords = { i : 0 for i in mylist }