from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import eWaste_Db_Connect
from RadioBtn import RadioButn


def start_Driver():
    global unit_RadioVariable, mainWindow, otherUnit_RadioButton
    mainWindow = Tk()
    mainWindow.title('E-Waste Management System')
    mainWindow.geometry('1050x950+180+10')

    topFrame = Frame(mainWindow)
    topFrame.pack(fill=X, side=TOP)

    topLabel = Label(topFrame, text='E-waste Management System',
                     font='MingLiU_HKSCS-ExtB 25 bold')
    topLabel.pack(fill=X, anchor=CENTER)

    ewaste_unit_frame = LabelFrame(mainWindow, text=' Unit Type ',
                                   font='MingLiU_HKSCS-ExtB 15 bold', bd=2)
    ewaste_unit_frame.pack(ipady=20, padx=40, fill=X)

    unit_RadioVariable = StringVar()
    unit_RadioVariable.set('Assorted Item')

    assorted_RadioButton = RadioButn(ewaste_unit_frame)
    assorted_RadioButton.make_radio_btn('Assorted Item', unit_RadioVariable)

    monitor_RadioButton = RadioButn(ewaste_unit_frame)
    monitor_RadioButton.make_radio_btn('Monitor', unit_RadioVariable)

    desktop_RadioButton = RadioButn(ewaste_unit_frame)
    desktop_RadioButton.make_radio_btn('Desktop', unit_RadioVariable)

    printer_RadioButton = RadioButn(ewaste_unit_frame)
    printer_RadioButton.make_radio_btn('Printer', unit_RadioVariable)

    printer_RadioButton = RadioButn(ewaste_unit_frame)
    printer_RadioButton.make_radio_btn('Router/Switch', unit_RadioVariable)

    otherUnit_RadioButton = RadioButn(ewaste_unit_frame)
    otherUnit_RadioButton.make_radio_btn(
        'Other', unit_RadioVariable, command=getUnitOther)

    ewaste_make_Frame = LabelFrame(
        mainWindow, text=' Make ', font='MingLiU_HKSCS-ExtB 15 bold', bd=2)
    ewaste_make_Frame.pack(ipady=20, padx=40, pady=20, fill=X)

    make_RadioVariable = StringVar()
    make_RadioVariable.set('Dell')

    dell_radio_button = RadioButn(ewaste_make_Frame)
    dell_radio_button.make_radio_btn('Dell', make_RadioVariable)

    hp_radio_button = RadioButn(ewaste_make_Frame)
    hp_radio_button.make_radio_btn('HP', make_RadioVariable)

    ibm_radio_button = RadioButn(ewaste_make_Frame)
    ibm_radio_button.make_radio_btn('IBM', make_RadioVariable)

    lenovo_radio_button = RadioButn(ewaste_make_Frame)
    lenovo_radio_button.make_radio_btn('Lenovo', make_RadioVariable)

    thinkPad_radio_button = RadioButn(ewaste_make_Frame)
    thinkPad_radio_button.make_radio_btn(
        'ThinkPad/ThinkCentre', make_RadioVariable)

    other_make_option = RadioButn(ewaste_make_Frame)
    other_make_option.make_radio_btn('Other', make_RadioVariable)

    mainWindow.mainloop()


def get_radio_value():
    print(unit_RadioVariable.get())


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
        otherUnit_RadioButton.name.config(
            text=unit_RadioVariable.get(), value=unit_RadioVariable.get())
        otherUnitWindow.destroy()


def exitWindow(event, window):
    window.destroy()


if __name__ == '__main__':
    start_Driver()
