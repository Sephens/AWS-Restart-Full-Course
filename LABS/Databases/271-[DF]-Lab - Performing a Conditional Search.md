# Performing Conditional Searches in SQL: Comprehensive Guide

## Task 2: Querying with Conditions

### Basic WHERE Clause Usage

1. **Range filtering with AND**:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea, Population 
   FROM world.country 
   WHERE Population >= 50000000 AND Population <= 100000000;
   ```

2. **Simplified range with BETWEEN**:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea, Population 
   FROM world.country 
   WHERE Population BETWEEN 50000000 AND 100000000;
   ```

### Pattern Matching with LIKE

1. **Basic pattern matching**:
   ```sql
   SELECT SUM(Population) 
   FROM world.country 
   WHERE Region LIKE "%Europe%";
   ```

2. **With column alias**:
   ```sql
   SELECT SUM(Population) AS "Europe Population Total" 
   FROM world.country 
   WHERE Region LIKE "%Europe%";
   ```

### Case-Insensitive Searching

```sql
SELECT Name, Capital, Region, SurfaceArea, Population 
FROM world.country 
WHERE LOWER(Region) LIKE "%central%";
```

## Challenge Solution

**Sum of surface area and population for North America**:

```sql
SELECT 
    SUM(SurfaceArea) AS "Total Surface Area",
    SUM(Population) AS "Total Population"
FROM world.country
WHERE Continent = 'North America';
```

## Key SQL Features Demonstrated

| Feature | Purpose | Example |
|---------|---------|---------|
| `WHERE` | Filter rows | `WHERE Population > 1000000` |
| `BETWEEN` | Range filtering | `WHERE Population BETWEEN x AND y` |
| `LIKE` | Pattern matching | `WHERE Region LIKE '%Europe%'` |
| `SUM()` | Aggregate function | `SUM(Population)` |
| `AS` | Column alias | `SUM(x) AS "Total"` |
| `LOWER()` | Case conversion | `WHERE LOWER(Region) = 'central'` |

## Advanced Conditional Techniques

1. **Multiple conditions**:
   ```sql
   SELECT Name, Population
   FROM world.country
   WHERE (Continent = 'Europe' OR Continent = 'Asia')
     AND Population > 50000000;
   ```

2. **NULL handling**:
   ```sql
   SELECT Name, IndepYear
   FROM world.country
   WHERE IndepYear IS NOT NULL;
   ```

3. **Date filtering**:
   ```sql
   SELECT Name, IndepYear
   FROM world.country
   WHERE IndepYear BETWEEN 1900 AND 2000;
   ```

4. **Subqueries in conditions**:
   ```sql
   SELECT Name
   FROM world.country
   WHERE Code IN (SELECT CountryCode FROM world.city WHERE Population > 5000000);
   ```

## Best Practices for Conditional Queries

1. **Use BETWEEN for ranges** instead of chained AND conditions
2. **Put most selective conditions first** in WHERE clauses
3. **Use LIKE carefully** - leading wildcards (`%text`) prevent index usage
4. **Consider COLLATION** for case-sensitive databases
5. **Format complex conditions** clearly with parentheses and indentation

## Performance Considerations

1. **Index-friendly conditions**:
   ```sql
   -- Good for indexes
   WHERE Population > 1000000
   
   -- Bad for indexes
   WHERE Population + 1000000 > 2000000
   ```

2. **Avoid functions on indexed columns**:
   ```sql
   -- Bad (can't use index on Region)
   WHERE LOWER(Region) = 'central'
   
   -- Better (if collation is case-insensitive)
   WHERE Region = 'Central'
   ```

3. **EXPLAIN to analyze** query execution plans:
   ```sql
   EXPLAIN SELECT * FROM world.country WHERE Population > 1000000;
   ```

This lab provides essential skills for filtering and analyzing data that form the foundation for effective database reporting and application development.