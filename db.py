import sqlite3
def init_db():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("create table if not exists tasks("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "name TEXT NOT NULL,"
                       "status TEXT NOT NULL,"
                       "due_date TEXT NOT NULL)")
        conn.commit()
def addtodb(name,status,due_date):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("insert into tasks(name,status,due_date) values (?,?,?)",(name,status,due_date))
        conn.commit()

def viewdb():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("select id,name,status,due_date from tasks")
        print("S.NO".ljust(10)+"NAME".ljust(20)+"STATUS".ljust(15)+"DUE-DATE")
        for i,row in enumerate(cursor.fetchall(),start=1):
            id,name,status,due_date=row
            print(f"{i}".ljust(10)+name.ljust(20)+status.ljust(15)+due_date)

def gettask():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("select id,name,status,due_date from tasks")
        return cursor.fetchall()

def deletetask(id):
    tasks = gettask()
    if id <1 or id > len(tasks):
        print("INVALID TASK NUMBER")
        return
    task_id = tasks[id-1][0]
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("delete from tasks where id = ?",(task_id,))
        conn.commit()

def modifytitle(id,title_new):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        #change column name in table
        cursor.execute("UPDATE tasks SET name = ? WHERE id = ?",(title_new,id))
        conn.commit()

def modifystatus(id,status_new):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?",(status_new,id))
        conn.commit()

def modifydate(id,date_new):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET due_date = ? WHERE id = ?",(date_new,id))
        conn.commit()

if __name__ == "__main__":
    print("This file is only mean to be imported, not run directly.")

