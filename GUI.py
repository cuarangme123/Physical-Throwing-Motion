import time
import BackEnd
from tkinter import *
from tkinter.font import *
from tkinter.constants import *

GUI = Tk()
graph = Canvas(width=1280, height=680)
imgbg = PhotoImage(file = "background.png")
graph.create_image(0, 0, image = imgbg, anchor = NW)
#graph.create_line(160, 637.45, 1120, 637.45, width = 5 )
#graph.create_line(160, 640, 160, 42.5, width = 5 )
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
    ButtonC = button(GUI, text = "Bắt Đầu!", command = lambda: BackEnd.StartCal(storage.choiceA, storage.choiceB),
    height = 1, width = 8)  # Confirmed
    ButtonBa = button(graph, text = "Quay lại", command = lambda: manager.Start(0), 
    height = 1, width = 8)  # Back Page Graph

    BoxSpeedA = entry(GUI, width = 9)
    BoxHeightA = entry(GUI, width = 9)
    BoxAngleA = entry(GUI, width = 9)

    ###################################

    BoxSpeedB = entry(GUI, width = 9)
    BoxHeightB = entry(GUI, width = 9)
    BoxAngleB = entry(GUI, width = 9)

    TextTitle = TextUI(GUI, text = "Chọn dạng chuyển động:", height = 2, width = 40)

    TextHeightA = TextUI(GUI, text = "Nhập độ cao của vật A (m)", height = 1, width = 30)
    TextAngleA = TextUI(GUI, text = "Nhập góc ném của vật A (°)", height = 1, width = 30)
    TextSpeedA = TextUI(GUI, text = "Nhập vận tốc của vật A (m/s)", height = 1, width = 30)

    ######################################################################################

    TextHeightB = TextUI(GUI, text = "Nhập độ cao của vật B (m)", height = 1, width = 30)
    TextAngleB = TextUI(GUI, text = "Nhập góc ném của vật B (°)", height = 1, width = 30)
    TextSpeedB = TextUI(GUI, text = "Nhập vận tốc của vật B (m/s)", height = 1, width = 30)
    TextWA = TextUI(GUI, text = "Vui lòng nhập lại", height = 1, width = 30)
    Choice, choiceA, choiceB = None, None, None
#test = button(GUI, text = "Ném", command = lambda: manager.Start(0), height = 4, width = 7)
#test.place(relx = 0.5, rely = 0.25, anchor = CENTER)

class show:
    def ShowEntry( ValueA, ValueB ):
        if ( ValueA == 0 ):
            storage.BoxHeightA.place(relx = 0.5, rely = 0.15, anchor = CENTER)
            storage.BoxHeightA.delete(0, 'end')
        else:
            storage.BoxAngleA.place(relx = 0.5, rely = 0.15, anchor = CENTER)
            storage.BoxAngleA.delete(0, 'end')
        storage.BoxSpeedA.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        storage.BoxSpeedA.delete(0, 'end')
        if ( ValueB == 0 ):
            storage.BoxHeightB.place(relx = 0.5, rely = 0.55, anchor = CENTER)
            storage.BoxHeightB.delete(0, 'end')
        else:
            storage.BoxAngleB.place(relx = 0.5, rely = 0.55, anchor = CENTER)
            storage.BoxAngleB.delete(0, 'end')
        storage.BoxSpeedB.place(relx = 0.5, rely = 0.75, anchor = CENTER)
        storage.BoxSpeedB.delete(0, 'end')

    def ShowText01():
        storage.TextTitle.place(relx = 0.5, rely = 0.15, anchor = CENTER)
        storage.Choice = True

    def ShowText02( ValueA, ValueB ):
        if ( ValueA == 0 ):
            storage.TextHeightA.place(relx = 0.5, rely = 0.05, anchor = CENTER)
        else:
            storage.TextAngleA.place(relx = 0.5, rely = 0.05, anchor = CENTER)
        storage.TextSpeedA.place(relx = 0.5, rely = 0.25, anchor = CENTER)
        if ( ValueB == 0 ):
            storage.TextHeightB.place(relx = 0.5, rely = 0.45, anchor = CENTER)
        else:
            storage.TextAngleB.place(relx = 0.5, rely = 0.45, anchor = CENTER)
        storage.TextSpeedB.place(relx = 0.5, rely = 0.65, anchor = CENTER)

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
        storage.BoxHeightA.place_forget()
        storage.BoxAngleA.place_forget()
        storage.BoxSpeedA.place_forget()
        ################################
        storage.BoxHeightB.place_forget()
        storage.BoxAngleB.place_forget()
        storage.BoxSpeedB.place_forget()

    def HideText01():
        storage.TextTitle.place_forget()

    def HideText02():
        storage.TextHeightA.place_forget()
        storage.TextAngleA.place_forget()
        storage.TextSpeedA.place_forget()
        #################################
        storage.TextHeightB.place_forget()
        storage.TextAngleB.place_forget()
        storage.TextSpeedB.place_forget()

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
            if ( storage.Choice ):
                storage.choiceA = value
                storage.Choice = False
                storage.choiceB = value
                storage.Choice = None
            if ( storage.Choice == None ):
                graph.pack_forget()
                hide.HideButton01()
                hide.HideText01()
                show.ShowEntry(storage.choiceA, storage.choiceB)
                show.ShowButton02()
                show.ShowText02(storage.choiceA, storage.choiceB)
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
