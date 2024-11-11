# app/app.py
from flask import Flask, request, render_template_string, jsonify
import sqlite3
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Database connection function for SQLite
def get_db_connection():
    connection = sqlite3.connect('database.db')
    return connection

# Vulnerable SQL Query (SQL Injection)
@app.route('/search')
def search():
    query = request.args.get('query')  # User input directly used in SQL query
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{query}'")  # SQL Injection vulnerability
    results = cursor.fetchall()
    connection.close()
    return jsonify([dict(zip([column[0] for column in cursor.description], row)) for row in results])

# Vulnerable XSS Endpoint
@app.route('/greet')
def greet():
    name = request.args.get('name', '')
    return render_template_string(f"<h1>Hello, {name}!</h1>")  # XSS vulnerability

@app.route('/')
def index():
    return render_template_string(open('templates/index.html').read())

if __name__ == "__main__":
    app.run(debug=True)
