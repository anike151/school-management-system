from app.credential import get_connection

def sign_up(name, email, password):
    """Register a new user."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, email, password))
            connection.commit()
            return "User registered successfully!"
    except Exception as e:
        return f"Error: {e}"
    finally:
        connection.close()
