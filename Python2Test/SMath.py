# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:10:28 2015

@author: Administrator
"""

"""利用python作为科学计算器。熟悉Python中的常用运算符，并分别求出表达
式12*34+78-132/6、(12*(34+78)-132)/6、(86/40)**5的值。并利用math模块进行数学计算，
分别求出145/23的余数，0.5的sin和cos值
（注意sin和cos中参数是弧度制表示）提醒:可通过import math; help("math")查看math帮助."""

import math

x = 12*34+78-132/6
y = (12*(34+78)-132)/6
z = (86/40)**5

print x
print y
print z

a = math.fmod(145,23)
b = math.sin(0.5)
c = math.cos(0.5)

print a
print b
print c