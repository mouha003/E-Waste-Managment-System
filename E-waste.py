from select import select
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import eWaste_Db_Connect

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


def mainDriver():
    global mainWindow, my_table, unit_RadioVariable, otherUnit_RadioButton, make_RadioVariable, other_make_option, \
        pallet_number_entry, dbTable, serial_number_entry, quantity_entry, pallet_number_entry
    dbTable = 'ewaste'

    mainWindow = Tk()

    mainWindow.title('E-Waste Management System')
    mainWindow.geometry('1250x950+180+10')
    # mainWindow.resizable(False, False)
    # Create a topFrame to hold the topLabel "E-waste"
    topFrame = Frame(mainWindow)
    topFrame.pack(fill=X, side=TOP)
    # Throw topLabel inside the topFrame
    topLabel = Label(topFrame, text='E-waste Management System',
                     font='MingLiU_HKSCS-ExtB 25 bold')
    topLabel.pack(fill=X, anchor=CENTER)

    tableFrame = Frame(mainWindow)
    tableFrame.pack()

    style = ttk.Style(tableFrame)
    style.theme_use('classic')

    style.configure('Treeview', bg='#3BA4B9', fg='black',
                    rowheight=40, fieldbackground='gray', font='arial 12')
    style.configure("Treeview.Heading", background='#e55d5d',
                    foreground='white', font='arial 13 bold')
    style.map("Treeview", background=[('selected', '#6F5EA2')])

    tree_ScrollBar = Scrollbar(tableFrame, orient=VERTICAL)
    tree_ScrollBar.pack(side=RIGHT, fill=Y)

    my_table = ttk.Treeview(
        tableFrame, yscrollcommand=tree_ScrollBar.set, selectmode="extended", height=10)
    my_table.tag_configure('even', background='white')  # configure the tags
    my_table.tag_configure('odd', background='#fdf2f2')  # configure the tags

    my_table.pack(pady=10)
    tree_ScrollBar.config(command=my_table.yview)

    my_table['columns'] = ('id', 'unit', 'make',
                           'model_serial', 'item_qty', 'pallet')
    my_table.column('#0', width=0, stretch=NO)
    my_table.column('id', width=80)
    my_table.column('unit', width=150)
    my_table.column('make', width=200)
    my_table.column('model_serial', width=250)
    my_table.column('item_qty', width=450)
    my_table.column('pallet', width=120)

    my_table.heading('#0', text='', anchor=W)
    my_table.heading('id', text='  ID', anchor=W)
    my_table.heading('unit', text='  Unit', anchor=W)
    my_table.heading('make', text='  Make', anchor=W)
    my_table.heading('model_serial', text='  Model / Serial', anchor=W)
    my_table.heading('item_qty', text='  Item - Quantity', anchor=W)
    my_table.heading('pallet', text='  Pallet #', anchor=W)

    # =============================================== Unit type Frame =========================================================================================
    unitFrame = LabelFrame(mainWindow, text=' Unit Type ',
                           font='MingLiU_HKSCS-ExtB 15 bold', bd=2)
    unitFrame.pack(ipady=20, padx=40, fill=X)

    unit_RadioVariable = StringVar()
    # default Radio value to Assorted Item
    unit_RadioVariable.set('Assorted Item')

    assorted_RadioButton = Radiobutton(
        unitFrame, text='Assorted Item', value='Assorted Item', variable=unit_RadioVariable, font='arial 12')
    assorted_RadioButton.pack(padx=25, side=LEFT)

    monitor_RadioButton = Radiobutton(
        unitFrame, text='Monitor', value='Monitor', variable=unit_RadioVariable, font='arial 12')
    monitor_RadioButton.pack(padx=25, side=LEFT)
    desktop_RadioButton = Radiobutton(
        unitFrame, text='Desktop', value='Desktop', variable=unit_RadioVariable, font='arial 12')
    desktop_RadioButton.pack(padx=25, side=LEFT)
    printer_RadioButton = Radiobutton(
        unitFrame, text='Printer', value='Printer', variable=unit_RadioVariable, font='arial 12')
    printer_RadioButton.pack(padx=25, side=LEFT)
    rs_RadioButton = Radiobutton(unitFrame, text='Router/Switch', value='Router_Switch',
                                 variable=unit_RadioVariable, font='arial 12')  # Router Switch button
    rs_RadioButton.pack(padx=25, side=LEFT)
    otherUnit_RadioButton = Radiobutton(
        unitFrame, text='Other', value='other', variable=unit_RadioVariable, font='arial 12', command=getUnitOther)
    otherUnit_RadioButton.pack(padx=25, side=LEFT)
    # =============================================== Unit Type end =========================================================================================
    # =======================================================================================================================================================

    # =============================================== Make type Frame =======================================================================================
    ewaste_make_Frame = LabelFrame(
        mainWindow, text=' Make ', font='MingLiU_HKSCS-ExtB 15 bold', bd=2)
    ewaste_make_Frame.pack(ipady=20, padx=40, pady=20, fill=X)

    # Set Default value to Assorted Item
    make_RadioVariable = StringVar()
    make_RadioVariable.set('Dell')

    # Create all Radio button and values
    dell_radio_button = Radiobutton(
        ewaste_make_Frame, text='Dell', value='Dell', variable=make_RadioVariable, font='arial 12')

    dell_radio_button.pack(padx=25, side=LEFT)

    hp_radio_button = Radiobutton(
        ewaste_make_Frame, text='HP', value='HP', variable=make_RadioVariable, font='arial 12')

    hp_radio_button.pack(padx=25, side=LEFT)

    ibm_radio_button = Radiobutton(
        ewaste_make_Frame, text='IBM', value='IBM', variable=make_RadioVariable, font='arial 12')

    ibm_radio_button.pack(padx=25, side=LEFT)

    lenovo_radio_button = Radiobutton(
        ewaste_make_Frame, text='Lenovo',  value='Lenovo', variable=make_RadioVariable, font='arial 12')

    lenovo_radio_button.pack(padx=25, side=LEFT)

    thinkPad_radio_button = Radiobutton(
        ewaste_make_Frame, text='ThinkPad/ThinkCentre', value='ThinkPad/ThinkCentre', variable=make_RadioVariable, font='arial 12')

    thinkPad_radio_button.pack(padx=25, side=LEFT)

    other_make_option = Radiobutton(ewaste_make_Frame, text='Other', value='other',
                                    variable=make_RadioVariable, font='arial 12', command=getMakeOther)
    other_make_option.pack(padx=25, side=LEFT)
    # =============================================== Make end =========================================================================================
    # ==================================================================================================================================================

    bottomFrame = Frame(mainWindow)
    bottomFrame.pack()
    serial_number = Label(
        bottomFrame, text='Model / Serial Number', font='MingLiU_HKSCS-ExtB 12 bold')
    serial_number.pack(padx=8, pady=30, side=LEFT)

    serial_number_entry = Entry(bottomFrame, width=20, font=('Arial 18'))
    serial_number_entry.pack(side=LEFT)

    quantity_label = Label(bottomFrame, text='Quantity',
                           font='MingLiU_HKSCS-ExtB 12 bold')
    quantity_label.pack(padx=12, pady=30, side=LEFT)

    quantity_entry = Entry(bottomFrame, width=18, font=('Arial 18'))
    quantity_entry.pack(side=LEFT)

    pallet_number_label = Label(
        bottomFrame, text='Pallet #', font='MingLiU_HKSCS-ExtB 12 bold')
    pallet_number_label.pack(padx=12, pady=30, side=LEFT)

    pallet_number_entry = Entry(bottomFrame, width=10, font=('Arial 18'))
    pallet_number_entry.pack(side=LEFT)

    btn_Frame = Frame(mainWindow)
    btn_Frame.pack(padx=60, pady=40, anchor=W)  # padx=60, pady=40, anchor=W)

    addBtn = Button(btn_Frame, text='ADD', height=2, width=10,
                    bg='#5fb28f', fg='white', font=('Arial 10 bold'), command=add_ewaste_records)
    # addBtn.pack(side=LEFT, padx=34)
    addBtn.grid(column=0, columnspan=5, row=0, padx=100, sticky=W)

    updateBtn = Button(btn_Frame, text='Update', height=2,
                       width=10, bg='#f3aa33', fg='white', font=('Arial 10 bold'), command=update_ewaste_record)
    # updateBtn.pack(side=LEFT, padx=60)
    updateBtn.grid(column=1, columnspan=5, row=0, padx=400, sticky=W)

    deleteBtn = Button(btn_Frame, text='Delete', height=2,
                       width=10, bg='#e55d5d', fg='white', font=('Arial 10 bold'), command=delete_ewaste_record)
    # #deleteBtn.pack(side=LEFT, padx=60)
    deleteBtn.grid(column=2, columnspan=5, row=0, padx=700, sticky=W)

    editPalletNum = Button(btn_Frame, text='Edit Pallet #', height=2,
                           width=10, bg='#e55d5d', fg='white', font=('Arial 10 bold'))
    # #editPalletNum.pack(side=LEFT, padx=21)
    editPalletNum.grid(column=3, columnspan=5, row=0, padx=1120, sticky=W)

    queryData()
    mainWindow.bind("<Escape>", lambda e: exitWindow(e, mainWindow))
    my_table.bind("<Double-1>", OnDoubleClick)
    # my_table.bind("<ButtonRelease-1>", reset_record)
    mainWindow.mainloop()


def OnDoubleClick(event):
    reset_table_fields()
    item = my_table.selection()[0]
    record_values = my_table.item(item, "value")
    print(f"You Clicked on {record_values[1].strip()}.")
    unit_RadioVariable.set('Assorted Item')
    unit_RadioVariable.set(str(record_values[1].strip()))
    make_RadioVariable.set(str(record_values[2].strip()))
    serial_number_entry.insert(0, record_values[3])
    quantity_entry.insert(0, record_values[4])
    pallet_number_entry.insert(0, record_values[5])


def getUnitOther():
    global otherUnitWindow, otherUnitEntry, otherUnit_errorMsg
    otherUnitWindow = Toplevel(mainWindow)
    otherUnitWindow.title('Unit Type')
    otherUnitWindow.geometry("600x200+600+250")

    otherUnit_errorMsg = Label(
        otherUnitWindow, text='', font='arial 25', fg='red')
    otherUnit_errorMsg.pack()
    otherLabel = Label(otherUnitWindow, text='Unit Type', font='arial 20')
    otherLabel.pack(padx=40, side=LEFT)
    otherUnitEntry = Entry(otherUnitWindow, font='arial 12')
    otherUnitEntry.pack(side=LEFT)
    otherUnitEntry.focus()
    okButton = Button(otherUnitWindow, text='OK',
                      font='arial 15', command=exit_getOtherUnit)
    okButton.pack(padx=40, side=LEFT)

    otherUnitWindow.grab_set()
    otherUnitWindow.bind('<Return>', lambda e: exit_getOtherUnit())
    otherUnitWindow.bind('<Escape>', lambda e: exitWindow(e, otherUnitWindow))
    otherUnitWindow.mainloop()


def exit_getOtherUnit():
    if otherUnitEntry.get() == '':
        otherUnit_errorMsg.config(text='NOTHING WAS ENTERED')
    else:
        unit_RadioVariable.set(otherUnitEntry.get())
        otherUnit_RadioButton.config(
            text=unit_RadioVariable.get(), value=unit_RadioVariable.get())
        otherUnitWindow.destroy()


def getMakeOther():
    global otherMakeWindow, otherMakeEntry, otherMake_errorMsg
    otherMakeWindow = Toplevel(mainWindow)
    otherMakeWindow.title('Make')
    otherMakeWindow.geometry("600x200+600+250")

    otherMake_errorMsg = Label(
        otherMakeWindow, text='', font='arial 25', fg='red')
    otherMake_errorMsg.pack()
    otherLabel = Label(otherMakeWindow, text='Make', font='arial 20')
    otherLabel.pack(padx=40, side=LEFT)
    otherMakeEntry = Entry(otherMakeWindow, font='arial 12')
    otherMakeEntry.pack(side=LEFT)
    otherMakeEntry.focus()
    okButton = Button(otherMakeWindow, text='OK',
                      font='arial 15', command=exit_getOtherMake)
    okButton.pack(padx=40, side=LEFT)

    otherMakeWindow.grab_set()
    otherMakeWindow.bind('<Return>', lambda e: exit_getOtherMake())
    otherMakeWindow.bind('<Escape>', lambda e: exitWindow(e, otherMakeWindow))
    otherMakeWindow.mainloop()


def exit_getOtherMake():
    if otherMakeEntry.get() == '':
        otherMake_errorMsg.config(text='NOTHING WAS ENTERED')
    else:
        make_RadioVariable.set(otherMakeEntry.get())
        other_make_option.config(
            text=make_RadioVariable.get(), value=unit_RadioVariable.get())
        otherMakeWindow.destroy()


def exitWindow(event, window):
    window.destroy()


def reset_table_fields():
    unit_RadioVariable.set('Assorted Item'),
    make_RadioVariable.set('Dell'),
    serial_number_entry.delete(0, 'end'),
    quantity_entry.delete(0, 'end'),
    pallet_number_entry.delete(0, 'end')
    my_table.focus()
    serial_number_entry.focus()


def add_ewaste_records():
    eWaste_Db_Connect.connectDB(dbTable)
    cur = eWaste_Db_Connect.myCursor.execute(
        'INSERT INTO ewaste (unit, make, model_serial, item_qty, pallet) VALUES(" % s"," % s"," % s"," % s"," % s");'
        % (unit_RadioVariable.get(), make_RadioVariable.get(), serial_number_entry.get(), quantity_entry.get(), pallet_number_entry.get()))

    rowID = cur.lastrowid

    sql = f"SELECT * FROM ewaste where id = {rowID}"
    fetchResult = eWaste_Db_Connect.myCursor.execute(sql).fetchall()

    if (rowID-1) % 2 == 0:
        my_table.insert('', 0, values=fetchResult[0], tags='even')
    else:
        my_table.insert('', 0, values=fetchResult[0], tags='odd')

    reset_table_fields()

    eWaste_Db_Connect.commitCloseDb()


def delete_ewaste_record():
    messageDelete = messagebox.askyesno(
        "Delete", "Do you want to permanently delete this record?")
    if messageDelete > 0:
        eWaste_Db_Connect.connectDB(dbTable)
        cur = eWaste_Db_Connect.myCursor
        for selected_data in my_table.selection():
            selected_data_ID = my_table.set(selected_data, 'id')
            my_table.delete(selected_data)
            deleted_recored = cur.execute(
                f"Delete From ewaste where id={selected_data_ID}")
    print("item has been Deleted")
    eWaste_Db_Connect.commitCloseDb()


def update_ewaste_record():
    selected = my_table.selection()[0]
    record_value = my_table.item(selected, "value")
    print(record_value)

    messageUpdate = messagebox.askyesno(
        "Update", "Are you sure you want to update this record?")

    if messageUpdate > 0:

        eWaste_Db_Connect.connectDB(dbTable)
        update_query = """ Update ewaste SET unit=?, make=?, model_serial=?, item_qty=?, pallet=? WHERE id = ? """
        columValues = (unit_RadioVariable.get(), make_RadioVariable.get(
        ), serial_number_entry.get(), quantity_entry.get(), pallet_number_entry.get(), record_value[0])
        print(columValues)
        my_table.item(selected, text="", values=(record_value[0], unit_RadioVariable.get(), make_RadioVariable.get(
        ), serial_number_entry.get(), quantity_entry.get(), pallet_number_entry.get()))

        eWaste_Db_Connect.myCursor.execute(update_query, columValues)
        # cur.execute(
        #     f"Update ewase SET unit ={unit_RadioVariable.get()}, make = {make_RadioVariable.get()}, model_serial = {serial_number_entry.get()},item_qty = {quantity_entry.get()}, pallet = {pallet_number_entry.get()} WHERE id = {record_value[0]}",)

    reset_table_fields()
    eWaste_Db_Connect.commitCloseDb()


def queryData():
    global currentPallet

    eWaste_Db_Connect.connectDB(dbTable)

    myData_From_DB = eWaste_Db_Connect.myCursor.execute(
        'SELECT * FROM ewaste;').fetchall()

    for record in myData_From_DB:
        if myData_From_DB.index(record) % 2 == 0:
            my_table.insert('', index=0, values=record, tags='even')
        else:
            my_table.insert('', index=0, values=record, tags='odd')

    # Read config.txt file and grab the current Pallet value
    with open(r"C:\Users\Mouhari Mouhamed\Downloads\E-Waste\config.txt", 'r') as r:
        currentPallet = "     "+r.readline()

    pallet_number_entry.insert(0, currentPallet)
    pallet_number_entry.config(state=DISABLED)


if __name__ == '__main__':
    mainDriver()
