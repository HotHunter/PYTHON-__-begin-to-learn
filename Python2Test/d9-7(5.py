__author__ = 'Administrator'

from Tkinter import *
def hello():
    print('hello world')

win = Tk()
win.title('hellomotherfucker')
win.geometry('400x200')

btn = Button(win, text='Click my dick!', command=hello)

btn.pack(expand=YES, fill=BOTH)

mainloop()