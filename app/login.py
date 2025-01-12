from app.credential import get_connection

def login(email, password):
    """Authenticate user by email and password."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email=%s AND password=%s"
            cursor.execute(sql, (email, password))
            user = cursor.fetchone()
            return user
    finally:
        connection.close()
