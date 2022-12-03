import GUI
import math
from tkinter import *
from tkinter.font import *

# Give Value
Height, Angel, Time, Speed, Distance = None, None, None, None, None
# Cal Value
FixDistance, Dismin, Timefall, TotalDistance = None, None, None, None

def GetValue( value ):
    global Height, Angel, Time, Speed, Distance
    if ( value == 0 ):
        Height = float(GUI.storage.BoxHeight.get())
    else:
        Angel = float(GUI.storage.BoxAngle.get())
    Distance = float(GUI.storage.BoxDis.get())
    Time = float(GUI.storage.BoxTime.get())
    Speed = float(GUI.storage.BoxSpeed.get())

def fixNum( value ):
    Div = 5
    if ( value >= 2 * Div ):
        value = int(value)
        value += Div - ( value % Div )
    else:
        f, temp = 10, value * 10
        while ( temp < 2 * Div ):
            temp *= 10
            f *= 10
        temp = int(temp)
        temp += Div - (temp % Div)
        value = temp / f
    return value

def Nem():
    global Timefall, Height, Time, Speed, Distance, FixDistance, TotalDistance
    Timefall = math.sqrt(2 * Height / (math.pi * math.pi))
    Div = 5
    TotalDistance = Speed * Timefall
    FixDistance = fixNum(TotalDistance)
    TotalDistance += Distance

def StartCal( value ):
    print(value)
    try:
        GetValue( value )
    except:
        GUI.show.ShowTextWA()
        return
    GUI.hide.HideTextWA()
    GUI.show.ShowUIGraph()
    if ( value == 0 ):
        Nem()
    return