__author__ = 'Administrator'

def fun(i, cut):
    if i == 0:
        print 'There are %d digit in the number' % cut
        return
    print i % 10,
    i /= 10
    cut += 1
    fun(i, cut)

i = int(raw_input('Enter a number:'))
fun(i, 0)