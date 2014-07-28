import Tkinter
import tkMessageBox
import socket
import pickle
import pygame

top = Tkinter.Tk()
joyFrame = Tkinter.Frame(top)
noJoyFrame = Tkinter.Frame(top)
port = 8081
host999 = "10.99.99.7"
host = "192.168.1.79"
pygame.init()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#j =0;
s.bind(("", 0))
started = False
def startSession():
    started = True
    s.sendto(pickle.dumps(started), (host, port))
    top.after(2000, sendJoystickVal)
def endSession():
    started = False
    #s.bind(("", 0))
    s.sendto(pickle.dumps(started), (host, port))
    s.close()
    top.destroy()
sessionStart = Tkinter.Button(top, text ="Start Session", command = startSession)
sessionEnd = Tkinter.Button(top, text="End Session", command=endSession)

def isJoystick():
    return pygame.joystick.get_count()>0

def whileJoyCon():
    if(isJoystick()):
        sessionStart.config(state="normal")
        sessionStart.pack()
        sessionEnd.config(state="normal")
        sessionEnd.pack()
        howTo = Tkinter.Text(top)
        howTo.insert(Tkinter.INSERT, "Press Start on the Joystick or end session to stop the program")
        howTo.pack()
    else:
        print isJoystick()
        sessionStart.config(state="disable")
        sessionStart.pack()
        sessionEnd.config(state="disable")
        sessionEnd.pack()
        noJoy = Tkinter.Text(top)
        noJoy.insert(Tkinter.INSERT, "No Joystick Connected. Please connect a Joystick and Restart the program")
        noJoy.pack()        
def sendJoystickVal():
    #print isJoy
    #if(isJoystick):
        pygame.event.pump()
        j = pygame.joystick.Joystick(0)
        j.init()
        xAxis = j.get_axis(1)
        yAxis=j.get_axis(3)
        i=1
        button =-1;
        
        for i in range(j.get_numbuttons()):
            if(j.get_button(i)==True):
                button = i
                break
        
        data = [xAxis, yAxis, button]
        s.sendto(pickle.dumps(data), (host, port))
        print data
        top.after(2000, sendJoystickVal)
whileJoyCon()
#rint started
#f(started):
#top.after(2000, sendJoystickVal)
top.mainloop()
