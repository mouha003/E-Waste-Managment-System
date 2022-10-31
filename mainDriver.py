from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3
# import dbconnection


def mainDriver():
    global rootDriver
    rootDriver = Tk()

    rootDriver.title('Hello Mouhari')
    rootDriver.geometry('1250x800+400+10')
    rootDriver.resizable(False, False)

    # blank = Label(rootDriver, text='BLANK')
    # blank.grid(row=0, column=0, padx=200, pady=50, sticky=W)
    mainLabel = Label(rootDriver, text='All About Me!',
                      font='MingLiU_HKSCS-ExtB 40 bold')
    mainLabel.grid(row=0, column=0, columnspan=2, sticky=NE, pady=60, padx=100)

    fnLabel = Label(rootDriver, text="FirstName:", font='ariel 12 bold')
    fnLabel.grid(row=2, column=0, pady=2)

    fnEntry = Entry(rootDriver, width=25)
    fnEntry.grid(row=2, column=0, columnspan=2, padx=220, pady=2, sticky=W)

    lnLabel = Label(rootDriver, text="Lastname:", font='ariel 12 bold')
    lnLabel.grid(row=3, column=0, pady=2)

    lnEntry = Entry(rootDriver, width=25)
    lnEntry.grid(row=3, column=0, columnspan=2, padx=220, pady=2, sticky=W)

    commentLabel = Label(rootDriver, text='Something abour yourself')
    commentLabel.configure(font='ariel 14 bold')
    commentLabel.grid(row=4, column=0, columnspan=2,
                      sticky=NW, pady=60, padx=120)

    commentTextBox = scrolledtext.ScrolledText(
        rootDriver, height=10, width=100)
    commentTextBox.grid(row=5, column=0, columnspan=6, sticky=S, padx=120)

    fnEntry.focus()

    def clearAll():
        fnEntry.delete(0, END)
        lnEntry.delete(0, END)
        commentTextBox.delete("1.0", END)

    def submit():
        if fnEntry.get() == '' or lnEntry.get() == '':
            messagebox.showerror(
                title='Error', message='One of the field is empty.')
        else:
            dbconnection.connectDB()
            dbconnection.myCursor.execute("""INSERT INTO customers VALUES (:firstName, :lastName, :comment)""",
                                          {'firstName': fnEntry.get(), 'lastName': lnEntry.get(), 'comment': commentTextBox.get('1.0', END)})
            dbconnection.commitCloseDb()
            messagebox.showinfo(
                title='Submit!', message='Your Information has been submitted!')
            clearAll()

        fnEntry.focus()

    submitBtn = Button(rootDriver, text='Submit', height=2, width=10, bg='lightblue',
                       command=submit)

    submitBtn.grid(row=6, column=0, columnspan=2, sticky=S, padx=120, pady=50)

    clearBtn = Button(rootDriver, text='Clear', height=2,
                      width=10, bg='lightgreen', command=clearAll)
    clearBtn.grid(row=6, column=1, columnspan=2, sticky=S, padx=100, pady=50)

    userDashboard = Button(rootDriver, text="Dashboard", height=2,
                           width=19, bg='lightpink', command=openDashboardWindow)
    userDashboard.grid(row=6, column=1, columnspan=5,
                       sticky=S, padx=300, pady=50)

    def terminate(event):
        rootDriver.destroy()

    def hitEnterKey(event):
        submit()

    rootDriver.bind('<Escape>', lambda e: terminate(e))
    rootDriver.bind('<Return>', lambda e: hitEnterKey(e))
    rootDriver.mainloop()

# ---------------- Create toplevel and create treeview for data display ---------------------------------------


def openDashboardWindow():
    global my_Tree

    dashboardWindow = Toplevel(rootDriver)

    dashboardWindow.title('User Dashboard')
    dashboardWindow.geometry('1250x800+600+15')
    dashboardWindow.resizable(False, False)

    style = ttk.Style(dashboardWindow)
    style.theme_use('default')

    style.configure('Treeview', bg='#3BA4B9', fg='black',
                    rowheight=40, fieldbackground='gray', font='ariel 12')
    style.configure("Treeview.Heading", background='lightblue',
                    font='ariel 13 bold')
    style.map("Treeview", background=[('selected', '#6F5EA2')])

    myFrame = Frame(dashboardWindow)
    myFrame.pack(padx=10, pady=2, anchor=N)

    # Creating the scrollbar
    tree_ScrollBar = Scrollbar(myFrame, orient=VERTICAL)
    tree_ScrollBar.pack(side=RIGHT, fill=Y)

    my_Tree = ttk.Treeview(
        myFrame, yscrollcommand=tree_ScrollBar.set, selectmode="extended", height=10)
    my_Tree.tag_configure('even', background='#B3E3B3')  # configure the tags
    my_Tree.tag_configure('odd', background='#F3F2F6')  # configure the tags

    my_Tree.pack(pady=10, anchor=N, expand=YES)
    tree_ScrollBar.config(command=my_Tree.yview)

    my_Tree['columns'] = ('FirstName', 'LastName', 'Comment')
    my_Tree.column('#0', width=0, stretch=NO)
    my_Tree.column('FirstName', width=150)
    my_Tree.column('LastName', width=150)
    my_Tree.column('Comment', width=350)

    my_Tree.heading('#0', text='', anchor=W)
    my_Tree.heading('FirstName', text='  First Name', anchor=W)
    my_Tree.heading('LastName', text='  Last Name', anchor=W)
    my_Tree.heading('Comment', text='  Comment', anchor=W)

    queryData()
    dashboardWindow.mainloop()


# ---------------- Query data from database into Treeview ---------------------------------------
def queryData():
    myDBData = dbconnection
    myDBData.connectDB()
    myCustdata = myDBData.myCursor.execute(
        "SELECT * FROM customers").fetchall()
    print(myCustdata)
    for i in myCustdata:
        if myCustdata.index(i) % 2 == 0:
            my_Tree.insert('', index=0, values=i, tags='even')
        else:
            my_Tree.insert('', index=0, values=i, tags='odd')


if __name__ == '__main__':
    mainDriver()
