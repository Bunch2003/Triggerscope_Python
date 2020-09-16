from tkinter import*
import time
import serial
import serial.tools.list_ports




tgS = serial.Serial()
portSelect = 0
tgsCom = "NONE"                 #Sets tgsCom to be "None" this allows

#****** Root/title/Frames ******
root = Tk()             #Begining of the window process
root.title("ARC Triggerscope Regulator")     # title of root window
root.iconbitmap(r'ARC.ico')      # Window Icon

# ******  ARC Logo ******


# ****** Functions/software *******

def Open_COM():
    global tgsCom
    global tgS
    #tgsCom = "COM7"  ##### MODIFY THIS LINE FOR YOUR SERIAL PORT NAME OR NUMBER
    tgS = serial.Serial()
    tgS.baudrate = 57600
    tgS.port = tgsCom
    tgS.bytesize = serial.EIGHTBITS  # number of bits per bytes
    tgS.parity = serial.PARITY_NONE  # set parity check: no parity
    tgS.stopbits = serial.STOPBITS_ONE  # number of stop bits
    # tgS.timeout = None          #block read
    tgS.timeout = 0.5  # non-block read
    tgS.xonxoff = False  # disable software flow control
    tgS.rtscts = False  # disable hardware (RTS/CTS) flow control
    tgS.dsrdtr = False  # disable hardware (DSR/DTR) flow control
    tgS.writeTimeout = 0  # timeout for write


def on_select(selection):                    # open the port and command it to start the LED blinking here
    global tgsCom
    default = StringVar(root,selection)    #Makes default = the selection
    tgsCom = default.get()          # Grabs the value of default
    tgsCom = tgsCom[:4]                 # makes tgsCom only have the value of the first four letters/numbers of the selection
    default.get()           #opens the value of default in order to see a change
    print("ComboBox Has selected "+ default.get() + " on mouse click")
    print("Truncated to " + tgsCom + " for compatability " )


#a = "BOB"
#if(a[0] == 'B'):
#    print("this is bob")

ports = serial.tools.list_ports.comports()      #Def that allows the dropdown box to show all COM ports
default = StringVar(root, "Please Select Port")             #default stringvar, this allows the orginal value, as well as text on dropbox. Dont think it's currently in use.
myPort = StringVar(root)            # Defs the myPort
myPort.set("None")              # Makes the stringvar's value = "None"
portSelect = OptionMenu(root, myPort, *ports, command=on_select).pack()         #portSelect is the optionmenu/box that shows the com ports.


pnum = 0            #Port number, set to 0
def OPENCOM():              #Def OPENCOM set to the OPENCOM button.
        global tgsCom
        global portSelect
        #print(myPort)           #prints the myPort variable
        #print(portSelect)       #Prints the value of portSelect
        portSelect = tgsCom  # sets the portSelect value to be the same as tgsCom
        #print("we are inside openCOM and now portSelect is ==" + portSelect)            #Shows what the value of portSelect is
        if portSelect != "None":            #If the value of portSelect doesn't = none, then excute the command
            Open_COM()
            try:                        # Begins the command
                print("Activating Triggerscope...")     # Prints activiating TRGSCPE
                tgS.open()      #Opens tgS
            except Exception as e:
                print("ERROR: Triggerscope Com port NOT OPEN: " + str(e))
                exit()
            if tgS.isOpen():
                try:
                    tgS.flushInput()  # flush input buffer, discarding all its contents
                    tgS.flushOutput()  # flush output buffer, aborting current output
                    tgS.write("*\n".encode())  # send an ack to tgs to make sure it's up
                    time.sleep(0.3)  # give the serial port sometime to receive the data
                    print("Rx: " + tgS.readline().decode())
                    print("Triggerscope Port is Open")
                except Exception as e1:
                    print("triggerscope serial communication error...: " + str(e1))

            else:
                print("cannot open triggerscope port ")
#Port_button = Button(command = OPENCOM())
Port_button = Button(root,text = "Open Port", command = OPENCOM )
Port_button.pack()

def toggle():         #Toggle animation for TTL Buttons as well as opening the labelsensor def

    if TTL1.config('relief')[-1] == 'sunken':
        TTL1.config(relief="raised")
        Toff1.config(bg = "red")
        labelsensor()

    else:
        TTL1.config(relief="sunken")
        Toff1.config(bg = "green2")
        labelsensor()

TTL1 = Button(text = "TTL1", command =toggle)
TTL1.config(bg = "gold")
TTL1.pack()
Toff1 = Label(bg = "red")
Toff1.pack()

def labelsensor():                              # Turns the Triggerscope TTL on.
    if Toff1['background'] == 'green2':
        print("ON")
        print(writetgs("TTL1,1\n"))
    else:
        print("OFF")
        print(writetgs("TTL1,0\n"))

def dacPos(event):                  # Event that grabs the value and sends it to the Triggerscope
    DAC1.get()          #Grabs the currrent value of the scale
    out = "DAC1," + str(DAC1.get()) + "\n"      #Makes "Out" the current variable of the corrisponding scale
    print(writetgs(out))        #Print the command the trigerscope got, Should be to set it to whatever number it is.


DAC1 = Scale(width= 10, from_=0, to= 65535, orient=HORIZONTAL, bg= "black", fg= "Green")      #The DAC scale
DAC1.configure(relief = FLAT)       # make the relief of the scale flat
DAC1.bind("<ButtonRelease>", dacPos)        # Bind the scale to run the dacPos command when the curser is done selecting the amount
DAC1.pack()    #Puts the scale on the canvas


def writetgs(tgin):
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

root.mainloop()