tasks = {}
active = True

def addTask():
    taskId = input("\n enter taskId: ")
    if taskId in tasks:
        print("\n || taskId already taken, enter another one ||")
    else:    
        task = input("\n please enter task: ")
        tasks[taskId] = task
        print("\n || task added successfully ||")
        
        
def removeTask():
        taskId = input("\n please enter the id of the task yoy wish to remove: ")
        if taskId in tasks:
            del tasks[taskId]
            print("\n  || task deleted successfully ||")
        else:
            print("\n || there is no task with that id ||")    

def updateTask():
    taskId = input("\n || please enter the taskId of the task you wish to update: ||")
    task= input("\n enter new task: ")
    
    if taskId in tasks:
        tasks[taskId]= task
        print("\n || task updated successfully ||")
    else:
        print("\n || There is no task with that id ||")

def getAllTasks():
     if tasks:
         print(tasks)
     else:
         print("\n || There are no tasks ||")
 
def getSingleTask():
    taskId = input("\n enter task id: ")
    if taskId in tasks:
        tasks[taskId]
    else:
        print("no rask wirh that id")    

def run():
    print("\n ___Welcome To Terminal Task___")
    while True:
         print("")
         print("1. Add a Task.")
         print("2.Get single Task ")
         print("3. Get all Task")
         print("4. Update a Task")
         print("5. Delete Task")
         print("6. Exit")
         choice = input("\n Enter a choice: ")
         
         if choice == "1":
             addTask()
         elif choice == "2":
             getSingleTask()
         elif choice =="3":
             getAllTasks()
         elif choice == "4":
             updateTask()
         elif choice=="5":
             removeTask()
         elif choice == "6":
             print("\n Thank you  for using Terminal Task")
             break
         else:
             print("\n please enter a valid choice")                                                                                         
run()