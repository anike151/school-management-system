from app.credential import get_connection

def list_courses():
    """Retrieve a list of all courses."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM courses"
            cursor.execute(sql)
            courses = cursor.fetchall()
            return courses
    finally:
        connection.close()
