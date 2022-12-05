import GUI
import time
import math
import _thread
from tkinter import *
from tkinter.font import *
import numpy as np

# Give Value
HeightA, AngleA, SpeedA, HeightB, AngleB, SpeedB = None, None, None, None, None, None
BeginX, EndX, BeginY, EndY = 160, 1120, 42.5, 640

#Cal
ScaleX, ScaleY, Ys, ScaleXY, TimeX = None, None, None, None, None
# Screen
WidthScr, HeightScr = EndX - BeginX, EndY - BeginY
#test git hub
def GetValue( ValueA, ValueB ):
    global HeightA, AngleA, SpeedA, HeightB, AngleB, SpeedB
    if ( ValueA == 0 ):
        HeightA = float(GUI.storage.BoxHeightA.get())
    else:
        AngleA = float(GUI.storage.BoxAngleA.get())
    SpeedA = float(GUI.storage.BoxSpeedA.get())
    if ( ValueB == 0 ):
        HeightB = float(GUI.storage.BoxHeightB.get())
    else:
        AngleB = float(GUI.storage.BoxAngleB.get())
    SpeedB = float(GUI.storage.BoxSpeedB.get())

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
    global HeightScr, WidthScr, ScaleX, ScaleY, BeginX, EndX, Ys
    more = 0
    if ( Ys != Height ):
        more = abs(Ys - Height)
    Time, posX, posY = 0, 0, 0
    while ( posY <= EndY - 5 ):
        Time += 0.01
        posX = ( Speed * Time / ScaleXY ) + BeginX
        posY = ( 0.5 * ( math.pi ** 2 ) * ( Time ** 2 ) ) + BeginY
        posY += 5
        posX += 2
        if ( more != None ):
            posY += (more / max(Ys, Height)) * max(Ys,Height) / ScaleY
        GUI.graph.create_rectangle(posX,posY,posX,posY,outline = Color, width = 2, tags = 's')
        time.sleep(0.001)

def Xien( Speed, Angle, Color ):
    global HeightScr, WidthScr, ScaleX, ScaleY, BeginX, EndX, Ys, TimeX
    posX, posY, Time = 0, 0, 0
    theta = Angle * np.pi / 180
    cos = np.cos(theta)
    sin = np.sin(theta)
    while ( posY >= 0 ):
        Time += TimeX
        posX = ( Speed * cos * Time ) / ScaleXY
        posY = ((Speed * sin * Time) - ((math.pi ** 2) * (Time ** 2) / 2)) / ScaleXY
        posX += BeginX
        GUI.graph.create_rectangle(posX, EndY - posY, posX, EndY - posY, outline = Color, width = 2, tags = 's')
        time.sleep(0.0005)

def CalScale( ValueA, ValueB ):
    global ScaleX, ScaleY, Ys, HeightA, HeightB, ScaleXY, TimeX
    TimefallScr, ScaleXX = None, None
    WidA, WidB, WidMax = None, None, None
    if ( ValueA == 0 ):
        ScaleY = HeightA
    else:
        theta = AngleA * np.pi / 180
        HeightA = (( SpeedA ** 2 ) * (np.sin(theta) ** 2)) / (2 * math.pi ** 2)
        ScaleY = HeightA
        WidA = (SpeedA ** 2) * np.sin(2*theta) / ( math.pi ** 2 )
        WidMax = WidA
    if ( ValueB == 0 ):
        ScaleY = max(ScaleY, HeightB)
    else:
        theta = AngleB * np.pi / 180
        HeightB = (( SpeedB ** 2 ) * (np.sin(theta) ** 2)) / (2 * math.pi ** 2)
        ScaleY = max(ScaleY, HeightB)
        WidB = (SpeedB ** 2) * np.sin(2*theta) / ( math.pi ** 2 )
        if ( WidA != None ):
            WidMax = max(WidA, WidB)
        else:
            WidMax = WidB
    if ( WidMax != None ):
        ScaleXX = WidMax / WidthScr
    Ys = ScaleY
    ScaleY /= HeightScr
    fix = ScaleY
    for i in range(31415):
        if ( ValueA == 0 ):
            if ( Ys != HeightA ):
                temp = Ys - HeightA
                temp = HeightScr - (temp / fix)
                TimefallScr = math.sqrt(2 * temp / (math.pi ** 2))
                ScaleX = SpeedA * TimefallScr / WidthScr
            else:
                TimefallScr = math.sqrt(2 * HeightScr / (math.pi ** 2))
                ScaleX = SpeedA * TimefallScr / WidthScr
        if ( ValueB == 0 ):
            if ( Ys != HeightB ):
                temp = Ys - HeightB
                temp = HeightScr - (temp / fix)
                TimefallScr = math.sqrt(2 * temp / (math.pi ** 2))
                if ( ScaleX != None ):
                    ScaleX = max( ScaleX, SpeedB * TimefallScr / WidthScr )
                else:
                    ScaleX = SpeedB * TimefallScr / WidthScr
            else:
                TimefallScr = math.sqrt(2 * HeightScr / (math.pi ** 2))
                if ( ScaleX != None ):
                    ScaleX = max( ScaleX, SpeedB * TimefallScr / WidthScr )
                else:
                    ScaleX = SpeedB * TimefallScr / WidthScr
        if ( ScaleXX != None ):
            if ( ScaleX != None ):
                ScaleX = max(ScaleX, ScaleXX)
            else:
                ScaleX = ScaleXX
        ScaleXY = max(ScaleX, ScaleY)
        fix = ScaleXY
    if ( ValueA == 1 ):
        theta = AngleA * np.pi / 180
        TimeX = ( SpeedA * np.cos(theta) * 1 ) / ScaleXY
        TimeX = max(TimeX, ((SpeedA * np.sin(theta) * 1) - ((math.pi ** 2) * (1 ** 2) / 2)) / ScaleXY)
    if ( ValueB == 1 ):
        theta = AngleB * np.pi / 180
        if ( TimeX != None ):
            TimeX = max(TimeX, ( SpeedB * np.cos(theta) * 1 ) / ScaleXY)
            TimeX = max(TimeX, ((SpeedB * np.sin(theta) * 1) - ((math.pi ** 2) * (1 ** 2) / 2)) / ScaleXY)
        else:
            TimeX = ( SpeedB * np.cos(theta) * 1 ) / ScaleXY
            TimeX = max(TimeX, ((SpeedB * np.sin(theta) * 1) - ((math.pi ** 2) * (1 ** 2) / 2)) / ScaleXY)
    if TimeX != None:
        TimeX = 1 / TimeX
    #temp = ( Speed * np.cos(theta) * 1 ) / ScaleXY
    #temp = max(temp, ((Speed * np.sin(theta) * 1) - ((math.pi ** 2) * (1 ** 2) / 2)) / ScaleXY)
    #temp = 1 / temp
    #print(ScaleX) 
    #print(ScaleY)
    #print(ScaleXY)
def StartCal( ValueA, ValueB ):
    GUI.graph.delete('s')
    global ScaleX, ScaleY, Ys, TimefallScr, AngleA, ScaleXY, ScaleX, ScaleY, TimeX
    ScaleXY, ScaleX, ScaleY, TimeX = None, None, None, None
    print(ValueA, ValueB)
    try:
        GetValue( ValueA, ValueB )
    except:
        GUI.show.ShowTextWA()
        return
    GUI.hide.HideTextWA()
    GUI.show.ShowUIGraph()
    CalScale( ValueA, ValueB )
    if ( ValueA == 0 ):
        _thread.start_new_thread(Nem, (HeightA, SpeedA, "red"))
    else:
        _thread.start_new_thread(Xien, (SpeedA, AngleA, "red"))
    if ( ValueB == 0 ):
        _thread.start_new_thread(Nem, (HeightB, SpeedB, "green"))
    else:
        _thread.start_new_thread(Xien, (SpeedB, AngleB, "green"))
    return
