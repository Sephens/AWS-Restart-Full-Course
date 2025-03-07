import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Databases/world.db')
cursor = conn.cursor()

# Read the SQL file
with open('Databases/world.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit the changes
conn.commit()

# Close the connection
cursor.close()
conn.close()