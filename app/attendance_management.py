from app.credential import get_connection

def mark_attendance(student_id, course_id, status):
    """Mark attendance for a student in a specific course."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO attendance (student_id, course_id, status) VALUES (%s, %s, %s)"
            cursor.execute(sql, (student_id, course_id, status))
            connection.commit()
            return "Attendance marked successfully!"
    except Exception as e:
        return f"Error: {e}"
    finally:
        connection.close()

def view_attendance(student_id):
    """View attendance records for a student."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM attendance WHERE student_id=%s"
            cursor.execute(sql, (student_id,))
            attendance_records = cursor.fetchall()
            return attendance_records
    finally:
        connection.close()
