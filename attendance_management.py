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
def record_attendance():
    student_id = attendance_student_id_entry.get()
    course_id = attendance_course_id_entry.get()
    date = attendance_date_entry.get()
    status = attendance_status_entry.get()

    if student_id and course_id and date and status:
        query = "INSERT INTO attendance (student_id, course_id, date, status) VALUES (%s, %s, %s, %s)"
        values = (student_id, course_id, date, status)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Attendance recorded successfully")
        clear_attendance_fields()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

def clear_attendance_fields():
    attendance_student_id_entry.delete(0, tk.END)
    attendance_course_id_entry.delete(0, tk.END)
    attendance_date_entry.delete(0, tk.END)
    attendance_status_entry.delete(0, tk.END)

# GUI for Attendance Tracking
attendance_window = tk.Toplevel(root)
attendance_window.title("Attendance Tracking")

tk.Label(attendance_window, text="Student ID:").grid(row=0, column=0, padx=10, pady=10)
attendance_student_id_entry = tk.Entry(attendance_window)
attendance_student_id_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(attendance_window, text="Course ID:").grid(row=1, column=0, padx=10, pady=10)
attendance_course_id_entry = tk.Entry(attendance_window)
attendance_course_id_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(attendance_window, text="Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)
attendance_date_entry = tk.Entry(attendance_window)
attendance_date_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(attendance_window, text="Status:").grid(row=3, column=0, padx=10, pady=10)
attendance_status_entry = tk.Entry(attendance_window)
attendance_status_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Button(attendance_window, text="Record Attendance", command=record_attendance).grid(row=4, column=0, columnspan=2, pady=20)
