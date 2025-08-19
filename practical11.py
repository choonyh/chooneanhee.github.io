from tkinter import *

class widgetTest:
    def __init__(self):
        window = Tk()
        window.title("Widget Test")

        frame1 = Frame(window)
        frame1.pack()

        #create a variable for two value
        self.var1 = IntVar()
        self.var2 = StringVar()

        #create checkbox buttons and add them to the frame1
        cbxBold = Checkbutton(frame1, text="Bold", variable = self.var1, command = self.processCheckButton)

        #create radio buttons and add them to the frame1
        rbred = Radiobutton(frame1, text="Red", bg = "Red",  value = "Red", variable = self.var2, command = self.processRadioButton)
        rbyel = Radiobutton(frame1, text="Yellow", bg = "Yellow", value = "Yellow", variable = self.var2, command = self.processRadioButton)

        #organize the checkbox and radio buttons in frame1 using grid mmanager
        cbxBold.grid(row = 1, column = 1)
        rbred.grid(row = 1, column = 2)
        rbyel.grid(row = 1, column = 3)

        #create label, an entry and a button, next add to the frame2
        frame2 = Frame(window)
        frame2.pack()

        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btName = Button(frame2, text = "Submit")

        #organize the label,  text entry and button to the window using grid manager
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btName.grid(row = 1, column = 3)

        #output text
        text = Text(window)
        text.pack()
        text.insert(END, "This is a text widget")
        text.insert(END, "You can enter text here")

       

        #create window amd event loop
        window.mainloop()
    #process
    def processCheckButton(self):
        print("The check box has been ticked" + (" checked" if self.var1.get() == 1 else " unchecked"))

    def processRadioButton(self):
        print("The radio button has been selected with value: " + self.var2.get())

#creatw an gui
widgetTest()