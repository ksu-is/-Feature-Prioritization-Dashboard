import tkinter as tk
import customtkinter as ctk 
from tkinter import messagebox

# I already started on this locally but I didnt realize we were supposed to show progress so I uploaded it

ctk.set_appearance_mode("light")
#ctk.set_default_color_theme("green") This was a test

class FeaturePrio:
    def __init__(self, root):
        self.root = root
        self.root.title("Feature Prioritization Dashboard")
        self.root.geometry("1600x900")
        self.root.config(bg="#F5F5F5")
        #self.root.config(bg="#d6f7ff") og color




        ##These are the boards
        self.must_frame = self.create_frame("Must Have", 0, "#9ad1ff")
        self.should_frame = self.create_frame("Should Have", 1, "#ff74c8")
        self.could_frame = self.create_frame("Could Have", 2, "#ffa929")
        self.wont_frame = self.create_frame("Wont Have", 3, "#ff5050")



        
        # Input field and add button
        self.entry = ctk.CTkEntry(self.root, width=400,height=30, font=("Segoe UI", 17),
                              fg_color="white", bg_color="white", border_color=("#caedff")
                              )
        self.entry.insert(0, "Enter a task here")
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.grid(row=1, column=0, columnspan=2, pady=10, padx=10,
                        sticky="ew")
        self.entry.bind('<Return>', lambda event: self.add_task())

        self.add_button = ctk.CTkButton(
            self.root,
            text="Add Task",
            command=self.add_task,
            font=("Segoe UI", 17),
            fg_color=("white"),
            bg_color=("white"),
            text_color=("black"),
            hover_color=("#caedff"),
            border_color=("#caedff"),
            corner_radius=5,
           border_width=3,
            #width=100,
            #height=35

        )
        self.add_button.grid(row=1, column=2, pady=10, padx=10)

        for frame in [self.must_frame, self.should_frame, self.could_frame, self.wont_frame]:
            listbox = frame.listbox
            listbox.bind("<Button-1>", self.start_drag)
            listbox.bind("<B1-Motion>", self.do_drag)
            listbox.bind("<ButtonRelease-1>", self.stop_drag)

        self.drag_data = None

    def clear_placeholder(self, event):
            if self.entry.get() == "Enter a task here":
                self.entry.delete(0, tk.END)


    def create_frame(self, title, col, fg_color):
        frame = ctk.CTkFrame(self.root,fg_color=fg_color, border_width=50, border_color=fg_color)
        frame.grid(row=0, column=col, padx=10, pady=10, sticky="nsew")




        #label
        label = tk.Label(frame, text=title, font=("Segoe UI", 25, "bold"),
                        bg=fg_color, fg="white")
        label.pack(side=tk.TOP, fill=tk.X, pady=5)




        #listbox for tasks
        listbox = tk.Listbox(frame, height=15, width=25, font=("Segoe UI", 16),
                             bg="#edf2f4", fg="#2b2d42")
        listbox.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        frame.listbox = listbox





        # Buttons for moving tasks

        if col== 0:  # Must Have Column
            move_button = ctk.CTkButton(
                frame, text="Move to Should Have ->", fg_color="white", bg_color="#9ad1ff", text_color="black",
                hover_color=("#ebf8ff"), border_color=("#caedff"), corner_radius=5, border_width=1,
                font=("Segoe UI", 13),
                command=lambda: self.move_task(self.must_frame,
                                               self.should_frame)
            )
        elif col == 1: # Should Have column
            move_button = ctk.CTkButton(
                frame, text="Move to Could Have ->", fg_color="white", bg_color="#ff74c8", text_color="black",
                hover_color=("#fff0f9"), border_color=("#caedff"), corner_radius=5, border_width=1,
                font=("Segoe UI", 13),
                command=lambda: self.move_task(self.should_frame,
                                               self.could_frame)
            )
        elif col == 2: # Could Have column
            move_button = ctk.CTkButton(
                frame, text="Move to Wont Have ->", fg_color="white", bg_color="#ffa929", text_color="black",
                hover_color=("#fff6e9"), border_color=("#caedff"), corner_radius=5, border_width=1,
                font=("Segoe UI", 13),
                command=lambda: self.move_task(self.could_frame,
                                               self.wont_frame)
            )
        else: # Wont Have Column
            move_button = ctk.CTkButton(
                frame, text="  Delete Task  ", fg_color="white", bg_color="#ff5050", text_color="black",
                hover_color=("#ffeeee"), border_color=("#caedff"), corner_radius=5, border_width=1,
                font=("Segoe UI", 13),
                command=lambda: self.delete_task(self.wont_frame)
            )
        move_button.pack(side=tk.BOTTOM, pady=10)

        return frame
    

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.must_frame.listbox.insert(tk.END, task)
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
                                f"Task '{task}' has been deleted!")
        else:
            messagebox.showerror("Error", "No Task selected to delete!")




#Click and drag was made by chatgpt. I couldnt find any tutorials, documentation, or forums on how to click and drag
#I even asked chatgpt if i can find tutorials for me or to refine my search terms so i can get better results and It coulndt but it was able to do it somehow

    def start_drag(self, event):
        widget = event.widget
        index = widget.nearest(event.y)
        if index >= 0:
            self.drag_data = {
                "widget": widget,
                "index": index,
                "text": widget.get(index),
            }

    def do_drag(self, event):
        pass

    def stop_drag(self, event):
        if not self.drag_data:
            return

        drop_widget = event.widget.winfo_containing(event.x_root, event.y_root)
        if isinstance(drop_widget, tk.Listbox) and drop_widget != self.drag_data["widget"]:
            self.drag_data["widget"].delete(self.drag_data["index"])
            drop_widget.insert(tk.END, self.drag_data["text"])
        self.drag_data = None

    

# Initialize the app
if __name__ == "__main__":
    root = ctk.CTk()
    root.grid_columnconfigure((0, 1, 2, 3),
                             weight=1)
    root.grid_rowconfigure(0, weight=1)
    app = FeaturePrio(root)
    root.mainloop()