__author__ = 'Administrator'

#卧槽这个方法思路好牛逼，筛选法求质数


a = [0]*101

for i in range(2, 11):
    for j in range(i+i, 101, i):
        a[j] = -1
for i in range(2, 101):
    if a[i] != -1:
        print ' ', i,