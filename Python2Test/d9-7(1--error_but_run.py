__author__ = 'Administrator'

a = [1,2,3,4,5,6,7,8,9]
l = len(a)
print a

for i in range(5):
    a[i], a[l-i-1] = a[l-i-1], a[i]

print a