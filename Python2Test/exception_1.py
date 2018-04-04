# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:03:29 2015

@author: Administrator
"""

try:
    x = input('enter the first number: ')
    y = input('enter the senond number: ')
    print x/y
    
except ZeroDivisionError:
    print "The second number can't be zero!!"