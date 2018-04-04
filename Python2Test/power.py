# -*- coding: utf-8 -*-
"""
Created on Sun Aug 09 21:24:06 2015

@author: Administrator
"""

def power(x,n):
    if n == 1:
        return x
    else:
        return x * power(x,n-1)
        
print power(2,5)