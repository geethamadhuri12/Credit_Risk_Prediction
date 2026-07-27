from database import conn

if conn.is_connected():
    print("Database Connected Successfully!")
else:
    print("Connection Failed")