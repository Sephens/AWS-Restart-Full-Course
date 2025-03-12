# Inserting Data into a Database

This module focuses on **inserting data** into a database, including importing data from `.csv` files, cleaning data, and using SQL statements like `INSERT INTO` and `DESCRIBE`.

---

## 1. **What is a `.csv` File?**
- A `.csv` (comma-separated values) file is a simple text file where data is separated by commas.
- Each line in the file represents a row, and each data point is separated by a comma.
- Commonly used for importing/exporting data between databases and spreadsheets.

### Example `.csv` File:
```plaintext
ABW,Aruba,North America,193.00
AFG,Afghanistan,Asia,652090.00
AGO,Angola,Africa,1246700.00
```

---

## 2. **Importing Data from a `.csv` File**
### Steps to Import a `.csv` File:
1. **Verify**: Ensure the `.csv` file matches the table's column structure and data types.
2. **Create Table**: Create a table in the database with the same structure as the `.csv` file.
3. **Import Data**: Use the `LOAD DATA` statement to import the `.csv` file.

### Example: Importing a `.csv` File into MySQL
```sql
LOAD DATA INFILE 'c:/tmp/city.csv'
INTO TABLE city
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

---

## 3. **Exporting Data to a `.csv` File**
### Example: Exporting Data from MySQL
```sql
SELECT id, name, countrycode
FROM city
INTO OUTFILE '/tmp/mysqlfiles/city.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

---

## 4. **Cleaning Data**
### SQL Functions for Cleaning Data:
- **`TRIM`**: Removes extra spaces from strings.
- **`CONCAT`**: Combines strings from multiple columns.
- **`LOWER`/`UPPER`**: Converts strings to lowercase/uppercase.

### Example: Cleaning Data with `TRIM`
```sql
UPDATE employees
SET name = TRIM(name);
```

---

## 5. **Common Database Errors**
### Examples of Errors:
- **Data-entry errors**: Extra spaces, typos.
- **Wrong data type**: Inserting text into a numeric column.
- **Missing data**: NULL values where data is expected.
- **Duplicate data**: Repeated rows in a table.

### Solutions:
- Use `TRIM` to remove extra spaces.
- Validate data types before insertion.
- Use `UNIQUE` constraints to prevent duplicates.

---

## 6. **DESCRIBE Statement**
- The `DESCRIBE` statement provides the structure of a table, including column names, data types, and constraints.

### Example:
```sql
DESCRIBE country;
```

---

## 7. **INSERT INTO Statement**
- The `INSERT INTO` statement is used to add new rows to a table.
- Can insert a single row or multiple rows at once.

### Example: Inserting a Single Row
```sql
INSERT INTO country (Code, Name, SurfaceArea)
VALUES ('BRA', 'Brazil', 8547403.00);
```

### Example: Inserting Multiple Rows
```sql
INSERT INTO country (Code, Name, SurfaceArea)
VALUES ('CAN', 'Canada', 9984670.00),
       ('MEX', 'Mexico', 1964375.00);
```

---

## 8. **NULL Values**
- **NULL** represents a missing or unknown value.
- **NULL** is different from zero or an empty string.
- Columns with `NOT NULL` constraints cannot contain `NULL` values.

### Example: Inserting a NULL Value
```sql
INSERT INTO employees (id, name, salary)
VALUES (1, 'John Doe', NULL);
```

---

## 9. **Key Takeaways**
- **Importing `.csv` Files**: Verify the file structure, create a matching table, and use `LOAD DATA` to import.
- **Cleaning Data**: Use SQL functions like `TRIM`, `CONCAT`, and `LOWER` to clean and standardize data.
- **INSERT INTO**: Add single or multiple rows to a table using the `INSERT INTO` statement.
- **NULL Values**: Use `NULL` to represent missing or unknown data, but ensure columns allow `NULL` values.

---

## 10. **Examples**
### Example 1: Importing a `.csv` File
```sql
LOAD DATA INFILE 'c:/tmp/city.csv'
INTO TABLE city
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

### Example 2: Inserting Data
```sql
INSERT INTO country (Code, Name, SurfaceArea)
VALUES ('BRA', 'Brazil', 8547403.00);
```

### Example 3: Cleaning Data
```sql
UPDATE employees
SET name = TRIM(name);
```

---

This module provides a comprehensive understanding of how to insert data into a database, including importing `.csv` files, cleaning data, and using SQL statements effectively.

Thank you for reviewing these comprehensive notes! Let me know if you need further clarification or additional details.
