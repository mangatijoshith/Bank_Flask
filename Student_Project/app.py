import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# --- Helper Function ---
# This connects to the database safely
def get_db_connection():
    conn = sqlite3.connect('university.db')
    # This magic line makes rows look like Dictionaries (key:value)
    conn.row_factory = sqlite3.Row 
    return conn

# --- Route 1: Homepage ---
@app.route('/')
def home():
    return "<h1>Student System is Online!</h1><p>Go to <a href='/api/students'>/api/students</a> to see data.</p>"

# --- Route 2: The API (JSON) ---
@app.route('/api/students')
def get_students():
    conn = get_db_connection()
    
    # 1. Fetch data from the DB file
    rows = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    
    # 2. Convert database rows to Python List of Dicts
    student_list = []
    for row in rows:
        student_list.append({
            "id": row['id'],
            "name": row['name'],
            "marks": row['marks']
        })
        
    # 3. Send as JSON
    return jsonify(student_list)

if __name__ == '__main__':
    app.run(debug=True)