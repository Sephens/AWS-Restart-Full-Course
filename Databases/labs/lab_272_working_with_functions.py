import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Default XAMPP user
    password="",  # No password by default
    database="world"  # Change to your database name
)
cursor = conn.cursor()

# To show the existing databases
#------------------------------------------------------------------------
# cursor.execute("SHOW DATABASES;")
# for i in cursor:
#     print(i)
#------------------------------------------------------------------------



# To review the table schema, data, and number of rows in the country table,
#------------------------------------------------------------------------
# cursor.execute("SELECT * FROM world.country;")
# for i in cursor:
#     print(i)
#----------------------------------------------------------------------



# The following query demonstrates how to use aggregate functions SUM(), MIN(), MAX(), and AVG() to summarize data. Because the query does not include a WHERE condition, the functions aggregate data from all records in the country table.
#------------------------------------------------------------------------
cursor.execute(
    "SELECT sum(Population), avg(Population), max(Population), min(Population), count(Population) FROM world.country;"
)
result = cursor.fetchone()
for sum,average,max,min in cursor:
    sum = float(result[0])
    average = float(result[1])
    max = float(result[2])
    min = float(result[3])

    print(f"Total population: {sum}")
    print(f"Average population: {average}")
    print(f"Maximum population: {max}")
    print(f"Minimum population: {min}")