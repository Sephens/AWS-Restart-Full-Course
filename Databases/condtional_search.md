# Performing a Conditional Search - Comprehensive Notes and Examples

This document provides a detailed summary of the "Performing a Conditional Search" module, including key concepts, syntax, examples, and important considerations.

---

## Key Takeaways

1. **Search Conditions**: Used to filter data in SQL queries using the `WHERE` clause.
2. **Operators**:
   - **Arithmetic Operators**: Perform mathematical operations (e.g., `+`, `-`, `*`, `/`, `%`).
   - **Comparison Operators**: Compare values (e.g., `=`, `!=`, `<`, `>`, `<=`, `>=`).
   - **Logical Operators**: Combine multiple conditions (e.g., `AND`, `OR`, `IN`, `LIKE`, `BETWEEN`, `NOT`).
3. **Aliases**: Temporary names assigned to columns or tables in a query.
4. **NULL Values**: Represent the absence of a value and require special handling in SQL queries.
5. **Operator Precedence**: Determines the order in which operators are evaluated in a SQL statement.

---

## Important Notes

### 1. **Search Conditions and the WHERE Clause**
   - **Purpose**: The `WHERE` clause filters rows based on specified conditions.
   - **Syntax**:
     ```sql
     SELECT column1, column2, ...
     FROM table_name
     WHERE condition;
     ```
   - **Example**:
     ```sql
     SELECT name, population
     FROM city
     WHERE population > 1000000;
     ```

### 2. **Operators**
   - **Arithmetic Operators**:
     - `+` (Addition)
     - `-` (Subtraction)
     - `*` (Multiplication)
     - `/` (Division)
     - `%` (Modulus)
   - **Comparison Operators**:
     - `=` (Equal to)
     - `!=` or `<>` (Not equal to)
     - `<` (Less than)
     - `>` (Greater than)
     - `<=` (Less than or equal to)
     - `>=` (Greater than or equal to)
   - **Logical Operators**:
     - `AND`: All conditions must be true.
     - `OR`: At least one condition must be true.
     - `IN`: Matches any value in a list.
     - `LIKE`: Matches a pattern using wildcards (`%` for multiple characters, `_` for a single character).
     - `BETWEEN`: Matches values within a range.
     - `NOT`: Reverses the condition.

### 3. **Aliases**
   - **Purpose**: Assign temporary names to columns or tables in a query.
   - **Syntax**:
     ```sql
     SELECT column_name AS alias_name
     FROM table_name;
     ```
   - **Example**:
     ```sql
     SELECT name, population AS pop
     FROM city;
     ```

### 4. **NULL Values**
   - **Purpose**: Represent the absence of a value.
   - **Handling**:
     - Use `IS NULL` to find rows with NULL values.
     - Use `IS NOT NULL` to exclude rows with NULL values.
   - **Example**:
     ```sql
     SELECT name, lifeexpectancy
     FROM country
     WHERE lifeexpectancy IS NULL;
     ```

### 5. **Operator Precedence**
   - **Order of Evaluation**:
     1. Parentheses
     2. Multiplication, Division, Modulus
     3. Addition, Subtraction
     4. Comparison Operators
     5. `NOT`
     6. `AND`
     7. `OR`, `BETWEEN`, `IN`, `LIKE`
   - **Example**:
     ```sql
     SELECT name, population
     FROM city
     WHERE (countrycode = 'USA' OR countrycode = 'CAN')
     AND population > 1000000;
     ```

---

## Examples

### Example 1: Arithmetic Operators
```sql
SELECT name, lifeexpectancy, lifeexpectancy + 5.5 AS new_lifeexpectancy
FROM country
WHERE gnp > 1300000;
```
**Output**:
| name           | lifeexpectancy | new_lifeexpectancy |
|----------------|----------------|--------------------|
| Germany        | 77.4           | 82.9               |
| France         | 78.8           | 84.3               |
| United Kingdom | 77.7           | 83.2               |
| Japan          | 80.7           | 86.2               |
| United States  | 77.1           | 82.6               |

---

### Example 2: Comparison Operators
```sql
SELECT name, population
FROM city
WHERE population > 5000000;
```
**Output**:
| name       | population |
|------------|------------|
| Mumbai     | 11978451   |
| Seoul      | 9981619    |
| Sao Paulo  | 9968485    |
| Shanghai   | 9696300    |
| Jakarta    | 9604900    |

---

### Example 3: Logical Operators
```sql
SELECT name, district, population
FROM city
WHERE countrycode = 'IND'
AND district = 'Delhi';
```
**Output**:
| name               | district | population |
|--------------------|----------|------------|
| Delhi              | Delhi    | 7206704    |
| New Delhi          | Delhi    | 301297     |
| Delhi Cantonment   | Delhi    | 94326      |

---

### Example 4: LIKE Operator with Wildcards
```sql
SELECT name, district
FROM city
WHERE district LIKE 'West%';
```
**Output**:
| name       | district          |
|------------|-------------------|
| Perth      | West Australia    |
| Brugge     | West Flanderi     |
| Cape Town  | Western Cape      |
| Paarl      | Western Cape      |
| George     | Western Cape      |

---

### Example 5: BETWEEN Operator
```sql
SELECT name, population
FROM city
WHERE population BETWEEN 500000 AND 505000;
```
**Output**:
| name         | population |
|--------------|------------|
| Chandigarh   | 504094     |
| Sanaa        | 503600     |
| Pointe-Noire | 500000     |

---

### Example 6: NULL Values
```sql
SELECT name, lifeexpectancy
FROM country
WHERE lifeexpectancy IS NULL;
```
**Output**:
| name                          | lifeexpectancy |
|-------------------------------|----------------|
| Antarctica                    | NULL           |
| French Southern territories   | NULL           |
| British Indian Ocean Territory| NULL           |

---

### Example 7: Aliases
```sql
SELECT name, population AS pop
FROM city
WHERE population > 1000000;
```
**Output**:
| name       | pop      |
|------------|----------|
| Mumbai     | 11978451 |
| Seoul      | 9981619  |
| Sao Paulo  | 9968485  |

---

### Example 8: Operator Precedence
```sql
SELECT name, population
FROM city
WHERE (countrycode = 'USA' OR countrycode = 'CAN')
AND population > 1000000;
```
**Output**:
| name       | population |
|------------|------------|
| New York   | 8008278    |
| Los Angeles| 3694820    |
| Chicago    | 2896016    |

---

## Checkpoint Questions

1. **What is the purpose of a condition in a query?**
   - Conditions are used to filter the results of a query based on specified criteria.

2. **Why should you use aliases in SQL?**
   - Aliases make column names more understandable and can simplify complex queries.

3. **How do you handle NULL values in SQL?**
   - Use `IS NULL` to find rows with NULL values and `IS NOT NULL` to exclude them.

---

## Conclusion

- **Search Conditions**: The `WHERE` clause is essential for filtering data in SQL queries.
- **Operators**: Arithmetic, comparison, and logical operators are used to build complex search conditions.
- **Aliases**: Provide temporary names for columns or tables, making queries easier to read.
- **NULL Values**: Represent the absence of a value and require special handling using `IS NULL` and `IS NOT NULL`.
- **Operator Precedence**: Determines the order in which operators are evaluated, and parentheses can be used to override the default order.

---

Thank you for reviewing these comprehensive notes! Let me know if you need further clarification or additional details.