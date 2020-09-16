# Download the helper library from https://www.twilio.com/docs/python/install

import os
import twilio
from twilio.rest import Client
import time
import tkinter
from tkinter import*

Me = "+17073869477"+"Me"
Tiffany = "+18018749647"+"Tiffany"
Tiago = "+18013686811"+"Tiago"
Jd = "+15308450573"+"Jd"
Miles = "+19163802190"+"Miles"
Aiden_Bunch = "+19165819795"+"Aiden_Bunch"
James_Bunch = "+17073927550"+"James_Bunch"
Sophia = "+19168844531"+"Sophia"
Dillon = "+19168737971"+"Dillon"
Ryan_K = "+19163358808"+"Ryan_K"



root= Tk()
root.title("ThePanda_message_access")
root.config(bg = "grey")


choises = {Me,Tiffany,Tiago,Jd,Miles,Aiden_Bunch,James_Bunch,Sophia,Dillon,Ryan_K}
var = StringVar(root)
var.set("Me")



# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe94ffc2992e5815fa3f4e5778a11cf0e'
auth_token = '8a6fa63b93aa153bb90767acc6b53a1a'
client = Client(account_sid, auth_token)


popupMenu = OptionMenu(root, var, *choises)
Label(root, text="Choose a person")
popupMenu.pack()


def text_box():
    x1=entry1.get()
    print(x1)
    say_smth(x1)

def get_person():
    print("person is",var.get())
    global Person
    Person = var.get()



person_get = Button(text="Load subject", command = get_person)
person_get.pack()

entry1 = Entry(root)
entry1.pack()


def say_smth(x1):
    print(Person[:12])
    for x in range(1):
        message = client.messages \
            .create(
                body=x1,
                from_='+19162371542',
                to= (Person[:12])
        )
#print(message.sid)

Send = Button(text="Send", bg = "Black", fg="white",command= text_box)
Send.pack()
root.mainloop()