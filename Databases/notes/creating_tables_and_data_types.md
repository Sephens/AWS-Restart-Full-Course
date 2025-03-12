# Creating Tables and Learning Different Data Types

This module focuses on **creating tables** in a relational database and understanding **data types** used in SQL. It also covers **SQL sublanguages**, **constraints**, and **keys** that ensure data integrity.

---

## 1. **Relational Database Anatomy**
- **Database**: A collection of related data organized into tables.
- **Tables**: Analogous to spreadsheets, tables store related information about a specific concept.
  - **Columns (Fields)**: Represent attributes (e.g., `Name`, `Continent`).
  - **Rows (Records)**: Represent individual entities (e.g., a country or city).
- **Example**: A `Country` table might have columns like `Code`, `Name`, `Continent`, and `Region`.

---

## 2. **SQL Overview**
- **SQL (Structured Query Language)**: A standard language for querying and manipulating relational databases.
- **SQL Sublanguages**:
  - **DML (Data Manipulation Language)**:
    - Used to view, add, change, or delete data.
    - **Statements**: `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
    - **Example**:
      ```sql
      INSERT INTO city (id, name, countrycode, district)
      VALUES (1, 'New York', 'USA', 'NY');
      ```
  - **DDL (Data Definition Language)**:
    - Used to define and maintain database objects (e.g., tables, columns).
    - **Statements**: `CREATE`, `ALTER TABLE`, `DROP`.
    - **Example**:
      ```sql
      CREATE TABLE city (
          id INTEGER PRIMARY KEY,
          name VARCHAR(50),
          countrycode CHAR(3),
          district VARCHAR(50)
      );
      ```
  - **DCL (Data Control Language)**:
    - Controls access to data.
    - **Statements**: `GRANT`, `REVOKE`.
    - **Example**:
      ```sql
      GRANT SELECT ON city TO user1;
      ```

---

## 3. **Creating Tables**
- **CREATE TABLE Statement**:
  - Used to create a new table in a database.
  - **Syntax**:
    ```sql
    CREATE TABLE table_name (
        column1 DATA_TYPE [CONSTRAINTS],
        column2 DATA_TYPE [CONSTRAINTS],
        ...
    );
    ```
  - **Example**:
    ```sql
    CREATE TABLE city (
        id INTEGER NOT NULL PRIMARY KEY,
        name VARCHAR(20) DEFAULT NULL,
        countrycode VARCHAR(25) NOT NULL,
        district INTEGER NOT NULL
    );
    ```
  - **IF NOT EXISTS**: Ensures the table is only created if it doesn’t already exist.
    ```sql
    CREATE TABLE IF NOT EXISTS city (...);
    ```

---

## 4. **Data Types**
- **Predefined Data Types**: SQL provides built-in data types for columns.
  - **Numeric Types**:
    - `INTEGER`: Whole numbers (e.g., `120000`).
      ```sql
      age INTEGER
      ```
    - `DECIMAL(p, s)`: Exact decimal numbers (e.g., `123.456`).
      ```sql
      price DECIMAL(10, 2)
      ```
    - `FLOAT`: Approximate floating-point numbers (e.g., `3.1415`).
      ```sql
      temperature FLOAT
      ```
  - **Character String Types**:
    - `CHAR(length)`: Fixed-length strings (e.g., `'USA'`).
      ```sql
      countrycode CHAR(3)
      ```
    - `VARCHAR(length)`: Variable-length strings (e.g., `'New York'`).
      ```sql
      name VARCHAR(50)
      ```
    - `CLOB`: Large text data (e.g., a book chapter).
      ```sql
      description CLOB
      ```
  - **Date and Time Types**:
    - `DATE`: Represents a date (e.g., `2022-07-18`).
      ```sql
      hire_date DATE
      ```
    - `TIME`: Represents a time (e.g., `16:48:12`).
      ```sql
      start_time TIME
      ```
    - `TIMESTAMP`: Represents a date and time (e.g., `2022-07-18 16:48:12`).
      ```sql
      created_at TIMESTAMP
      ```

---

## 5. **Constraints**
- **Constraints** enforce rules on the data stored in tables.
  - **NOT NULL**: Ensures a column cannot have a `NULL` value.
    ```sql
    id INTEGER NOT NULL
    ```
  - **UNIQUE**: Ensures all values in a column are unique.
    ```sql
    email VARCHAR(255) UNIQUE
    ```
  - **DEFAULT**: Provides a default value if none is specified.
    ```sql
    status VARCHAR(10) DEFAULT 'active'
    ```
  - **PRIMARY KEY**: Uniquely identifies each row in a table.
    ```sql
    id INTEGER PRIMARY KEY
    ```
  - **FOREIGN KEY**: Links two tables by referencing the primary key of another table.
    ```sql
    countrycode VARCHAR(25) REFERENCES country(Code)
    ```

---

## 6. **Primary Keys (PK) and Foreign Keys (FK)**
- **Primary Key (PK)**:
  - A unique identifier for each row in a table.
  - **Example**:
    ```sql
    CREATE TABLE employee (
        employee_id INTEGER PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50)
    );
    ```
- **Foreign Key (FK)**:
  - A column that references the primary key of another table.
  - **Example**:
    ```sql
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        product_id INTEGER REFERENCES products(product_id),
        quantity INTEGER
    );
    ```
- **Referential Integrity**:
  - Ensures that every non-NULL foreign key value matches an existing primary key value.
  - **Example**: If `countrycode` in the `city` table is `IND`, there must be a corresponding `Code` in the `country` table with the value `IND`.

---

## 7. **Dropping Tables**
- **DROP TABLE Statement**:
  - Permanently removes a table and its data from the database.
  - **Syntax**:
    ```sql
    DROP TABLE table_name;
    ```
  - **Example**:
    ```sql
    DROP TABLE city;
    ```

---

## 8. **Naming Conventions**
- **Identifiers**: Names of database objects (e.g., tables, columns).
- **Best Practices**:
  - Use descriptive names (e.g., `customer_orders`).
  - Be consistent with singular/plural names (e.g., `order` vs. `orders`).
  - Avoid reserved SQL keywords (e.g., `SELECT`, `CREATE`).

---

## 9. **Key Takeaways**
- **Identifiers**: Names of database objects (e.g., tables, columns).
- **Primary Key**: Uniquely identifies each row in a table.
- **Foreign Key**: Links tables by referencing a primary key in another table.
- **Data Types**: Use appropriate data types (e.g., `INTEGER`, `VARCHAR`, `DATE`) for columns.
- **Constraints**: Enforce rules on data (e.g., `NOT NULL`, `UNIQUE`, `DEFAULT`).
- **SQL Sublanguages**: DML, DDL, and DCL are used for different database operations.

---

## 10. **Examples**
### Example 1: Creating a Table
```sql
CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    hire_date DATE DEFAULT CURRENT_DATE
);