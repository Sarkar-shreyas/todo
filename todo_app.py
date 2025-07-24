TICK = "✓"
BOX = "□"
TASKS = []

#Simple options menu
def menu():
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Mark task as complete")
    print("4. Mark task as incomplete")
    print("5. Show complete tasks")
    print("6. Show incomplete tasks")
    print("7. Show all tasks")
    print("8. Quit")

#Add a task to the list
def addTask(task):
    print("Please enter the task description: ")
    newTask = input()
    task.append(f"{newTask} {BOX}")
    print("Your task was successfully added!")
    print("What would you like to do next?")
    return task

#Remove a task from the list
def removeTask(task):
    if not task:
        print("The task list is currently empty!")
        return
    showTasks(task)
    print("Enter which task you would like to remove: ")
    remove = input()
    while not remove.isdigit():
        print("Please enter the corresponding task number:")
        remove = input()
    while int(remove) > len(task):
        print("Please enter a valid number!\n")
        remove = input()

    del task[int(remove) - 1]
    return f"Task {remove} has been successfully deleted!"

#Mark a task as complete
def markComplete(task):
    if not task:
        print("The task list is currently empty!")
        return
    showTasks(task)
    print("Which task has been completed?")
    tasknum = input()
    while int(tasknum) > len(task):
        print("Please enter a valid number!")
        tasknum = input()

    task[int(tasknum)-1] = task[int(tasknum)-1].replace(BOX, TICK)
    return f"Congratulations! Task {tasknum} has been completed!"

#Mark a task as incomplete
def markIncomplete(task):
    if not task:
        return "The task list is currently empty!"

    showTasks(task)
    print("Which task do you want to mark incomplete?")
    tasknum = input()
    while int(tasknum) > len(task):
        print("Please enter a valid number!")
        tasknum = input()
    if BOX in task[int(tasknum)-1]:
        return "That task is already marked incomplete!"

    task[int(tasknum)-1] = task[int(tasknum)-1].replace(TICK, BOX)
    return f"Task {tasknum} has been marked incomplete!"


#Print out all currently logged tasks
def showTasks(task, num=0):
    if not task:
        print("The task list is currently empty!")
        return
    if num == 0:
        print("Would you like to see the current list of tasks?\nEnter Y or N:")
        show = input()
        while show.lower() != "y" and show.lower() != "n":
            print("Please enter Y or N:")
            show = input()
        if show.lower() == "y":
            for item in task:
                print(f"{task.index(item)+1}. {item}")
    elif num == 7:
        print("This is the list of current tasks:")
        for item in task:
            print(f"{task.index(item) + 1}. {item}")
    elif num == 6:
        print("This is the list of incomplete tasks:")
        for item in task:
            if BOX in item:
                print(f"{task.index(item) + 1}. {item}")
    elif num == 5:
        print("This is the list of completed tasks:")
        for item in task:
            if TICK in item:
                print(f"{task.index(item) + 1}. {item}")


def main():

    print("Welcome to the todo-list app!")
    while True:
        print("What would you like to do?")
        menu()
        print("Enter your choice: ")
        choice = input()

        if choice == '8':
            print("Thank you for using the todo-list app! :)")
            return
        elif choice == '1':
            addTask(TASKS)
        elif choice == '2':
            removeTask(TASKS)
        elif choice == '3':
            markComplete(TASKS)
        elif choice == '4':
            markIncomplete(TASKS)
        elif choice == '5':
            showTasks(TASKS, int(choice))
        elif choice == '6':
            showTasks(TASKS, int(choice))
        elif choice == '7':
            showTasks(TASKS, int(choice))
        else:
            print("Please enter a valid choice: ")
            choice = input()

if __name__ == "__main__":
    main()
