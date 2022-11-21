from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
from Default_Home import *
import Ewaste


class HomePage(Default_Home):
    def __init__(self, windows):
        self.windows = windows
        super().__init__(self.windows)

        home_bgImg = Image.open('images\\clipart36.png')

        # photo = ImageTk.PhotoImage(home_bgImg.resize((1050, 610)))
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(self.windows, image=photo, bg='#ffffff')
        home_bg.image = photo
        home_bg.place(relx=0.380, rely=0.300)

        heading = Label(self.windows, text='Manage and Track your E-Waste ',
                        bg='#e6eef1', fg='#ff6c38', font=("yu gothic ui", 39, "italic"))
        heading.place(relx=0.250, rely=0.112)

        footer = Label(self.windows, text='© E-WASTE MANAGEMENT SYSTEM',
                       bg='#e6eef1', fg='#ff6c38', font=("yu gothic ui", 16, "bold"))
        footer.place(relx=0.670, rely=0.960)

        # self.home_button.configure(command=lambda: self.home())
        self.ewaste_button.configure(
            bg='#f6f6f9', fg='#7a7a7a', command=lambda: self.ewaste())
        self.windows.protocol("WM_DELETE_WINDOW", self.closeWin)

    def closeWin(self):
        # sure = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        # if sure == True:
        #     # window.destroy()
        #     self.windows.destroy()
        super().closeWin()

    def home(self):
        win = Toplevel()
        HomePage(win)
        self.dashboard_window.withdraw()
        win.deiconify()

    def ewaste(self):
        win = Toplevel()
        Ewaste.EWaste(win)
        self.dashboard_window.withdraw()
        self.ewaste_button.configure(bg='#fd6a36', fg='white')
        self.dashboard_window.title("E-Waste Mangement System")
        self.homepage.configure(background='#f6f6f9')
        win.deiconify()


def page():
    global window
    window = Tk()
    homePage = HomePage(window)

    window.mainloop()


if __name__ == '__main__':
    page()
