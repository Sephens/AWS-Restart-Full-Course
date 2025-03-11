# Working with Functions - Comprehensive Notes and Examples

This document provides a detailed summary of the "Working with Functions" module, including key concepts, syntax, examples, and important considerations.

---

## Key Takeaways

1. **Built-in Functions**: SQL provides a variety of built-in functions to manipulate and calculate data.
2. **Aggregate Functions**: Perform calculations on a set of values and return a single value (e.g., `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).
3. **String Functions**: Manipulate and analyze character strings (e.g., `CHAR_LENGTH`, `INSERT`, `TRIM`).
4. **Date Functions**: Perform operations on date and time values (e.g., `CURRENT_DATE`, `DATE_ADD`).
5. **DISTINCT Keyword**: Used to return unique values from a column or set of columns.

---

## Important Notes

### 1. **Built-in Functions**
   - **Purpose**: Built-in functions are pre-defined functions in SQL that perform specific operations on data.
   - **Types of Functions**:
     - **Aggregate Functions**: Operate on a set of rows and return a single value.
     - **String Functions**: Manipulate and analyze text data.
     - **Date Functions**: Perform operations on date and time values.
     - **Mathematical Functions**: Perform arithmetic operations.
     - **Control Flow Functions**: Control the flow of execution in SQL queries.

---

### 2. **Aggregate Functions**
   - **Purpose**: Aggregate functions perform calculations on a set of values and return a single value.
   - **Common Aggregate Functions**:
     - **`COUNT`**: Returns the number of rows in a set.
     - **`SUM`**: Returns the sum of all values in a set.
     - **`AVG`**: Returns the average of all values in a set.
     - **`MIN`**: Returns the minimum value in a set.
     - **`MAX`**: Returns the maximum value in a set.
   - **Example**:
     ```sql
     SELECT COUNT(*) AS 'Total Number of Rows' FROM countrylanguage;
     ```
     **Output**:
     | Total Number of Rows |
     |----------------------|
     | 984                  |

---

### 3. **String Functions**
   - **Purpose**: String functions manipulate and analyze text data.
   - **Common String Functions**:
     - **`CHAR_LENGTH`**: Returns the length of a string in characters.
     - **`INSERT`**: Inserts a substring into a string at a specified position.
     - **`TRIM`**: Removes leading and trailing spaces from a string.
     - **`RTRIM`**: Removes trailing spaces from a string.
     - **`LTRIM`**: Removes leading spaces from a string.
   - **Example**:
     ```sql
     SELECT CHAR_LENGTH('District');
     ```
     **Output**:
     | CHAR_LENGTH('District') |
     |-------------------------|
     | 8                       |

---

### 4. **Date Functions**
   - **Purpose**: Date functions perform operations on date and time values.
   - **Common Date Functions**:
     - **`CURRENT_DATE`**: Returns the current date.
     - **`DATE_ADD`**: Adds a specified time interval to a date.
   - **Example**:
     ```sql
     SELECT CURRENT_DATE();
     ```
     **Output**:
     | CURRENT_DATE() |
     |----------------|
     | 2023-10-05     |

---

### 5. **DISTINCT Keyword**
   - **Purpose**: The `DISTINCT` keyword is used to return unique values from a column or set of columns.
   - **Example**:
     ```sql
     SELECT DISTINCT CountryCode, District FROM city;
     ```
     **Output**:
     | CountryCode | District          |
     |-------------|-------------------|
     | BRA         | Distrito Federal  |
     | BRA         | Rio de Janeiro    |
     | BRA         | Sao Paulo         |
     | CHN         | Guangdong         |
     | CHN         | Shanghai          |
     | GBR         | England           |
     | GBR         | Scotland          |

---

### 6. **TRIM Functions**
   - **Purpose**: TRIM functions remove leading and trailing spaces from strings.
   - **Common TRIM Functions**:
     - **`RTRIM`**: Removes trailing spaces.
     - **`LTRIM`**: Removes leading spaces.
   - **Example**:
     ```sql
     SELECT ID, RTRIM(District) AS District FROM city;
     ```
     **Output**:
     | ID  | District      |
     |-----|---------------|
     | 1024| Maharashtra   |
     | 2331| Seoul         |
     | 3793| New York      |

---

## Examples

### Example 1: Aggregate Functions
```sql
SELECT AVG(LifeExpectancy) FROM country;
```
**Output**:
| AVG(LifeExpectancy) |
|---------------------|
| 72.51200            |

---

### Example 2: String Functions
```sql
SELECT INSERT('Population', 1, 2, 'Man1');
```
**Output**:
| INSERT('Population', 1, 2, 'Man1') |
|------------------------------------|
| Manipulation                        |

---

### Example 3: Date Functions
```sql
SELECT DATE_ADD('2023-10-05', INTERVAL 3 DAY);
```
**Output**:
| DATE_ADD('2023-10-05', INTERVAL 3 DAY) |
|----------------------------------------|
| 2023-10-08                             |

---

### Example 4: DISTINCT Keyword
```sql
SELECT COUNT(DISTINCT CountryCode) AS Unique_Country_Codes FROM city;
```
**Output**:
| Unique_Country_Codes |
|----------------------|
| 118                  |

---

### Example 5: TRIM Functions
```sql
SELECT ID, RTRIM(District) AS District FROM city;
```
**Output**:
| ID  | District      |
|-----|---------------|
| 1024| Maharashtra   |
| 2331| Seoul         |
| 3793| New York      |

---

## Checkpoint Questions

1. **Which functions remove leading and trailing spaces on strings?**
   - **Answer**: `TRIM`, `RTRIM`, and `LTRIM` functions remove leading and trailing spaces on strings.

2. **What is an aggregate function?**
   - **Answer**: An aggregate function performs calculations on a set of values and returns a single value (e.g., `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).

3. **What are five common aggregate functions?**
   - **Answer**: `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`.

---

## Conclusion

- **Built-in Functions**: SQL provides a variety of built-in functions to manipulate and calculate data.
- **Aggregate Functions**: Perform calculations on a set of values and return a single value.
- **String Functions**: Manipulate and analyze text data.
- **Date Functions**: Perform operations on date and time values.
- **DISTINCT Keyword**: Returns unique values from a column or set of columns.

---

Thank you for reviewing these comprehensive notes! Let me know if you need further clarification or additional details.