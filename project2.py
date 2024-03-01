import sqlite3

# Function to create a new student table
def create_student_table():
    conn = sqlite3.connect('students.db')  # Connect to or create the database file
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 age INTEGER,
                 email TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()

# Function to add a new student
def add_student(name, age, email):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''INSERT INTO students (name, age, email) VALUES (?, ?, ?)''', (name, age, email))
    conn.commit()
    conn.close()

# Function to retrieve all students
def get_all_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM students''')
    students = c.fetchall()
    conn.close()
    return students

# Function to search for a student by email
def search_student_by_email(email):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM students WHERE email=?''', (email,))
    student = c.fetchone()
    conn.close()
    return student

# Function to delete a student by email
def delete_student(email):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''DELETE FROM students WHERE email=?''', (email,))
    conn.commit()
    conn.close()

# Example usage
if __name__ == "__main__":
    create_student_table()
    add_student("John Doe", 20, "john@example.com")
    add_student("Jane Smith", 22, "jane@example.com")

    print("All Students:")
    print(get_all_students())

    print("\nSearching for student with email 'john@example.com':")
    print(search_student_by_email("john@example.com"))

    print("\nDeleting student with email 'john@example.com':")
    delete_student("john@example.com")
    print(get_all_students())
