from tkinter import *
from tkinter import ttk
from datetime import * 
import calendar



month_names = tuple(calendar.month_name)

class Calendar(ttk.Frame):
     

    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent, height=args['height'],width=args['width']) #para informar si o si de la altura y anchura 
        self.pack_propagate(0)

        
        self.__btnLastYear = ttk.Button(self, width = 3,text = '<<', command = self._backYear).place(x=10, y=5)
        self.__btnLastMonth = ttk.Button(self, text = '<', width = 3,command = self._backMonth).place(x=100, y=5)
        self.__btnNextMonth = ttk.Button(self, text = '>', width = 3, command = self._nextMonth).place(x=380,y=5)
        self.__btnNextYear = ttk.Button(self, text = '>>', width = 3, command = self._nextYear).place(x=470, y=5)
        self.lblMonth = ttk.Label(self,text = 'Enero 2019', font = ('Arial', 28, 'bold')).place(x=180,y=3)

        self.__Lunes = ttk.Label(self, width=9,font=('Arial', 11), text = 'Lunes').place(x=0,y=38)
       
        self.__Martes = ttk.Label(self, font=('Arial', 11), text = 'Martes', width=9).place(x=64,y=38)
        self.__Miércoles = ttk.Label(self, font=('Arial', 11), text = 'Miércoles', width=13).place(x=128,y=38)
        self.__Jueves = ttk.Label(self, font=('Arial', 11), text = 'Jueves', width=12).place(x=222,y=38)
        self.__Viernes = ttk.Label(self, font=('Arial', 11), text = 'Viernes', width=12).place(x=306,y=38)
        self.__Sábado = ttk.Label(self, font=('Arial', 11), text = 'Sábado', width=11).place(x=390,y=38)
        self.__Domingo = ttk.Label(self, font=('Arial', 11), text = 'Domingo', width=8).place(x=470,y=38)
        


    def _backYear(self):
        self.__valor+=1
        self.__label.config(text=str(self.__valor))
    
    def _nextYear(self):
        self.__valor+=1
        self.__label.config(text=str(self.__valor))
    def _backMonth(self):
        self.__valor+=1
        self.__label.config(text=str(self.__valor))
    def _nextMonth(self):
        self.__valor+=1
        self.__label.config(text=str(self.__valor))    




class month(ttk.Frame):
    def __init__(self, parent, **args):
        ttk.Frame.__init__(self, parent,height=args['height'],width=args['width']) 

    #self.dates = 














class MainApp (Tk):
    

    def __init__(self):
        Tk.__init__(self)
        self.geometry('532x422')
        self.title('Calendario Universal')  
        
        self.__Calendar = Calendar(self, width=532, height=422)
        self.__Calendar.place(x=0,y=0)
        
    
    
    def start(self):
        self.mainloop()



if __name__ == '__main__':
    app = MainApp()
    app.start()
