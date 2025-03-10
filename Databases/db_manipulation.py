import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Default XAMPP user
    password="",  # No password by default
    database="world"  # Change to your database name
)
cursor = conn.cursor()

# cursor.execute("SHOW DATABASES")
cursor.execute(cursor.execute("SELECT SUM(SurfaceArea) AS 'N. America Surface Area', SUM(Population) AS 'N. America Population' FROM world.country WHERE Region = 'North America'")
)

result = cursor.fetchone()
surface_area = float(result[0])  # Convert to float
population = int(result[1])  # Convert to int

print("N. America Surface Area:", surface_area)
print("N. America Population:", population)

cursor.close()
conn.close()