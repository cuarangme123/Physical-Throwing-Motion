import GUI

h, angel, t, speed, dis = None, None, None, None, None

def GetValue( value ):
    if ( value == 0 ):
        h = GUI.storage.BoxHeight.get()
        angel = ""
    else: 
        angel = GUI.storage.BoxAngle.get()
    dis = GUI.storage.BoxDis.get()
    t = GUI.storage.BoxTime.get()
    speed = GUI.storage.BoxSpeed.get()

def StartCal( value ):
    GetValue( value )