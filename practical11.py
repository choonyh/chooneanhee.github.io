from tkinter import *

class widgetTest:
    def __init__(self):
        window = Tk()
        window.title("Widget Test")

        frame1 = Frame(window)
        frame1.pack()

        #create checkbox buttons and add them to the frame1
        cbxBold = Checkbutton(frame1, text="Bold")

        #create radio buttons and add them to the frame1
        rbred = Radiobutton(frame1, text="Red")
        rbyel = Radiobutton(frame1, text="Yellow")

        #organize the checkbox and radio buttons in frame1
        cbxBold.grid(row = 1, column = 1)
        rbred.grid(row = 1, column = 2)
        rbyel.grid(row = 1, column = 3)

widgetTest()