# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:54:29 2015

@author: Administrator
"""

year = input("give me a year:")

if year%400==0 or year%4==0 and year%100<>0:
    print "%s is runnian " %year
else:
    print "%s is not runnian" %year 