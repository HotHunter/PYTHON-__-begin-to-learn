__author__ = 'Administrator'

from Tkinter import *

root = Tk()

def hello():
    print('i love you wanglianhui!!!')

menubar = Menu(root)
menubar.add_command(label="Fuck!", command=hello)
menubar.add_command(label="ME!", command=root.quit)

root.config(menu=menubar)

mainloop()