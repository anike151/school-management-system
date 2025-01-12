import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1ms22cs040",
    database="school_management"
)
cursor = db.cursor()
def add_course():
    course_name = course_name_entry.get()
    teacher_id = teacher_id_entry.get()

    if course_name and teacher_id:
        query = "INSERT INTO courses (course_name, teacher_id) VALUES (%s, %s)"
        values = (course_name, teacher_id)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Course added successfully")
        clear_course_fields()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

def clear_course_fields():
    course_name_entry.delete(0, tk.END)
    teacher_id_entry.delete(0, tk.END)

# GUI for Course Management
course_window = tk.Toplevel(root)
course_window.title("Course Management")

tk.Label(course_window, text="Course Name:").grid(row=0, column=0, padx=10, pady=10)
course_name_entry = tk.Entry(course_window)
course_name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(course_window, text="Teacher ID:").grid(row=1, column=0, padx=10, pady=10)
teacher_id_entry = tk.Entry(course_window)
teacher_id_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(course_window, text="Add Course", command=add_course).grid(row=2, column=0, columnspan=2, pady=20)
