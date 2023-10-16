import tkinter as tk
from tkinter import Toplevel, messagebox
from PIL import Image, ImageTk


class TODOLISTAPP:
    def __init__(self, root):
        self.root = root
        self.root.title("TO DO LIST")
        self.root.geometry("1000x700")

        #setting up background image for todolist app.
        background_image = Image.open("flat-lay-workstation-with-copy-space-laptop.jpg")  # Replace with your image file
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(root, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.page_title = tk.Label(root, text="WELCOME TO TODO LIST", font=("Helvetica", 14))
        self.page_title.place(x=70, y=10)

        self.input_frame = tk.Frame(root)
        self.input_frame.place(x=20, y=150, width=450)
        self.text_entry = tk.Entry(self.input_frame, font=("Helvetica", 17))
        self.text_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(self.input_frame, text="ADD TASK", font=("Helvetica", 15), command=self.add_task, bg="#3498db")
        self.add_button.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_list = tk.Listbox(root, font=("Helvetica", 24), selectmode=tk.SINGLE)
        self.task_list.place(x=500, y=200, relwidth=0.5, relheight=0.5)  # Adjust the relheight value as needed
        self.task_list.bind('<<ListboxSelect>>', self.on_task_select)

        #self.task_list = tk.Listbox(root, font=("Helvetica", 15), selectmode=tk.SINGLE)
        #self.task_list.place(x=500, y=200, relwidth=0.5, height=400)
        #self.task_list.bind('<<ListboxSelect>>', self.on_task_select)

        self.delete_button = tk.Button(root, text="DELETE TASK", font=("Helvetica", 15), command=self.delete_task, bg="red")
        self.delete_button.place(x=500, y=610, width=225)

        self.edit_button = tk.Button(root, text="EDIT TASK", font=("Helvetica", 15), command=self.edit_task, bg="green")
        self.edit_button.place(x=725, y=610, width=225)

        self.delete_all_button = tk.Button(root, text="DELETE ALL", font=("Helvetica", 15), command=self.delete_all, bg="orange")
        self.delete_all_button.place(x=950, y=610, width=225)

        self.selected_task_index = None
        self.edit_window = None

    def add_task(self):
        task = self.text_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.text_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("info", "cool....fill the field first.")

    def delete_task(self):
        if self.selected_task_index:
            self.task_list.delete(self.selected_task_index)
            self.selected_task_index = None
        else:
            messagebox.showinfo("error", "yo...select task to delete.")

    def delete_all(self):
        if self.task_list.size() == 0:
            messagebox.showinfo("Info", "Nothing to delete.")
        else:
            self.task_list.delete(0, tk.END)

    def on_task_select(self, event):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.selected_task_index = selected_task_index

    def edit_task(self):
        if self.selected_task_index:
            selected_task = self.task_list.get(self.selected_task_index)
            self.edit_window = Toplevel(self.root)
            self.edit_window.title("Edit Task")
            self.edit_entry = tk.Entry(self.edit_window, font=("Helvetica", 17))
            self.edit_entry.pack(fill=tk.BOTH, expand=True)
            self.edit_entry.insert(0, selected_task)
            save_button = tk.Button(self.edit_window, text="Save", font=("Helvetica", 15), command=self.save_edit)
            save_button.pack()
        else:
            messagebox.showinfo("error", "select task to edit.")

    def save_edit(self):
        edited_task = self.edit_entry.get()
        if edited_task:
            self.task_list.delete(self.selected_task_index)
            self.task_list.insert(self.selected_task_index, edited_task)
            self.edit_window.destroy()
            self.selected_task_index = None

if __name__ == '__main__':
    root = tk.Tk()
    app = TODOLISTAPP(root)
    root.mainloop()
