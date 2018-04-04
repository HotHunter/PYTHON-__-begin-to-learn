# -*- coding: utf-8 -*-
"""
Created on Sun Aug 09 20:31:14 2015

@author: Administrator
"""

def story(**kwds):
    return 'Once upon a time, there was a '\
            '%(job)s called %(name)s.' % kwds
#pow()  x的y次幂           
def power(x,y, *others):
    if others:
        print 'Received redundant paramenters:' , others
    return pow(x, y)
    
def interval(start , stop=None , step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0 , start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result
    
params = {'job' : 'language', 'name' : 'Python'}
paramz = (5,) * 2

print paramz


