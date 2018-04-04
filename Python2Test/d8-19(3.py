__author__ = 'Administrator'

s = 100
h = 50.0

for i in range(2,11):
    s += h
    h /= 2

print 'length:%f' % s
print 'last:%f' %h