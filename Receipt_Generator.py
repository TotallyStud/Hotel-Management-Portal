from __main__ import *
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

fo1=open("recipt.txt","r")
list1=fo1.readlines()

del list1[1]
del list1[2]
del list1[3]
del list1[4]
del list1[5]
list1[0]=list1[0][:-1]
list1[1]=list1[1][:-1]
list1[2]=list1[2][:-1]
list1[3]=list1[3][:-1]
list1[4]=list1[4][:-1]

p='''
@@@@@@@@@@@  Tempt Hotel & Resort  @@@@@@@@@@@@@
@@@@@@@@@@@@ Thane, Maharastra @@@@@@@@@@@@@@
@@@@@@@@@@ Serving Guest Since @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@    ###2021###       @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
NAME-%s
ADDRESS-%s
MOBILE NO.-%s
YOUR TOTAL BILL IS Rs.-%s
YOUR ROOM NUMBER IS %s    
     
     
     
'''%(list1[0],list1[1],list1[2],list1[4],list1[3])

        





class recipt:
    def __init__(self):
        root=Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#3366ff' 
        _fgcolor = '#3366ff' 
        _compcolor = '#3366ff' 
        _ana1color = '#3366ff' 
        _ana2color = '#3366ff' 

        root.geometry("800x800")
        root.title("recipt")
        root.configure(background="#d9d9d9")



        self.Label1 = Label(root)
        self.Label1.configure(background="#33ccff")
        self.Label1.place(relx=0, rely=0, height=800, width=800)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground= "black")
        self.Label1.configure(text=p)
        self.Label1.configure(anchor=N)

        self.Label1.configure(wraplength=1000)
        self.Label1.configure(justify =CENTER)

        self.Label1.configure(width=582)
        root.mainloop()


if __name__ == '__main__':
    recipt1=recipt()


