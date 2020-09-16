from tkinter import *
import tkinter
import time
import serial
import serial.tools.list_ports


tgS = serial.Serial()
portSelect = 0
tgsCom = "NONE"                 #Sets tgsCom to be "None" this allows


def Open_COM():
  global tgsCom
  global tgS
  # tgsCom = "COM7"  ##### MODIFY THIS LINE FOR YOUR SERIAL PORT NAME OR NUMBER
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

def on_select(selection):  # open the port and command it to start the LED blinking here
  global tgsCom
  default = StringVar(root, selection)  # Makes default = the selection
  tgsCom = default.get()  # Grabs the value of default
  tgsCom = tgsCom  # makes tgsCom only have the value of the first four letters/numbers of the selection
  default.get()  # opens the value of default in order to see a change
  print("ComboBox Has selected " + default.get() + " on mouse click")
  print("Truncated to " + tgsCom + " for compatability ")

pnum = 0  # Port number, set to 0

def OPENCOM():  # Def OPENCOM set to the OPENCOM button.
  global tgsCom
  global portSelect
  # print(myPort)           #prints the myPort variable
  # print(portSelect)       #Prints the value of portSelect
  portSelect = tgsCom  # sets the portSelect value to be the same as tgsCom
  # print("we are inside openCOM and now portSelect is ==" + portSelect)            #Shows what the value of portSelect is
  if portSelect != "None":  # If the value of portSelect doesn't = none, then excute the command
    Open_COM()
    try:  # Begins the command
      print("Activating Triggerscope...")  # Prints activiating TRGSCPE
      tgS.open()  # Opens tgS
    except Exception as e:
      print("ERROR: Triggerscope Com port NOT OPEN: " + str(e))
      #exit()
      SLight.config(bg="red")
    if tgS.isOpen():
      try:
        tgS.flushInput()  # flush input buffer, discarding all its contents
        tgS.flushOutput()  # flush output buffer, aborting current output
        tgS.write("*\n".encode())  # send an ack to tgs to make sure it's up
        time.sleep(0.3)  # give the serial port sometime to receive the data
        print("Rx: " + tgS.readline().decode())
        print("Triggerscope Port is Open")
        SLight.config(bg="Green2")
      except Exception as e1:
        print("triggerscope serial communication error...: " + str(e1))

    else:
      print("cannot open triggerscope port ")
      Slight.config(bg="red")



def writetgs(tgin):
  '''send a serial command to the triggerscope...
              Args:
                  tgin: input string to send. Note the command terminator should be included in the string.
              Returns:
                  char string of whatever comes back on the serial line.
              Raises:
                  none.
              '''
  scomp = '!' + tgin
  tgS.flushInput()  # flush input buffer, discarding all its contents
  tgS.flushOutput()  # flush output buffer, aborting current output
  tgS.write(tgin.encode())  # send an ack to tgs to make sure it's up
  time.sleep(0.1)  # give the serial port sometime to receive the data 50ms works well...
  bufa = ""
  bufa = tgS.readline().decode()
  return bufa

def quit():
  root.destroy()

# ****** Functions/software *******




root = Tk()       # Root
root.configure(bg="grey90")

Grid.rowconfigure(root, 0, weight=1)    #Creating the base grid
Grid.columnconfigure(root, 0, weight=1)   #Setting the columns to the grid

frame=Frame(root, bg="grey80", highlightbackground="black", highlightthickness=1)      #Frame has been created
frame.grid(row=1, column=1)   #G
Grid.rowconfigure(frame, 0, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

button1 = Button(text = "Quit", command = quit) #Quit Button that exits the program
button1.configure(width = 10, activebackground = "#33B5E5", relief = RAISED) #gives the button detail
button1.grid(row= 0, column=0, sticky = N+W)


ports = serial.tools.list_ports.comports()      # Sets "ports" to be the list of COM ports.
default = StringVar(root, "Please Select Port")
myPort = StringVar(root)            # Defs the myPort
myPort.set("Please Select Port")              # Makes the stringvar's value = "None"
portSelect = OptionMenu(root, myPort, *ports, command=on_select) #The Option menu is set, with the command of on_select
portSelect.grid(row=1, column = 0)



OPENPORT = Button(text = "Open Port", command = OPENCOM)     #Button that opens the communication to the COM port
OPENPORT.grid(row =2 , column=0)

Status = Label(text = "Port Status:", bg = "grey90", fg="black")
Status.grid(row=1, column= 0, pady=(75,0))

SLight = Label(bg= "red", width = 1)
SLight.grid(row=1, column= 0, pady=(75,0), padx= (80,0))

#Port_button = Button(root,text = "Open Port", command = OPENCOM )
#Port_button.pack()

#****** Root/title/Frames ******
root.title("ARC Triggerscope Regulator")     # title of root window
root.iconbitmap(r'ARC.ico')      # Window Icon


btn_list = [] # List to hold the button objects
dv = list()

G = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
F = []
COLOR = list()

def Switch(idx):
  global G
  G[idx] = 1


def Switch2(idx):
  global G
  G[idx] = 0

DacVal= [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]

def main(height=4,width=4):
  flipper = TRUE

  def updateButtonlabels():
    for x in range(16):
      if (G[x] == 1):
        Toff.config(bg='green2')
      else:
        Toff.config(bg='red')
        # make label red

  def dacUpdate(barf):
    #print(barf)
    f = 0
    for i in dv:
      D = i.get()
      if (D != DacVal[f]):
        out = "DAC" + str(f+1) + "," + str(D) + "\n"  # Makes "Out" the current variable of the corrisponding scale
        print(writetgs(out))  # Print the command the trigerscope got, Should be to set it to whatever number it is.
        DacVal[f] = D
      f = f + 1


  def toggle(idx):  # Toggle animation for TTL Buttons as well as opening the labelsensor def
    if (idx <= 7):
      idx= idx+1
      global G
      if (G[idx] == 0):
        print(writetgs("TTL" + str(idx+1) + ",1\n"))
        F[idx].config(bg = "green2")
        Switch(idx)
      else:
        print(writetgs("TTL" + str(idx+1) + ",0\n"))
        F[idx].config(bg = "red")
        Switch2(idx)

    if (idx >= 8):
      if (G[idx] == 0):
        print(writetgs("TTL" + str(idx+1) + ",1\n"))
        F[idx].config(bg="green2")
        if (idx == 15):
          F[idx].config(bg = "green2")
        print(idx)
        Switch(idx)
      else:
        print(writetgs("TTL" + str(idx+1) + ",0\n"))
        F[idx].config(bg="red")
        Switch2(idx)
    updateButtonlabels()
    print(G)

  for y in range(height):
    for x in range(width):
      Tname = ""
      Lname = ""
      Dname = ""
      if(flipper):
        Tname = "TTL:" + str(x+1)
        Lname = str(x+1)
      if(not flipper):
        Tname = "TTL:" + str(x+1)
        Lname = str(x+1)

      if (y == 0):
        TTL = tkinter.Button(frame, bg = "grey90", fg="black", text = Tname, command = lambda idx = x: toggle(idx-1))
        TTL.grid(column=x, row=y, padx= 50)
        Toff = Label(frame, bg="red", width = 1)
        Toff.grid(column=x, row=y, sticky = E, padx = 15)
        F.append(Toff)
        COLOR.append(TTL)
        print (Toff)
        if (x == 7):
          break

      if (y == 1):
        DAC = Scale(frame, width=13, from_=0, to=65535, orient=HORIZONTAL,bg="grey90", fg="black", highlightbackground="skyblue")
        DAC.grid(column=x, row=y+1, pady=(0,25))
        DAC.configure(relief=RAISED)  # make the relief of the scale flat
        DAC.bind("<ButtonRelease>",dacUpdate)  # Bind the scale to run the dacUpdate command when the curser is done selecting the amount
        dv.append(DAC)
        if (x == 7):
          break

      if (y == 3):
        Tname2 = "TTL:" + str(x + 9)
        Lname2 = x+9
        TTL = tkinter.Button(frame, bg="grey90",fg="black", text = Tname2, command = lambda idx = x + 9: toggle(idx-1))
        TTL.grid(column=x, row=y)
        Toff = Label(frame, bg="red", width = 1)
        Toff.grid(column=x, row=y, sticky = E, padx = 14)
        F.append(Toff)
        COLOR.append(TTL)
        print(Toff)
        if (x == 7):
          break


      if (y == 4):
        #nam.append(Scale(master, from_=100, to=0, orient=VERTICAL))
        DAC = Scale(frame, width=13, from_=0, to=65535, orient=HORIZONTAL, bg="grey90", fg="black", highlightbackground="skyblue")
        DAC.grid(column=x, row=y+1)
        DAC.configure(relief=RAISED)  # make the relief of the scale flat
        DAC.bind("<ButtonRelease>", dacUpdate)
        dv.append(DAC)
        #DAC.bind("<ButtonRelease>", dacPos)  # Bind the scale to run the dacPos command when the curser is done selecting the amount
        if (x == 7):
          break

      print("Column = " +str(x) + "row="+str(y))
      flipper = not flipper
      #btn_list.append(TTL)  # Append the button to a list
      def classic():
        root.config(bg="grey90")
        frame.config(bg="grey80", highlightbackground="black")
        Status.config(bg="grey90", fg="black")
        button1.config(bg="grey90")
        for x in range(16):
          dv[x].config(bg="grey90", fg="black", highlightbackground="skyblue")     #Adjusts the color of the DAC sliders
        for y in range(16):
          COLOR[y].config(bg="grey90", fg="black")     #Adjusts the color of the TTL buttons

        print("classic")

      def dark():
        root.config(bg="black")
        frame.config(bg="black", highlightbackground="white")
        Status.config(bg="black", fg="white")
        button1.config(bg="gold")
        for x in range(16):
          dv[x].config(bg="black", fg="green2", highlightbackground="white")
        print("dark")
        for y in range(16):
          COLOR[y].config(bg= "gold", fg= "black")

      my_menu = Menu(root)
      root.config(menu=my_menu)
      theme_menu = Menu(my_menu)
      my_menu.add_cascade(label="Theme", menu=theme_menu)
      theme_menu.add_command(label="Classic", command=classic)
      theme_menu.add_command(label="Dark", command=dark)

  return frame









w= main(5,16)
tkinter.mainloop()
