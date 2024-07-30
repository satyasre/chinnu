import tkinter as tk
from tkinter import ttk

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.configure(bg='white')

# Entry field
entry = ttk.Entry(root, font=('Helvetica', 20), justify='right')
entry.pack(fill=tk.BOTH, ipadx=10, ipady=10, padx=10, pady=10)

# Button frame
button_frame = tk.Frame(root, bg='white')
button_frame.pack(expand=True, fill=tk.BOTH)

# Button configurations
number_button_config = {
    'font': ('Helvetica', 18), 
    'bg': '#E1F5FE', 
    'fg': 'black', 
    'bd': 1, 
    'highlightthickness': 0, 
    'activebackground': '#B3E5FC', 
    'activeforeground': 'black'
}

operator_button_config = {
    'font': ('Helvetica', 18), 
    'bg': '#FFCDD2', 
    'fg': 'black', 
    'bd': 1, 
    'highlightthickness': 0, 
    'activebackground': '#EF9A9A', 
    'activeforeground': 'black'
}

special_button_config = {
    'font': ('Helvetica', 18), 
    'bg': '#C8E6C9', 
    'fg': 'black', 
    'bd': 1, 
    'highlightthickness': 0, 
    'activebackground': '#A5D6A7', 
    'activeforeground': 'black'
}

# Buttons
buttons = [
    ('C', 0, 0, 1, 2), ('/', 0, 2, 1, 1), ('*', 0, 3, 1, 1),
    ('7', 1, 0, 1, 1), ('8', 1, 1, 1, 1), ('9', 1, 2, 1, 1), ('-', 1, 3, 1, 1),
    ('4', 2, 0, 1, 1), ('5', 2, 1, 1, 1), ('6', 2, 2, 1, 1), ('+', 2, 3, 1, 1),
    ('1', 3, 0, 1, 1), ('2', 3, 1, 1, 1), ('3', 3, 2, 1, 1), ('=', 3, 3, 2, 1),
    ('0', 4, 0, 1, 2), ('.', 4, 2, 1, 1)
]

for (text, row, col, rowspan, colspan) in buttons:
    if text in {'+', '-', '*', '/', '='}:
        button = tk.Button(button_frame, text=text, command=lambda t=text: button_click(t) if t != '=' else calculate(), **operator_button_config)
    elif text == 'C':
        button = tk.Button(button_frame, text=text, command=clear, **special_button_config)
    else:
        button = tk.Button(button_frame, text=text, command=lambda t=text: button_click(t), **number_button_config)
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky='nsew', padx=5, pady=5)

# Configure grid
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()