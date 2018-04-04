# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 21:33:39 2015

@author: Administrator
"""

girls = ['alice' , 'bernice' , 'clarice']
boys = ['chris' , 'arnold' , 'bob']

letterGirls = {}

for girl in girls:
    letterGirls.setdefault(girl[0] , []).append(girl)
    
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]