__author__ = 'Administrator'


def fun(n):
    if n == 1:
        return 10
    else:
        return fun(n-1) + 2

print fun(5)