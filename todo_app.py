import argparse as ap
import os
import json
import sys
TICK = "✓"
BOX = "□"
#Set up the parser
parser = ap.ArgumentParser(description="A simple todo-list cli app.")

#Add arguments to accept
parser.add_argument("command", help="add, del, mc (mark complete), mic (mark incomplete), lc (list complete), lic (list incomplete), l (list all), cl (clear all), q (quit)")
parser.add_argument("task", nargs="?", default="", help="Task description or number")

args = parser.parse_args()

#Load tasks from file
def loadTasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

#Save tasks to file
def saveTasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)


#Add a task to the list
def addTask(task):
    tasks = loadTasks()
    if not task == "":
        tasks.append(f"{BOX} {task}")
        saveTasks(tasks)
        print(f"'{task}' has been successfully added.")
    else:
        print("This task has no description")
        print("Usage: python todo_app.py add 'Task description'")
        return

#Remove a task from the list
def removeTask(index):
    tasks = loadTasks()
    if not tasks:
        print("There are no tasks currently logged.")
    else:
        if not index.isdigit():
            print("You must enter a number.")
            print("Usage: python todo_app.py del 'Task number'")
            return
        else:
            taskindex = int(index)-1
            if 0 <= taskindex < len(tasks):
                task = tasks[taskindex]
                tasks.pop(taskindex)
                saveTasks(tasks)
                print(f"'{task}' has been successfully removed.")
            else:
                print("Invalid index.")

#Remove all tasks from the list
def clearTasks():
    tasks = loadTasks()
    if not tasks:
        print("There are no tasks currently logged.")
    else:
        tasks.clear()
        saveTasks(tasks)
        print("All tasks have been removed.")

#Mark a task as complete
def markComplete(index):
    tasks = loadTasks()
    if not index.isdigit():
        print("You must enter a number.")
        print("Usage: python todo_app.py mc 'Task number'")
        return
    else:
        taskindex = int(index)-1
        if 0 <= taskindex < len(tasks):
            if BOX in tasks[taskindex]:
                tasks[taskindex] = tasks[taskindex].replace(BOX, TICK)
                saveTasks(tasks)
                print(f"'{tasks[taskindex]}' is now complete.")
            else:
                print("That task is already complete.")
        else:
            print("Invalid index.")

#Mark a task as incomplete
def markIncomplete(index):
    tasks = loadTasks()
    if not index.isdigit():
        print("You must enter a number.")
        print("Usage: python todo_app.py mic 'Task number'")
        return
    else:
        taskindex = int(index)-1
        if 0 <= taskindex < len(tasks):
            if TICK in tasks[taskindex]:
                tasks[taskindex] = tasks[taskindex].replace(TICK, BOX)
                saveTasks(tasks)
                print(f"'{tasks[taskindex]}' is now incomplete.")
            else:
                print("That task is already incomplete.")
        else:
            print("Invalid index.")


#Print all tasks
def listTasks():
    tasks = loadTasks()
    if not tasks:
        print("There are no tasks currently logged.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

#Print all completed tasks
def listComplete():
    tasks = loadTasks()
    if not tasks:
        print("There are no tasks currently logged.")
    else:
        if not any(TICK in task for task in tasks):
            print("There are no complete tasks.")
        else:
            for i, task in enumerate(tasks, start=1):
                if TICK in task:
                    print(f"{i}. {task}")

#Print all incomplete tasks
def listIncomplete():
    tasks = loadTasks()
    if not tasks:
        print("There are no tasks currently logged.")
    else:
        if not any(BOX in task for task in tasks):
            print("All tasks are complete.")
        else:
            for i, task in enumerate(tasks, start=1):
                if BOX in task:
                    print(f"{i}. {task}")

#Main body
def main():
    #Fetch command and task
    command = args.command.lower()
    task = args.task

    #Respond to each command
    match command:
        case 'q' | 'quit':
            print("Thank you for using the todo-list app! :)")
            sys.exit()
        case 'add':
            addTask(task)
        case 'del' | 'delete':
            removeTask(args.task)
        case 'mc' | 'mark complete':
            markComplete(args.task)
        case 'mic' | 'mark incomplete':
            markIncomplete(args.task)
        case 'lc' | 'list complete':
            #showTasks(tasks, int(choice))
            listComplete()
        case 'lic' | 'list incomplete':
            #showTasks(tasks, int(choice))
            listIncomplete()
        case 'l' | 'list':
            listTasks()
        case 'cl' | 'clear':
            clearTasks()
        case _:
            print("Invalid command.")

if __name__ == "__main__":
    main()
