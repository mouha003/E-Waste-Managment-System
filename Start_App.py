

from tkinter import *
from tkinter.ttk import Progressbar
import sys
import os


root = Tk()
image = PhotoImage(file="images\\clipart36.png")
height = 430
width = 530


x = (root.winfo_screenwidth()//2) - (width//2)
y = (root.winfo_screenheight()//2) - (height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)


root.wm_attributes('-topmost', True)
root.config(background='#fd6a36')


welcome_label = Label(text='E-WASTE MANGEMENT SYSTEM',
                      bg='#fd6a36', font=("yu gothic ui", 18, "bold"), fg='black')

welcome_label.place(x=90, y=25)

bg_label = Label(root, image=image, bg='#fd6a36')
bg_label.place(x=80, y=55)

progress_label = Label(root, text='Please Wait...',
                       font=('yu gothic ui', 13, 'bold'), fg='black')
progress_label.place(x=210, y=355)


progress = Progressbar(root, orient=HORIZONTAL,
                       length=500, mode='determinate')
progress.place(x=15, y=390)

exit_btn = Button(text='x', bg='#fd6a36', command=lambda: exit_window(
), bd=0, font=("yu gothic ui", 16, "bold"), activebackground='#fd6a36')

exit_btn.place(x=499, y=0)


def exit_window():
    sys.exit(root.destroy())


def top():
    root.withdraw()
    os.system("python Home_Page.py")
    root.destroy()


i = 0


def load():
    global i
    if i <= 10:
        txt = 'Please Wait...  ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(300, load)
        progress['value'] = 10*i
        i += 1
    else:
        top()


load()


root.mainloop()
