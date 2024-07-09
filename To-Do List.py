tasks = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
    elif choice == '2':
        task_number = int(input("Enter the task number to remove: "))
        if 0 < task_number <= len(tasks):
            tasks.pop(task_number - 1)
    elif choice == '3':
        break
    else:
        print("Invalid choice! Please choose again.")


tasklist = open("checklist.txt","w")
for task in tasks:
    taskstr = str(tasks.index(task)+1)+ ". "+ task + "\n"
    #print(taskstr)
    tasklist.write(taskstr)
tasklist.close()