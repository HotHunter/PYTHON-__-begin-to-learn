__author__ = 'Administrator'

from os import *
from sys import *
from wx import *
ID_OPEN = 101
ID_EXIT = 110
ID_SAVE = 111
ID_BUTTON = 112

class MainWindow(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500,100))
        self.control = wx.TextCtrl(self, 1, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        filemenu  = wx.Menu()
        filemenu.Append(ID_OPEN, "open_file", "open file")
        filemenu.AppendSeparator()
        filemenu.Append(ID_SAVE, "save_file", "save file")
        filemenu.AppendSeparator()
        filemenu.Append(ID_EXIT, "exit", "exit")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "files")
        self.SetMenuBar(menuBar)
        wx.EVT_MENU(self, ID_OPEN, self.open)
        wx.EVT_MENU(self, ID_SAVE, self.save)
        wx.EVT_MENU(self, ID_EXIT, self.exit)
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []

        for i in range(0,6):
            self.buttons.append(wx.Button(self,ID_BUTTON+i,"Button &"+'i'))
            self.sizer2.Add(self.buttons[i],1,wx.EXPAND)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sezer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        self.Show(True)

    def exit(self):
        self.Close(True)

    def open(self):

        self.dirname = ''
        dlg = wx.FileDialog(self, "chose a file", self.dirname, "", "*.*", wx.OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def save(self):

        try:
            f = open(os.path.join(self.dirname, self.filename), 'w')

        except AttributeError:
            print 'file is not exist'
            sys.exit(0)

        content = self.control.GetValue()
        try:
            f.write(content)

        except UnboundLocalError:
            print 'file is not exist'
            sys.exit(0)
        finally:
            f.close()

app = wx.PySimpleApp()
frame = MainWindow(None, -1, 'Small editor')
app.MainLoop()

