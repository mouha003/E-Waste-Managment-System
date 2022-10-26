from calendar import leapdays
from cgitb import text
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3
from tkinter import font
# import dbconnection

myData = [
    ("Monitor", "Dell", "9f7ds8f", "00", 50),
    ("Assorted Item", "IBM", "9f7ds0f", "01", 51),
    ("Desktop", "Lenovo", "9f7ds1f", "02", 52),
    ("Printer", "ThinkPad/ThinkCentre", "9f7ds2f", "03", 53),
    ("Router/Switch", "N/A", "9f7ds3f", "04", 54),
    ("Monitor", "Dell", "9f7ds8f", "05", 50),
    ("Assorted Item", "IBM", "9f7ds0f", "06", 51),
    ("Desktop", "Lenovo", "9f7ds1f", "07", 52),
    ("Printer", "ThinkPad/ThinkCentre", "9f7ds2f", "08", 53),
    ("Router/Switch", "N/A", "9f7ds3f", "09", 54),
    ("Monitor", "Dell", "9f7ds8f", "10", 50),
    ("Assorted Item", "IBM", "9f7ds0f", "11", 51),
    ("Desktop", "Lenovo", "9f7ds1f", "12", 52),
    ("Printer", "ThinkPad/ThinkCentre", "9f7ds2f", "13", 53),
    ("Router/Switch", "N/A", "9f7ds3f", "14", 54)
]


def mainDriver():

    mainWindow = Tk()

    mainWindow.title('E-Waste Management System')
    mainWindow.geometry('1350x750+200+10')
    mainWindow.resizable(False, False)
    # Create a topFrame to hold the topLabel "E-waste"
    topFrame = Frame(mainWindow)
    topFrame.pack(fill=X, side=TOP, pady=13)

    ewasteLabel = Label(topFrame, text='E-waste Management System',
                        font='MingLiU_HKSCS-ExtB 25 bold')
    ewasteLabel.pack()

    mainWindow.mainloop()


if __name__ == '__main__':
    mainDriver()
