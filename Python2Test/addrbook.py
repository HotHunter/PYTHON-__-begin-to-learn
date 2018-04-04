# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 21:05:07 2015

@author: Administrator
"""

people = {
    'Alice':{
        'phone':2344234,
        'addr':'hahah'
    },
    
    'Beth':{
        'phone':979789,
        'addr':'okokok'
        },
    
    'Jay':{
        'phone':687876,
        'addr':'bybyby'
        }
}

labels = {
    'phone' : 'phone number',
    'addr' : 'address'
    }
    
name = raw_input('Name:')

request = raw_input('phone number(p) or address(a)?')

if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

if name in people : print "%s's %s is %s ." %\
    (name, labels[key], people[name][key])