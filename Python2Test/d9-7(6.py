__author__ = 'Administrator'

from Tkinter import *
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="QUIT", fg = 'red', command=frame.quit)
        self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text="who are your lover?", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "must you my lady,nice to meet you~~"

win = Tk()
app = App(win)
win.mainloop()