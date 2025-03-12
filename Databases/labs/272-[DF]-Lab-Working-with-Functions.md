# Working with Functions

## Scenario
The database operations team has created a relational database named `world` containing three tables: `city`, `country`, and `countrylanguage`. Based on specific use cases in the lab exercise, you will write a few queries using database functions with the `SELECT` statement and `WHERE` clause.

---

## Lab Overview and Objectives
This lab demonstrates how to use some common database functions with the `SELECT` statement and `WHERE` clause.

After completing this lab, you should be able to:
1. Use aggregate functions `SUM()`, `MIN()`, `MAX()`, and `AVG()` to summarize data.
2. Use the `SUBSTRING_INDEX()` function to split strings.
3. Use the `LENGTH()` and `TRIM()` functions to determine the length of a string.
4. Use the `DISTINCT()` function to filter duplicate records.
5. Use functions in the `SELECT` statement and `WHERE` clause.

When you start the lab, the following resources are already created for you:
- A **Command Host** instance and `world` database containing three tables (`city`, `country`, and `countrylanguage`).

At the end of this lab, you will have used the `SELECT` statement and `WHERE` clause with some common database functions:
- A lab user is connected to a database instance. A database called `world` containing three tables (`city`, `country`, and `countrylanguage`) is created.
- It also displays some commonly used SQL database functions.

**Note**: Sample data in this course is taken from Statistics Finland, General regional statistics, February 4, 2022.

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
   - A **red circle** next to **AWS** at the upper-left corner of this page indicates that the lab has not been started.
   - A **yellow circle** next to **AWS** indicates that the lab is starting.
   - A **green circle** next to **AWS** indicates that the lab is ready.
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
1. In the AWS Management Console, choose the **Services** menu. Under **Compute**, choose **EC2**.
2. In the navigation pane, choose **Instances**.
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
   - **Tip**: At any stage of the lab, if the Sessions Manager window is not responsive or if you need to reconnect to the database instance, follow these steps:
     - Close the Sessions Manager window, and try to reconnect using the previous steps.
     - Run the following commands in the terminal:
       ```bash
       sudo su
       cd /home/ec2-user/
       mysql -u root --password='re:St@rt!9'
       ```

---

## Task 2: Query the World Database
In this task, you query the `world` database using various `SELECT` statements and database functions. You use functions to process and manipulate data in a query.

### Steps:
1. To show the existing databases, enter the following command in the terminal:
   ```sql
   SHOW DATABASES;
   ```
   - Verify that a database named `world` is available. If the `world` database is not available, contact your instructor.
2. To review the table schema, data, and number of rows in the `country` table, run the following query:
   ```sql
   SELECT * FROM world.country;
   ```
3. To use aggregate functions (`SUM()`, `AVG()`, `MAX()`, `MIN()`, and `COUNT()`) to summarize data, run the following query:
   ```sql
   SELECT 
       SUM(Population) AS "Total Population",
       AVG(Population) AS "Average Population",
       MAX(Population) AS "Maximum Population",
       MIN(Population) AS "Minimum Population",
       COUNT(Population) AS "Number of Countries"
   FROM world.country;
   ```
   - **Explanation**:
     - `SUM()` adds all the population values together.
     - `AVG()` generates an average across all the population values.
     - `MAX()` finds the row with the highest population value.
     - `MIN()` finds the row with the lowest population value.
     - `COUNT()` finds the number of rows with a population value.
4. To split a string using the `SUBSTRING_INDEX()` function, run the following query:
   ```sql
   SELECT Region, SUBSTRING_INDEX(Region, " ", 1) AS "First Part of Region" 
   FROM world.country;
   ```
   - This query splits the `Region` column at the first space and returns the first part of the region name.
5. To filter records using `SUBSTRING_INDEX()` in the `WHERE` clause, run the following query:
   ```sql
   SELECT Name, Region 
   FROM world.country 
   WHERE SUBSTRING_INDEX(Region, " ", 1) = "Southern";
   ```
   - This query returns records where the first part of the region name is "Southern."
6. To determine the length of a string using `LENGTH()` and `TRIM()`, run the following query:
   ```sql
   SELECT Region 
   FROM world.country 
   WHERE LENGTH(TRIM(Region)) < 10;
   ```
   - This query returns regions with fewer than 10 characters in their names after trimming leading and trailing spaces.
7. To filter duplicate records using the `DISTINCT()` function, run the following query:
   ```sql
   SELECT DISTINCT(Region) 
   FROM world.country 
   WHERE LENGTH(TRIM(Region)) < 10;
   ```
   - This query returns unique regions with fewer than 10 characters in their names.

---

## Challenge
Query the `country` table to return a set of records based on the following requirement:
**Write a query to return rows that have "Micronesian/Caribbean" as the name in the `Region` column. The output should split the region as "Micronesia" and "Caribbean" into two separate columns: one named `Region Name 1` and one named `Region Name 2`.**

### Solution:
```sql
SELECT 
    SUBSTRING_INDEX(Region, "/", 1) AS "Region Name 1",
    SUBSTRING_INDEX(Region, "/", -1) AS "Region Name 2"
FROM world.country 
WHERE Region = "Micronesian/Caribbean";
```

---

## Conclusion
Congratulations! You have now successfully:
1. Used aggregate functions `SUM()`, `MIN()`, `MAX()`, and `AVG()` to summarize data.
2. Used the `SUBSTRING_INDEX()` function to split strings.
3. Used the `LENGTH()` and `TRIM()` functions to determine the length of a string.
4. Used the `DISTINCT()` function to filter duplicate records.
5. Used functions in the `SELECT` statement and `WHERE` clause.

---

## Lab Complete
Choose **End Lab** at the top of this page, and then select **Yes** to confirm that you want to end the lab. An **Ended AWS Lab Successfully** message is briefly displayed indicating that the lab has ended.

---

## Additional Notes and Examples
### Notes:
1. **Aggregate Functions**: Use `SUM()`, `AVG()`, `MAX()`, `MIN()`, and `COUNT()` to perform calculations on data.
2. **String Functions**: Use `SUBSTRING_INDEX()` to split strings, `LENGTH()` to determine string length, and `TRIM()` to remove leading and trailing spaces.
3. **Filtering Duplicates**: Use `DISTINCT()` to return unique values in a column.

### Examples:
1. **Average Population by Continent**:
   ```sql
   SELECT Continent, AVG(Population) AS "Average Population" 
   FROM world.country 
   GROUP BY Continent;
   ```
2. **Longest Region Name**:
   ```sql
   SELECT Region 
   FROM world.country 
   ORDER BY LENGTH(Region) DESC 
   LIMIT 1;
   ```
3. **Filter by String Length**:
   ```sql
   SELECT Name, Region 
   FROM world.country 
   WHERE LENGTH(TRIM(Region)) > 15;
   ```

By following these steps and examples, you can confidently use SQL functions to manipulate and analyze data in a relational database.