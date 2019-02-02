from tkinter import *
from datetime import *
from tkinter import ttk


class Calendar(ttk.Frame)
    
    def __init__(self, parent, **args):
      ttk.Frame.__init__(self, parent, )  










class MainApp (Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('532x422')
        self.title('Calendario Universal')   


    def start(self):
        self.mainloop()



if __name__ == '__main__':
    app = MainApp()
    app.start()
