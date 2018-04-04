# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:49:25 2015

@author: Administrator
"""

try:
    x = input('enter the first number: ')
    y = input('enter the senond number: ')
    print x/y
    
except (ZeroDivisionError, TypeError), e:
    print e