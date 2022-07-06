print("Hi, I'm PAL your automatic assistant.")
print("How can I assist you today?")

main_menu = """
0: Exit
1: Add Task
2: Display Task List
3: Mark Task as Complete
"""
task = []
finished = False

while not finished:
    print(main_menu)
    selection = input("Please Make A Selection: ")
    print()
    if selection == "0":
        finished = True
    elif selection == "1":
        add = input("Please add a task: ")
        item = add.title()
        task.append(item)
    elif selection == "2":
        if(len(task) == 0):
            print("No Tasks to complete")
        else:
            print("Task List")
            print("-"*10)
            for item in task:
                print(item)
    elif selection == "3":
        remove = input("Awsome Work! Which task has been completed: ")
        item = remove.title()
        task.remove(item)
    else:
        print("Sorry, I do not understand the entry. Please try again")