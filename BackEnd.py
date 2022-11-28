import GUI
import math
from tkinter import *
from tkinter.font import *
h, angel, t, speed, dis, timef = None, None, None, None, None, None
timemin, dismin, timefix = None, None, None

def GetValue( value ):
    global h, angel, t, speed, dis
    if ( value == 0 ):
        h = float(GUI.storage.BoxHeight.get())
    else:
        angel = float(GUI.storage.BoxAngle.get())
    dis = float(GUI.storage.BoxDis.get())
    t = float(GUI.storage.BoxTime.get())
    speed = float(GUI.storage.BoxSpeed.get())

def StartCal( value ):
    GUI.show.ShowUIGraph()
    global timef
    GetValue( value )
    if ( value == 0 ):
        timef = math.sqrt(2 * h / (math.pi * math.pi))
    timefix = int((int(timef / 5) + 1) * 5)
    timemin = int(timefix / 5)
    print("Time fall", timef, "Time min", timemin)