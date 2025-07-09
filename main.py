import db
from datetime import datetime

def get_valid_date():
    while True:
        date_input = input("Enter due date (YYYY-MM-DD): ")
        try:
            valid_date = datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format! Please enter in YYYY-MM-DD format.")

def menu():
    print("-----MAIN MENU-----");
    print(" 1. ADD TASK\n 2. MODIFY TASK\n 3. REMOVE TASK\n 4. VIEW TASK\n 5. EXIT")

def addtask():
    name=input("ENTER TASK NAME : ")
    status=input("ENTER TASK STATUS : ")
    due_date=get_valid_date()
    db.addtodb(name,status,due_date)

def modifytask():
    db.viewdb()
    while True:
        try:
            task_id=int(input("ENTER TASK NO TO MODIFY : "))
            tasks = db.gettask()
            if task_id <1 or task_id > len(tasks):
                print("INVALID TASK NUMBER")
            else:
                task = tasks[task_id-1][0]
                break
        except ValueError:
            print("INVALID NUMBER")
    while True:
        try:
            t=int(input("1. CHANGE STATUS\n2. CHANGE TITTLE\n3. CHANGE DUE-DATE\n4. MAIN MENU\n-->> "))
            if t in [1,2,3,4]:
                break
            else:
                print("ENTER FROM GIVEN CHOICE")
        except ValueError:
            print("INVALID CHOICE")
    if t==1:
        status_new = input("ENTER TASK STATUS : ")
        db.modifystatus(task,status_new)
    elif t==2:
        title_new = input("ENTER TASK TITLE : ")
        db.modifytitle(task,title_new)
    elif t==3:
        date_new = get_valid_date()
        db.modifydate(task,date_new)
    elif t==4:
        main()

def removetask():
    db.viewdb()
    try:
        id = int(input("ENTER TASK ID : "))
    except ValueError:
        print("INVALID ID")
    db.deletetask(id)

def main():
    while True:
        menu()
        try:
            choice=int(input("Enter Choice : "))
        except ValueError:
            print("ENTER CORRECT VALUE")
            continue
        if choice==1:
            addtask()
        elif choice ==2:
            modifytask()
        elif choice ==3:
            removetask()
        elif choice ==4:
            db.viewdb()
            input("Press ENTER to continue")
            print("\n" * 25)
        elif choice ==5:
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()