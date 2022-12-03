import GUI
import math
from tkinter import *
from tkinter.font import *

# Give Value
HeightA, AngelA, SpeedA, HeightB, AngelB, SpeedB = None, None, None, None, None, None

def GetValue( ValueA, ValueB ):
    global HeightA, AngelA, SpeedA, HeightB, AngelB, SpeedB
    if ( ValueA == 0 ):
        HeightA = float(GUI.storage.BoxHeightA.get())
    else:
        AngelA = float(GUI.storage.BoxAngleA.get())
    SpeedA = float(GUI.storage.BoxSpeedA.get())
    if ( ValueB == 0 ):
        HeightB = float(GUI.storage.BoxHeightA.get())
    else:
        AngelB = float(GUI.storage.BoxAngleA.get())
    SpeedB = float(GUI.storage.BoxSpeedA.get())

def fixNum( value ):
    Div = 5
    if ( value >= 2 * Div ):
        value = int(value)
        t = value % Div
        value += Div - t
        if ( ( value / 5 ) % 2 != 0 ):
            value += 5
    else:
        f, temp = 10, value * 10
        while ( temp < 2 * Div ):
            temp *= 10
            f *= 10
        temp = int(temp)
        temp += Div - (temp % Div)
        if ( ( temp / 5 ) % 2 != 0 ):
            temp += 5
        value = temp / f
    return value

def Nem( Height, Speed ):
    Timefall = math.sqrt(2 * Height / (math.pi * math.pi))
    TotalDistance = Speed * Timefall
    FixDistance = fixNum(TotalDistance)
    FixHeight = fixNum(Height)
    print("FixDistance:", FixDistance, "\nFixHeight", FixHeight)

def StartCal( ValueA, ValueB ):
    print(ValueA, ValueB)
    try:
        GetValue( ValueA, ValueB )
    except:
        GUI.show.ShowTextWA()
        return
    GUI.hide.HideTextWA()
    GUI.show.ShowUIGraph()
    if ( ValueA == 0 ):
        Nem(HeightA, SpeedA)
    if ( ValueB == 0 ):
        Nem(HeightB, SpeedB)
    return