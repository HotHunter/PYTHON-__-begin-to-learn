# -*- coding: utf-8 -*-
"""
Created on Sun Aug 09 21:15:52 2015

@author: Administrator
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
        
        
print factorial(4)