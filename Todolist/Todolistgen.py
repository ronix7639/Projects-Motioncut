import tkinter as tk
from tkinter import messagebox

tasks = []
completedtasks = []

# Adds a new task
def addtask():
    description = description_entry.get()
    due_date = due_date_entry.get()
    priority = priority_entry.get()

    if description:
        task = {
            "description": description,
            "due_date": due_date,
            "priority": priority
        }
        tasks.append(task)
        task_list.insert(tk.END, task["description"])
        description_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)


#Updates current task
def updatetask():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        description = description_entry.get()
        due_date = due_date_entry.get()
        priority = priority_entry.get()

        if description:
            task_index = selected_task_index[0]
            task = tasks[task_index]
            task["description"] = description
            task["due_date"] = due_date
            task["priority"] = priority
            task_list.delete(task_index)
            task_list.insert(task_index, task["description"])
            description_entry.delete(0, tk.END)
            due_date_entry.delete(0, tk.END)
            priority_entry.delete(0, tk.END)

#Removes an existing task
def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        del tasks[task_index]
        task_list.delete(task_index)

#Shifts from to-do list to the completed list
def mark_complete():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task = tasks[task_index]
        completedtasks.append(task)
        completed_list.insert(tk.END, task["description"])
        remove_task()

root = tk.Tk()
root.title("To-Do List App")
root.geometry("800x400")


# Create and configure the task list
task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=15, bg="#00ecec")
task_list.pack(side=tk.LEFT, padx=10)

# Create and configure the completed tasks list
completed_list = tk.Listbox(root, selectmode=tk.SINGLE, width=30, height=15, bg="#85CFDB")
completed_list.pack(side=tk.RIGHT, padx=10)

# Task details entry fields
entry_frame = tk.Frame(root)
entry_frame.pack(side=tk.LEFT, padx=10)

description_label = tk.Label(entry_frame, text="Description:")
description_label.pack()
description_entry = tk.Entry(entry_frame, width=40)
description_entry.pack()

due_date_label = tk.Label(entry_frame, text="Due Date:")
due_date_label.pack()
due_date_entry = tk.Entry(entry_frame, width=40)
due_date_entry.pack()

priority_label = tk.Label(entry_frame, text="Priority:")
priority_label.pack()
priority_entry = tk.Entry(entry_frame, width=40)
priority_entry.pack()

# Buttons frame design  
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, padx=10)
#add button design 
add_button = tk.Button(button_frame, text="Add Task", command=addtask)
add_button.pack()
#update button design 
update_button = tk.Button(button_frame, text="Update Task", command=updatetask)
update_button.pack()
#Remove button deisgn 
remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.pack()
#Mark comlete button
mark_complete_button = tk.Button(button_frame, text="Mark as Completed", command=mark_complete)
mark_complete_button.pack()

root.mainloop()
