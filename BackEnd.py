import GUI
import time
import math
import _thread
from tkinter import *
from tkinter.font import *

# Give Value
HeightA, AngelA, SpeedA, HeightB, AngelB, SpeedB = None, None, None, None, None, None
BeginX, EndX, BeginY, EndY = 160, 1120, 42.5, 640

#Cal
ScaleX, ScaleY, Ys = None, None, None

# Screen
WidthScr, HeightScr = EndX - BeginX, EndY - BeginY
TimefallScr = math.sqrt(2 * HeightScr / (math.pi ** 2))

# Scale
DistanceMax = None

def GetValue( ValueA, ValueB ):
    global HeightA, AngelA, SpeedA, HeightB, AngelB, SpeedB
    if ( ValueA == 0 ):
        HeightA = float(GUI.storage.BoxHeightA.get())
    else:
        AngelA = float(GUI.storage.BoxAngleA.get())
    SpeedA = float(GUI.storage.BoxSpeedA.get())
    if ( ValueB == 0 ):
        HeightB = float(GUI.storage.BoxHeightB.get())
    else:
        AngelB = float(GUI.storage.BoxAngleB.get())
    SpeedB = float(GUI.storage.BoxSpeedB.get())

def YCal( Value, Angle, Time ):
    if ( Value == 0 ):
        return 0.5 * math.pi ** 2 * Time ** 2
def XCal( Value, Angle, Speed, Time ):
    if ( Value == 0 ):
        return Speed * Time

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

def Nem( Height, Speed, Color ):
    global DistanceMax, HeightScr, WidthScr, ScaleX, ScaleY, BeginX, EndX, Ys
    more = None
    if ( Ys != Height ):
        more = abs(Ys - Height)
    Time, posX, posY = 0, 0, 0
    while ( posY <= EndY ):
        Time += 0.01
        posX = ( Speed * Time / ScaleX ) + BeginX
        posY = ( 0.5 * ( math.pi ** 2 ) * ( Time ** 2 ) ) + BeginY
        if ( more != None ):
            posY += (more / ScaleY)
        GUI.graph.create_rectangle(posX,posY,posX,posY,outline=Color, width=5)
        time.sleep(0.001)

def StartCal( ValueA, ValueB ):
    global ScaleX, ScaleY, Ys
    print(ValueA, ValueB)
    try:
        GetValue( ValueA, ValueB )
    except:
        GUI.show.ShowTextWA()
        return
    GUI.hide.HideTextWA()
    GUI.show.ShowUIGraph()
    if ( ValueA == 0 ):
        ScaleX = SpeedA * TimefallScr / WidthScr
        ScaleY = HeightA
    if ( ValueB == 0 ):
        ScaleX = max(ScaleX, SpeedB * TimefallScr / WidthScr)
        ScaleY = max(ScaleY, HeightB)
    Ys = ScaleY
    ScaleY /= HeightScr
    print(ScaleY)
    if ( ValueA == 0 ):
        _thread.start_new_thread(Nem, (HeightA, SpeedA, "red"))
    if ( ValueB == 0 ):
        _thread.start_new_thread(Nem, (HeightB, SpeedB, "green"))
    return