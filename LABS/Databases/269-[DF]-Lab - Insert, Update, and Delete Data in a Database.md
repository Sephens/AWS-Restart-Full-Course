# Database Data Manipulation: INSERT, UPDATE, DELETE Operations

## Task 1: Connecting to the Database

### Connection Steps
1. Access AWS EC2 Console
2. Connect to "Command Host" via Session Manager
3. Elevate privileges and navigate to home:
   ```bash
   sudo su
   cd /home/ec2-user/
   ```
4. Connect to MySQL:
   ```bash
   mysql -u root --password='re:St@rt!9'
   ```

5. Verify databases:
   ```sql
   SHOW DATABASES;
   ```

## Task 2: Inserting Data

### Inserting Single Rows
```sql
-- Insert Ireland record
INSERT INTO world.country VALUES 
('IRL','Ireland','Europe','British Islands',70273.00,1921,3775100,76.8,75921.00,73132.00,'Ireland/Éire','Republic',1447,'IE');

-- Insert Australia record
INSERT INTO world.country VALUES 
('AUS','Australia','Oceania','Australia and New Zealand',7741220.00,1901,18886000,79.8,351182.00,392911.00,'Australia','Constitutional Monarchy, Federation',135,'AU');
```

### Verification
```sql
SELECT * FROM world.country WHERE Code IN ('IRL', 'AUS');
```

## Task 3: Updating Data

### Mass Updates (Caution!)
```sql
-- Update all populations to 0
UPDATE world.country SET Population = 0;

-- Update multiple columns
UPDATE world.country SET Population = 100, SurfaceArea = 100;
```

### Verification
```sql
SELECT * FROM world.country;
```

## Task 4: Deleting Data

### Complete Table Deletion
```sql
-- Disable foreign key checks temporarily
SET FOREIGN_KEY_CHECKS = 0;

-- Delete all records
DELETE FROM world.country;

-- Verify deletion
SELECT * FROM world.country;
```

## Task 5: Bulk Data Import

### Import Process
1. Exit MySQL:
   ```sql
   QUIT;
   ```

2. Verify import file:
   ```bash
   ls /home/ec2-user/world.sql
   ```

3. Run import:
   ```bash
   mysql -u root --password='re:St@rt!9' < /home/ec2-user/world.sql
   ```

4. Reconnect and verify:
   ```sql
   USE world;
   SHOW TABLES;
   SELECT * FROM country LIMIT 5;
   ```

## Key SQL Commands

| Operation | Command | Example |
|-----------|---------|---------|
| Insert | `INSERT INTO` | `INSERT INTO t VALUES (1, 'A');` |
| Update | `UPDATE SET` | `UPDATE t SET col=1;` |
| Delete | `DELETE FROM` | `DELETE FROM t;` |
| Import | `mysql < file.sql` | `mysql -u user < data.sql` |

## Best Practices

1. **Always backup** before mass updates/deletes
2. **Use transactions** where possible:
   ```sql
   START TRANSACTION;
   INSERT INTO t VALUES (1);
   COMMIT;
   ```
3. **Be specific** with WHERE clauses to avoid mass updates
4. **Test first** with SELECT before UPDATE/DELETE
5. **Consider constraints** (disable temporarily if needed)

## Common Pitfalls

1. **Omitting WHERE clauses** causing mass updates
2. **Violating constraints** during inserts
3. **Data type mismatches** in inserts
4. **Case sensitivity** in string comparisons
5. **Forgetting to re-enable** foreign key checks

## Advanced Techniques

### Conditional Inserts
```sql
INSERT INTO country
SELECT * FROM new_countries
WHERE region = 'Europe';
```

### Batch Updates
```sql
UPDATE country
SET Population = Population * 1.1
WHERE Continent = 'Asia';
```

### Safe Deletes
```sql
-- First verify
SELECT * FROM city WHERE CountryCode NOT IN (SELECT Code FROM country);

-- Then delete orphans
DELETE FROM city WHERE CountryCode NOT IN (SELECT Code FROM country);
```

This lab provides essential skills for data manipulation that form the foundation for database administration and application development.