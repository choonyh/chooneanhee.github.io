from tkinter import *

class ImageDemo:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Image Demo")  # Set title

        # Create PhotoImage objects
        oneImage = PhotoImage(file = "images/1.gif")
        twoImage = PhotoImage(file = "images/2.gif")
        threeImage = PhotoImage(file = "images/3.gif")
        fourImage = PhotoImage(file = "images/4.gif")
        fiveImage = PhotoImage(file = "images/5.gif")
        sixImage = PhotoImage(file = "images/6.gif")
        sevenImage = PhotoImage(file = "images/7.gif")
        eightImage = PhotoImage(file = "images/8.gif")
        nineImage = PhotoImage(file = "images/9.gif")
        tenImage = PhotoImage(file = "images/0.gif")

        # frame1 to contain Label and canvas
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, image = oneImage).pack(side = LEFT)
        canvas = Canvas(frame1)
        canvas.create_image(90, 50, image = twoImage)
        canvas["width"] = 200
        canvas["height"] = 100
        canvas.pack(side = LEFT)

        # frame2 contains buttons, check buttons, and radio buttons
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, image = threeImage).pack(side = LEFT)
        Button(frame2, image = fourImage).pack(side = LEFT)
        Checkbutton(frame2, image = fiveImage).pack(side = LEFT)
        Checkbutton(frame2, image = sixImage).pack(side = LEFT)
        Radiobutton(frame2, image = sevenImage, value = 1).pack(side = LEFT)
        Radiobutton(frame2, image = eightImage, value = 2).pack(side = LEFT)

        window.mainloop()  # Create an event loop

ImageDemo()  # Create GUI
