# !/usr/bin/env python
from tkinter import *
import serial
import time
import serial.tools.list_ports

#stick open ports function and opencom function here


def get_ports():                # Grabs all the COM ports from the computer
    ports = serial.tools.list_ports.comports()      #List of COM Ports
    default.set(ports)      # Turns the StringVar to the selected COM Port

def OpenCOM():          # Definition that opens the communications to the COM port
   port = default.get()     #Grabs the current selection of the COM port, and assigns "port" to be it
   print("Doing stuff with port", (port[:4]))   #Test for if the port is reading correctly
   tgsCOM = port[:4]  ##### MODIFY THIS LINE FOR YOUR SERIAL PORT NAME OR NUMBER
   tgS = serial.Serial(port= port[:4])  #Uses the same method as ^^ to make the line only read the beggining.
   tgS.baudrate = 57600
   tgS.port = tgsCOM
   tgS.bytesize = serial.EIGHTBITS  # number of bits per bytes
   tgS.parity = serial.PARITY_NONE  # set parity check: no parity
   tgS.stopbits = serial.STOPBITS_ONE  # number of stop bits
   # tgS.timeout = None          #block read
   tgS.timeout = 0.5  # non-block read
   tgS.xonxoff = False  # disable software flow control
   tgS.rtscts = False  # disable hardware (RTS/CTS) flow control
   tgS.dsrdtr = False  # disable hardware (DSR/DTR) flow control
   tgS.writeTimeout = 0  # timeout for write
   try:             # If the definition is activated, it will attempt to open the port.
       print("Activating Triggerscope...")
       tgS.open()           #Opens the selected COM port
   except Exception as e:           # If it cannot open the com port
       print("ERROR: Triggerscope Com port NOT OPEN: " + str(e))
   if tgS.isOpen():   #If the COM port succesfully opens, send code to the triggerscope to open communication and talk back
       print ("Port is on")

ports = serial.tools.list_ports.comports()      # Sets "ports" to be the list of COM ports.
default = StringVar("Please Select Port")     # The list box originally says "Please select port"


#get_ports()
#OpenCOM()

# ***** Window *****
root = Tk()         #Creates the root window
root.title("ARC Triggerscope Regulator")     # title of root window
root.iconbitmap(r'ARC.ico')      # Window Icon
root.maxsize(height= 600, width= 725)     # Sets Maximum size of the window
# ***** Background *****
canvas = Canvas(root, width = 725, height = 600, bg="black")    #Sets the canvas for the background
canvas.pack(fill=BOTH, expand=YES)  #Sets the canvas to fill the whole window

canvas.create_line(35, 50, 285, 50, width = 1, fill = "white")      #All lines for the design
canvas.create_line(35, 50, 35, 285, width = 1, fill = "white")
canvas.create_line(35, 285, 285, 285, width = 1, fill = "white")
canvas.create_line(285, 285, 285, 50, width = 1, fill = "white")

canvas.create_line(290, 50, 665, 50, width = 1, fill = "white")
canvas.create_line(665, 50, 665, 285, width = 1, fill = "white")
canvas.create_line(665, 285, 290, 285, width = 1, fill ="white")
canvas.create_line(290, 285, 290, 50, width = 1, fill ="white")

canvas.create_line(290, 300, 665, 300, width = 1, fill ="white")
canvas.create_line(665, 300, 665, 525, width = 1, fill ="white")
canvas.create_line(665, 525, 290, 525, width = 1, fill ="white")
canvas.create_line(290, 525, 290, 300, width = 1, fill ="white")

canvas.create_line(350, 300, 350, 285, width = 2, fill = "white")
canvas.create_line(475, 300, 475, 285, width = 2, fill = "white")
canvas.create_line(600, 300, 600, 285, width = 2, fill = "white")

canvas.create_line(285,110,290, 110, width = 2, fill = "white")
canvas.create_line(285,230,290, 230, width = 2, fill = "white")     #End of white design lines

# ***** Background Logo *****

ARC_BG = PhotoImage(file='TB.png')        #ARC Logo
canvas.create_image(275, 375, image=ARC_BG, anchor=NE)  #Sets the image in


# ***** Functions *****



# ***** Drop-down menu*****
menu = Menu(root)           # Sets menu in the window
root.config(menu=menu)  #Makes the menu appear


subMenu = Menu(menu)  #Adds a second menu, both are not in use currently

def on_select(selection):       # Function that shows the selection of a widget
    print(selection)


#def getFolderPath():
 #   folder_selected = filedialog.askdirectory()
 #   folderPath.set(folder_selected)


#def doStuff():
 #   folder = folderPath.get()
  #  print("Doing stuff with folder", folder)

#folderPath = StringVar()
#a = Label(gui, text="Enter name")
#a.grid(row=0, column=0)
#E = Entry(gui, textvariable=folderPath)
#E.grid(row=0, column=1)
#btnFind = ttk.Button(gui, text="Browse Folder", command=getFolderPath)
#btnFind.grid(row=0, column=2)



def get_ports():                # Grabs all the COM ports from the computer
    ports = serial.tools.list_ports.comports()      #List of COM Ports
    default.set(ports)      # Turns the StringVar to the selected COM Port

def OpenCOM():          # Definition that opens the communications to the COM port
   port = default.get()     #Grabs the current selection of the COM port, and assigns "port" to be it
   print("Doing stuff with port", (port[:4]))   #Test for if the port is reading correctly
   tgsCOM = port[:4]  ##### MODIFY THIS LINE FOR YOUR SERIAL PORT NAME OR NUMBER
   tgS = serial.Serial(port= port[:4])  #Uses the same method as ^^ to make the line only read the beggining.
   tgS.baudrate = 57600
   tgS.port = tgsCOM
   tgS.bytesize = serial.EIGHTBITS  # number of bits per bytes
   tgS.parity = serial.PARITY_NONE  # set parity check: no parity
   tgS.stopbits = serial.STOPBITS_ONE  # number of stop bits
   # tgS.timeout = None          #block read
   tgS.timeout = 0.5  # non-block read
   tgS.xonxoff = False  # disable software flow control
   tgS.rtscts = False  # disable hardware (RTS/CTS) flow control
   tgS.dsrdtr = False  # disable hardware (DSR/DTR) flow control
   tgS.writeTimeout = 0  # timeout for write
   try:             # If the definition is activated, it will attempt to open the port.
       print("Activating Triggerscope...")
       tgS.open()           #Opens the selected COM port
   except Exception as e:           # If it cannot open the com port
       print("ERROR: Triggerscope Com port NOT OPEN: " + str(e))
   if tgS.isOpen():   #If the COM port succesfully opens, send code to the triggerscope to open communication and talk back
       print ("Port is on")



ports = serial.tools.list_ports.comports()      # Sets "ports" to be the list of COM ports.
default = StringVar(root, "Please Select Port")     # The list box originally says "Please select port"
COM_Menu = OptionMenu(root, default, *ports, command=on_select) #The Option menu is set, with the command of on_select
COM_Menu_window = canvas.create_window(350, 30, window = COM_Menu) # Binds the option menu to the canvas.



OPENPORT = Button(text = "OPEN COM", command = OpenCOM)     #Button that opens the communication to the COM port
OPENPORT_window = canvas.create_window(600, 31, window = OPENPORT) #Binds the button to the canvas
# ***** Quit Button *****

button1 = Button(text = "Quit", command = quit, anchor = W, bg= "gold") #Quit Button that exits the program
button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT) #gives the button detail
button1_window = canvas.create_window(10, 10, anchor=NW, window=button1) # Binds the button to the canvas

# ***** TTL Buttons *****
def labelsensor():                              # Turns the Triggerscope TTL on.
    if Toff1['background'] == 'green2':         #If the background is green, then print the callback from the triggerscope
        print("ON")  #Print "On", might take out soon
        print(writetgs("TTL1,1\n"))       #print that the triggerscope TTL is on
    else:
        print("OFF")   # Print "off", might also take this out soon
        print(writetgs("TTL1,0\n"))     # Print that the triggercope TTL is off


def toggle():         #Toggle animation for TTL Buttons, as well as executing the command for the TTL buttons

    if TTL1.config('relief')[-1] == 'sunken':  # If the button is up/unpressed, then make the label next to the button RED
        TTL1.config(relief="raised")
        Toff1.configure(bg = "red")
        labelsensor()   # Runs the Labelsensor command, which talks to the triggerscope, this should show TTL1, 0

    else:
        TTL1.config(relief="sunken")  # When the button is depressed/pressed, then make the color of label green, and talk to the triggerscope.
        Toff1.configure(bg= "green2")
        labelsensor()



TTL1 = Button(text ="TTL 1", bg = "gold", command = toggle) #First TTL button, make the color gold, and use the command toggle to turn on the corrisponding TTL output.
TTL1.configure(relief = FLAT, width= 5) # Make the size of the button
TTL1_window = canvas.create_window (100, 80, window= TTL1)  #Bind the button to the canvas

Toff1 = Label(bg = "red")  # The "Light" next to the button shows red
Toff1.configure(width = 1, height = 1)      # Makes the size of the "Light"
Toff1_window = canvas.create_window(140, 80, window= Toff1)     #Binds the "Light" to the canvas.



def labelsensor2():                              # Turns the Triggerscope TTL on, repeats the process of TTL1, but talks to a different TTL output
    if Toff2['background'] == 'green2':
        print("ON")
        print(writetgs("TTL2,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL2,0\n"))



def toggle():         #Toggle animation for TTL Buttons

    if TTL2.config('relief')[-1] == 'sunken':
        TTL2.config(relief="raised")
        Toff2.configure(bg = "red")
        labelsensor2()
    else:
        TTL2.config(relief="sunken")
        Toff2.configure(bg= "green2")
        labelsensor2()


TTL2 = Button(text ="TTL 2", bg = "gold", command = toggle)
TTL2.configure(relief = FLAT, width= 5)
TTL2_window = canvas.create_window (225, 80, window= TTL2)

Toff2 = Label( bg = "red")
Toff2.configure(width = 1, height = 1)
Toff2_window = canvas.create_window(265, 80, window= Toff2)


def labelsensor3():                              # Turns the Triggerscope TTL on. repeats the process of TTL1, but talks to a different TTL output
    if Toff3['background'] == 'green2':
        print("ON")
        print(writetgs("TTL3,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL3,0\n"))


def toggle():         #Toggle animation for TTL Buttons

    if TTL3.config('relief')[-1] == 'sunken':
        TTL3.config(relief="raised")
        Toff3.configure(bg = "red")
        labelsensor3()
    else:
        TTL3.config(relief="sunken")
        Toff3.configure(bg= "green2")
        labelsensor3()


TTL3 = Button(text ="TTL 3", bg = "gold", command = toggle)
TTL3.configure(relief = FLAT, width= 5)
TTL3_window = canvas.create_window (350, 80, window= TTL3)

Toff3 = Label( bg = "red")
Toff3.configure(width = 1, height = 1)
Toff3_window = canvas.create_window(390, 80, window= Toff3)

def labelsensor4():                              # Turns the Triggerscope TTL on.
    if Toff4['background'] == 'green2':
        print("ON")
        print(writetgs("TTL4,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL4,0\n"))



def toggle():         #Toggle animation for TTL Buttons

    if TTL4.config('relief')[-1] == 'sunken':
        TTL4.config(relief="raised")
        Toff4.configure(bg = "red")
        labelsensor4()
    else:
        TTL4.config(relief="sunken")
        Toff4.configure(bg= "green2")
        labelsensor4()


TTL4 = Button(text ="TTL 4", bg = "gold", command = toggle)
TTL4.configure(relief = FLAT, width= 5)
TTL4_window = canvas.create_window (475, 80, window= TTL4)

Toff4 = Label( bg = "red")
Toff4.configure(width = 1, height = 1)
Toff4_window = canvas.create_window(515, 80, window= Toff4)



def labelsensor5():                              # Turns the Triggerscope TTL on.
    if Toff5['background'] == 'green2':
        print("ON")
        print(writetgs("TTL5,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL5,0\n"))



def toggle():         #Toggle animation for TTL Buttons

    if TTL5.config('relief')[-1] == 'sunken':
        TTL5.config(relief="raised")
        Toff5.configure(bg = "red")
        labelsensor5()
    else:
        TTL5.config(relief="sunken")
        Toff5.configure(bg= "green2")
        labelsensor5()



TTL5 = Button(text ="TTL 5", bg = "gold", command = toggle)
TTL5.configure(relief = FLAT, width= 5)
TTL5_window = canvas.create_window (600, 80, window= TTL5)

Toff5 = Label( bg = "red")
Toff5.configure(width = 1, height = 1)
Toff5_window = canvas.create_window(640, 80, window= Toff5)



def labelsensor6():                              # Turns the Triggerscope TTL on.
    if Toff6['background'] == 'green2':
        print("ON")
        print(writetgs("TTL6,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL6,0\n"))


def toggle():         #Toggle animation for TTL Buttons

    if TTL6.config('relief')[-1] == 'sunken':
        TTL6.config(relief="raised")
        Toff6.configure(bg = "red")
        labelsensor6()
    else:
        TTL6.config(relief="sunken")
        Toff6.configure(bg= "green2")
        labelsensor6()



TTL6 = Button(text ="TTL 6", bg = "gold", command = toggle)
TTL6.configure(relief = FLAT, width= 5)
TTL6_window = canvas.create_window (100, 200, window= TTL6)

Toff6 = Label( bg = "red")
Toff6.configure(width = 1, height = 1)
Toff6_window = canvas.create_window(140, 200, window= Toff6)

def labelsensor7():                              # Turns the Triggerscope TTL on.
    if Toff7['background'] == 'green2':
        print("ON")
        print(writetgs("TTL7,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL7,0\n"))



def toggle():         #Toggle animation for TTL Buttons

    if TTL7.config('relief')[-1] == 'sunken':
        TTL7.config(relief="raised")
        Toff7.configure(bg = "red")
        labelsensor7()
    else:
        TTL7.config(relief="sunken")
        Toff7.configure(bg= "green2")
        labelsensor7()



TTL7 = Button(text ="TTL 7", bg = "gold", command = toggle)
TTL7.configure(relief = FLAT, width= 5)
TTL7_window = canvas.create_window (225, 200, window= TTL7)

Toff7 = Label( bg = "red")
Toff7.configure(width = 1, height = 1)
Toff7_window = canvas.create_window(265, 200, window= Toff7)

def labelsensor8():                              # Turns the Triggerscope TTL on.
    if Toff8['background'] == 'green2':
        print("ON")
        print(writetgs("TTL8,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL8,0\n"))


def toggle():         #Toggle animation for TTL Buttons

    if TTL8.config('relief')[-1] == 'sunken':
        TTL8.config(relief="raised")
        Toff8.configure(bg = "red")
        labelsensor8()
    else:
        TTL8.config(relief="sunken")
        Toff8.configure(bg= "green2")
        labelsensor8()


TTL8 = Button(text ="TTL 8", bg = "gold", command = toggle)
TTL8.configure(relief = FLAT, width= 5)
TTL8_window = canvas.create_window (350, 200, window= TTL8)

Toff8 = Label( bg = "red")
Toff8.configure(width = 1, height = 1)
Toff8_window = canvas.create_window(390, 200, window= Toff8)

def labelsensor9():                              # Turns the Triggerscope TTL on.
    if Toff9['background'] == 'green2':
        print("ON")
        print(writetgs("TTL9,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL9,0\n"))



def toggle():         #Toggle animation for TTL Buttons

    if TTL9.config('relief')[-1] == 'sunken':
        TTL9.config(relief="raised")
        Toff9.configure(bg = "red")
        labelsensor9()
    else:
        TTL9.config(relief="sunken")
        Toff9.configure(bg= "green2")
        labelsensor9()

TTL9 = Button(text ="TTL 9", bg = "gold", command = toggle)
TTL9.configure(relief = FLAT, width= 5)
TTL9_window = canvas.create_window (475, 200, window= TTL9)

Toff9 = Label( bg = "red")
Toff9.configure(width = 1, height = 1)
Toff9_window = canvas.create_window(515, 200, window= Toff9)


def labelsensor10():                              # Turns the Triggerscope TTL on.
    if Toff10['background'] == 'green2':
        print("ON")
        print(writetgs("TTL10,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL10,0\n"))


def toggle():         #Toggle animation for TTL Buttons

    if TTL10.config('relief')[-1] == 'sunken':
        TTL10.config(relief="raised")
        Toff10.configure(bg = "red")
        labelsensor10()
    else:
        TTL10.config(relief="sunken")
        Toff10.configure(bg= "green2")
        labelsensor10()



TTL10 = Button(text ="TTL 10", bg = "gold", command = toggle)
TTL10.configure(relief = FLAT, width= 5)
TTL10_window = canvas.create_window (600, 200, window= TTL10)

Toff10 = Label( bg = "red")
Toff10.configure(width = 1, height = 1)
Toff10_window = canvas.create_window(640, 200, window= Toff10)


def labelsensor11():                              # Turns the Triggerscope TTL on.
    if Toff11['background'] == 'green2':
        print("ON")
        print(writetgs("TTL11,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL11,0\n"))

def toggle():         #Toggle animation for TTL Buttons

    if TTL11.config('relief')[-1] == 'sunken':
        TTL11.config(relief="raised")
        Toff11.configure(bg = "red")
        labelsensor11()
    else:
        TTL11.config(relief="sunken")
        Toff11.configure(bg= "green2")
        labelsensor11()



TTL11 = Button(text ="TTL 11", bg = "gold", command = toggle)
TTL11.configure(relief = FLAT, width= 5)
TTL11_window = canvas.create_window (350, 320, window= TTL11)

Toff11 = Label( bg = "red")
Toff11.configure(width = 1, height = 1)
Toff11_window = canvas.create_window(390, 320, window= Toff11)

def labelsensor12():                              # Turns the Triggerscope TTL on.
    if Toff12['background'] == 'green2':
        print("ON")
        print(writetgs("TTL12,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL12,0\n"))

def toggle():         #Toggle animation for TTL Buttons

    if TTL12.config('relief')[-1] == 'sunken':
        TTL12.config(relief="raised")
        Toff12.configure(bg = "red")
        labelsensor12()
    else:
        TTL12.config(relief="sunken")
        Toff12.configure(bg= "green2")
        labelsensor12()

TTL12 = Button(text ="TTL 12", bg = "gold", command = toggle)
TTL12.configure(relief = FLAT, width= 5)
TTL12_window = canvas.create_window (475, 320, window= TTL12)

Toff12 = Label( bg = "red")
Toff12.configure(width = 1, height = 1)
Toff12_window = canvas.create_window(515, 320, window= Toff12)

def labelsensor13():                              # Turns the Triggerscope TTL on.
    if Toff13['background'] == 'green2':
        print("ON")
        print(writetgs("TTL13,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL13,0\n"))


def toggle():         #Toggle animation for TTL Buttons

    if TTL13.config('relief')[-1] == 'sunken':
        TTL13.config(relief="raised")
        Toff13.configure(bg = "red")
        labelsensor13()
    else:
        TTL13.config(relief="sunken")
        Toff13.configure(bg= "green2")
        labelsensor13()


TTL13 = Button(text ="TTL 13", bg = "gold", command = toggle)
TTL13.configure(relief = FLAT, width= 5)
TTL13_window = canvas.create_window (600, 320, window= TTL13)

Toff13 = Label( bg = "red")
Toff13.configure(width = 1, height = 1)
Toff13_window = canvas.create_window(640, 320, window= Toff13)

def labelsensor14():                              # Turns the Triggerscope TTL on.
    if Toff14['background'] == 'green2':
        print("ON")
        print(writetgs("TTL14,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL14,0\n"))



def toggle():         #Toggle animation for TTL Buttons

    if TTL14.config('relief')[-1] == 'sunken':
        TTL14.config(relief="raised")
        Toff14.configure(bg = "red")
        labelsensor14()
    else:
        TTL14.config(relief="sunken")
        Toff14.configure(bg= "green2")
        labelsensor14()


TTL14 = Button(text ="TTL 14", bg = "gold", command = toggle)
TTL14.configure(relief = FLAT, width= 5)
TTL14_window = canvas.create_window (350, 440, window= TTL14)

Toff14 = Label( bg = "red")
Toff14.configure(width = 1, height = 1)
Toff14_window = canvas.create_window(390, 440, window= Toff14)

def labelsensor15():                              # Turns the Triggerscope TTL on.
    if Toff15['background'] == 'green2':
        print("ON")
        print(writetgs("TTL15,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL15,0\n"))


def toggle():         #Toggle animation for TTL Buttons

    if TTL15.config('relief')[-1] == 'sunken':
        TTL15.config(relief="raised")
        Toff15.configure(bg = "red")
        labelsensor15()
    else:
        TTL15.config(relief="sunken")
        Toff15.configure(bg= "green2")
        labelsensor15()

TTL15 = Button(text ="TTL 15", bg = "gold", command = toggle)
TTL15.configure(relief = FLAT, width= 5)
TTL15_window = canvas.create_window (475, 440, window= TTL15)

Toff15 = Label( bg = "red")
Toff15.configure(width = 1, height = 1)
Toff15_window = canvas.create_window(515, 440, window= Toff15)

def labelsensor16():                              # Turns the Triggerscope TTL on.
    if Toff16['background'] == 'green2':
        print("ON")
        print(writetgs("TTL16,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL16,0\n"))


def toggle():         #Toggle animation for TTL Buttons

    if TTL16.config('relief')[-1] == 'sunken':
        TTL16.config(relief="raised")
        Toff16.configure(bg = "red")
        labelsensor16()
    else:
        TTL16.config(relief="sunken")
        Toff16.configure(bg= "green2")
        labelsensor16()



TTL16 = Button(text ="TTL 16", bg = "gold", command = toggle)
TTL16.configure(relief = FLAT, width= 5)
TTL16_window = canvas.create_window (600, 440, window= TTL16)

Toff16 = Label( bg = "red")
Toff16.configure(width = 1, height = 1)
Toff16_window = canvas.create_window(640, 440, window= Toff16)




# ***** DAC Sliders *****

def dacPos(event):                  # Event that grabs the value and sends it to the Triggerscope
    DAC1.get()          #Grabs the currrent value of the scale
    out = "DAC1," + str(DAC1.get()) + "\n"      #Makes "Out" the current variable of the corrisponding scale
    print(writetgs(out))        #Print the command the trigerscope got, Should be to set it to whatever number it is.


DAC1 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")      #The DAC scale
DAC1.configure(relief = FLAT)       # make the relief of the scale flat
DAC1.bind("<ButtonRelease>", dacPos)        # Bind the scale to run the dacPos command when the curser is done selecting the amount
DAC1_window = canvas.create_window (100, 110, window = DAC1)    #Puts the scale on the canvas

def dacPos(event):                  # Event that grabs the value and sends it to the Triggerscope
    DAC2.get()
    out = "DAC2," + str(DAC2.get()) + "\n"
    print(writetgs(out))

DAC2 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC2.configure(relief = FLAT)
DAC2.bind("<ButtonRelease>", dacPos)
DAC2_window = canvas.create_window (225, 110, window = DAC2)

def dacPos(event):                  # Event that grabs the value and sends it to the Triggerscope
    DAC3.get()
    out = "DAC3," + str(DAC3.get()) + "\n"
    print(writetgs(out))

DAC3 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC3.configure(relief = FLAT)
DAC3.bind("<ButtonRelease>", dacPos)
DAC3_window = canvas.create_window (350, 110, window = DAC3)

def dacPos(event):                  # Event that grabs the value and sends it to the Triggerscope
    DAC4.get()
    out = "DAC4," + str(DAC4.get()) + "\n"
    print(writetgs(out))

DAC4 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC4.configure(relief = FLAT)
DAC4.bind("<ButtonRelease>", dacPos)
DAC4_window = canvas.create_window (475, 110, window = DAC4)

def dacPos(event):                  # Event that grabs the value and sends it to the Triggerscope
    DAC5.get()
    out = "DAC5," + str(DAC5.get()) + "\n"
    print(writetgs(out))

DAC5 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC5.configure(relief = FLAT)
DAC5.bind("<ButtonRelease>", dacPos)
DAC5_window = canvas.create_window (600, 110, window = DAC5)


def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC6.get()
    out = "DAC6," + str(DAC6.get()) + "\n"
    print(writetgs(out))


DAC6 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC6.configure(relief = FLAT)
DAC6.bind("<ButtonRelease>", dacPos)
DAC6_window = canvas.create_window (100, 230, window = DAC6)

def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC7.get()
    out = "DAC7," + str(DAC7.get()) + "\n"
    print(writetgs(out))

DAC7 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC7.configure(relief = FLAT)
DAC7.bind("<ButtonRelease>", dacPos)
DAC7_window = canvas.create_window (225, 230, window = DAC7)

def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC8.get()
    out = "DAC8," + str(DAC8.get()) + "\n"
    print(writetgs(out))

DAC8 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC8.configure(relief = FLAT)
DAC8.bind("<ButtonRelease>", dacPos)
DAC8_window = canvas.create_window (350, 230, window = DAC8)

def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC9.get()
    out = "DAC9," + str(DAC9.get()) + "\n"
    print(writetgs(out))

DAC9 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC9.configure(relief = FLAT)
DAC9.bind("<ButtonRelease>", dacPos)
DAC9_window = canvas.create_window (475, 230, window = DAC9)

def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC10.get()
    out = "DAC10," + str(DAC10.get()) + "\n"
    print(writetgs(out))

DAC10 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC10.configure(relief = FLAT)
DAC10.bind("<ButtonRelease>", dacPos)
DAC10_window = canvas.create_window (600, 230, window = DAC10)

def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC11.get()
    out = "DAC11," + str(DAC11.get()) + "\n"
    print(writetgs(out))

DAC11 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC11.configure(relief = FLAT)
DAC11.bind("<ButtonRelease>", dacPos)
DAC11_window = canvas.create_window (350, 350, window = DAC11)

def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC12.get()
    out = "DAC12," + str(DAC12.get()) + "\n"
    print(writetgs(out))

DAC12 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC12.configure(relief = FLAT)
DAC12.bind("<ButtonRelease>", dacPos)
DAC12_window = canvas.create_window (475, 350, window = DAC12)

def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC13.get()
    out = "DAC13," + str(DAC13.get()) + "\n"
    print(writetgs(out))

DAC13 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC13.configure(relief = FLAT)
DAC13.bind("<ButtonRelease>", dacPos)
DAC13_window = canvas.create_window (600, 350, window = DAC13)

def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC14.get()
    out = "DAC14," + str(DAC14.get()) + "\n"
    print(writetgs(out))

DAC14 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC14.configure(relief = FLAT)
DAC14.bind("<ButtonRelease>", dacPos)
DAC14_window = canvas.create_window (350, 470, window = DAC14)

def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC15.get()
    out = "DAC15," + str(DAC15.get()) + "\n"
    print(writetgs(out))

DAC15 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC15.configure(relief = FLAT)
DAC15.bind("<ButtonRelease>", dacPos)
DAC15_window = canvas.create_window (475, 470, window = DAC15)

def dacPos(event):  # Event that grabs the value and sends it to the Triggerscope
    DAC16.get()
    out = "DAC16," + str(DAC16.get()) + "\n"
    print(writetgs(out))

DAC16 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")
DAC16.configure(relief = FLAT)
DAC16.bind("<ButtonRelease>", dacPos)
DAC16_window = canvas.create_window (600, 470, window = DAC16)



# ***** Voltage Range Cascade *****      Will Probably take these out before first launch
Range1 = Label(text="Range:", bg = "black", fg = "gold")    #The text saying "Range:"
Range1.configure(width= 6)
Range1_window = canvas.create_window(65, 140, window = Range1)  #Show the text

variable1 = StringVar(root)    #creates a new variable for the range selections
variable1.set("Volts") # default value/ original text in the selecton box

Range1V= OptionMenu(root, variable1, "0V-5V", "5V-10V", "10V-15V")  #The selection menu for choosing which amount of voltage is needed
Range1V.configure(width= 4, height=  0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0) #makes the details of the menus
Range1V_window = canvas.create_window(120, 140, window = Range1V)  #Show the option menu, and put it on the canvas

Range2 = Label(text="Range:", bg = "black", fg = "gold") #Same set of progressions as the Range 1
Range2.configure(width= 6)
Range2_window = canvas.create_window(190, 140, window = Range2)

variable2 = StringVar(root)
variable2.set("Volts") # default value

Range2V= OptionMenu(root, variable2, "0V-5V", "5V-10V", "10V-15V")
Range2V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range2V_window = canvas.create_window(245, 140, window = Range2V)

Range3 = Label(text="Range:", bg = "black", fg = "gold")
Range3.configure(width= 6)
Range3_window = canvas.create_window(315, 140, window = Range3)

variable3 = StringVar(root)
variable3.set("Volts") # default value

Range3V= OptionMenu(root, variable3, "0V-5V", "5V-10V", "10V-15V")
Range3V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range3V_window = canvas.create_window(370, 140, window = Range3V)

Range4 = Label(text="Range:", bg = "black", fg = "gold")
Range4.configure(width= 6)
Range4_window = canvas.create_window(440, 140, window = Range4)

variable4 = StringVar(root)
variable4.set("Volts") # default value

Range4V= OptionMenu(root, variable4, "0V-5V", "5V-10V", "10V-15V")
Range4V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range4V_window = canvas.create_window(495, 140, window = Range4V)

Range5 = Label(text="Range:", bg = "black", fg = "gold")
Range5.configure(width= 6)
Range5_window = canvas.create_window(565, 140, window = Range5)

variable5 = StringVar(root)
variable5.set("Volts") # default value

Range5V= OptionMenu(root, variable5, "0V-5V", "5V-10V", "10V-15V")
Range5V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range5V_window = canvas.create_window(620, 140, window = Range5V)

Range6 = Label(text="Range:", bg = "black", fg = "gold")
Range6.configure(width= 6)
Range6_window = canvas.create_window(65, 260, window = Range6)

variable6 = StringVar(root)
variable6.set("Volts") # default value

Range6V= OptionMenu(root, variable6, "0V-5V", "5V-10V", "10V-15V")
Range6V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range6V_window = canvas.create_window(120, 260, window = Range6V)

Range7 = Label(text="Range:", bg = "black", fg = "gold")
Range7.configure(width= 6)
Range7_window = canvas.create_window(190, 260, window = Range7)

variable7 = StringVar(root)
variable7.set("Volts") # default value

Range7V= OptionMenu(root, variable7, "0V-5V", "5V-10V", "10V-15V")
Range7V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range7V_window = canvas.create_window(245, 260, window = Range7V)

Range8 = Label(text="Range:", bg = "black", fg = "gold")
Range8.configure(width= 6)
Range8_window = canvas.create_window(315, 260, window = Range8)

variable8 = StringVar(root)
variable8.set("Volts") # default value

Range8V= OptionMenu(root, variable8, "0V-5V", "5V-10V", "10V-15V")
Range8V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range8V_window = canvas.create_window(370, 260, window = Range8V)

Range9 = Label(text="Range:", bg = "black", fg = "gold")
Range9.configure(width= 6)
Range9_window = canvas.create_window(440, 260, window = Range9)

variable9 = StringVar(root)
variable9.set("Volts") # default value

Range9V= OptionMenu(root, variable9, "0V-5V", "5V-10V", "10V-15V")
Range9V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range9V_window = canvas.create_window(495, 260, window = Range9V)

Range10 = Label(text="Range:", bg = "black", fg = "gold")
Range10.configure(width= 6)
Range10_window = canvas.create_window(565, 260, window = Range10)

variable10 = StringVar(root)
variable10.set("Volts") # default value

Range10V= OptionMenu(root, variable10, "0V-5V", "5V-10V", "10V-15V")
Range10V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range10V_window = canvas.create_window(620, 260, window = Range10V)

Range11 = Label(text="Range:", bg = "black", fg = "gold")
Range11.configure(width= 6)
Range11_window = canvas.create_window(315, 380, window = Range11)

variable11 = StringVar(root)
variable11.set("Volts") # default value

Range11V= OptionMenu(root, variable11, "0V-5V", "5V-10V", "10V-15V")
Range11V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range11V_window = canvas.create_window(370, 380, window = Range11V)

Range12 = Label(text="Range:", bg = "black", fg = "gold")
Range12.configure(width= 6)
Range12_window = canvas.create_window(440, 380, window = Range12)

variable12 = StringVar(root)
variable12.set("Volts") # default value

Range12V= OptionMenu(root, variable12, "0V-5V", "5V-10V", "10V-15V")
Range12V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range12V_window = canvas.create_window(495, 380, window = Range12V)

Range13 = Label(text="Range:", bg = "black", fg = "gold")
Range13.configure(width= 6)
Range13_window = canvas.create_window(565, 380, window = Range13)

variable13 = StringVar(root)
variable13.set("Volts") # default value

Range13V= OptionMenu(root, variable13, "0V-5V", "5V-10V", "10V-15V")
Range13V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range13V_window = canvas.create_window(620, 380, window = Range13V)

Range14 = Label(text="Range:", bg = "black", fg = "gold")
Range14.configure(width= 6)
Range14_window = canvas.create_window(315, 500, window = Range14)

variable14 = StringVar(root)
variable14.set("Volts") # default value

Range14V= OptionMenu(root, variable14, "0V-5V", "5V-10V", "10V-15V")
Range14V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range14V_window = canvas.create_window(370, 500, window = Range14V)

Range15 = Label(text="Range:", bg = "black", fg = "gold")
Range15.configure(width= 6)
Range15_window = canvas.create_window(440, 500, window = Range15)

variable15 = StringVar(root)
variable15.set("Volts") # default value

Range15V= OptionMenu(root, variable15, "0V-5V", "5V-10V", "10V-15V")
Range15V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range15V_window = canvas.create_window(495, 500, window = Range15V)

Range16 = Label(text="Range:", bg = "black", fg = "gold")
Range16.configure(width= 6)
Range16_window = canvas.create_window(565, 500, window = Range16)

variable16 = StringVar(root)
variable16.set("Volts") # default value

Range16V= OptionMenu(root, variable16, "0V-5V", "5V-10V", "10V-15V")
Range16V.configure(width= 4, height= 0, bg = "black", fg="gold", relief = FLAT, borderwidth= 0)
Range16V_window = canvas.create_window(620, 500, window = Range16V)



# ***** Triggerscope Connection testing *****

port = default.get()     #Grabs the current selection of the COM port, and assigns "port" to be it

tgsCOM    = port      ##### MODIFY THIS LINE FOR YOUR SERIAL PORT NAME OR NUMBER
tgS = serial.Serial()
tgS.baudrate = 57600
tgS.port = tgsCOM
tgS.bytesize = serial.EIGHTBITS #number of bits per bytes
tgS.parity = serial.PARITY_NONE #set parity check: no parity
tgS.stopbits = serial.STOPBITS_ONE #number of stop bits
#tgS.timeout = None          #block read
tgS.timeout = 0.5            #non-block read
tgS.xonxoff = False     #disable software flow control
tgS.rtscts = False     #disable hardware (RTS/CTS) flow control
tgS.dsrdtr = False       #disable hardware (DSR/DTR) flow control
tgS.writeTimeout = 0     #timeout for write

#def TEST():             # current Testing of the best way to open the com port, could be taken out once com port issue is solved
 #   try:
  #      print("Activating Triggerscope...")
   #     tgS.open()
#    except Exception as e:
#        print ("ERROR: Triggerscope Com port NOT OPEN: " + str(e))
#        exit()
#    if tgS.isOpen():
#        try:
#            tgS.flushInput() #flush input buffer, discarding all its contents
#            tgS.flushOutput()#flush output buffer, aborting current output
#            tgS.write("*\n".encode() ) #send an ack to tgs to make sure it's up
#            time.sleep(0.3)  #give the serial port sometime to receive the data
#            print("Rx: " + tgS.readline().decode())
#        except Exception as e1:
#            print ("triggerscope serial communication error...: " + str(e1))

 #   else:
  #      print ("cannot open triggerscope port ")



def writetgs(tgin):     # One of the most important sections of code, allows for the initial setup of the COM ports, and allows everything regardng connection to the device.
    '''send a serial command to the triggerscope...
    Args:
        tgin: input string to send. Note the command terminator should be included in the string.
    Returns:
        char string of whatever comes back on the serial line.
    Raises:
        none.
    '''
    scomp = '!'+tgin
    tgS.flushInput() #flush input buffer, discarding all its contents
    tgS.flushOutput()#flush output buffer, aborting current output
    tgS.write(tgin.encode()) #send an ack to tgs to make sure it's up
    time.sleep(0.1)  #give the serial port sometime to receive the data 50ms works well...
    bufa = ""
    bufa = tgS.readline().decode()
    return bufa

# ****** TEST ZONE *********





# ***** Status Bar *****  #Not working just yet, defenitley a good feature to have nearing the selling point. 
#status = Label(root, text = "Running...", bd =1, relief = SUNKEN, anchor= W, bg="grey75")
#status.pack(side= BOTTOM, fill=BOTH,  expand= YES)

root.mainloop()
