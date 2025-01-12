import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    """Establish and return a database connection."""
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        cursorclass=pymysql.cursors.DictCursor,
    )
