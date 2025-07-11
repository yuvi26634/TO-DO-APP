import sqlite3
def init_db():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("create table if not exists tasks("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "name TEXT NOT NULL,"
                       "status TEXT NOT NULL DEFAULT 'PENDING',"
                       "due_date TEXT NOT NULL,"
                       "created_date TEXT NOT NULL,"
                       "completed_date TEXT DEFAULT '-',"
                       "priority TEXT NOT NULL DEFAULT 'LOW')")
        conn.commit()
def addtodb(name,status,due_date,created_date,priority):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("insert into tasks(name,status,due_date,created_date,priority) values (?,?,?,?,?)",(name,status,due_date,created_date,priority))
        conn.commit()

def viewdb():
    tasks = gettask()
    if len(tasks) == 0:
        print("NO TASKS FOUND")
        return
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("select name,status,due_date,created_date,completed_date,priority from tasks")
        print("S.NO".ljust(10)+"NAME".ljust(20)+"STATUS".ljust(15)+"DUE-DATE".ljust(15)+"CREATED-ON".ljust(15)+"COMPLETED-ON".ljust(15)+"PRIORITY".ljust(10))
        for i,row in enumerate(cursor.fetchall(),start=1):
            name,status,due_date,created_date,completed_date,priority=row
            print(f"{i}".ljust(10)+name.ljust(20)+status.ljust(15)+due_date.ljust(15)+created_date.ljust(15)+completed_date.ljust(15)+priority.ljust(10))

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
        cursor.execute("UPDATE tasks SET name = ? WHERE id = ?",(title_new,id))
        conn.commit()

def modifystatus(id,status_new,date):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        if status_new == "COMPLETED":
            cursor.execute("UPDATE tasks SET status = ?,completed_date = ? WHERE id = ?",(status_new,date,id))
        else:
            cursor.execute("UPDATE tasks SET status = ?,completed_date = ? WHERE id = ?", (status_new,'-',id))
        conn.commit()

def modify_due_date(id,date_new):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET due_date = ? WHERE id = ?",(date_new,id))
        conn.commit()

def modifypriority(id,priority):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET priority = ? WHERE id = ?",(priority,id))
        conn.commit()

def search_task(keyword,field):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        query = f"select * from tasks where {field} like ?"
        cursor.execute(query,('%'+keyword+'%',))
        results = cursor.fetchall()
        if not results:
            print("NO MATCHING TASKS FOUND")
            return
        print("S.NO".ljust(10) + "NAME".ljust(20) + "STATUS".ljust(15) + "DUE-DATE".ljust(15) + "CREATED-ON".ljust(15) + "COMPLETED-ON".ljust(15) + "PRIORITY".ljust(10))
        for i, row in enumerate(results, start=1):
            id,name, status, due_date, created_date, completed_date, priority = row
            print(f"{i}".ljust(10) + name.ljust(20) + status.ljust(15) + due_date.ljust(15) + created_date.ljust(15) + completed_date.ljust(15) + priority.ljust(10))

if __name__ == "__main__":
    print("This file is only meant to be imported, not run directly.")



