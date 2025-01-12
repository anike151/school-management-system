from flask import Flask, render_template, request, redirect, url_for
from app.login import login
from app.sign_up import sign_up
from app.attendance_management import mark_attendance, view_attendance
from app.course import list_courses
from app.teacher import list_teachers
import os
import sys

print("Current working directory:", os.getcwd())
print("Python PATH:", sys.path)


app = Flask(__name__, template_folder="../templates")


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def user_login():
    email = request.form["email"]
    password = request.form["password"]
    user = login(email, password)
    if user:
        return redirect(url_for("dashboard"))
    return "Invalid credentials!"

@app.route("/sign_up", methods=["POST", "GET"])
def register_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        message = sign_up(name, email, password)
        return message
    return render_template("sign_up.html")

@app.route("/dashboard")
def dashboard():
    courses = list_courses()
    teachers = list_teachers()
    return render_template("dashboard.html", courses=courses, teachers=teachers)

@app.route("/attendance", methods=["POST"])
def attendance():
    student_id = request.form["student_id"]
    course_id = request.form["course_id"]
    status = request.form["status"]
    result = mark_attendance(student_id, course_id, status)
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
