# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 22:23:22 2015

@author: Administrator
"""

fibs = [0,1]

num = input('How may Fibonacci numbers do you want?')

for i in range(num-2):
    fibs.append(fibs[-2] + fibs[-1])
print fibs