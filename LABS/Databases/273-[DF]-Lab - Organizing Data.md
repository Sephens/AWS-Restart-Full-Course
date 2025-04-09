# Organizing Data with GROUP BY and Window Functions

## Task 2: Data Organization Techniques

### Basic GROUP BY Aggregation

```sql
SELECT Region, SUM(Population) 
FROM world.country 
WHERE Region = 'Australia and New Zealand' 
GROUP BY Region 
ORDER BY SUM(Population) DESC;
```

### Window Functions with OVER()

1. **Running Total Calculation**:
   ```sql
   SELECT 
       Region, 
       Name, 
       Population,
       SUM(Population) OVER(PARTITION BY Region ORDER BY Population) AS 'Running Total'
   FROM world.country 
   WHERE Region = 'Australia and New Zealand';
   ```

2. **Ranking Within Groups**:
   ```sql
   SELECT 
       Region, 
       Name, 
       Population,
       SUM(Population) OVER(PARTITION BY Region ORDER BY Population) AS 'Running Total',
       RANK() OVER(PARTITION BY Region ORDER BY Population) AS 'Ranked'
   FROM world.country 
   WHERE Region = 'Australia and New Zealand';
   ```

## Challenge Solution

**Rank countries in each region by population (largest to smallest)**:

```sql
SELECT 
    Region,
    Name,
    Population,
    RANK() OVER(PARTITION BY Region ORDER BY Population DESC) AS PopulationRank
FROM world.country
ORDER BY Region, PopulationRank;
```

## Key Concepts Explained

| Feature | Purpose | When to Use |
|---------|---------|-------------|
| `GROUP BY` | Aggregates data into summary rows | When you need totals/averages per group |
| `OVER()` | Performs calculations across related rows | When you need rankings or running totals |
| `PARTITION BY` | Defines window/group for OVER() | Similar to GROUP BY but without collapsing rows |
| `RANK()` | Assigns ranking with gaps for ties | When you need competition-style rankings |
| `SUM() OVER()` | Calculates running totals | For cumulative sums within groups |

## Advanced Techniques

1. **Multiple window functions**:
   ```sql
   SELECT 
       Region,
       Name,
       Population,
       RANK() OVER(PARTITION BY Region ORDER BY Population DESC) AS Rank,
       PERCENT_RANK() OVER(PARTITION BY Region ORDER BY Population DESC) AS Percentile
   FROM world.country;
   ```

2. **Moving averages**:
   ```sql
   SELECT 
       Name,
       Year,
       GDP,
       AVG(GDP) OVER(ORDER BY Year ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS MovingAvg
   FROM economic_data;
   ```

3. **Group comparisons**:
   ```sql
   SELECT 
       Continent,
       Name,
       Population,
       Population / SUM(Population) OVER(PARTITION BY Continent) * 100 AS PercentOfContinent
   FROM world.country;
   ```

## Performance Considerations

1. **Index columns** used in PARTITION BY and ORDER BY clauses
2. **Limit window size** with ROWS/RANGE when possible
3. **Avoid sorting** the same data multiple times
4. **Consider materialized views** for complex aggregations
5. **Test with EXPLAIN** to analyze execution plans

## Practical Applications

1. **Leaderboards**:
   ```sql
   SELECT 
       player_name,
       score,
       RANK() OVER(ORDER BY score DESC) AS rank
   FROM game_scores;
   ```

2. **Sales analysis**:
   ```sql
   SELECT 
       region,
       product,
       sales,
       SUM(sales) OVER(PARTITION BY region ORDER BY month) AS running_total
   FROM sales_data;
   ```

3. **Population distribution**:
   ```sql
   SELECT 
       continent,
       country,
       population,
       ROUND(population * 100.0 / SUM(population) OVER(PARTITION BY continent), 2) AS percentage
   FROM world.country;
   ```

This lab provides essential skills for organizing and analyzing data at different levels of granularity, enabling more sophisticated reporting and analytics capabilities.