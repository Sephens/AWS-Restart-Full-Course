import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="admin",  # Default XAMPP user
    password="yourpassword",  # No password by default
    database="world"  # Change to your database name
)
cursor = conn.cursor()

# cursor.execute("SHOW DATABASES;")
# for i in cursor:
#     print(i)

# cursor.execute("SELECT Region, Name, Population FROM world.country WHERE Region = 'Australia and New Zealand' ORDER By Population desc;")

# for i in cursor:
#     print(i)

cursor.execute("SELECT Region, Name, Population, SUM(Population) OVER(partition by Region ORDER BY Population) as 'Running Total' FROM world.country WHERE Region = 'Australia and New Zealand';")

for i in cursor:
    print(i)