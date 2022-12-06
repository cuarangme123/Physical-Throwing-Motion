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
HeightFix, WidgetFix = 0, 0
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

def Xien( Speed, Angle, Color ):
    global HeightScr, WidthScr, ScaleX, ScaleY, BeginX, EndX, Ys, TimeX, HeightFix, WidgetFix
    posX, posY, Time = 0, 0, 0
    theta = Angle * np.pi / 180
    cos = np.cos(theta)
    sin = np.sin(theta)
    while ( posY >= 0 ):
        Time += TimeX
        posX = ( Speed * cos * Time ) / ScaleXY
        posY = ((Speed * sin * Time) - ((math.pi ** 2) * (Time ** 2) / 2)) / ScaleXY
        #print(posX * ScaleXY, posY * ScaleXY)
        posX += BeginX
        GUI.graph.create_rectangle(posX, EndY - posY, posX, EndY - posY, outline = Color, width = 2, tags = 's')
        time.sleep(0.0005)

def CalScale( ValueA, ValueB ):
    global ScaleX, ScaleY, ScaleXY, TimeX, HeightFix, WidgetFix
    TimefallScr, ScaleXX = None, None
    WidA, WidB, WidMax, TimeX = None, None, 0, 0
    if ( ValueA == 1 ):
        theta = AngleA * np.pi / 180
        HeightA = (( SpeedA ** 2 ) * (np.sin(theta) ** 2)) / (2 * math.pi ** 2)
        ScaleY = HeightA
        WidA = (SpeedA ** 2) * np.sin(2*theta) / ( math.pi ** 2 )
        WidMax = max(WidMax, WidA)
    if ( ValueB == 1 ):
        theta = AngleB * np.pi / 180
        HeightB = (( SpeedB ** 2 ) * (np.sin(theta) ** 2)) / (2 * math.pi ** 2)
        ScaleY = max(ScaleY, HeightB)
        WidB = (SpeedB ** 2) * np.sin(2*theta) / ( math.pi ** 2 )
        WidMax = max(WidMax, WidB)
    if ( WidMax != None ):
        WidgetFix = WidMax
        ScaleX = fixNum(WidgetFix) / WidthScr
    HeightFix = ScaleY
    ScaleY = fixNum(ScaleY)
    ScaleY /= HeightScr
    ScaleXY = max(ScaleX, ScaleY)
    if ( ValueA == 1 ):
        theta = AngleA * np.pi / 180
        TimeX = ( SpeedA * np.cos(theta) * 1 ) / ScaleXY
        TimeX = max(TimeX, ((SpeedA * np.sin(theta) * 1) - ((math.pi ** 2) * (1 ** 2) / 2)) / ScaleXY)
    if ( ValueB == 1 ):
        theta = AngleB * np.pi / 180
        TimeX = max(TimeX, ( SpeedB * np.cos(theta) * 1 ) / ScaleXY)
        TimeX = max(TimeX, ((SpeedB * np.sin(theta) * 1) - ((math.pi ** 2) * (1 ** 2) / 2)) / ScaleXY)
    TimeX = 1 / TimeX
    print(HeightScr, HeightA / ScaleXY, HeightB / ScaleXY, HeightFix / ScaleXY)
    print(WidthScr, WidA / ScaleXY, WidB / ScaleXY, WidgetFix / ScaleXY)
    temp = HeightScr - ( HeightFix / ScaleXY )
    temp *= ScaleXY
    HeightFix += temp
    temp = WidthScr - ( WidgetFix / ScaleXY )
    temp *= ScaleXY
    WidgetFix += temp
def StartCal( ValueA, ValueB ):
    GUI.graph.delete('s')
    global ScaleX, ScaleY, Ys, TimefallScr, AngleA, ScaleXY, ScaleX, ScaleY, TimeX, HeightFix, WidgetFix
    ScaleXY, ScaleX, ScaleY, TimeX = None, None, None, None
    HeightFix, WidgetFix = 0, 0
    print(ValueA, ValueB)
    try:
        GetValue( ValueA, ValueB )
    except:
        GUI.show.ShowTextWA()
        return
    GUI.hide.HideTextWA()
    GUI.show.ShowUIGraph()
    CalScale( ValueA, ValueB )
    num, pos = -HeightFix / 5, EndY + 119.5
    for i in range(0, 6):
        pos -= 119.5
        num += HeightFix / 5
        num = round(num, 2)
        msg = str(num)
        GUI.graph.create_text(100, pos, text=msg, tags = 's')
    num , pos = -WidgetFix / 5, BeginX - 192
    for i in range(0, 6):
        pos += 192
        num += WidgetFix / 5
        num = round(num, 2)
        msg = str(num)
        GUI.graph.create_text(pos, 670, text=msg, tags = 's')

    if ( ValueA == 1 ):
        _thread.start_new_thread(Xien, (SpeedA, AngleA, "red"))
    if ( ValueB == 1 ):
        _thread.start_new_thread(Xien, (SpeedB, AngleB, "green"))
    # fix
    return
