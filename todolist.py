import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Create GUI components
entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
listbox = tk.Listbox(root)

# Place GUI components on the window
entry.pack(pady=10)
add_button.pack()
remove_button.pack()
listbox.pack(pady=10)

# Start GUI loop
root.mainloop()
