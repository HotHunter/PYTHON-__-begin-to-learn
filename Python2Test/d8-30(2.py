__author__ = 'Administrator'

#�Բ��������˼·��ţ�ƣ�ɸѡ��������


a = [0]*101

for i in range(2, 11):
    for j in range(i+i, 101, i):
        a[j] = -1
for i in range(2, 101):
    if a[i] != -1:
        print ' ', i,