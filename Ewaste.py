from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter import scrolledtext as tkst
from PIL import ImageTk, Image
import Home_Page
from Default_Home import *
from Home_Page import *
import sqlite3
import eWaste_Db_Connect
import csv
import pandas as pd


class EWaste(Default_Home):
    def __init__(self, windows):
        self.windows = windows
        super().__init__(self.windows)
        global dbTable, dbName
        dbTable = 'ewaste'
        dbName = 'Inventory.db'
        self.export_to_xls = Button(self.windows, text='Export File', bg='#f6f6f9', font=("", 16, "bold"), bd=0, fg='#7a7a7a',
                                    cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a', command=lambda: csv_file())
        self.export_to_xls.place(x=330, y=30)

        coverFrame = Frame(self.windows, bg='#ffffff')
        coverFrame.place(x=400, y=100, width=1055, height=630)
        topFrame = LabelFrame(coverFrame, bg='#f1f1f1', bd='2.4')
        topFrame.place(x=70, y=20, width=897, height=40)
        title = Label(topFrame, text='E-WASTE MANAGEMENT SYSTEM', font=("yu gothic ui", 13, "bold"),
                      fg='#ff6c38')
        title.place(x=300, y=3)

        coverFrame2 = Frame(self.windows, bg='#ffffff')
        coverFrame2.place(x=0, y=100, width=390, height=630)

        manageEwaste = Label(coverFrame2, text='MANAGE E-WASTE', font=("yu gothic ui", 13, "bold"), bg='#ffffff',
                             fg='#ff6c38')
        manageEwaste.place(x=115, y=0)

        coverFrame3 = LabelFrame(coverFrame2, bg='#ffffff', bd='2.4')
        coverFrame3.place(x=10, y=35, width=370, height=580)

        unitFrame = Label(coverFrame3, text=' Unit Type ',
                          font=('yu gothic ui', 14, "bold"), bg="#ffffff", bd=1)
        unitFrame.place(x=5, y=21)
# =======================================================================================================================
        serial_num = StringVar()
        quantity = StringVar()
        pallet = StringVar()
        unit_RadioVariable = StringVar()
        # default Radio value to Assorted Item
        unit_RadioVariable.set('Assorted Item')

        assorted_RadioButton = Radiobutton(coverFrame3, text='Assorted Item', value='Assorted Item', bg="#ffffff",
                                           variable=unit_RadioVariable, font='arial 12')
        assorted_RadioButton.place(x=20, y=50)

        monitor_RadioButton = Radiobutton(
            coverFrame3, text='Monitor', value='Monitor', bg="#ffffff", variable=unit_RadioVariable, font='arial 12')
        monitor_RadioButton.place(x=155, y=50)

        desktop_RadioButton = Radiobutton(
            coverFrame3, text='Desktop', value='Desktop', bg="#ffffff", variable=unit_RadioVariable, font='arial 12')
        desktop_RadioButton.place(x=245, y=50)

        printer_RadioButton = Radiobutton(
            coverFrame3, text='Printer', value='Printer', bg="#ffffff", variable=unit_RadioVariable, font='arial 12')
        printer_RadioButton.place(x=20, y=80)

        rs_RadioButton = Radiobutton(
            coverFrame3, text='Router/Switch', value='Router/Switch', bg="#ffffff", variable=unit_RadioVariable, font='arial 12')
        rs_RadioButton.place(x=110, y=80)

        otherUnit_RadioButton = Radiobutton(
            coverFrame3, text='Other', value='other', bg="#ffffff", variable=unit_RadioVariable, font='arial 12', command=lambda: otherOptionEntry('Unit Type', unit_RadioVariable, otherUnit_RadioButton))
        otherUnit_RadioButton.place(x=250, y=80)
        style = ttk.Style()
        style.configure('TButton', bg='skyblue', fg='white')
# =======================================================================================================================

        makeFrame = Label(coverFrame3, text='Make',
                          font=('yu gothic ui', 14, "bold"), bg="#ffffff", bd=1)
        makeFrame.place(x=5, y=120)

        make_RadioVariable = StringVar()
        # default Radio value to Assorted Item
        make_RadioVariable.set('Dell')

        dell_radio_button = Radiobutton(coverFrame3, text='Dell', value='Dell', bg="#ffffff",
                                        variable=make_RadioVariable, font='arial 12')
        dell_radio_button.place(x=20, y=150)

        hp_radio_button = Radiobutton(coverFrame3, text='HP', value='HP', bg="#ffffff",
                                      variable=make_RadioVariable, font='arial 12')
        hp_radio_button.place(x=90, y=150)

        ibm_radio_button = Radiobutton(
            coverFrame3, text='IBM', value='IBM', bg="#ffffff", variable=make_RadioVariable, font='arial 12')
        ibm_radio_button.place(x=160, y=150)

        lenovo_radio_button = Radiobutton(
            coverFrame3, text='Lenovo', value='Lenovo', bg="#ffffff", variable=make_RadioVariable, font='arial 12')
        lenovo_radio_button.place(x=230, y=150)

        thinkPad_radio_button = Radiobutton(
            coverFrame3, text='ThinkPad/ThinkCentre', value='ThinkPad/ThinkCentre', bg="#ffffff", variable=make_RadioVariable, font='arial 12')
        thinkPad_radio_button.place(x=20, y=180)

        other_make_option = Radiobutton(
            coverFrame3, text='Other', value='other', bg="#ffffff", variable=make_RadioVariable, font='arial 12', command=lambda: otherOptionEntry('Make', make_RadioVariable, other_make_option))
        other_make_option.place(x=220, y=180)
# =======================================================================================================================

        serial_number = Label(
            coverFrame3, text="Model/Serial #", bg='#ffffff', font=("yu gothic ui", 14, "bold"))
        serial_number.place(x=60, y=220)

        serial_number_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                    textvariable=serial_num, font=("", 12, 'bold'))
        serial_number_entry.place(x=10, y=250, width=225, height=34)
        serial_number_entry.config(
            highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # IN STOCK AND ENTRY
        quantity_label = Label(coverFrame3, text="Quantity", bg='#ffffff', font=(
            "yu gothic ui", 14, "bold"))
        quantity_label.place(x=80, y=300)

        quantity_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                               textvariable=quantity, font=("", 12, 'bold'))
        quantity_entry.place(x=10, y=330, width=225, height=34)
        quantity_entry.config(
            highlightbackground="#6b6a69", highlightcolor="#ff6c38")

        # PRICE AND ENTRY
        pallet_number_label = Label(coverFrame3, text="Pallet #", bg='#ffffff', font=(
            "yu gothic ui", 14, "bold"))
        pallet_number_label.place(x=90, y=370)

        pallet_number_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                    textvariable=pallet, font=("", 12, 'bold'))
        pallet_number_entry.place(x=80, y=400, width=100, height=34)
        pallet_number_entry.config(
            highlightbackground="#6b6a69", highlightcolor="#ff6c38")
# =======================================================================================================================

        def csv_file():
            try:
                query = " Select * from ewaste"
                my_conn = sqlite3.connect(dbName)
                df = pd.read_sql(query, my_conn, index_col='id')
                # print(df.head(2))
                file = filedialog.asksaveasfilename(initialdir=os.getcwd(
                ), title="Save CSV", filetypes=(("CSV File", "*xlsx"), ("All Files")), defaultextension=".xlsx")

                df.to_excel(file)
            except:
                print("Unexpected Errow Has Occured!!!")
            messagebox.showinfo("Message", "Export Completed")

        def otherOptionEntry(title, value, newVal):
            global otherMakeWindow, otherMakeEntry, otherMake_errorMsg
            otherMakeWindow = Toplevel(self.windows)
            otherMakeWindow.title(title)
            otherMakeWindow.geometry("600x200+600+250")
            otherMake_errorMsg = Label(
                otherMakeWindow, text='', font='arial 25', fg='red')
            otherMake_errorMsg.pack()
            otherLabel = Label(otherMakeWindow, text=title, font='arial 20')
            otherLabel.pack(padx=40, side=LEFT)
            otherMakeEntry = Entry(otherMakeWindow, font='arial 12')
            otherMakeEntry.pack(side=LEFT)
            otherMakeEntry.focus()
            okButton = Button(otherMakeWindow, text='OK',
                              font='arial 15', command=lambda: exit_getOtherMake(value, newVal))
            okButton.pack(padx=40, side=LEFT)

            otherMakeWindow.grab_set()
            otherMakeWindow.bind(
                '<Return>', lambda e: exit_getOtherMake(value, newVal))
            otherMakeWindow.bind(
                '<Escape>', lambda e: exitWindow(e, otherMakeWindow))
            otherMakeWindow.mainloop()

        def exit_getOtherMake(value, newVal):
            if otherMakeEntry.get() == '':
                otherMake_errorMsg.config(text='NOTHING WAS ENTERED')
            else:
                value.set(otherMakeEntry.get())
                newVal.config(
                    text=value.get(), value=value.get())
                otherMakeWindow.destroy()

        def exitWindow(event, window):
            window.destroy()

        def refresh():
            clear_all()
            reset_TreeView_Display()
            queryData()
            focus_cursor_toTop()

        def reset_TreeView_Display():
            for record in my_table.get_children():
                my_table.delete(record)

        def focus_cursor_toTop():
            if len(my_table.get_children()) > 0:
                child_id = my_table.get_children()[0]
                # print(child_id + ' ----- HERE')
                my_table.focus(child_id)
                my_table.selection_set(child_id)
                my_table.see(child_id)

        def queryData():
            # global currentPallet
            eWaste_Db_Connect.connectDB(dbName, dbTable)
            myData_From_DB = eWaste_Db_Connect.myCursor.execute(
                'SELECT * FROM ewaste;').fetchall()
            reset_TreeView_Display()
            if len(myData_From_DB) != 0:
                my_table.delete(*my_table.get_children())
                for row in myData_From_DB:
                    if myData_From_DB.index(row) % 2 == 0:
                        my_table.insert(
                            '', index=0, values=row, tags='even')
                    else:
                        my_table.insert(
                            '', index=0, values=row, tags='odd')
                get_default_pallet()
                eWaste_Db_Connect.commitCloseDb()
# =======================================================================================================================

        self.home_button.configure(
            bg='#f6f6f9', fg='#7a7a7a', command=lambda: self.home())
        self.windows.protocol("WM_DELETE_WINDOW", self.closeWin)
# =======================================================================================================================
        self.deleteBtn = Button(coverFrame3)
        self.deleteBtn.place(relx=0.539, rely=0.849, width=86, height=25)
        self.deleteBtn.configure(relief="flat")
        self.deleteBtn.configure(overrelief="flat")
        self.deleteBtn.configure(activebackground="#fd6a36")
        self.deleteBtn.configure(cursor="hand2")
        self.deleteBtn.configure(foreground="#ffffff")
        self.deleteBtn.configure(background="#fd6a36")
        self.deleteBtn.configure(
            font="-family {Poppins SemiBold} -size 10")
        self.deleteBtn.configure(borderwidth="0")
        self.deleteBtn.configure(text="""Delete""")
        self.deleteBtn.configure(command=lambda: delete_ewaste_record())
# =======================================================================================================================

        self.addBtn = Button(coverFrame3)
        self.addBtn.place(relx=0.059, rely=0.849, width=84, height=25)
        self.addBtn.configure(relief="flat")
        self.addBtn.configure(overrelief="flat")
        self.addBtn.configure(activebackground="#fd6a36")
        self.addBtn.configure(cursor="hand2")
        self.addBtn.configure(foreground="#ffffff")
        self.addBtn.configure(background="#fd6a36")
        self.addBtn.configure(
            font="-family {Poppins SemiBold} -size 10")
        self.addBtn.configure(borderwidth="0")
        self.addBtn.configure(text="""Add""")
        self.addBtn.configure(command=lambda: add_ewaste_records())
# =======================================================================================================================

        self.updateBtn = Button(coverFrame3)
        self.updateBtn.place(relx=0.059, rely=0.929, width=86, height=25)
        self.updateBtn.configure(relief="flat")
        self.updateBtn.configure(overrelief="flat")
        self.updateBtn.configure(activebackground="#fd6a36")
        self.updateBtn.configure(cursor="hand2")
        self.updateBtn.configure(foreground="#ffffff")
        self.updateBtn.configure(background="#fd6a36")
        self.updateBtn.configure(
            font="-family {Poppins SemiBold} -size 10")
        self.updateBtn.configure(borderwidth="0")
        self.updateBtn.configure(text="""Update""")
        self.updateBtn.configure(command=lambda: update_pallet())
# =======================================================================================================================

        def reset_TreeView_Display():
            for record in my_table.get_children():
                my_table.delete(record)

        def clear_all():
            unit_RadioVariable.set('Assorted Item'),
            make_RadioVariable.set('Dell'),
            serial_number_entry.delete(0, 'end'),
            quantity_entry.delete(0, 'end'),
            pallet_number_entry.delete(0, 'end')
            serial_number_entry.focus()

        self.clearBtn = Button(coverFrame3)
        self.clearBtn.place(relx=0.539, rely=0.929, width=86, height=25)
        self.clearBtn.configure(relief="flat")
        self.clearBtn.configure(overrelief="flat")
        self.clearBtn.configure(activebackground="#fd6a36")
        self.clearBtn.configure(cursor="hand2")
        self.clearBtn.configure(foreground="#ffffff")
        self.clearBtn.configure(background="#fd6a36")
        self.clearBtn.configure(
            font="-family {Poppins SemiBold} -size 10")
        self.clearBtn.configure(borderwidth="0")
        self.clearBtn.configure(text="""Clear""")
        self.clearBtn.configure(command=clear_all)
# =======================================================================================================================

        def add_ewaste_records():
            try:
                eWaste_Db_Connect.connectDB(dbName, dbTable)
                eWaste_Db_Connect.myCursor.execute(
                    'INSERT INTO ewaste (unit, make, model_serial, item_qty, pallet) VALUES(" % s"," % s"," % s"," % s"," % s");'
                    % (unit_RadioVariable.get(), make_RadioVariable.get(), serial_number_entry.get(), quantity_entry.get(), pallet_number_entry.get().strip()))

                with open(r"config.txt", 'w') as r:
                    r.write(pallet_number_entry.get())

                eWaste_Db_Connect.commitCloseDb()
                focus_cursor_toTop()
                refresh()
                reset_other_option()
            except:
                print("ERROR ADDING")

        def delete_ewaste_record():
            messageDelete = messagebox.askyesno(
                "Delete", "Do you want to permanently delete this record?")
            if messageDelete:
                eWaste_Db_Connect.connectDB(dbName, dbTable)
                cur = eWaste_Db_Connect.myCursor

                # Using a for loop so multiple selection can be deleted within the application
                for selected_data in my_table.selection():
                    selected_data_ID = my_table.set(selected_data, 'id')
                    cur.execute(
                        f"Delete From ewaste where id={selected_data_ID};")
                    print(" -- DATA DELETED --")

                sortID()
            eWaste_Db_Connect.commitCloseDb()
            refresh()

        def reset_other_option():
            other_make_option.configure(text='Other', value='Other')
            otherUnit_RadioButton.configure(text='Other', value='Other')

        def sortID():
            currentIDs = eWaste_Db_Connect.myCursor.execute(
                "SELECT id FROM ewaste").fetchall()
            for i in range(len(eWaste_Db_Connect.myCursor.execute("SELECT ID FROM ewaste").fetchall())):
                # eWaste_Db_Connect.myCursor.execute(f"UPDATE ewaste SET unit=123466789 WHERE id=2;")
                eWaste_Db_Connect.myCursor.execute(
                    "UPDATE ewaste SET id=%d WHERE id=%d;" % (i+1, currentIDs[i][0]))  # --> (1,)

        def edit_pallet():
            # pallet_number_entry.config(state='normal')
            global editPalletEntry, editPallet_errorMsg, editPallettWindow
            editPallettWindow = Toplevel(self.windows)
            editPallettWindow.title('Edit Pallet #')
            editPallettWindow.geometry("600x200+600+250")

            editPallet_errorMsg = Label(
                editPallettWindow, text='', font='arial 15', fg='red')
            editPallet_errorMsg.pack()

            editPalletLabel = Label(
                editPallettWindow, text='Pallet #', font='arial 20')

            editPalletLabel.pack(padx=40, side=LEFT)
            editPalletEntry = Entry(editPallettWindow, font='arial 12')
            editPalletEntry.pack(side=LEFT)
            editPalletEntry.focus()
            okButton = Button(editPallettWindow, text='Save',
                              font='arial 15', command=exit_pallet)
            okButton.pack(padx=40, side=LEFT)
            editPallettWindow.bind('<Return>', lambda e: exit_pallet())

        def update_pallet():
            selected = my_table.selection()
            record_value = my_table.item(selected, "value")
            print(record_value)

            messageUpdate = messagebox.askyesno(
                "Update", "Are you sure you want to update this record?")

            if messageUpdate > 0:

                eWaste_Db_Connect.connectDB(dbName, dbTable)
                update_query = """ Update ewaste SET unit=?, make=?, model_serial=?, item_qty=?, pallet=? WHERE id = ? """
                columValues = (unit_RadioVariable.get(), make_RadioVariable.get(
                ), serial_number_entry.get(), quantity_entry.get(), pallet_number_entry.get(), record_value[0])
                print(columValues)
                my_table.item(selected, text="", values=(record_value[0], unit_RadioVariable.get(), make_RadioVariable.get(
                ), serial_number_entry.get(), quantity_entry.get(), pallet_number_entry.get()))

                eWaste_Db_Connect.myCursor.execute(update_query, columValues)

                eWaste_Db_Connect.commitCloseDb()
                focus_cursor_toTop()
                clear_all()
                get_default_pallet()
            else:
                refresh

        def exit_pallet():
            if editPalletEntry.get() == '':
                editPallet_errorMsg.config(text='**NOTHING WAS ENTERED**')
                # print('NOTHING WAS ENTERED')
            else:
                with open(r"config.txt", 'w') as r:
                    r.write(editPalletEntry.get())

                # print("Call Query DATA", editPalletEntry.get())
                editPallettWindow.destroy()

                # print("Second Query call")

                queryData()
        self.editPallet = Button(coverFrame3)
        self.editPallet.place(relx=0.539, rely=0.705, width=86, height=25)
        self.editPallet.configure(relief="flat")
        self.editPallet.configure(overrelief="flat")
        self.editPallet.configure(activebackground="#fd6a36")
        self.editPallet.configure(cursor="hand2")
        self.editPallet.configure(foreground="#ffffff")
        self.editPallet.configure(background="#fd6a36")
        self.editPallet.configure(
            font="-family {Poppins SemiBold} -size 10")
        self.editPallet.configure(borderwidth="0")
        self.editPallet.configure(text="""Edit Pallet #""")
        self.editPallet.configure(command=edit_pallet)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure('Treeview', bg='#3BA4B9', rowheight=30,
                        fg='black', fieldbackground='gray',  font=("yu gothic ui", 11))
        style.map("Treeview", background=[('selected', '#6F5EA2')])
        scrollbarx = Scrollbar(self.windows, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.windows, orient=VERTICAL)

        my_table = ttk.Treeview(coverFrame)
        my_table.tag_configure('even', background='white')
        my_table.tag_configure('odd', background='#fdf2f2')
        my_table.place(relx=0.0640, rely=0.108,
                       width=900, height=510)
        my_table.configure(
            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set
        )
        my_table.configure(selectmode="extended")

        # my_table.tag_configure('even', background='white')
        # my_table.tag_configure('odd', background='#fdf2f2')

        scrollbary.configure(command=my_table.yview)
        scrollbarx.configure(command=my_table.xview)

        scrollbary.place(relx=0.976, rely=0.323, width=25, height=412)
        scrollbarx.place(relx=0.242, rely=0.979, width=1015, height=15)

        my_table.configure(
            columns=(
                "id",
                "unit",
                "make",
                "model_serial",
                "item_qty",
                "pallet"
            )
        )

        my_table.heading("#0", text="", anchor=N)
        my_table.heading("id", text="ID", anchor=N)
        my_table.heading("unit", text="Unit", anchor=N)
        my_table.heading("make", text="Make", anchor=N)
        my_table.heading(
            "model_serial", text=" Model / Serial", anchor=N)
        my_table.heading(
            "item_qty", text="Item - Quantity", anchor=N)
        my_table.heading("pallet", text="Pallet #", anchor=N)

        my_table.column("#0", stretch=NO, minwidth=0, width=0)
        my_table.column(
            "id", stretch=NO, minwidth=0, width=50, anchor=N)
        my_table.column(
            "unit", stretch=NO, minwidth=0, width=288, anchor=N)
        my_table.column(
            "make", stretch=NO, minwidth=0, width=176, anchor=N)
        my_table.column(
            "model_serial", stretch=NO, minwidth=0, width=110, anchor=N)
        my_table.column(
            "item_qty", stretch=NO, minwidth=0, width=110, anchor=N)
        my_table.column(
            "pallet", stretch=NO, minwidth=0, width=160, anchor=N)

        def ewaste_info(ev):
            viewInfo = my_table.focus()
            ewaste_data = my_table.item(viewInfo)
            row = ewaste_data['values']
            # print(row)
            # coffee_id.set(row[0])
            unit_RadioVariable.set(row[1].strip())
            make_RadioVariable.set(row[2].strip())
            serial_num.set(row[3])
            quantity.set(row[4])
            pallet.set(row[5])
            pallet_number_entry.config(state=NORMAL)

        my_table.bind("<ButtonRelease-1>", ewaste_info)

        def get_default_pallet():
            with open(r"config.txt", 'r') as r:
                currentPallet = " "+r.readline().strip()
            # print("Curent pallet", currentPallet)
            pallet_number_entry.config(state=NORMAL)
            pallet_number_entry.delete(0, 'end')
            pallet.set(currentPallet)
            # pallet_number_entry.insert(0, currentPallet)
            pallet_number_entry.config(state=DISABLED)

        option_menu = Menu(my_table, tearoff=0)
        # option_menu.add_command(label='Update', command=update_pallet)
        option_menu.add_command(label='Delete', command=delete_ewaste_record)
        option_menu.add_command(label='Export', command=csv_file)
        option_menu.add_separator()
        option_menu.add_command(label='Refresh', command=refresh)

        def do_popup(event):
            try:
                option_menu.tk_popup(event.x_root, event.y_root)
            finally:
                option_menu.grab_release()
        queryData()
        focus_cursor_toTop()
        my_table.bind("<Button-3>", do_popup)

    def home(self):
        Home_Page.HomePage(self.windows)
        self.dashboard_window.withdraw()
        self.windows.deiconify()

    def closeWin(self):
        super().closeWin()


def page():
    window = Tk()

    ewaste = EWaste(window)
    ewaste.ewaste_button.configure(bg='#fd6a36', fg='white')
    ewaste.dashboard_window.title("E-Waste Mangement System")
    ewaste.homepage.configure(background='#f6f6f9')

    window.mainloop()


if __name__ == '__main__':
    page()
