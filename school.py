import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1ms22cs040",
    database="attendance_management"
)

cursor = db.cursor()

# Functions
def add_student():
    name = entry_name.get()
    roll_no = entry_roll_no.get()
    if not name or not roll_no:
        messagebox.showerror("Input Error", "All fields are required!")
        return
    try:
        cursor.execute("INSERT INTO students (name, roll_no) VALUES (%s, %s)", (name, roll_no))
        db.commit()
        messagebox.showinfo("Success", "Student added successfully!")
        entry_name.delete(0, tk.END)
        entry_roll_no.delete(0, tk.END)
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def mark_attendance():
    roll_no = entry_roll_no_attendance.get()
    status = attendance_status.get()
    if not roll_no or not status:
        messagebox.showerror("Input Error", "All fields are required!")
        return
    try:
        cursor.execute("SELECT student_id FROM students WHERE roll_no = %s", (roll_no,))
        student = cursor.fetchone()
        if student:
            student_id = student[0]
            cursor.execute(
                "INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)",
                (student_id, datetime.now().date(), status)
            )
            db.commit()
            messagebox.showinfo("Success", "Attendance marked successfully!")
            entry_roll_no_attendance.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Student not found!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def view_attendance():
    try:
        cursor.execute("""
            SELECT students.roll_no, students.name, attendance.date, attendance.status
            FROM attendance
            JOIN students ON attendance.student_id = students.student_id
        """)
        records = cursor.fetchall()
        attendance_window = tk.Toplevel(root)
        attendance_window.title("Attendance Records")
        for idx, record in enumerate(records, start=1):
            tk.Label(attendance_window, text=f"{idx}. Roll No: {record[0]}, Name: {record[1]}, Date: {record[2]}, Status: {record[3]}").pack()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
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


# GUI setup
root = tk.Tk()
root.title("Student Attendance Management System")

# Add Student Section
frame_add = tk.LabelFrame(root, text="Add Student")
frame_add.pack(fill="both", expand="yes", padx=10, pady=10)

tk.Label(frame_add, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(frame_add)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_add, text="Roll No:").grid(row=1, column=0, padx=10, pady=5)
entry_roll_no = tk.Entry(frame_add)
entry_roll_no.grid(row=1, column=1, padx=10, pady=5)

btn_add = tk.Button(frame_add, text="Add Student", command=add_student)
btn_add.grid(row=2, columnspan=2, pady=10)

# Mark Attendance Section
frame_attendance = tk.LabelFrame(root, text="Mark Attendance")
frame_attendance.pack(fill="both", expand="yes", padx=10, pady=10)

tk.Label(frame_attendance, text="Roll No:").grid(row=0, column=0, padx=10, pady=5)
entry_roll_no_attendance = tk.Entry(frame_attendance)
entry_roll_no_attendance.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_attendance, text="Status:").grid(row=1, column=0, padx=10, pady=5)
attendance_status = tk.StringVar(value="Present")
tk.OptionMenu(frame_attendance, attendance_status, "Present", "Absent").grid(row=1, column=1, padx=10, pady=5)

btn_mark = tk.Button(frame_attendance, text="Mark Attendance", command=mark_attendance)
btn_mark.grid(row=2, columnspan=2, pady=10)

# View Attendance Section
btn_view = tk.Button(root, text="View Attendance Records", command=view_attendance)
btn_view.pack(pady=10)
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

course_window = tk.Toplevel(root)
course_window.title("Course Management")

tk.Label(course_window, text="Course Name:").grid(row=0, column=0, padx=10, pady=10)
course_name_entry = tk.Entry(course_window)
course_name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(course_window, text="Teacher ID:").grid(row=1, column=0, padx=10, pady=10)
teacher_id_entry = tk.Entry(course_window)
teacher_id_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(course_window, text="Add Course", command=add_course).grid(row=2, column=0, columnspan=2, pady=20)

# Run the GUI
root.mainloop()

# Close database connection
db.close()
