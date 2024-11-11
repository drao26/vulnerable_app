# app/initialise_db.py
import sqlite3

# Connect to the SQLite database (or create it if it doesn’t exist)
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Create the `users` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert some sample data into the `users` table
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'mypassword')")

# Commit changes and close the connection
connection.commit()
connection.close()

print("Database and table created successfully with sample data.")
