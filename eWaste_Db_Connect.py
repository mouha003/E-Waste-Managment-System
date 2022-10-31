import sqlite3
from tkinter import messagebox


def connectDB(tableName):
    global myConnection, myCursor
    dbName = 'Inventory.db'
    try:
        myConnection = sqlite3.connect(dbName)
        myCursor = myConnection.cursor()
        myCursor.execute(f"""CREATE TABLE if not exists {tableName} (
                        id INTEGER PRIMARY KEY, unit TEXT, make TEXT,  model_serial TEXT, item_qty TEXT, pallet TEXT);""")

    except:
        messagebox.showerror(title='Connection Error',
                             message='Error Connecting to DataBase')


def commitCloseDb():
    myConnection.commit()
    myConnection.close()
