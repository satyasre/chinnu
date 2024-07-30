import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x400")
        self.root.configure(bg='lightblue')

        self.contacts = []

        # Title label
        self.title_label = ttk.Label(root, text="Contact Book", font=('Helvetica', 16, 'bold'), background='lightblue', foreground='darkblue')
        self.title_label.pack(pady=10)

        # Contact list frame
        self.contact_list_frame = tk.Frame(root, bg='lightblue')
        self.contact_list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Treeview to display contacts
        self.columns = ("Name", "Phone", "Email")
        self.contact_tree = ttk.Treeview(self.contact_list_frame, columns=self.columns, show='headings')
        for col in self.columns:
            self.contact_tree.heading(col, text=col)
            self.contact_tree.column(col, minwidth=0, width=150)
        self.contact_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the treeview
        self.scrollbar = ttk.Scrollbar(self.contact_list_frame, orient=tk.VERTICAL, command=self.contact_tree.yview)
        self.contact_tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Button frame
        self.button_frame = tk.Frame(root, bg='lightblue')
        self.button_frame.pack(pady=10)

        # Buttons for add, update, delete, search, and view all contacts
        self.add_button = ttk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=5)

        self.update_button = ttk.Button(self.button_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=0, column=1, padx=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.search_button = ttk.Button(self.button_frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=0, column=3, padx=5)

        self.view_all_button = ttk.Button(self.button_frame, text="View All Contacts", command=self.view_all_contacts)
        self.view_all_button.grid(row=0, column=4, padx=5)

        # Configure styles
        style = ttk.Style(root)
        style.configure('TButton', font=('Helvetica', 12), background='gold', foreground='black')
        style.configure('TLabel', font=('Helvetica', 12), background='lightblue', foreground='black')
        style.configure('Treeview', font=('Helvetica', 12))
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        phone = simpledialog.askstring("Input", "Enter Phone:")
        email = simpledialog.askstring("Input", "Enter Email:")
        if name and phone and email:
            self.contacts.append((name, phone, email))
            self.contact_tree.insert("", tk.END, values=(name, phone, email))
        else:
            messagebox.showwarning("Warning", "All fields must be filled out")

    def update_contact(self):
        selected_item = self.contact_tree.selection()
        if selected_item:
            current_values = self.contact_tree.item(selected_item, 'values')
            new_name = simpledialog.askstring("Input", "Update Name:", initialvalue=current_values[0])
            new_phone = simpledialog.askstring("Input", "Update Phone:", initialvalue=current_values[1])
            new_email = simpledialog.askstring("Input", "Update Email:", initialvalue=current_values[2])
            if new_name and new_phone and new_email:
                self.contact_tree.item(selected_item, values=(new_name, new_phone, new_email))
                self.contacts = [(new_name, new_phone, new_email) if contact == current_values else contact for contact in self.contacts]
            else:
                messagebox.showwarning("Warning", "All fields must be filled out")
        else:
            messagebox.showwarning("Warning", "You must select a contact to update")

    def delete_contact(self):
        selected_item = self.contact_tree.selection()
        if selected_item:
            current_values = self.contact_tree.item(selected_item, 'values')
            self.contacts = [contact for contact in self.contacts if contact != current_values]
            self.contact_tree.delete(selected_item)
        else:
            messagebox.showwarning("Warning", "You must select a contact to delete")

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter search term (name, phone, or email):")
        if search_term:
            search_results = [contact for contact in self.contacts if search_term.lower() in map(str.lower, contact)]
            self.contact_tree.delete(*self.contact_tree.get_children())
            for contact in search_results:
                self.contact_tree.insert("", tk.END, values=contact)
        else:
            messagebox.showwarning("Warning", "You must enter a search term")

    def view_all_contacts(self):
        self.contact_tree.delete(*self.contact_tree.get_children())
        for contact in self.contacts:
            self.contact_tree.insert("", tk.END, values=contact)

# Initialize the main window
root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()