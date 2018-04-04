# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:33:14 2015

@author: Administrator
"""

from math import sqrt

result1 = []
for num in range(2, 100):
     f = True
     for snu in range(2, int(sqrt(num))+1):
         if num % snu == 0:
            f = False
            break
     if f:
         result1.append(num)
print result1
