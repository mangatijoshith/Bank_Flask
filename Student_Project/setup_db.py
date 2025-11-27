import sqlite3

# 1. Create/Connect to the file
connection = sqlite3.connect('university.db')
cursor = connection.cursor()

# 2. Create the Table (The Structure)
# We add "IF NOT EXISTS" so it doesn't crash if you run it twice
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        marks INTEGER
    )
''')

# 3. Insert Dummy Data (The Content)
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Alice", 90))
cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", ("Bob", 85))

# 4. Save and Close
connection.commit()
connection.close()
print("✅ Database 'university.db' created successfully with 2 students!")