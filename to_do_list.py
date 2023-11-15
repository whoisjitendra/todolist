import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        
        self.tasks = []

       
        self.task_entry = tk.Entry(root, width=80)
        self.task_entry.pack(pady=30)

        
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()

        
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
        self.task_listbox.pack(pady=10)

        
        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.pack()

        
        exit_button = tk.Button(root, text="Exit", command=root.destroy)
        exit_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.tasks.remove(task)
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
