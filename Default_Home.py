from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox


class Default_Home:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window
        self.dashboard_window.rowconfigure(0, weight=1)
        self.dashboard_window.columnconfigure(0, weight=1)
        # 1600
        self.screen_width = self.dashboard_window.winfo_screenwidth()
        # 1
        self.screen_height = self.dashboard_window.winfo_height()
        app_width = 1540
        app_height = 800
        x = (self.screen_width/2) - (app_width/2)
        y = (self.screen_height/160) - (app_height/160)
        self.dashboard_window.geometry(
            f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        # window Icon
        icon = PhotoImage(file='images\clipart36.png')
        self.dashboard_window.iconphoto(True, icon)
        self.dashboard_window.title('Welcome')

        self.homepage = Frame(self.dashboard_window)
        self.homepage.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()
        show_frame(self.homepage)
        self.homepage.config(background='#ffffff')

        logoIcon = Image.open('images\clipart42.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(self.homepage, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(x=5, y=5)

        menuBar_line = Canvas(self.homepage, width=2800,
                              height=1.5, bg="#e6e6e6", highlightthickness=0)
        menuBar_line.place(x=0, y=90)

        # ========== HOME BUTTON =======
        self.home_button = Button(self.homepage, text='Home', bg='#fd6a36', font=("", 16, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        self.home_button.place(x=120, y=30)

        # ========== MANAGE BUTTON =======
        self.ewaste_button = Button(self.homepage, text='E-Waste', bg='#f6f6f9', font=("", 16, "bold"), bd=0, fg='#7a7a7a',
                                    cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a')
        self.ewaste_button.place(x=210, y=30)

        self.dashboard_button = Button(self.homepage, text='Dashboard', bg='#f6f6f9', font=("", 16, "bold"), bd=0, fg='#7a7a7a',
                                       cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a')
        self.dashboard_button.place(x=330, y=30)

    def closeWin(self):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if sure == True:
            # window.destroy()
            self.dashboard_window.destroy()


# def page():
#     window = Tk()
#     Default_Home(window)
#     window.mainloop()


# if __name__ == '__main__':
#     page()
