# Database Table Operations: Comprehensive Guide

## Task 1: Connecting to the Database

### Steps to Connect:
1. Access AWS EC2 Console
2. Select "Command Host" instance
3. Connect via Session Manager
4. Elevate privileges and navigate to home directory:
   ```bash
   sudo su
   cd /home/ec2-user/
   ```
5. Connect to MySQL:
   ```bash
   mysql -u root --password='re:St@rt!9'
   ```

**Troubleshooting Tip**: If disconnected, simply reconnect and rerun the commands.

## Task 2: Creating and Modifying Database Objects

### Database Operations:
1. **List existing databases**:
   ```sql
   SHOW DATABASES;
   ```

2. **Create new database**:
   ```sql
   CREATE DATABASE world;
   ```

3. **Verify creation**:
   ```sql
   SHOW DATABASES;
   ```

### Table Operations:
1. **Create country table**:
   ```sql
   CREATE TABLE world.country (
     `Code` CHAR(3) NOT NULL DEFAULT '',
     `Name` CHAR(52) NOT NULL DEFAULT '',
     `Conitinent` enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') NOT NULL DEFAULT 'Asia',
     -- Additional columns...
     PRIMARY KEY (`Code`)
   );
   ```

2. **Verify table creation**:
   ```sql
   USE world;
   SHOW TABLES;
   ```

3. **View table structure**:
   ```sql
   SHOW COLUMNS FROM world.country;
   ```

4. **Fix column name typo**:
   ```sql
   ALTER TABLE world.country RENAME COLUMN Conitinent TO Continent;
   ```

### Challenge 1 Solution:
```sql
CREATE TABLE world.city (
  `Name` CHAR(52), 
  `Region` CHAR(26)
);
```

## Task 3: Deleting Database Objects

### Dropping Objects:
1. **Drop city table**:
   ```sql
   DROP TABLE world.city;
   ```

2. **Challenge 2 Solution**:
   ```sql
   DROP TABLE world.country;
   ```

3. **Verify tables dropped**:
   ```sql
   SHOW TABLES;
   ```

4. **Drop entire database**:
   ```sql
   DROP DATABASE world;
   ```

5. **Verify database dropped**:
   ```sql
   SHOW DATABASES;
   ```

## Key SQL Commands Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `CREATE DATABASE` | Create new database | `CREATE DATABASE world;` |
| `CREATE TABLE` | Create new table | `CREATE TABLE t (id INT);` |
| `SHOW DATABASES` | List all databases | `SHOW DATABASES;` |
| `SHOW TABLES` | List tables in current DB | `SHOW TABLES;` |
| `SHOW COLUMNS` | Show table structure | `SHOW COLUMNS FROM table;` |
| `ALTER TABLE` | Modify table structure | `ALTER TABLE t RENAME COLUMN old TO new;` |
| `DROP TABLE` | Delete a table | `DROP TABLE t;` |
| `DROP DATABASE` | Delete a database | `DROP DATABASE db;` |

## Best Practices

1. **Always verify** before dropping objects
2. **Use transactions** when available for DDL operations
3. **Maintain backups** before destructive operations
4. **Follow naming conventions** (consistent case, meaningful names)
5. **Document schema changes** for team awareness

## Common Pitfalls

1. **Forgetting to select database** with `USE` command
2. **Misspelling column/table names** in ALTER statements
3. **Dropping wrong objects** - double-check names
4. **Case sensitivity issues** depending on DB platform
5. **Locking issues** during schema changes on production

## Extended Learning

1. **Constraints**:
   ```sql
   ALTER TABLE city ADD CONSTRAINT fk_country 
   FOREIGN KEY (CountryCode) REFERENCES country(Code);
   ```

2. **Indexes**:
   ```sql
   CREATE INDEX idx_name ON city(Name);
   ```

3. **Advanced data types**:
   ```sql
   CREATE TABLE demo (
     id UUID PRIMARY KEY,
     metadata JSON,
     coords GEOMETRY
   );
   ```

This lab provides essential skills for database schema management that form the foundation for more advanced database administration and development tasks.