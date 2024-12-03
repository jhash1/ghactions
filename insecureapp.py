import sqlite3
import os

# Database setup
def setup_database():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

# Function with an SQL injection vulnerability
def fetch_user(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Vulnerable query (SQL injection)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"Executing query: {query}")
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Function with command injection vulnerability
def execute_command(command):
    # Vulnerable to command injection
    os.system(command)

# Main function
def main():
    setup_database()
    
    # Add a test user
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("testuser", "password123"))
    conn.commit()
    conn.close()

    # Prompt user for input (vulnerable to SQL injection)
    username = input("Enter username to search: ")
    user_data = fetch_user(username)
    print(f"User data: {user_data}")

    # Prompt user for command (vulnerable to command injection)
    command = input("Enter command to execute: ")
    execute_command(command)

if __name__ == "__main__":
    main()
