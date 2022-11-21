from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
from Default_Home import *


class Dashboard(Default_Home):
    def __init__(self, windows):
        super().__init__(windows)

        home_bgImg = Image.open('images\\clipart36.png')

        # photo = ImageTk.PhotoImage(home_bgImg.resize((1050, 610)))
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(windows, image=photo, bg='#ffffff')
        home_bg.image = photo
        home_bg.place(relx=0.350, rely=0.200)

        heading = Label(windows, text='Manage and Track your E-Waste ',
                        bg='#e6eef1', fg='#ff6c38', font=("yu gothic ui", 39, "italic"))
        heading.place(relx=0.250, rely=0.112)

        footer = Label(windows, text='© E-WASTE MANAGEMENT SYSTEM',
                       bg='#e6eef1', fg='#ff6c38', font=("yu gothic ui", 16, "bold"))
        footer.place(relx=0.670, rely=0.960)


def page():
    window = Tk()
    dashboard = Dashboard(window)
    window.mainloop()


if __name__ == '__main__':
    page()
