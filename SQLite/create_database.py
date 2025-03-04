# Filename: create_database.py
# Desctiption: Create a sqlite database

# Cursor: Allows to execute sql commands


import sqlite3

# Create a file sqlite3 database
conn = sqlite3.connect("employee.db")

# Create a cursor
cursor = conn.cursor()


# cursor.execute("""
#     CREATE TABLE employees (
#         first text,
#         last text,
#         pay integer
#         )
#     """)


# Insert data
# cursor.execute("INSERT INTO employees VALUES ('John', 'Doe', 60000)")
cursor.execute("select * from employees")
print(cursor.fetchall())

emp = "employee"

# # Context manager
# # This way the connection is closed and commited automatically
# def add_employee(emp):
#     with conn:
#         cursor.execute("SQL STATMENT")



# Commit changes
conn.commit()

# Close connection
conn.close()