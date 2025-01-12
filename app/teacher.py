from app.credential import get_connection

def list_teachers():
    """Retrieve a list of all teachers."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM teachers"
            cursor.execute(sql)
            teachers = cursor.fetchall()
            return teachers
    finally:
        connection.close()
