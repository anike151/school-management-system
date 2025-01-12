import tkinter as tk
from tkinter import messagebox
from attendance_management import attendance_window
from course import course_registration_window
import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1ms22cs040",
        database="school_management"
    )


def main_menu():
    root = tk.Tk()
    root.title("School Management System")
    root.geometry("500x400")

    tk.Button(root, text="Manage Attendance", command=attendance_window).grid(row=0, column=0, pady=20, padx=20)
    tk.Button(root, text="Register for Courses", command=course_registration_window).grid(row=1, column=0, pady=20, padx=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
