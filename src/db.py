import sqlite3

def initialize_database():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    # Create the expenses table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

if name == "main":
    initialize_database()
    print("Database initialized successfully!")
