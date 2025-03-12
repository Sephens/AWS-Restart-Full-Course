# Selecting Data from a Database

## Scenario
The database operations team has created a relational database named `world` containing three tables: `city`, `country`, and `countrylanguage`. Based on specific use cases defined in the lab exercise, you will write a few queries using database operators and the `SELECT` statement.

---

## Lab Overview and Objectives
This lab demonstrates how to use some common database operators and the `SELECT` statement.

After completing this lab, you should be able to:
1. Use the `SELECT` statement to query a database.
2. Use the `COUNT()` function.
3. Use the following operators to query a database:
   - `<`
   - `>`
   - `=`
   - `WHERE`
   - `ORDER BY`
   - `AND`

When you start the lab, the following resources are already created for you:
- A **Command Host** instance and `world` database containing three tables (`city`, `country`, and `countrylanguage`).

At the end of this lab, you will have used the `SELECT` statement and some common database operators:
- A lab user is connected to a database instance. A database called `world` containing three tables (`city`, `country`, and `countrylanguage`) is created.
- It also displays some commonly used database operations.

**Note**: Sample data in this course is taken from Statistics Finland, general regional statistics, February 4, 2022.

---

## Duration
This lab requires approximately **45 minutes** to complete.

---

## AWS Service Restrictions
In this lab environment, access to AWS services and service actions might be restricted to the ones that you need to complete the lab instructions. You might encounter errors if you attempt to access other services or perform actions beyond the ones that this lab describes.

---

## Accessing the AWS Management Console
1. At the upper-right corner of these instructions, choose **Start Lab**.
   - **Troubleshooting Tip**: If you get an **Access Denied** error, close the error box, and choose **Start Lab** again.
2. The following information indicates the lab status:
   - A **red circle** next to **AWS** at the upper-left corner of this page indicates the lab has not been started.
   - A **yellow circle** next to **AWS** indicates the lab is starting.
   - A **green circle** next to **AWS** indicates the lab is ready.
3. Wait for the lab to be ready before proceeding.
4. At the top of these instructions, choose the **green circle** next to **AWS**.
   - This option opens the AWS Management Console in a new browser tab. The system automatically signs you in.
   - **Tip**: If a new browser tab does not open, a banner or icon at the top of your browser will indicate that your browser is preventing the site from opening pop-up windows. Choose the banner or icon, and choose **Allow pop-ups**.
5. Arrange the AWS Management Console tab so that it displays alongside these instructions. Ideally, you should be able to see both browser tabs at the same time so that you can follow the lab steps.
6. **Do not change the lab Region** unless specifically instructed to do so.

---

## Task 1: Connect to the Command Host
In this task, you connect to an instance containing a database client, which is used to connect to a database. This instance is referred to as the **Command Host**.

### Steps:
1. In the AWS Management Console, choose the **Services** menu. Choose **Compute**, and then choose **EC2**.
2. In the left navigation menu, choose **Instances**.
3. Next to the instance labelled **Command Host**, select the check box and then choose **Connect**.
   - **Note**: If you do not see the **Command Host**, the lab is possibly still being provisioned, or you may be using another Region.
4. For **Connect to instance**, choose the **Session Manager** tab.
5. Choose **Connect** to open a terminal window.
   - **Note**: If the **Connect** button is not available, wait for a few minutes and try again.
6. To configure the terminal to access all required tools and resources, run the following command:
   ```bash
   sudo su
   cd /home/ec2-user/
   ```
   - **Tips**:
     - Copy and paste the command into the Session Manager terminal window.
     - If you are using a Windows system, press `Shift+Ctrl+v` to paste the command.
7. To connect to the database server, run the following command in the terminal. A password was configured when the database was installed.
   ```bash
   mysql -u root --password='re:St@rt!9'
   ```
   - **Tip**: At any stage of the lab, if the Sessions Manager window is not responsive or if you need to reconnect to the database, follow these steps:
     - Close the Sessions Manager window, and try to reconnect using the previous steps.
     - Run the following commands in the terminal:
       ```bash
       sudo su
       cd /home/ec2-user/
       mysql -u root --password='re:St@rt!9'
       ```

---

## Task 2: Query the World Database
In this task, you query the `world` database using various `SELECT` statements and database operators.

### Steps:
1. To show the existing databases, enter the following command in the terminal:
   ```sql
   SHOW DATABASES;
   ```
   - Verify that a database named `world` is available. If the `world` database is not available, contact your instructor.
2. To list all rows and columns in the `country` table, run the following query:
   ```sql
   SELECT * FROM world.country;
   ```
3. To count the number of rows in the `country` table, use the `COUNT()` function:
   ```sql
   SELECT COUNT(*) FROM world.country;
   ```
   - **Note**: To count the number of rows that have a value in a specific column, include the column name as a parameter in the `COUNT()` function. For example:
     ```sql
     SELECT COUNT(Population) FROM world.country;
     ```
4. To list all columns in the `country` table, run the following query to understand the table schema:
   ```sql
   SHOW COLUMNS FROM world.country;
   ```
5. To query specific columns in the `country` table, run the following query to return a result set that includes the `Name`, `Capital`, `Region`, `SurfaceArea`, and `Population` columns:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea, Population FROM world.country;
   ```
6. To add a more descriptive column name to the query output, use the `AS` option:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population FROM world.country;
   ```
   - **Note**: Scroll to the top of the query results, and observe that the `SurfaceArea` column is displayed as `Surface Area`.
7. To order the output based on the `Population` column, use the `ORDER BY` option:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population FROM world.country ORDER BY Population;
   ```
   - By default, the `ORDER BY` option orders data in ascending order.
8. To order data in descending order, use the `DESC` option with `ORDER BY`:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population FROM world.country ORDER BY Population DESC;
   ```
9. To list all rows with a population greater than 50,000,000, use the `WHERE` clause:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population FROM world.country WHERE Population > 50000000 ORDER BY Population DESC;
   ```
   - **Note**: You have used the `>` comparison operator. Similarly, you can use other comparison operators like `<`, `=`, etc.
10. To construct a `WHERE` clause using multiple conditions, use the `AND` operator:
    ```sql
    SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population FROM world.country WHERE Population > 50000000 AND Population < 100000000 ORDER BY Population DESC;
    ```
    - This query returns all rows with a population greater than 50,000,000 and less than 100,000,000.

---

## Challenge
Query the `country` table to return a set of records based on the following question:
**Which country in Southern Europe has a population greater than 50,000,000?**

### Solution:
```sql
SELECT Name, Capital, Region, SurfaceArea AS "Surface Area", Population 
FROM world.country 
WHERE Region = 'Southern Europe' AND Population > 50000000;
```

---

## Conclusion
Congratulations! You have now successfully:
1. Used the `SELECT` statement to query a database.
2. Used the `COUNT()` function.
3. Used the following operators to query a database:
   - `<`
   - `>`
   - `=`
   - `WHERE`
   - `ORDER BY`
   - `AND`

---

## Lab Complete
Choose **End Lab** at the top of this page, and then select **Yes** to confirm that you want to end the lab. An **Ended AWS Lab Successfully** message is briefly displayed indicating that the lab has ended.

---

## Additional Notes and Examples
### Notes:
1. **Comparison Operators**: Use comparison operators like `<`, `>`, `=`, `<=`, `>=`, and `!=` to filter data in `WHERE` clauses.
2. **Alias (`AS`)**: Use the `AS` keyword to provide more readable column names in query results.
3. **Ordering Data**: Use `ORDER BY` to sort query results in ascending (`ASC`) or descending (`DESC`) order.
4. **Combining Conditions**: Use `AND` and `OR` to combine multiple conditions in `WHERE` clauses.

### Examples:
1. **Count Specific Rows**:
   ```sql
   SELECT COUNT(*) FROM world.country WHERE Population > 100000000;
   ```
2. **Filter by Region**:
   ```sql
   SELECT Name, Capital, Region FROM world.country WHERE Region = 'Southern Europe';
   ```
3. **Order by Surface Area**:
   ```sql
   SELECT Name, SurfaceArea FROM world.country ORDER BY SurfaceArea DESC;
   ```
4. **Combine Conditions**:
   ```sql
   SELECT Name, Population FROM world.country WHERE Population > 50000000 AND Region = 'Asia';
   ```

By following these steps and examples, you can confidently query and analyze data in a relational database using SQL.