#to do list
to_do=[]
def menu():
    print("-----MAIN MENU-----");
    print(" 1. ADD TASK\n 2. MODIFY TASK\n 3. REMOVE TASK\n 4. VIEW TASK\n 5. EXIT")

def addtask():
    task = {"TITLE":input("ENTER TASK TITLE : ").upper(),"STATUS":"PENDING"}
    to_do.append(task)
def modifytask():
    viewtask()
    if not to_do:
        print("NO TASK TO VIEW")
        return
    while True:
        try:
            n=int(input("ENTER TASK NO TO MODIFY : "))
            if 1<=n<=len(to_do):
                break
            else:
                print("Invalid Task No. Please Enter Valid Task No.")
        except ValueError:
            print("INVALID NUMBER")

    while True:
        try:
            t=int(input("1. MARK COMPLETED\n2. CHANGE TITTLE\n-->> "))
            if t in [1,2]:
                break
            else:
                print("ENTER 1 OR 2")
        except ValueError:
            print("INVALID CHOICE")
    if t==1:
        to_do[n-1]["STATUS"]="COMPLETED"
        print("TASK MARKED")
    elif t==2:
        to_do[n-1]["TITLE"]=input("ENTER TASK TIITLE : ").upper()
        print("TITLE CHANGES")
def removetask():
    if not to_do:
        print("NO TASK TO REMOVE")
        return
    viewtask()
    try:
        n=int(input("ENTER TASK NO TO REMOVE : "))
        if 1<=n<= len(to_do):
            del to_do[n-1]
            print("TASK REMOVED SUCCESFULLY")
        else:
            print("TASK NOT FOUND")
    except ValueError:
        print("PLEASE ENTER A VALID TASK NO")
def viewtask():
    if not to_do:
        print("NO TASK TO VIEW")
        return
    print("-"*40)
    print("SR NO".ljust(6)+" TASK".ljust(20)+"STATUS")
    for j,i in enumerate(to_do,start=1):
        print(f"{j}".ljust(6)+i["TITLE"].ljust(20)+i["STATUS"])
    input("Press Enter to Continue...")
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
        viewtask()
    elif choice ==5:
        break
    else:
        print("invalid choice")


