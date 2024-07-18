import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

tasks = []

def update_tasks():
    task_listbox.delete(0,tk.END)
    for i, task in enumerate(tasks, 1):
        task_listbox.insert(tk.END, f"{i}. {task}")

def add_task():
    task = simpledialog.askstring("Add Task", "Enter your task:")
    tasks.append(task)
    update_tasks()
def remove_task():
    task_number = simpledialog.askinteger("Remove Task", "Enter the number of the task you want to delete.")
    tasks.pop(task_number - 1)
    update_tasks()
def save_tasks():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    with open(filepath, "w") as tasklist:
        for task in tasks:
            tasklist.write(task + "\n")
def exit_program():
    run.quit()

run = tk.Tk()
run.title("To-Do List")

frame = tk.Frame(run)
frame.pack(pady=10)

task_listbox = tk.Listbox(frame, width = 50, height = 10)
task_listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill = tk.Y)

button_frame = tk.Frame(run)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text = "Add Task", command = add_task)
add_button.grid(row=0,column=0,padx=5)

remove_button = tk.Button(button_frame, text = "Remove Task", command = remove_task)
remove_button.grid(row=0,column=1,padx=5)

save_button = tk.Button(button_frame, text = "Save List", command = save_tasks)
save_button.grid(row=0,column=2,padx=5)

exit_button = tk.Button(button_frame, text = "Exit", command = exit_program)
exit_button.grid(row=0,column=3,padx=5)

run.mainloop()