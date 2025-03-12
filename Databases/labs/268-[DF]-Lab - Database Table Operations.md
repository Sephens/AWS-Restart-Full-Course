# Database Table Operations - Comprehensive Notes and Examples

This document provides a **detailed and comprehensive** summary of the "Database Table Operations" lab, including **key concepts, step-by-step instructions, examples, and additional explanations**. The lab focuses on performing common database and table operations such as creating, altering, and dropping databases and tables.

---

## **Key Takeaways**
1. **Database Operations**:
   - **CREATE**: Used to create databases and tables.
   - **SHOW**: Used to view available databases and tables.
   - **ALTER**: Used to modify the structure of a table.
   - **DROP**: Used to delete databases and tables.
2. **MySQL Commands**:
   - **CREATE DATABASE**: Creates a new database.
   - **CREATE TABLE**: Creates a new table with a defined schema.
   - **SHOW DATABASES/TABLES**: Lists all databases or tables.
   - **ALTER TABLE**: Modifies the structure of an existing table.
   - **DROP TABLE/DATABASE**: Deletes a table or database.

---

## **Lab Overview**

### **Objectives**
- Use the **CREATE** statement to create databases and tables.
- Use the **SHOW** statement to view available databases and tables.
- Use the **ALTER** statement to alter the structure of a table.
- Use the **DROP** statement to delete databases and tables.

### **Duration**
- Approximately **45 minutes**.

---

## **Lab Steps**

### **Task 1: Connect to the Command Host**
1. **Steps**:
   - Navigate to **EC2** → **Instances** → Select **Command Host** → **Connect** → **Session Manager**.
   - Run the following commands to configure the terminal:
     ```bash
     sudo su
     cd /home/ec2-user/
     ```
   - Connect to the MySQL database:
     ```bash
     mysql -u root --password='re:St@rt!9'
     ```
2. **Result**:
   - You are connected to the MySQL database instance.
3. **Additional Explanation**:
   - The `mysql` command connects to the MySQL database using the root user and the provided password.
   - **Session Manager** allows you to connect to EC2 instances without needing SSH keys.

---

### **Task 2: Create a Database and a Table**
1. **Show Existing Databases**:
   - Run the following query:
     ```sql
     SHOW DATABASES;
     ```
   - **Expected Output**:
     ```plaintext
     +--------------------+
     | Database           |
     +--------------------+
     | information_schema |
     | mysql              |
     | performance_schema |
     | sys                |
     +--------------------+
     ```
2. **Create a New Database**:
   - Run the following command:
     ```sql
     CREATE DATABASE world;
     ```
   - Verify the creation:
     ```sql
     SHOW DATABASES;
     ```
   - **Expected Output**:
     ```plaintext
     +--------------------+
     | Database           |
     +--------------------+
     | information_schema |
     | mysql              |
     | performance_schema |
     | sys                |
     | world              |
     +--------------------+
     ```
3. **Create a Table**:
   - Run the following command to create a `country` table:
     ```sql
     CREATE TABLE world.country (
       `Code` CHAR(3) NOT NULL DEFAULT '',
       `Name` CHAR(52) NOT NULL DEFAULT '',
       `Conitinent` ENUM('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') NOT NULL DEFAULT 'Asia',
       `Region` CHAR(26) NOT NULL DEFAULT '',
       `SurfaceArea` FLOAT(10,2) NOT NULL DEFAULT '0.00',
       `IndepYear` SMALLINT(6) DEFAULT NULL,
       `Population` INT(11) NOT NULL DEFAULT '0',
       `LifeExpectancy` FLOAT(3,1) DEFAULT NULL,
       `GNP` FLOAT(10,2) DEFAULT NULL,
       `GNPOld` FLOAT(10,2) DEFAULT NULL,
       `LocalName` CHAR(45) NOT NULL DEFAULT '',
       `GovernmentForm` CHAR(45) NOT NULL DEFAULT '',
       `HeadOfState` CHAR(60) DEFAULT NULL,
       `Capital` INT(11) DEFAULT NULL,
       `Code2` CHAR(2) NOT NULL DEFAULT '',
       PRIMARY KEY (`Code`)
     );
     ```
   - Verify the table creation:
     ```sql
     USE world;
     SHOW TABLES;
     ```
   - **Expected Output**:
     ```plaintext
     +-----------------+
     | Tables_in_world |
     +-----------------+
     | country         |
     +-----------------+
     ```
4. **Show Table Columns**:
   - Run the following query:
     ```sql
     SHOW COLUMNS FROM world.country;
     ```
   - **Expected Output**:
     ```plaintext
     +----------------+---------------------+------+-----+---------+-------+
     | Field          | Type                | Null | Key | Default | Extra |
     +----------------+---------------------+------+-----+---------+-------+
     | Code           | char(3)             | NO   | PRI |         |       |
     | Name           | char(52)            | NO   |     |         |       |
     | Conitinent     | enum(...)           | NO   |     | Asia    |       |
     | Region         | char(26)            | NO   |     |         |       |
     | SurfaceArea    | float(10,2)         | NO   |     | 0.00    |       |
     | IndepYear      | smallint(6)         | YES  |     | NULL    |       |
     | Population     | int(11)             | NO   |     | 0       |       |
     | LifeExpectancy | float(3,1)          | YES  |     | NULL    |       |
     | GNP            | float(10,2)         | YES  |     | NULL    |       |
     | GNPOld         | float(10,2)         | YES  |     | NULL    |       |
     | LocalName      | char(45)            | NO   |     |         |       |
     | GovernmentForm | char(45)            | NO   |     |         |       |
     | HeadOfState    | char(60)            | YES  |     | NULL    |       |
     | Capital        | int(11)             | YES  |     | NULL    |       |
     | Code2          | char(2)             | NO   |     |         |       |
     +----------------+---------------------+------+-----+---------+-------+
     ```
5. **Fix a Typo in the Table Schema**:
   - The `Conitinent` column is misspelled. Fix it using the `ALTER TABLE` command:
     ```sql
     ALTER TABLE world.country RENAME COLUMN Conitinent TO Continent;
     ```
   - Verify the change:
     ```sql
     SHOW COLUMNS FROM world.country;
     ```
   - **Expected Output**:
     - The column name should now be `Continent`.

---

### **Challenge 1: Create a Table Named `city`**
1. **Steps**:
   - Create a table named `city` with two columns: `Name` and `Region`.
   - Run the following command:
     ```sql
     CREATE TABLE world.city (
       `Name` CHAR(52) NOT NULL DEFAULT '',
       `Region` CHAR(26) NOT NULL DEFAULT ''
     );
     ```
2. **Result**:
   - A new table named `city` is created with the specified columns.

---

### **Task 3: Delete a Database and Tables**
1. **Drop the `city` Table**:
   - Run the following command:
     ```sql
     DROP TABLE world.city;
     ```
   - Verify the deletion:
     ```sql
     SHOW TABLES;
     ```
   - **Expected Output**:
     ```plaintext
     +-----------------+
     | Tables_in_world |
     +-----------------+
     | country         |
     +-----------------+
     ```
2. **Drop the `country` Table**:
   - Run the following command:
     ```sql
     DROP TABLE world.country;
     ```
   - Verify the deletion:
     ```sql
     SHOW TABLES;
     ```
   - **Expected Output**:
     ```plaintext
     Empty set (0.00 sec)
     ```
3. **Drop the `world` Database**:
   - Run the following command:
     ```sql
     DROP DATABASE world;
     ```
   - Verify the deletion:
     ```sql
     SHOW DATABASES;
     ```
   - **Expected Output**:
     ```plaintext
     +--------------------+
     | Database           |
     +--------------------+
     | information_schema |
     | mysql              |
     | performance_schema |
     | sys                |
     +--------------------+
     ```

---

## **Key Concepts**

### **CREATE Statement**
- **CREATE DATABASE**: Creates a new database.
  ```sql
  CREATE DATABASE world;
  ```
- **CREATE TABLE**: Creates a new table with a defined schema.
  ```sql
  CREATE TABLE world.country (
    `Code` CHAR(3) NOT NULL DEFAULT '',
    `Name` CHAR(52) NOT NULL DEFAULT '',
    PRIMARY KEY (`Code`)
  );
  ```

### **SHOW Statement**
- **SHOW DATABASES**: Lists all databases.
  ```sql
  SHOW DATABASES;
  ```
- **SHOW TABLES**: Lists all tables in the current database.
  ```sql
  SHOW TABLES;
  ```
- **SHOW COLUMNS**: Lists all columns in a table.
  ```sql
  SHOW COLUMNS FROM world.country;
  ```

### **ALTER Statement**
- **ALTER TABLE**: Modifies the structure of an existing table.
  ```sql
  ALTER TABLE world.country RENAME COLUMN Conitinent TO Continent;
  ```

### **DROP Statement**
- **DROP TABLE**: Deletes a table.
  ```sql
  DROP TABLE world.country;
  ```
- **DROP DATABASE**: Deletes a database.
  ```sql
  DROP DATABASE world;
  ```

---

## **Conclusion**
- **Database and Table Operations**: Successfully created, altered, and dropped databases and tables.
- **MySQL Commands**: Used `CREATE`, `SHOW`, `ALTER`, and `DROP` statements to manage databases and tables.

---

**Next Steps**:
- Explore **indexes** to optimize query performance.
- Test **foreign keys** to enforce relationships between tables.
- Practice **backup and restore** operations for databases.

---