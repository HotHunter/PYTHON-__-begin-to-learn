__author__ = 'Administrator'

def fun(n, s):
    if s == 0:
        return
    print n[s-1]
    fun(n, s-1)

n = raw_input('Input a string:')
s = len(n)
fun(n, s)

# def output(s, l):
#      if l == 0:
#          return
#      print s[l-1]
#      output(s, l-1)
#
# s = raw_input('Input a string:')
# l = len(s)
# output(s, l)
