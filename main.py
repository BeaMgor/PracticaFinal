from tkinter import *
from tkinter import ttk
from datetime import * 


class Calendar(ttk.Frame):
    
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=args['height'],width=args['width'])  


        self.header = Frame(self, width = 532, height = 40).place(x=0, y=0)
        self.__btnLastYear = Button(self, text = '<<', font=('Arial',24), width = 3, height= 1).place(x=10, y=5)
        self.__btnLastMonth = Button(self, text = '<', font=('Arial',24), width = 3, height= 1).place(x=100, y=5)
        self.__btnNextMonth = Button(self, text = '>', font=('Arial',24), width = 3, height= 1).place(x=380,y=5)
        self.__btnNextYear = Button(self, text = '>>', font=('Arial',24), width = 3, height= 1).place(x=470, y=5)
        self.lblMonth = Label(self,text = 'Enero 2019', font = ('Arial', 28, 'bold')).place(x=180,y=3)


        self.daysName = Frame(self, width = 71, height = 20)
        
        self.__Lunes = Label(self, font=('Arial', 11), text = 'Lunes', width=9, height=2).place(x=0,y=38)
       
        self.__Martes = Label(self, font=('Arial', 11), text = 'Martes', width=9, height=2).place(x=64,y=38)
        self.__Miércoles = Label(self, font=('Arial', 11), text = 'Miércoles', width=13, height=2).place(x=128,y=38)
        self.__Jueves = Label(self, font=('Arial', 11), text = 'Jueves', width=12, height=2).place(x=222,y=38)
        self.__Viernes = Label(self, font=('Arial', 11), text = 'Viernes', width=12, height=2).place(x=306,y=38)
        self.__Sábado = Label(self, font=('Arial', 11), text = 'Sábado', width=11, height=2).place(x=390,y=38)
        self.__Domingo = Label(self, font=('Arial', 11), text = 'Domingo', width=8, height=2).place(x=470,y=38)
        
    



class month(ttk.Frame):
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent) 

    #self.dates = 














class MainApp (Tk):
    __Calendar = None

    def __init__(self):
        Tk.__init__(self)
        self.geometry('532x422')
        self.title('Calendario Universal')  
        
        self.__Calendar = Calendar(self, width=532, height=422).place(x=0,y=0)
    
    
    
    def start(self):
        self.mainloop()



if __name__ == '__main__':
    app = MainApp()
    app.start()
