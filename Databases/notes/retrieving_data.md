# Retrieving Data from Multiple Tables - Comprehensive Notes and Examples

This document provides a detailed summary of the "Retrieving Data from Multiple Tables" module, including key concepts, syntax, examples, and important considerations.

---

## Key Takeaways

1. **Set Operators**: Used to combine the results of multiple queries into a single result set.
   - **UNION**: Combines results without duplicates.
   - **UNION ALL**: Combines results including duplicates.
   - **INTERSECT**: Returns common data in both result sets.
   - **MINUS**: Returns data from the first result set that is not in the second.

2. **JOINs**: Used to combine rows from two or more tables based on related columns.
   - **INNER JOIN**: Returns rows that match in both tables.
   - **LEFT JOIN**: Returns all rows from the left table and matching rows from the right table.
   - **RIGHT JOIN**: Returns all rows from the right table and matching rows from the left table.
   - **FULL JOIN**: Returns all rows from both tables, with or without matches.

3. **Qualified Column Names**: Used to avoid confusion when columns in different tables have the same name.

---

## Important Notes

### 1. **Set Operators**
   - **Purpose**: Set operators combine the results of multiple queries into a single result set.
   - **Common Set Operators**:
     - **UNION**: Combines results without duplicates.
     - **UNION ALL**: Combines results including duplicates.
     - **INTERSECT**: Returns common data in both result sets.
     - **MINUS**: Returns data from the first result set that is not in the second.
   - **Example**:
     ```sql
     SELECT Name FROM country
     UNION
     SELECT Name FROM city;
     ```
     **Output**:
     | Name               |
     |--------------------|
     | Afghanistan        |
     | Kabul              |
     | Netherlands        |
     | Amsterdam          |

---

### 2. **JOINs**
   - **Purpose**: JOINs combine rows from two or more tables based on related columns.
   - **Types of JOINs**:
     - **INNER JOIN**: Returns rows that match in both tables.
     - **LEFT JOIN**: Returns all rows from the left table and matching rows from the right table.
     - **RIGHT JOIN**: Returns all rows from the right table and matching rows from the left table.
     - **FULL JOIN**: Returns all rows from both tables, with or without matches.
   - **Example**:
     ```sql
     SELECT ci.ID AS 'City ID', ci.Name AS 'City Name', co.Name AS 'Country Name'
     FROM city ci
     INNER JOIN country co
     ON ci.CountryCode = co.Code;
     ```
     **Output**:
     | City ID | City Name | Country Name |
     |---------|-----------|--------------|
     | 1       | Kabul     | Afghanistan  |
     | 5       | Amsterdam | Netherlands  |

---

### 3. **Qualified Column Names**
   - **Purpose**: Qualified column names avoid confusion when columns in different tables have the same name.
   - **Syntax**:
     ```sql
     TableName.ColumnName
     ```
   - **Example**:
     ```sql
     SELECT ci.ID AS 'City ID', ci.Name AS 'City Name', co.Name AS 'Country Name'
     FROM city ci
     INNER JOIN country co
     ON ci.CountryCode = co.Code;
     ```
     **Output**:
     | City ID | City Name | Country Name |
     |---------|-----------|--------------|
     | 1       | Kabul     | Afghanistan  |
     | 5       | Amsterdam | Netherlands  |

---

## Examples

### Example 1: UNION Operator
```sql
SELECT Name FROM country
UNION
SELECT Name FROM city;
```
**Output**:
| Name               |
|--------------------|
| Afghanistan        |
| Kabul              |
| Netherlands        |
| Amsterdam          |

---

### Example 2: UNION ALL Operator
```sql
SELECT Name FROM city
UNION ALL
SELECT Name FROM country;
```
**Output**:
| Name               |
|--------------------|
| Kabul              |
| Amsterdam          |
| Afghanistan        |
| Netherlands        |

---

### Example 3: INNER JOIN
```sql
SELECT ci.ID AS 'City ID', ci.Name AS 'City Name', co.Name AS 'Country Name'
FROM city ci
INNER JOIN country co
ON ci.CountryCode = co.Code;
```
**Output**:
| City ID | City Name | Country Name |
|---------|-----------|--------------|
| 1       | Kabul     | Afghanistan  |
| 5       | Amsterdam | Netherlands  |

---

### Example 4: LEFT JOIN
```sql
SELECT ci.ID AS 'City ID', ci.Name AS 'City Name', co.Name AS 'Country Name'
FROM city ci
LEFT JOIN country co
ON ci.CountryCode = co.Code;
```
**Output**:
| City ID | City Name | Country Name |
|---------|-----------|--------------|
| 1       | Kabul     | Afghanistan  |
| 5       | Amsterdam | Netherlands  |
| 6       | Berlin    | NULL         |

---

### Example 5: RIGHT JOIN
```sql
SELECT ci.ID AS 'City ID', ci.Name AS 'City Name', co.Name AS 'Country Name'
FROM city ci
RIGHT JOIN country co
ON ci.CountryCode = co.Code;
```
**Output**:
| City ID | City Name | Country Name |
|---------|-----------|--------------|
| 1       | Kabul     | Afghanistan  |
| 5       | Amsterdam | Netherlands  |
| NULL    | NULL      | Argentina    |

---

### Example 6: FULL JOIN
```sql
SELECT ci.ID AS 'City ID', ci.Name AS 'City Name', co.Name AS 'Country Name'
FROM city ci
FULL JOIN country co
ON ci.CountryCode = co.Code;
```
**Output**:
| City ID | City Name | Country Name |
|---------|-----------|--------------|
| 1       | Kabul     | Afghanistan  |
| 5       | Amsterdam | Netherlands  |
| 6       | Berlin    | NULL         |
| NULL    | NULL      | Argentina    |

---

### Example 7: Qualified Column Names
```sql
SELECT ci.ID AS 'City ID', ci.Name AS 'City Name', co.Name AS 'Country Name'
FROM city ci
INNER JOIN country co
ON ci.CountryCode = co.Code;
```
**Output**:
| City ID | City Name | Country Name |
|---------|-----------|--------------|
| 1       | Kabul     | Afghanistan  |
| 5       | Amsterdam | Netherlands  |

---

## Checkpoint Questions

1. **What is a JOIN?**
   - **Answer**: A JOIN is used to combine data from two or more tables based on related columns.

2. **What does a UNION do?**
   - **Answer**: A UNION combines the results of two queries into one result set, removing duplicates.

---

## Conclusion

- **Set Operators**: Use `UNION`, `UNION ALL`, `INTERSECT`, and `MINUS` to combine query results.
- **JOINs**: Use `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL JOIN` to combine rows from multiple tables.
- **Qualified Column Names**: Use `TableName.ColumnName` to avoid confusion when columns have the same name.

---

Thank you for reviewing these comprehensive notes! Let me know if you need further clarification or additional details.