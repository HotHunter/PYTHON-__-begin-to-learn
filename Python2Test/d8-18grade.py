__author__ = 'Administrator'

def main():
    s = int(raw_input('Enter a grade:'))

    if s>=90:
        grade = 'A'
    elif s>=60:
        grade = 'B'
    else:
        grade = 'C'
    print grade


main()