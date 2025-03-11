import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="admin",  # Default XAMPP user
    password="yourpassword",  # No password by default
    database="world"  # Change to your database name
)
cursor = conn.cursor()

# cursor.execute("SHOW DATABASES")
# cursor.execute(cursor.execute("SELECT SUM(SurfaceArea) AS 'N. America Surface Area', SUM(Population) AS 'N. America Population' FROM world.country WHERE Region = 'North America'")
# )

# cursor.execute("select Name, Population from city where Population > 10000000")

# cursor.execute("SELECT Name, Region, Population FROM country WHERE Population > 15000000 AND Region = 'South America' ORDER BY Population DESC")
# for i in cursor:
#     print(i)


#----- 1. Search Conditions and the WHERE Clause-----------------------

# cursor.execute(
# "SELECT name, population FROM city WHERE population > 1000000;"
# )

# for i in cursor:
#     print(i)

#--------------------------------------------------------------------

#--------------------2. Aliases--------------------------------------
# cursor.execute(
#     "SELECT name, population AS pop FROM city;"
# )

# for i in cursor:
#     print(i)

#--------------------------------------------------------------------

#--------------3. Operator Precedence-----------------------------------

# cursor.execute(
# "SELECT name, population FROM city WHERE (countrycode = 'USA' OR countrycode = 'CAN') AND population > 1000000;"
# )

# for i in cursor:
#     print(i)

#--------------------------------------------------------------------



#------------------------4. Arithmetic Operators-----------------------
# cursor.execute(
# "    SELECT name, lifeexpectancy, lifeexpectancy + 5.5 AS new_lifeexpectancy FROM country WHERE gnp > 1300000;"
# )
# results = cursor.fetchall()
# if results:  # Check if results exist
#     for country, lifeExpect, newLifeExpect in results:
#         print(f"Country: -> {country}, Life Expectancy: -> {float(lifeExpect)}, New Life Expectancy: -> {float(newLifeExpect)}")
# else:
#     print("No results found.")
#--------------------------------------------------------------------

#-------------------------5. Comparison Operators------------------------
# cursor.execute(
#     "SELECT name, population FROM city WHERE population > 5000000;"
# )

# for city, population in cursor:
#     print(f"{city} city has a population of: {population}")
#--------------------------------------------------------------------

#---------------6. Logical Operators------------------------------------
# cursor.execute(
#     "SELECT name, district, population FROM city WHERE countrycode = 'IND' AND district = 'Delhi';"
# )

# for name, district, population in cursor:
#     print(f"Name: {name}, District: {district}, Population: {population}")
#--------------------------------------------------------------------

#---------------7. LIKE Operator with Wildcards-------------------------
# cursor.execute(
#     "SELECT name, district FROM city WHERE district LIKE 'West%';"
# )

# for name, district in cursor:
#     print(f"✅ City: {name}, District: {district}")
#--------------------------------------------------------------------

#---------------------8. BETWEEN Operator-------------------------------
# cursor.execute(
#     "SELECT name, population FROM city WHERE population BETWEEN 500000 AND 505000;"
# )

# print("Cities with a population between 500000 and 505000")
# print("--------------------------------------------------")

# for name, population in cursor:
#     print(f"{name} city has a population of: {population}")

#--------------------------------------------------------------------

#--------------------------9. NULL Values--------------------------------
cursor.execute(
"SELECT name, lifeexpectancy FROM country WHERE lifeexpectancy IS NULL;"
)

print("Cities with NULL life expectancy")

for city, lifeExpect in cursor:
    print(city)
#--------------------------------------------------------------------


#--------------------------10. Aliases----------------------------------
# cursor.execute(
#     "SELECT name, population AS pop FROM city WHERE population > 1000000;"
# )
#--------------------------------------------------------------------


#--------------------------------------------------------------------

# result = cursor.fetchone()
# surface_area = float(result[0])  # Convert to float
# population = int(result[1])  # Convert to int

# print("N. America Surface Area:", surface_area)
# print("N. America Population:", population)






# ***********************************************************************
# WORKING WITH FUNCTIONS
#************************************************************************

#-----------------------Aggregate Functions-----------------------------

# Common Aggregate Functions:
# COUNT: Returns the number of rows in a set.
# SUM: Returns the sum of all values in a set.
# AVG: Returns the average of all values in a set.
# MIN: Returns the minimum value in a set.
# MAX: Returns the maximum value in a set.

# rows = cursor.execute(
#     "SELECT COUNT(*) AS 'Total Number of Rows' FROM countrylanguage;"

# )

# print(rows)















# cursor.close()
# conn.close()