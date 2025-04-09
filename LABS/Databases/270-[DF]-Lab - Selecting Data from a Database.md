# Querying Data from a Database: Comprehensive Guide

## Task 2: Querying the World Database

### Basic Query Operations

1. **List all databases**:
   ```sql
   SHOW DATABASES;
   ```

2. **View all data in country table**:
   ```sql
   SELECT * FROM world.country;
   ```

3. **Count rows in table**:
   ```sql
   SELECT COUNT(*) FROM world.country;
   ```

4. **View table structure**:
   ```sql
   SHOW COLUMNS FROM world.country;
   ```

### Selecting Specific Columns

```sql
SELECT Name, Capital, Region, SurfaceArea, Population 
FROM world.country;
```

### Column Aliases (Renaming Output Columns)

```sql
SELECT 
    Name, 
    Capital, 
    Region, 
    SurfaceArea AS "Surface Area", 
    Population 
FROM world.country;
```

### Sorting Results

1. **Ascending order (default)**:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
   FROM world.country 
   ORDER BY Population;
   ```

2. **Descending order**:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
   FROM world.country 
   ORDER BY Population DESC;
   ```

### Filtering with WHERE Clause

1. **Basic comparison**:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
   FROM world.country 
   WHERE Population > 50000000 
   ORDER BY Population DESC;
   ```

2. **Range filtering**:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
   FROM world.country 
   WHERE Population > 50000000 AND Population < 100000000 
   ORDER BY Population DESC;
   ```

### Challenge Solution

**Which country in Southern Europe has a population greater than 50,000,000?**

```sql
SELECT Name, Capital, Region, Population
FROM world.country
WHERE Region = 'Southern Europe' AND Population > 50000000;
```

## Key SQL Operators and Functions

| Feature | Description | Example |
|---------|-------------|---------|
| `SELECT` | Retrieves data | `SELECT * FROM table` |
| `COUNT()` | Counts rows | `SELECT COUNT(*) FROM table` |
| `WHERE` | Filters rows | `WHERE Population > 1000000` |
| `ORDER BY` | Sorts results | `ORDER BY Name DESC` |
| Comparison Operators | `=`, `>`, `<`, `>=`, `<=`, `<>` | `WHERE Population > 50000000` |
| `AND` | Logical AND | `WHERE A AND B` |
| `AS` | Column alias | `SELECT col AS "New Name"` |

## Advanced Query Techniques

1. **Combining conditions**:
   ```sql
   SELECT Name, Population 
   FROM world.country
   WHERE (Continent = 'Europe' OR Continent = 'Asia')
     AND Population BETWEEN 1000000 AND 5000000;
   ```

2. **Pattern matching**:
   ```sql
   SELECT Name 
   FROM world.country
   WHERE Name LIKE 'A%';  -- Starts with A
   ```

3. **Aggregate functions**:
   ```sql
   SELECT 
       Continent,
       COUNT(*) AS CountryCount,
       AVG(Population) AS AvgPopulation
   FROM world.country
   GROUP BY Continent;
   ```

4. **Joining tables**:
   ```sql
   SELECT c.Name, ci.Name AS CapitalCity
   FROM world.country c
   JOIN world.city ci ON c.Capital = ci.ID;
   ```

## Best Practices for Database Queries

1. **Be specific** in SELECT clauses (avoid `SELECT *` in production)
2. **Use aliases** for clarity
3. **Add comments** to complex queries
4. **Format queries** for readability
5. **Test first** with simple filters before adding complexity
6. **Consider indexes** on frequently filtered columns

## Common Pitfalls to Avoid

1. **Case sensitivity** in string comparisons
2. **NULL handling** (use `IS NULL` instead of `= NULL`)
3. **Date formatting** in comparisons
4. **Implicit type conversion** affecting performance
5. **Over-filtering** with too many AND conditions

## Performance Considerations

1. **Limit results** when possible:
   ```sql
   SELECT * FROM world.city LIMIT 100;
   ```

2. **Use EXPLAIN** to analyze query plans:
   ```sql
   EXPLAIN SELECT * FROM world.country WHERE Population > 1000000;
   ```

3. **Avoid functions** on indexed columns in WHERE clauses:
   ```sql
   -- Bad: WHERE YEAR(IndepYear) = 1991
   -- Good: WHERE IndepYear BETWEEN '1991-01-01' AND '1991-12-31'
   ```

This lab provides essential querying skills that form the foundation for more complex database operations and reporting.