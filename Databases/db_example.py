import sqlite3

# Step 1: Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Step 3: Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE      
)
''')

# Step 4: Insert data into the table
cursor.execute("INSERT INTO users (name, age, email) VALUES ('Steve', 28, 'steve@gmail.com')")
cursor.execute("INSERT INTO users (name, age, email) VALUES ('Joe', 25, 'joe@gmail.com')")
cursor.execute("INSERT INTO users (name, age, email) VALUES ('Bob', 25, 'bob@gmail.com')")

# Step 5: Commit the changes
conn.commit()

# Step 6: Query the database
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Display the results
print("Users in the database:")
for row in rows:
    print(row)

# Step 7: Update a record
cursor.execute("UPDATE users SET age = 31 WHERE name = 'Steve'")
conn.commit()

# Step 8: Delete a record
cursor.execute("DELETE FROM users WHERE name = 'Bob'")
conn.commit()

# Step 9: Query the database again
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("\nUsers after updates and deletions:")
for row in rows:
    print(row)

# Step 10: Close the connection
conn.close()