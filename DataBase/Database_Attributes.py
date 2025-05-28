import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
db = mysql.connector.connect(
    host=os.getenv("host"),
    port=os.getenv("port"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database"),
)
if db.is_connected():
    print('Database Connected')
else:
    print('Database is Interrupted')