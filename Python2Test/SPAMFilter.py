# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:46:52 2015

@author: Administrator
"""
#屏蔽某些字符的类   Filter(超类)  ****Filter(子类)
class Filter:
    def init(self):
        self.blocked = []
    
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]
        
class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']
        
f = Filter()
f.init()
print f.filter([1,2,3])


s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'SPAM', 'hello'])

#检查继承
print issubclass(SPAMFilter , Filter)
print issubclass(Filter , SPAMFilter)

#基类
print SPAMFilter.__bases__
print Filter.__bases__

#检查一个方法是否是一个类的实例
s = SPAMFilter()
print isinstance(s, SPAMFilter)
print isinstance(s, Filter)
print isinstance(s, str)