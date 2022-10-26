from tkinter import *
from functools import partial
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3


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
    global main_window, ewaste_table, my_canvas, second_frame
    main_window = Tk()

    main_window.title('E-Waste Management System')
    main_window.geometry('1350x750+120+10')
    # main_window.resizable(False, False)

    # Create a topFrame to hold the topLabel "E-waste"
    top_frame = Frame(main_window)
    top_frame.pack(fill=X, side=TOP, pady=13)

    ewaste_label = Label(top_frame, text='E-waste Management System',
                         font='MingLiU_HKSCS-ExtB 25 bold')
    ewaste_label.pack(fill=X, anchor=CENTER)

# ======= Main Frame / Canvas =======
    main_frame = Frame(main_window)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1, padx=60)

    win_scroll_bar = Scrollbar(
        main_frame, orient=VERTICAL, command=my_canvas.yview)
    win_scroll_bar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=win_scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# ========== E-Waste Table Frame / Style / TreeView ================
    table_frame = Frame(second_frame)
    table_frame.pack()

    # General theme style for Ewaste table
    table_style = ttk.Style(table_frame)
    table_style.theme_use('classic')

    # Configure Table Row and Heading Colors
    table_style.configure('Treeview', bg='black',
                          rowheight=40, fieldbackground='gray', font=('arial', 12))

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

    ewasteUnitType()
    ewasteMake()
    ewasteSerialNumber()
    ewasteQty_Pallet()
    addEwasteUnits()
    updateEwasteUnits()
    delEwasteUnits()
    queryData()
    main_window.mainloop()

# Generate Ewaste Labels Form


def ewasteUnitType():
    global other_unit_option
    # Create Label for ewaste Label Frame
    ewaste_unit_Frame = LabelFrame(
        second_frame, text='Unit Type', font='MingLiU_HKSCS-ExtB 15 bold', bd=2)
    ewaste_unit_Frame.pack(ipady=20, padx=20, pady=30, fill=X)

    # Set Default value to Assorted Item
    radio_variable = StringVar()
    radio_variable.set('Assorted Item')

    # Create all Radio button and values
    assorted_radio_button = Radiobutton(
        ewaste_unit_Frame, text='Assorted Item', value='Assorted Item', variable=radio_variable, font='arial 12')

    assorted_radio_button.pack(padx=25, side=LEFT)

    monitor_radio_button = Radiobutton(
        ewaste_unit_Frame, text='Monitor', value='Monitor', variable=radio_variable, font='arial 12')

    monitor_radio_button.pack(padx=25, side=LEFT)

    desktop_radio_button = Radiobutton(
        ewaste_unit_Frame, text='Desktop',  value='Desktop', variable=radio_variable, font='arial 12')

    desktop_radio_button.pack(padx=25, side=LEFT)

    printer_radio_button = Radiobutton(
        ewaste_unit_Frame, text='Printer', value='Printer', variable=radio_variable, font='arial 12')

    printer_radio_button.pack(padx=25, side=LEFT)
    # Router Switch button
    rs_radio_button = Radiobutton(
        ewaste_unit_Frame, text='Router/Switch', value='Router_Switch', variable=radio_variable, font='arial 12')

    rs_radio_button.pack(padx=25, side=LEFT)

    other_unit_option = Radiobutton(ewaste_unit_Frame)

    other_unit_option.configure(text='Other', value='other', variable=radio_variable,
                                font='arial 12',
                                command=partial(getOtherUnit, radio_variable, other_unit_option))

    other_unit_option.pack(padx=25, side=LEFT)


def getOtherUnit(r, otherOption):
    global otherOptionWindow, otherUnitEntry, otherUnit_errorMsg
    otherOptionWindow = Toplevel(second_frame)
    otherOptionWindow.title('Other Input')
    otherOptionWindow.geometry("600x200+600+250")

    otherUnit_errorMsg = Label(
        otherOptionWindow, text='', font='arial 12', fg='red')
    otherUnit_errorMsg.pack()
    otherLabel = Label(otherOptionWindow, text='Input', font='ariel 20')
    otherLabel.pack(padx=40, side=LEFT)
    otherUnitEntry = Entry(otherOptionWindow, font='arial 15')
    otherUnitEntry.pack(side=LEFT)
    otherUnitEntry.focus()
    otherButton = Button(otherOptionWindow, text='OK',
                         font='arial 12', command=partial(exit_getOtherUnit, r, otherOption))
    otherButton.pack(padx=40, side=LEFT)

    otherOptionWindow.grab_set()
    otherOptionWindow.bind('<Return>', partial(
        exit_getOtherUnit, r, otherOption))
    otherOptionWindow.mainloop()


def exit_getOtherUnit(r, otherOption, event=None):
    if otherUnitEntry.get() == '':
        otherUnit_errorMsg.config(text='***NOTHING WAS ENTERED***')
    else:
        # radio_variable.set(otherUnitEntry.get())
        r.set(otherUnitEntry.get())
        otherOption.config(
            text=r.get(), value=r.get())
        otherOptionWindow.destroy()


def ewasteMake():
    ewaste_make_Frame = LabelFrame(
        second_frame, text='Make', font='MingLiU_HKSCS-ExtB 15 bold', bd=2)
    ewaste_make_Frame.pack(ipady=20, padx=20, pady=30, fill=X)

    # Set Default value to Assorted Item
    radio_var = StringVar()
    radio_var.set('Dell')

    # Create all Radio button and values
    dell_radio_button = Radiobutton(
        ewaste_make_Frame, text='Dell', value='Dell', variable=radio_var, font='arial 12')

    dell_radio_button.pack(padx=25, side=LEFT)

    hp_radio_button = Radiobutton(
        ewaste_make_Frame, text='HP', value='HP', variable=radio_var, font='arial 12')

    hp_radio_button.pack(padx=25, side=LEFT)

    ibm_radio_button = Radiobutton(
        ewaste_make_Frame, text='IBM', value='IBM', variable=radio_var, font='arial 12')

    ibm_radio_button.pack(padx=25, side=LEFT)

    lenovo_radio_button = Radiobutton(
        ewaste_make_Frame, text='Lenovo',  value='Lenovo', variable=radio_var, font='arial 12')

    lenovo_radio_button.pack(padx=25, side=LEFT)

    thinkPad_radio_button = Radiobutton(
        ewaste_make_Frame, text='ThinkPad/ThinkCentre', value='ThinkPad/ThinkCentre', variable=radio_var, font='arial 12')

    thinkPad_radio_button.pack(padx=25, side=LEFT)

    other_make_option = Radiobutton(ewaste_make_Frame)

    other_make_option.configure(text='Other', value='other', variable=radio_var, font='arial 12', command=partial(
        getOtherUnit, radio_var, other_make_option))
    other_make_option.pack(padx=25, side=LEFT)


def ewasteSerialNumber():
    global acessoryFrame
    # Create Label for ewaste Model/ Serial Number
    acessoryFrame = Frame(second_frame)
    acessoryFrame.pack()
    serial_number = Label(
        acessoryFrame, text='Model / Serial Number', font='MingLiU_HKSCS-ExtB 12 bold')
    serial_number.pack(padx=8, pady=30, side=LEFT)

    serial_number_entry = Entry(acessoryFrame, width=20, font=('Arial 18'))
    serial_number_entry.pack(side=LEFT)


def ewasteQty_Pallet():

    # UNIT QUANTITY LABEL AND ENTRY
    quantity_label = Label(
        acessoryFrame, text='Quantity', font='MingLiU_HKSCS-ExtB 12 bold')
    quantity_label.pack(padx=12, pady=30, side=LEFT)

    quantity_entry = Entry(acessoryFrame, width=18, font=('Arial 18'))
    quantity_entry.pack(side=LEFT)


# PALLET NUMBER LABEL & ENTRY
    pallet_number_label = Label(
        acessoryFrame, text='Pallet #', font='MingLiU_HKSCS-ExtB 12 bold')
    pallet_number_label.pack(padx=12, pady=30, side=LEFT)

    pallet_number_entry = Entry(acessoryFrame, width=18, font=('Arial 18'))
    pallet_number_entry.pack(side=LEFT)


def addEwasteUnits():
    global btn_Frame
    btn_Frame = Frame(second_frame)
    btn_Frame.pack(fill=X,)

    addBtn = Button(btn_Frame, text='ADD',
                    height=2, width=10, bg='#5fb28f', fg='white', font=('Arial 10 bold'))
    addBtn.pack(pady=30, padx=200, side='left')


def updateEwasteUnits():
    updateBtn = Button(btn_Frame, text='Update',
                       height=2, width=10, bg='#f3aa33', fg='white', font=('Arial 10 bold'))
    updateBtn.pack(pady=30, padx=10, side='left')


def delEwasteUnits():
    deleteBtn = Button(btn_Frame, text='Delete',
                       height=2, width=10, bg='#e55d5d', fg='white', font=('Arial 10 bold'))
    deleteBtn.pack(pady=30, padx=10, side='left')


def queryData():
    for i in my_data:
        if my_data.index(i) % 2 == 0:
            ewaste_table.insert('', index=0, values=i, tags='even_rows')
        else:
            ewaste_table.insert('', index=0, values=i, tags='odd_rows')


if __name__ == '__main__':
    mainDriver()
