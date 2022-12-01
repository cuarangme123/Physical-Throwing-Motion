import time
import BackEnd
from tkinter import *
from tkinter.font import *

GUI = Tk()
graph = Canvas(width=1280, height=680)
graph.create_line(160, 637.45, 1120, 637.45, width = 5 )
graph.create_line(160, 640, 160, 42.5, width = 5 )
class entry(Entry):
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self['fg'] = "#008888"
        self['font'] = "Consolas", 22, BOLD
        self['bg'] = "#33FFCC"
        self['borderwidth'] = 3
        self['relief']= "sunken"

class button(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['fg'] = "#008B22"
        self['font'] = "Consolas", 22, BOLD
        self['bg'] = "#98FBBB"
        self['borderwidth'] = 3
        self['relief']= "raised"

class TextUI(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self['fg'] = "#008888"
        self['font'] = "Consolas", 22, BOLD
        self['bg'] = "#33FFCC"
        self['borderwidth'] = 3
        self['relief']= "raised"

class storage:
    ButtonE = button(GUI, text = "Thoát", command = lambda: manager.Start(-1), 
    height = 1, width = 5)  # Exit
    ButtonN = button(GUI, text = "Ném Ngang", command = lambda: manager.Start(0), 
    height = 4, width = 11) # Nem
    ButtonX = button(GUI, text = "Ném Xiên", command = lambda: manager.Start(1), 
    height = 4, width = 11) # Xien
    ButtonB = button(GUI, text = "Quay lại", command = lambda: manager.Start(2), 
    height = 1, width = 8)  # Back
    ButtonC = button(GUI, text = "Bắt Đầu!", command = lambda: BackEnd.StartCal(storage.choice),
    height = 1, width = 8)  # Confirmed
    ButtonBa = button(graph, text = "Quay lại", command = lambda: manager.Start(storage.choice), 
    height = 1, width = 8)  # Back Pace Graph
    BoxHeight = entry(GUI, width = 9)
    BoxTime = entry(GUI, width = 9)
    BoxSpeed = entry(GUI, width = 9)
    BoxHeight = entry(GUI, width = 9)
    BoxAngle = entry(GUI, width = 9)
    BoxDis = entry(GUI, width = 9)
    TextTitle = TextUI(GUI, text = "Chọn dạng chuyển động:", height = 2, width = 40)
    TextHeight = TextUI(GUI, text = "Nhập độ cao của vật (m)", height = 1, width = 25)
    TextAngle = TextUI(GUI, text = "Nhập số đo góc của vật khi ném (°)", height = 1, width = 40)
    TextDis = TextUI(GUI, text = "Nhập mốc tọa độ bề ngang của vật (m)", height = 1, width = 45)
    TextTime = TextUI(GUI, text = "Nhập mốc thời gian của vật (s)", height = 1, width = 35)
    TextSpeed = TextUI(GUI, text = "Nhập vật tốc ban đầu của vật (m/s)", height = 1, width = 40)
    TextWA = TextUI(GUI, text = "Vui lòng nhập lại", height = 1, width = 30)
    choice = None
#test = button(GUI, text = "Ném", command = lambda: manager.Start(0), height = 4, width = 7)
#test.place(relx = 0.5, rely = 0.25, anchor = CENTER)

class show:
    def ShowEntry(value):
        if ( value == 0 ):
            storage.BoxHeight.place(relx = 0.5, rely = 0.15, anchor = CENTER)
            storage.BoxHeight.delete(0, 'end')
        else:
            storage.BoxAngle.place(relx = 0.5, rely = 0.15, anchor = CENTER)
            storage.BoxAngle.delete(0, 'end')
        storage.BoxDis.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        storage.BoxDis.delete(0, 'end')
        storage.BoxTime.place(relx = 0.5, rely = 0.55, anchor = CENTER)
        storage.BoxTime.delete(0, 'end')
        storage.BoxSpeed.place(relx = 0.5, rely = 0.75, anchor = CENTER)
        storage.BoxSpeed.delete(0, 'end')

    def ShowText01():
        storage.TextTitle.place(relx = 0.5, rely = 0.15, anchor = CENTER)
    def ShowText02(value):
        if ( value == 0 ):
            storage.TextHeight.place(relx = 0.5, rely = 0.05, anchor = CENTER)
        else:
            storage.TextAngle.place(relx = 0.5, rely = 0.05, anchor = CENTER)
        storage.TextDis.place(relx = 0.5, rely = 0.25, anchor = CENTER)
        storage.TextTime.place(relx = 0.5, rely = 0.45, anchor = CENTER)
        storage.TextSpeed.place(relx = 0.5, rely = 0.65, anchor = CENTER)

    def ShowTextWA():
        storage.TextWA.place(relx = 0.5, rely = 0.95, anchor = CENTER )

    def ShowButton01():
        #Show button
        storage.ButtonN.place(relx = 0.25, rely = 0.4, anchor = CENTER)
        storage.ButtonX.place(relx = 0.75, rely = 0.4, anchor = CENTER)
        storage.ButtonE.place(relx = 0.5, rely = 0.8, anchor = CENTER)

    def ShowButton02():
        #Show button
        storage.ButtonB.place(relx = 1, rely = 0, anchor = NE)
        storage.ButtonC.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    def ShowButtonGraph():
        storage.ButtonBa.place(relx =  1, rely = 0, anchor = NE)
    def ShowUIGraph():
        graph.pack()
        show.ShowButtonGraph()
        hide.HideEntry()
        hide.HideButton02()
        hide.HideText02()

class hide:
    def HideEntry():
        storage.BoxAngle.place_forget()
        storage.BoxHeight.place_forget()
        storage.BoxDis.place_forget()
        storage.BoxTime.place_forget()
        storage.BoxSpeed.place_forget()

    def HideText01():
        storage.TextTitle.place_forget()

    def HideText02():
        storage.TextHeight.place_forget()
        storage.TextDis.place_forget()
        storage.TextTime.place_forget()
        storage.TextSpeed.place_forget()
        storage.TextAngle.place_forget()
        storage.TextSpeed.place_forget()

    def HideTextWA():
        storage.TextWA.place_forget()

    def HideButton01():
        storage.ButtonN.place_forget()
        storage.ButtonX.place_forget()
        storage.ButtonE.place_forget()
    def HideButton02():
        storage.ButtonB.place_forget()
        storage.ButtonC.place_forget()
    def HideButtonGraph():
        storage.ButtonBa.place_forget()
class manager:
    def Start( value ):
        global button
        if ( value == -1 ):
            exit()
        if ( value < 2 ): # Run Page 1
            graph.pack_forget()
            storage.choice = value
            hide.HideButton01()
            hide.HideText01()
            show.ShowEntry(value)
            show.ShowButton02()
            show.ShowText02(value)
        elif ( value == 2 ): # Back Page 1
            show.ShowButton01()
            show.ShowText01()
            hide.HideEntry()
            hide.HideButton02()
            hide.HideText02()
            hide.HideTextWA()
#--- Start ---#
def UI():
    global GUI, graph
    GUI.title("MÔ PHỎNG CHUYỂN CÁC DẠNG CHUYỂN ĐỘNG")
    GUI.geometry("1280x680")
    GUI.configure(bg="#CDCDB4")
    GUI.resizable(width=False, height=False)
    show.ShowButton01()
    show.ShowText01()
    #manager.ShowEntry()
    GUI.mainloop()