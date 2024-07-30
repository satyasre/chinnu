import tkinter as tk 
from tkinter import messagebox,simpledialog 
from tkinter import ttk
def add_task():
    task=task_entry.get()
    start_date=start_date_entry.get()
    due_date=due_date_entry.get()
    if task and start_date and due_date:
        task_tree.insert("",tk.END,values=(task,start_date,due_date,"Incomplete"))
        task_entry.delete(0,tk.END)
        start_date_entry.delete(0,tk.END)
        due_date_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","You must enter a task,start date,and due date.")
def update_task():
    selected_item=task_tree.selection()
    if selected_item:
        current_task=task_tree.item(selected_item,'values')
        updated_task=simpledialog.askstring("Update Task","Update the task:",initialvalue=current_task[0])
        updated_start_date=simpledialog.askstring("Update Start Date","Update the start date:",initialvalue=current_task[1])
        updated_due_date=simpledialog.askstring("Update Due Date","Update the due date:",initialvalue=current_task[2])
        if updated_task and updated_start_date and updated_due_date:
            task_tree.item(selected_item,values=(updated_task,updated_start_date,updated_due_date,current_task[3]))
        else:
            messagebox.showwarning("Warning","You must select a task to update.")
def delete_task():
    selected_item=task_tree.selection()
    if selected_item:
        task_tree.delete(selected_item)
    else:
        messagebox.showwarning("Warning","You must select a task to delete.")
def toggle_status():
    selected_item=task_tree.selection()
    if selected_item:
        current_status=task_tree.item(selected_item,'values')[3]
        new_status="Complete" if current_status=="Incomplete" else "Incomplete"
        task_tree.item(selected_item,values=(task_tree.item(selected_item,'values')[0],task_tree(selected_item,'values')[1],task_tree(selected_item,'values')[2]))
    else:
        messagebox.showwarning("Warning","You must select a task to mark as completed.")
# Initialise the main window
root=tk.Tk()
root.title("To-Do List")
root.geometry("600x600")
root.configure(bg='#f0f8ff')

# Title label
title_label=ttk.Label(root,text="To-Do List",font=('Helvettica',16,'bold'),background='#f0f8ff',foreground='#000080')
title_label.pack(pady=10)

# Task entry fields with labels
entry_frame=tk.Frame(root,bg='#f0f8ff')
entry_frame.pack(pady=10)

task_label=ttk.Label(entry_frame,text="Task:",font=('Helvetica',12),background='#f0f8ff')
task_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.E)
task_entry=ttk.Entry(entry_frame,width=30,font=('Helvetica',12))
task_entry.grid(row=0,column=1,padx=5,pady=5)

start_date_label=ttk.Label(entry_frame,text="Start Date:",font=('Helvetica',12),background='#f0f8ff')
start_date_label.grid(row=1,column=0,padx=5,pady=5,sticky=tk.E)
start_date_entry=ttk.Entry(entry_frame,width=30,font=('Helvetica',12))
start_date_entry.grid(row=1,column=1,padx=5,pady=5)

due_date_label=ttk.Label(entry_frame,text="Due Date:",font=('Helvetica',12),background='#f0f8ff')
due_date_label.grid(row=2,column=0,padx=5,pady=5,sticky=tk.E)
due_date_entry=ttk.Entry(entry_frame,width=30,font=('Helvetica',12))
due_date_entry.grid(row=2,column=1,padx=5,pady=5)

# Treeview to display tasks
style=ttk.Style()
style.configure("Treeview.Heading",font=('Helvetica',12,'bold'),background='#4682b4',foreground='white')
style.configure("Treeview",font=('Helvetica',11),background='white',foreground='black',rowheight=25,fieldbackground='white')
style.map("Treeview",background=[('selected','#6fa6db')],foreground=[('selected','white')])

columns=("Task","Start Date","Due Date","Status")
task_tree=ttk.Treeview(root,columns=columns,show='headings',selectmode='browse')
task_tree.heading("Task",text="Task")
task_tree.heading("Start Date",text="Start Date")
task_tree.heading("Due Date",text="Due Date")
task_tree.heading("Status",text="Status")
task_tree.column("Task",width=200)
task_tree.column("Start Date",width=100)
task_tree.column("Due Date",width=100)
task_tree.column("Status",width=80)
task_tree.pack(pady=10,fill=tk.BOTH,expand=True)

# Scroller for the treeview
scrollbar=ttk.Scrollbar(root,orient=tk.VERTICAL,command=task_tree.yview)
task_tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

# Buttons for add,update,delete,and toggle status
button_frame=tk.Frame(root,bg='#f0f8ff')
button_frame.pack(pady=10)

add_button=ttk.Button(button_frame,text="Add Task",command=add_task)
add_button.grid(row=0,column=0,padx=5)

update_button=ttk.Button(button_frame,text="Update Task",command=update_task)
update_button.grid(row=0,column=1,padx=5)

delete_button=ttk.Button(button_frame,text="Delete Task",command=delete_task)
delete_button.grid(row=0,column=2,padx=5)

toggle_button=ttk.Button(button_frame,text="Mark as Completed",command=toggle_status)
toggle_button.grid(row=0,column=3,padx=5)

# Pack and display the main window
root.mainloop()
