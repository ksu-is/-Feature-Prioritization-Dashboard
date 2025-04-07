import tkinter as tk
from tkinter import messagebox

#This is a kanban board im going to turn into moscow
# I already started on this locally but I didnt realize we were supposed to show progress so I uploaded it

class FeaturePrio:
    def __init__(self, root):
        self.root = root
        self.root.title("Feature Prioritization Dashboard")
        self.root.geometry("900x500")
        self.root.config(bg="#d6f7ff")


        ##These are the boards
        self.must_frame = self.create_frame("Must Have", 0, "#ef233c")
        self.should_frame = self.create_frame("Should Have", 1, "#ffd166")
        self.could_frame = self.create_frame("Could Have", 2, "#06d6a0")
        self.wont_frame = self.create_frame("Wont Have", 2, "#06d6a0")
        
        # Input field and add button
        self.entry = tk.Entry(self.root, width=40, font=("Arial", 14),
                              bg="#8d99ae", fg="#edf2f4")
        self.entry.grid(row=1, column=0, columnspan=2, pady=10, padx=10,
                        sticky="ew")
        self.add_button = tk.Button(
            self.root,
            text="Add Task",
            command=self.add_task,
            bg="#3a86ff",
            fg="white",
            font=("Arial", 12, "bold"),
            activebackground="#00509e",
        )
        self.add_button.grid(row=1, column=2, pady=10, padx=10)

    def create_frame(self, title, col, bg_color):
        frame = tk.Frame(self.root, bg=bg_color, bd=2, relief=tk.RIDGE)
        frame.grid(row=0, column=col, padx=10, pady=10, sticky="nsew")

        #label
        label = tk.Label(frame, text=title, font=("Arial", 16, "bold"),
                        bg=bg_color, fg="white")
        label.pack(side=tk.TOP, fill=tk.X, pady=5)

        #listbox for tasks
        listbox = tk.Listbox(frame, height=15, width=25, font=("Arial", 12),
                             bg="#edf2f4", fg="#2b2d42")
        listbox.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        frame.listbox = listbox

        # Buttons for moving tasks
        if col== 0:  # To-Do Column
            move_button = tk.Button(
                frame, text="move to Doing", bg="#06d6a0",
                command=lambda: self.move_task(self.todo_frame,
                                               self.doing_frame)
            )
        elif col == 1: # Doing column
            move_button = tk.Button(
                frame, text="Move to Done", bg="#06d6a0",
                command=lambda: self.move_task(self.doing_frame,
                                               self.done_frame)
            )
        else: # Done Column
            move_button = tk.Button(
                frame, text="Delete Task", bg="#ef233c",
                command=lambda: self.delete_task(self.done_frame)
            )
        move_button.pack(side=tk.BOTTOM, pady=10)

        return frame

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.todo_frame.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Task cannot be empty!")
    
    def move_task(self, from_frame, to_frame):
        selected = from_frame.listbox.curselection()
        if selected:
            task = from_frame.listbox.get(selected)
            from_frame.listbox.delete(selected)
            to_frame.listbox.insert(tk.END, task)
        else:
            messagebox.showerror("Error", "No task selected to move!")

    def delete_task(self, frame):
        selected = frame.listbox.curselection()
        if selected:
            task = frame.listbox.get(selected)
            frame.listbox.delete(selected)
            messagebox.showinfo("Task Deleted",
                                f"task '{task}' has been deleted!")
        else:
            messagebox.showerror("Error", "No Task selected to delete!")

# Initialize the app
if __name__ == "__main__":
    root = tk.Tk()
    root.grid_columnconfigure((8, 1, 2),
                             weight=1)
    root.grid_rowconfigure(0, weight=1)
    app = FeaturePrio(root)
    root.mainloop() 
