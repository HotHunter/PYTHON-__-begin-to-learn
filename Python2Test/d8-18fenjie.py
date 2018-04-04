__author__ = 'Administrator'


def main():
    n = int(raw_input('Enter a number:'))
    print n, '=',

    while(n != 1):
        for i in range(2, n+1):
            if(n % i) == 0:
                n /= i
                if(n == 1):
                    print i,
                else:
                    print i, '*',
                break

if __name__ == "__main__":
    main()