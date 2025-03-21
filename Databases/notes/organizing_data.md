# Organizing Data - Comprehensive Notes and Examples

This document provides a detailed summary of the "Organizing Data" module, including key concepts, syntax, examples, and important considerations.

---

## Key Takeaways

1. **Sorting Data**: Use the `ORDER BY` clause to sort query results in ascending (`ASC`) or descending (`DESC`) order.
2. **Grouping Data**: Use the `GROUP BY` clause to group query results based on specific columns.
3. **Filtering Groups**: Use the `HAVING` clause to filter groups created by the `GROUP BY` clause.
4. **Multiple Sort Operations**: You can sort data by multiple columns using the `ORDER BY` clause.
5. **Implicit Column Sorting**: Use column positions (e.g., `ORDER BY 1, 2`) instead of column names for sorting.

---

## Important Notes

### 1. **Sorting Data with ORDER BY**
   - **Purpose**: The `ORDER BY` clause is used to sort query results in a specific order.
   - **Syntax**:
     ```sql
     SELECT column1, column2, ...
     FROM table_name
     ORDER BY column1 ASC|DESC, column2 ASC|DESC;
     ```
   - **Example**:
     ```sql
     SELECT name, continent, surfacearea
     FROM country
     WHERE surfacearea >= 5000000
     ORDER BY surfacearea ASC;
     ```
     **Output**:
     | name               | continent      | surfacearea  |
     |--------------------|----------------|--------------|
     | Australia          | Oceania        | 7741220.00   |
     | Brazil             | South America  | 8547403.00   |
     | United States      | North America  | 9363520.00   |
     | China              | Asia           | 9572900.00   |
     | Canada             | North America  | 9970610.00   |
     | Antarctica         | Antarctica     | 13120000.00  |
     | Russian Federation | Europe         | 17075400.00  |

---

### 2. **Grouping Data with GROUP BY**
   - **Purpose**: The `GROUP BY` clause groups rows that have the same values in specified columns.
   - **Syntax**:
     ```sql
     SELECT column1, COUNT(column2)
     FROM table_name
     GROUP BY column1;
     ```
   - **Example**:
     ```sql
     SELECT continent, COUNT(name) AS 'countries'
     FROM country
     WHERE (continent = 'South America' AND population > 12000000)
     OR continent = 'Antarctica'
     GROUP BY continent;
     ```
     **Output**:
     | continent      | countries |
     |----------------|-----------|
     | Antarctica     | 5         |
     | South America  | 7         |

---

### 3. **Filtering Groups with HAVING**
   - **Purpose**: The `HAVING` clause filters groups created by the `GROUP BY` clause.
   - **Syntax**:
     ```sql
     SELECT column1, COUNT(column2)
     FROM table_name
     GROUP BY column1
     HAVING COUNT(column2) > value;
     ```
   - **Example**:
     ```sql
     SELECT continent, COUNT(name) AS 'countries'
     FROM country
     WHERE (continent = 'South America' AND population > 12000000)
     OR continent = 'Antarctica'
     GROUP BY continent
     HAVING COUNT(name) > 5;
     ```
     **Output**:
     | continent      | countries |
     |----------------|-----------|
     | South America  | 7         |

---

### 4. **Multiple Sort Operations**
   - **Purpose**: You can sort data by multiple columns using the `ORDER BY` clause.
   - **Syntax**:
     ```sql
     SELECT column1, column2, ...
     FROM table_name
     ORDER BY column1 ASC|DESC, column2 ASC|DESC;
     ```
   - **Example**:
     ```sql
     SELECT name, continent, surfacearea
     FROM country
     WHERE surfacearea >= 5000000
     ORDER BY continent ASC, surfacearea DESC;
     ```
     **Output**:
     | name               | continent      | surfacearea  |
     |--------------------|----------------|--------------|
     | Antarctica         | Antarctica     | 13120000.00  |
     | China              | Asia           | 9572900.00   |
     | Russian Federation | Europe         | 17075400.00  |
     | Canada             | North America  | 9970610.00   |
     | United States      | North America  | 9363520.00   |
     | Australia          | Oceania        | 7741220.00   |
     | Brazil             | South America  | 8547403.00   |

---

### 5. **Implicit Column Sorting**
   - **Purpose**: Instead of using column names, you can use column positions in the `ORDER BY` clause.
   - **Syntax**:
     ```sql
     SELECT column1, column2, ...
     FROM table_name
     ORDER BY 1 ASC|DESC, 2 ASC|DESC;
     ```
   - **Example**:
     ```sql
     SELECT name, continent, surfacearea
     FROM country
     WHERE surfacearea >= 5000000
     ORDER BY 2 ASC, 3 DESC;
     ```
     **Output**:
     | name               | continent      | surfacearea  |
     |--------------------|----------------|--------------|
     | Antarctica         | Antarctica     | 13120000.00  |
     | China              | Asia           | 9572900.00   |
     | Russian Federation | Europe         | 17075400.00  |
     | Canada             | North America  | 9970610.00   |
     | United States      | North America  | 9363520.00   |
     | Australia          | Oceania        | 7741220.00   |
     | Brazil             | South America  | 8547403.00   |

---

## Examples

### Example 1: Sorting Data in Ascending Order
```sql
SELECT name, continent, surfacearea
FROM country
WHERE surfacearea >= 5000000
ORDER BY surfacearea ASC;
```
**Output**:
| name               | continent      | surfacearea  |
|--------------------|----------------|--------------|
| Australia          | Oceania        | 7741220.00   |
| Brazil             | South America  | 8547403.00   |
| United States      | North America  | 9363520.00   |
| China              | Asia           | 9572900.00   |
| Canada             | North America  | 9970610.00   |
| Antarctica         | Antarctica     | 13120000.00  |
| Russian Federation | Europe         | 17075400.00  |

---

### Example 2: Sorting Data in Descending Order
```sql
SELECT name, continent, surfacearea
FROM country
WHERE surfacearea >= 5000000
ORDER BY surfacearea DESC;
```
**Output**:
| name               | continent      | surfacearea  |
|--------------------|----------------|--------------|
| Russian Federation | Europe         | 17075400.00  |
| Antarctica         | Antarctica     | 13120000.00  |
| Canada             | North America  | 9970610.00   |
| China              | Asia           | 9572900.00   |
| United States      | North America  | 9363520.00   |
| Brazil             | South America  | 8547403.00   |
| Australia          | Oceania        | 7741220.00   |

---

### Example 3: Grouping Data with GROUP BY
```sql
SELECT continent, COUNT(name) AS 'countries'
FROM country
WHERE (continent = 'South America' AND population > 12000000)
OR continent = 'Antarctica'
GROUP BY continent;
```
**Output**:
| continent      | countries |
|----------------|-----------|
| Antarctica     | 5         |
| South America  | 7         |

---

### Example 4: Filtering Groups with HAVING
```sql
SELECT continent, COUNT(name) AS 'countries'
FROM country
WHERE (continent = 'South America' AND population > 12000000)
OR continent = 'Antarctica'
GROUP BY continent
HAVING COUNT(name) > 5;
```
**Output**:
| continent      | countries |
|----------------|-----------|
| South America  | 7         |

---

### Example 5: Multiple Sort Operations
```sql
SELECT name, continent, surfacearea
FROM country
WHERE surfacearea >= 5000000
ORDER BY continent ASC, surfacearea DESC;
```
**Output**:
| name               | continent      | surfacearea  |
|--------------------|----------------|--------------|
| Antarctica         | Antarctica     | 13120000.00  |
| China              | Asia           | 9572900.00   |
| Russian Federation | Europe         | 17075400.00  |
| Canada             | North America  | 9970610.00   |
| United States      | North America  | 9363520.00   |
| Australia          | Oceania        | 7741220.00   |
| Brazil             | South America  | 8547403.00   |

---

### Example 6: Implicit Column Sorting
```sql
SELECT name, continent, surfacearea
FROM country
WHERE surfacearea >= 5000000
ORDER BY 2 ASC, 3 DESC;
```
**Output**:
| name               | continent      | surfacearea  |
|--------------------|----------------|--------------|
| Antarctica         | Antarctica     | 13120000.00  |
| China              | Asia           | 9572900.00   |
| Russian Federation | Europe         | 17075400.00  |
| Canada             | North America  | 9970610.00   |
| United States      | North America  | 9363520.00   |
| Australia          | Oceania        | 7741220.00   |
| Brazil             | South America  | 8547403.00   |

---

## Checkpoint Questions

1. **What is the ORDER BY clause used for in a SELECT statement?**
   - **Answer**: The `ORDER BY` clause is used to sort the rows in a query result set in a specific order (ascending or descending).

2. **What is the GROUP BY clause used for in a SELECT statement?**
   - **Answer**: The `GROUP BY` clause is used to combine rows into groups based on matching values in specified columns.

---

## Conclusion

- **Sorting Data**: Use the `ORDER BY` clause to sort query results in ascending or descending order.
- **Grouping Data**: Use the `GROUP BY` clause to group query results based on specific columns.
- **Filtering Groups**: Use the `HAVING` clause to filter groups created by the `GROUP BY` clause.
- **Multiple Sort Operations**: You can sort data by multiple columns using the `ORDER BY` clause.
- **Implicit Column Sorting**: Use column positions instead of column names for sorting.

---

Thank you for reviewing these comprehensive notes! Let me know if you need further clarification or additional details.

---

# LAB
Task 2: Query the world database
In this task, you query the world database using various SELECT statements and database functions.

To show the existing databases, enter the following command in the terminal. 

SHOW DATABASES;
Verify that a database named world is available. If the world database is not available, contact your instructor.

To review the table schema, data, and number of rows in the country table, enter the following query.

SELECT * FROM world.country;
To return a list of records where the Region is Australia and New Zealand, run the following query. This query includes an ORDER BY clause (which a previous lab introduced) that arranges the results by Population in descending order.

SELECT Region, Name, Population FROM world.country WHERE Region = 'Australia and New Zealand' ORDER By Population desc;
You can use the GROUP BY clause to group related records together. The following example starts by filtering records using a condition where the region is equal to Australia and New Zealand. The results are then grouped together by using a GROUP BY clause. The SUM() function is then applied to the grouped results to generate a total population for that region. Run the following query in your terminal.

SELECT Region, SUM(Population) FROM world.country WHERE Region = 'Australia and New Zealand' GROUP By Region ORDER By SUM(Population) desc;
This query returns a SUM() of the Population for the Australia and New Zealand region. Because the WHERE clause is filtered by Region, only the Australia and New Zealand records are aggregated. 

The following example uses a windowing function to generate a running total by adding the Population of the first record to the Population of the second record and subsequent records. This query uses the OVER() clause to group the records by Region and uses the SUM() function to aggregate the records. The output displays the population of a country along side a running total of the region. Run the following query in your terminal.

SELECT Region, Name, Population, SUM(Population) OVER(partition by Region ORDER BY Population) as 'Running Total' FROM world.country WHERE Region = 'Australia and New Zealand';
The following query groups the records by Region and orders them by Population with the OVER() clause. This query also includes the RANK() function to generate a rank number indicating the position of each record in the result set. The RANK() function is useful when dealing with large groups of records. Run the following query in your terminal.

SELECT Region, Name, Population, SUM(Population) OVER(partition by Region ORDER BY Population) as 'Running Total', RANK() over(partition by region ORDER BY population) as 'Ranked' FROM world.country WHERE region = 'Australia and New Zealand';
 

Challenge
Write a query to rank the countries in each region by their population from largest to smallest.

You have to determine whether to use either the GROUP BY or OVER grouping clause and either the SUM() or RANK() function.
SELECT Region, Name, Population, RANK() OVER(partition by Region ORDER BY Population desc) as 'Ranked' FROM world.country order by Region, Ranked;

Tip: Expand the question to reveal the solution.