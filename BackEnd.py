import GUI
import math
from tkinter import *
from tkinter.font import *

# Give Value
Height, Angel, Time, Speed, Distance = None, None, None, None, None
# Cal Value
AfterDistance, Dismin, Timefall = None, None, None

def GetValue( value ):
    global Height, Angel, Time, Speed, Distance
    if ( value == 0 ):
        Height = float(GUI.storage.BoxHeight.get())
    else:
        Angel = float(GUI.storage.BoxAngle.get())
    Distance = float(GUI.storage.BoxDis.get())
    Time = float(GUI.storage.BoxTime.get())
    Speed = float(GUI.storage.BoxSpeed.get())

def StartCal( value ):
    print(value)
    global Timefall, Height, Angel, Time, Speed, Distance, AfterDistance
    try:
        GetValue( value )
    except:
        GUI.show.ShowTextWA()
        return
    GUI.hide.HideTextWA()
    GUI.show.ShowUIGraph()
    if ( value == 0 ):
        Timefall = math.sqrt(2 * Height / (math.pi * math.pi))
    AfterDistance = Distance + Speed * Timefall
    print("Time fall: ", Timefall, "\nDistance:", AfterDistance)
    return