__author__ = 'Administrator'


MAXONE = lambda x,y : (x > y) * x + (x < y) * y
MINONE = lambda x,y : (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print "max:%d" % MAXONE(a,b)
    print "min:%d" % MINONE(a,b)