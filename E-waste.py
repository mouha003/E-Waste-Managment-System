
from asyncio import events
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3
from tkinter import font
from turtle import title
# import dbconnection

my_data = [
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

#  #e55d5d #dark pink
# fdf2f2  # light pink
# efefef  # green
# f3aa33  # yellow


def mainDriver():
    global main_window, ewaste_table
    main_window = Tk()

    main_window.title('E-Waste Management System')
    main_window.geometry('1350x750+120+10')
    main_window.resizable(False, False)

    # Create a topFrame to hold the topLabel "E-waste"
    top_frame = Frame(main_window)
    top_frame.pack(fill=X, side=TOP, pady=13)

    ewaste_label = Label(top_frame, text='E-waste Management System',
                         font='MingLiU_HKSCS-ExtB 25 bold')
    ewaste_label.pack(fill=X, anchor=CENTER)


# ========== E-Waste Table Frame / Style / TreeView ================
    table_frame = Frame(main_window)
    table_frame.pack()

    # General theme style for Ewaste table
    table_style = ttk.Style(table_frame)
    table_style.theme_use('classic')

    # Configure Table Row and Heading Colors
    table_style.configure('Treeview', bg='black',
                          rowheight=40, fieldbackground='gray', font=('ariel', 12))

    table_style.configure('Treeview.Heading', background='#e55d5d', rowheight=40, foreground='white',
                          font=("timesnewroman", 13, "bold"))

    table_style.map("Treeview", background=[('selected', '#f3aa33')])

    # add scroll bar ro table Direction:Y-axis
    table_scroll_bar = Scrollbar(table_frame, orient=VERTICAL)
    table_scroll_bar.pack(side=RIGHT, fill=Y, )

    # Add TreeView in table frame
    ewaste_table = ttk.Treeview(
        table_frame, yscrollcommand=table_scroll_bar.set, selectmode='extended', height=10)

    # Configure Stripped Rows
    ewaste_table.tag_configure('even_rows', background='white')
    ewaste_table.tag_configure('odd_rows', background='#fdf2f2')

    ewaste_table.pack()
    # configure the scroll on ewaste table
    table_scroll_bar.config(command=ewaste_table.yview)
    # Define Ewaste Table Columns
    ewaste_table['columns'] = (
        'unit', 'make', 'model_serial', 'pallet', 'item_qty')
    ewaste_table.column('#0', width=0, stretch=NO)
    ewaste_table.column('unit', width=200)
    ewaste_table.column('make', width=250)
    ewaste_table.column('model_serial', width=250)
    ewaste_table.column('pallet', width=150)
    ewaste_table.column('item_qty', width=350)

    # map heading data with text
    ewaste_table.heading('#0', text='', anchor=W)
    ewaste_table.heading('unit', text=' Unit', anchor=W)
    ewaste_table.heading('make', text=' Make', anchor=W)
    ewaste_table.heading('model_serial', text=' Model / Serial')
    ewaste_table.heading('pallet', text=' Pallet #', anchor=W)
    ewaste_table.heading('item_qty', text=' Item-Qty', anchor=W)

    queryData()
    # ewaste_Form()
    main_window.mainloop()

# # Generate Ewaste Labels Form


# def ewasteForm():
#     ewaste_unit_Frame = LabelFrame(main_window)
#     ewaste_unit_Frame.pack(ipady=20, padx=20)


def queryData():
    for i in my_data:
        if my_data.index(i) % 2 == 0:
            ewaste_table.insert('', index=0, values=i, tags='even_rows')
        else:
            ewaste_table.insert('', index=0, values=i, tags='odd_rows')


if __name__ == '__main__':
    mainDriver()
