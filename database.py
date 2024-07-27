import sqlite3
from datetime import datetime

DATABASE_FILE = 'sensitive_info.db'

def init_db():
    """
    Initialize the database, create the necessary tables if they don't exist,
    and populate it with initial data.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensitive_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        content TEXT NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Populate the table with initial data
    initial_data = [
        ('LFI', 'Local File Inclusion vulnerability details'),
        ('credentials', 'User credentials found in the system'),
        ('SQLi', 'SQL Injection vulnerability details')
        ('names', 'Names of people in the system'),
        ('comments', 'Comments in the system'),
        ('subdomains', 'Subdomains in the system'),
        ('directories', 'Directories in the system'),
        ('locations', 'Locations in the system')
    ]
    
    cursor.executemany('''
    INSERT INTO sensitive_info (type, content)
    VALUES (?, ?)
    ''', initial_data)
    conn.commit()
    conn.close()

def store_sensitive_info(info_type, content):
    """
    Store sensitive information in the database.

    Args:
        info_type (str): The type of sensitive information (e.g., 'LFI', 'credentials').
        content (str): The content of the sensitive information.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO sensitive_info (type, content)
    VALUES (?, ?)
    ''', (info_type, content))
    
    conn.commit()
    conn.close()

# Initialize the database when the module is imported
init_db()

