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

def get_valid_priority():
    priority_list = ["LOW", "MEDIUM", "HIGH"]
    while True:
        priority = input("ENTER TASK PRIORITY LOW, MEDIUM or HIGH(DEFAULT 'LOW') : ").strip().upper()
        if not priority:
            priority = "LOW"
            break
        elif priority in priority_list:
            break
        else:
            print("Invalid priority. Please enter in LOW, MEDIUM or HIGH.")
    return priority

def get_valid_status():
    status_list = ["COMPLETED", "IN-PROGRESS", "PENDING"]
    while True:
        status = input("ENTER TASK STATUS COMPLETED, IN-PROGRESS or PENDING : ").strip().upper()
        if status in status_list:
            break
        elif not status:
            status = "PENDING"
            break
        else:
            print('Invalid status entered. Please enter [COMPLETED,IN-PROGRESS,PENDING]')
    return status

def menu():
    print("-----MAIN MENU-----");
    print(" 1. ADD TASK\n 2. MODIFY TASK\n 3. REMOVE TASK\n 4. VIEW TASK\n 5. SEARCH TASK\n 6. EXIT")

def addtask():
    name=input("ENTER TASK NAME : ").strip().upper()
    status = get_valid_status()
    due_date=get_valid_date()
    created_date = datetime.today().strftime('%Y-%m-%d')
    priority = get_valid_priority()
    db.addtodb(name,status,due_date,created_date,priority)

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
            t=int(input("1. CHANGE STATUS\n2. CHANGE TITLE\n3. CHANGE DUE-DATE\n4. CHANGE PRIORITY\n5. MAIN-MENU\n-->> "))
            if t in [1,2,3,4]:
                break
            else:
                print("ENTER FROM GIVEN CHOICE")
        except ValueError:
            print("INVALID CHOICE")
    if t==1:
        status = get_valid_status()
        date = datetime.today().strftime('%Y-%m-%d')
        db.modifystatus(task,status,date)
    elif t==2:
        while True:
            title_new = input("ENTER TASK TITLE : ").strip().upper()
            if not title_new:
                print("INVALID TITLE")
            else:
                break
        db.modifytitle(task,title_new)
    elif t==3:
        date_new = get_valid_date()
        db.modify_due_date(task,date_new)
    elif t==4:
        priority = get_valid_priority()
        db.modifypriority(task,priority)
    elif t==5:
        main()

def removetask():
    db.viewdb()
    while True:
        try:
            id = int(input("ENTER TASK NUMBER TO DELETE : "))
            tasks = db.gettask()
            if id < 1 or id > len(tasks):
                print("INVALID TASK NUMBER")
            else:
                break
        except ValueError:
            print("ENTER IN CORRECT NUMBER FORMAT")
    db.deletetask(id)

def search():
    print("Search by :")
    print(" 1. Keyword")
    print(" 2. Status")
    print(" 3. Due Date")
    print(" 4. Created Date")
    choice = input("ENTER YOUR CHOICE : ").strip()
    field_map = {
        "1": "name",
        "2": "status",
        "3": "due_date",
        "4": "created_date"
    }
    if choice not in field_map:
        print("INVALID CHOICE.")
        return

    keyword = input(f"ENTER SEARCH KEYWORD FOR {field_map[choice].upper()} : ").strip().upper()
    if keyword:
        db.search_task(keyword,field_map[choice])
    else:
        print("SEARCH KEYWORD CAN NOT BE EMPTY.")

def main():
    db.init_db()
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
            search()
            input("Press ENTER to continue")
            print("\n"*25)
        elif choice ==6:
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()