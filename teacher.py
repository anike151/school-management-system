import tkinter as tk
from tkinter import messagebox
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1ms22cs040",
    database="school_management"
)
cursor = db.cursor()

def add_teacher():
    name = teacher_name_entry.get()
    subject = teacher_subject_entry.get()
    contact = teacher_contact_entry.get()

    if name and subject and contact:
        query = "INSERT INTO teachers (name, subject, contact) VALUES (%s, %s, %s)"
        values = (name, subject, contact)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Teacher added successfully")
        clear_teacher_fields()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

def clear_teacher_fields():
    teacher_name_entry.delete(0, tk.END)
    teacher_subject_entry.delete(0, tk.END)
    teacher_contact_entry.delete(0, tk.END)

# GUI for Teacher Management
teacher_window = tk.Toplevel(root)
teacher_window.title("Teacher Management")

tk.Label(teacher_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
teacher_name_entry = tk.Entry(teacher_window)
teacher_name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(teacher_window, text="Subject:").grid(row=1, column=0, padx=10, pady=10)
teacher_subject_entry = tk.Entry(teacher_window)
teacher_subject_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(teacher_window, text="Contact:").grid(row=2, column=0, padx=10, pady=10)
teacher_contact_entry = tk.Entry(teacher_window)
teacher_contact_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(teacher_window, text="Add Teacher", command=add_teacher).grid(row=3, column=0, columnspan=2, pady=20)
