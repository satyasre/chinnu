import tkinter as tk
from tkinter import ttk
import string
import random

def generate_password():
    length = int(length_spinbox.get())
    include_letters = letters_var.get()
    include_numbers = numbers_var.get()
    include_specials = specials_var.get()
    
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_specials:
        characters += string.punctuation
        
    if characters:
        password = "".join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    else:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "No character set selected")

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg='lightblue')

# Title label
title_label = ttk.Label(root, text="Password Generator", font=('Helvetica', 16, 'bold'), background='lightblue', foreground='darkblue')
title_label.pack(pady=10)

# Password length
length_label = ttk.Label(root, text="Password Length:", font=('Helvetica', 12), background='lightblue', foreground='black')
length_label.pack(pady=5)
length_spinbox = ttk.Spinbox(root, from_=6, to_=32, width=5, font=('Helvetica', 12))
length_spinbox.set(12)
length_spinbox.pack(pady=5)

# Options
options_frame = tk.Frame(root, bg='lightblue')
options_frame.pack(pady=10)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)

letters_check = ttk.Checkbutton(options_frame, text="Include Letters", variable=letters_var, onvalue=True, offvalue=False, style='TCheckbutton')
letters_check.grid(row=0, column=0, padx=5, pady=5)

numbers_check = ttk.Checkbutton(options_frame, text="Include Numbers", variable=numbers_var, onvalue=True, offvalue=False, style='TCheckbutton')
numbers_check.grid(row=0, column=1, padx=5, pady=5)

specials_check = ttk.Checkbutton(options_frame, text="Include Specials", variable=specials_var, onvalue=True, offvalue=False, style='TCheckbutton')
specials_check.grid(row=0, column=2, padx=5, pady=5)

# Password entry
password_entry = ttk.Entry(root, font=('Helvetica', 12), width=30)
password_entry.pack(pady=10)

# Generate button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password, style='TButton')
generate_button.pack(pady=10)

# Configure styles
style = ttk.Style(root)
style.configure('TButton', font=('Helvetica', 12), background='gold', foreground='black')
style.configure('TCheckbutton', background='lightblue', foreground='black', font=('Helvetica', 12))

# Pack and display the main window
root.mainloop()