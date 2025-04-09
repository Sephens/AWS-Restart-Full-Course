# Working with SQL Functions: Comprehensive Guide

## Task 2: Querying with Database Functions

### Aggregate Functions

```sql
SELECT 
    SUM(Population) AS TotalPopulation,
    AVG(Population) AS AvgPopulation,
    MAX(Population) AS MaxPopulation,
    MIN(Population) AS MinPopulation,
    COUNT(Population) AS CountryCount
FROM world.country;
```

### String Manipulation Functions

1. **Splitting strings with SUBSTRING_INDEX**:
   ```sql
   SELECT 
       Region, 
       SUBSTRING_INDEX(Region, " ", 1) AS FirstWord
   FROM world.country;
   ```

2. **Filtering with string functions**:
   ```sql
   SELECT Name, Region 
   FROM world.country 
   WHERE SUBSTRING_INDEX(Region, " ", 1) = "Southern";
   ```

3. **String length and trimming**:
   ```sql
   SELECT Region 
   FROM world.country 
   WHERE LENGTH(TRIM(Region)) < 10;
   ```

4. **Removing duplicates**:
   ```sql
   SELECT DISTINCT(Region) 
   FROM world.country 
   WHERE LENGTH(TRIM(Region)) < 10;
   ```

## Challenge Solution

**Splitting "Micronesia/Caribbean" into separate columns**:

```sql
SELECT 
    Name,
    SUBSTRING_INDEX(Region, "/", 1) AS "Region Name 1",
    SUBSTRING_INDEX(Region, "/", -1) AS "Region Name 2"
FROM world.country
WHERE Region LIKE "%/%";
```

## Key SQL Functions Explained

| Function | Purpose | Example |
|----------|---------|---------|
| `SUM()` | Total of values | `SUM(Population)` |
| `AVG()` | Average of values | `AVG(LifeExpectancy)` |
| `MAX()` | Highest value | `MAX(GNP)` |
| `MIN()` | Lowest value | `MIN(SurfaceArea)` |
| `COUNT()` | Count of rows | `COUNT(*)` |
| `SUBSTRING_INDEX()` | Split string by delimiter | `SUBSTRING_INDEX(Region, " ", 1)` |
| `LENGTH()` | String length | `LENGTH(Name)` |
| `TRIM()` | Remove whitespace | `TRIM(Region)` |
| `DISTINCT()` | Unique values | `DISTINCT(Continent)` |

## Advanced Function Usage

1. **Combining functions**:
   ```sql
   SELECT 
       ROUND(AVG(Population), 0) AS RoundedAvgPopulation,
       CONCAT(SUBSTRING(Name, 1, 3), '...') AS AbbreviatedName
   FROM world.country;
   ```

2. **Conditional aggregation**:
   ```sql
   SELECT 
       Continent,
       SUM(CASE WHEN Population > 10000000 THEN 1 ELSE 0 END) AS LargeCountries
   FROM world.country
   GROUP BY Continent;
   ```

3. **Date functions** (if available):
   ```sql
   SELECT Name, YEAR(IndepYear) AS IndependenceYear
   FROM world.country;
   ```

4. **Mathematical functions**:
   ```sql
   SELECT 
       Name, 
       Population,
       ROUND(Population/SurfaceArea, 2) AS PopulationDensity
   FROM world.country;
   ```

## Best Practices for Using Functions

1. **Understand function behavior** with NULL values
2. **Consider performance impact** of functions in WHERE clauses
3. **Use aliases** for complex function outputs
4. **Format nested functions** clearly
5. **Test functions** with sample data first
6. **Document complex logic** in comments

## Common Pitfalls

1. **Assuming case sensitivity** - Use `LOWER()`/`UPPER()` when needed
2. **Ignoring NULL handling** - Use `COALESCE()` or `IFNULL()`
3. **Over-nesting functions** - Break into multiple steps if too complex
4. **Locale differences** in string/date functions
5. **Performance bottlenecks** from functions on indexed columns

## Practical Applications

1. **Data cleaning**:
   ```sql
   UPDATE world.city
   SET District = TRIM(District)
   WHERE District LIKE ' %' OR District LIKE '% ';
   ```

2. **Reporting**:
   ```sql
   SELECT 
       Continent,
       COUNT(*) AS CountryCount,
       SUM(Population) AS TotalPopulation,
       ROUND(AVG(LifeExpectancy), 1) AS AvgLifeSpan
   FROM world.country
   GROUP BY Continent;
   ```

3. **Data validation**:
   ```sql
   SELECT Name, Code, Code2
   FROM world.country
   WHERE LENGTH(Code) != 3 OR LENGTH(Code2) != 2;
   ```

This lab provides essential skills for transforming and analyzing data using SQL functions, which are fundamental for database reporting, application development, and data analysis tasks.