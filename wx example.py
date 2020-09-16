from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import serial
import ctypes
from functools import partial


def connect(ser):    #button that starts a connection, ser
    try:
        global ser       #makes ser a global variable accessible to other functions
        port = D.get()    #snags the number in the dropdown
        print(D.get())
        ser = serial.Serial(port = "COM" +str(port),baudrate=9600,)
        print(s.port)
    except:
        ctypes.windll.user32.MessageBoxW(0, "Fail", title, 0)
        ser.close()
    return ser

def running(ser):    #button that runs a ton of commands through ser
    P['value']=0
    ser.write(b'lottsacommands')
    P['value']=100
    root.update_idletasks()

root = tk.Tk()
bottomframe = Frame(root)    #frame for bottom of root window
bottomframe.pack(side=tk.BOTTOM)

D = StringVar(bottomframe)
P = Progressbar(bottomframe,orient=HORIZONTAL,length=100,mode='determinate')  #build a progress bar in the window 'P'
B = tk.Button(bottomframe,text='Begin Run In',command=partial(running, ser))     #build the button 'B'
B2 = tk.Button(bottomframe,text="Connect To Serial",command=partial(connect, ser))
T2 = tk.Text(bottomframe, height=1, width=7)    #box that says comm

P.pack()    #pack progress bar
B.pack(side=tk.RIGHT)       #formats the button
B2.pack(side=tk.LEFT)
T2.pack(side=tk.LEFT)       #format the ports dropdown

ports = {1,2,3,4,5,6,7,8,9}
DR = OptionMenu(bottomframe, D, *choices)   #creates the dropdown
DR.pack()

T2.insert(tk.END, 'COMM')    #makes the box say comm
tk.mainloop()    #runs the loop