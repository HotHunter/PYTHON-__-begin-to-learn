__author__ = 'Administrator'

ans = ['Yes', 'No']

i = int(raw_input('Input a number(10000~99999):'))
if i<10000 or i>99999:
    print 'Input Error'
else:
    i = str(i)
    flag = 0
    for j in range(0, 2):
        if i[j] != i[4-j]:
            flag = 1
            break
    print ans[flag]