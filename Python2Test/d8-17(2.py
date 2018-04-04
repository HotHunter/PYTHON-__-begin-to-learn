__author__ = 'Administrator'
# -*- coding: utf-8 -*-

y = input('Enter the year:')
m = input('Enter the month:')
d = input('Enter the day:')

sum = 0
end = 0

for i in range(1,m+1):
    if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
        if i == (1, 3, 5, 7, 8, 10, 12):
            sum += 31
        elif i == 2:
            sum += 29
        else:
            sum += 30
    else:
        if i == (1, 3, 5, 7, 8, 10, 12):
            sum += 31
        elif i == 2:
            sum += 28
        else:
            sum += 30
end = sum+d
print end

#草泥马的我就是个弱智啊！！！！