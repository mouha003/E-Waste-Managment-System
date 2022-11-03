from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import eWaste_Db_Connect


class RadioButn:
    def make_radio_btn(self, text_value, variable):
        self.name.config(text=text_value, value=text_value,
                         variable=variable, font='arial 12')
        self.name.pack(padx=25, side=LEFT)

    def make_radio_btn(self, text_value, variable, command=None):
        self.name.config(text=text_value, value=text_value,
                         variable=variable, font='arial 12', command=command)
        self.name.pack(padx=25, side=LEFT)

    def __init__(self, frame):
        self.name = Radiobutton(frame)
