import sqlite3
from tkinter import messagebox


def connectDB(dbName, tableName):
    global myConnection, myCursor
    try:
        myConnection = sqlite3.connect(dbName)
        myCursor = myConnection.cursor()
        myCursor.execute(f"""CREATE TABLE if not exists {tableName} (
                        id INTEGER PRIMARY KEY, unit TEXT, make TEXT,  model_serial TEXT, item_qty TEXT, pallet TEXT);""")
        keep_order_sql = """CREATE TRIGGER keep_in_order_delete AFTER DELETE ON ewaste
                            Begin
                            UPDATE ewaste Set id = id - 1 where id > old.id;
                            end; """
        # myCursor.execute(f"""CREATE TRIGGER keep_in_order_delete AFTER DELETE ON ewaste
        #                     Begin
        #                     UPDATE ewaste Set id = id - 1 where id > old.id;
        #                     end; """)

    except:
        messagebox.showerror(title='Connection Error',
                             message='Error Connecting to DataBase')


def commitCloseDb():
    myConnection.commit()
    myConnection.close()
