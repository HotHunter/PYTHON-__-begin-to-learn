__author__ = 'Administrator'

a = 2.0
b = 1.0
s = 0.0

for i in range(0, 50):
    s = s+a/b
    a = a+b
    b = a-b

print s