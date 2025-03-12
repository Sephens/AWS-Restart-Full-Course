# Performing a Conditional Search

## Scenario
The database operations team has created a relational database named `world` containing three tables: `city`, `country`, and `countrylanguage`. To help the team, you will write a few queries to search for records in the `country` table by using the `SELECT` statement and a `WHERE` clause.

---

## Lab Overview and Objectives
This lab demonstrates how to use the `SELECT` statement and a `WHERE` clause to filter records with a conditional search.

After completing this lab, you should be able to:
1. Write a search condition by using the `WHERE` clause.
2. Use the `BETWEEN` operator.
3. Use the `LIKE` operator with wildcard characters.
4. Use the `AS` operator to create a column alias.
5. Use functions in a `SELECT` statement.
6. Use functions in a `WHERE` clause.

When you start the lab, the following resources are already created for you:
- A **Command Host** instance with a database client installed. You will use the Command Host to query the `world` database, which contains three tables (`city`, `country`, and `countrylanguage`).

At the end of this lab, you will have learned how to use the `WHERE` clause, `BETWEEN` operator, and `LIKE` function to filter records:
- A lab user connects to a Command Host instance to query the tables in the `world` database.
- Commonly used SQL clauses, operators, and database functions are displayed.

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
2. The lab status can be interpreted as follows:
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
In this task, you connect to an Amazon Elastic Compute Cloud (Amazon EC2) instance containing a database client, which you will use to connect to a database. This instance is referred to as the **Command Host**.

### Steps:
1. In the AWS Management Console, choose the **Services** menu. Choose **Compute**, and then choose **EC2**.
2. In the left navigation menu, choose **Instances**.
3. Next to the instance labelled **Command Host**, select the check box and then choose **Connect**.
   - **Note**: If you do not see the **Command Host**, the lab is probably still being provisioned, or you might be using another Region.
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
     - If you are using a Windows system, press `Shift+Ctrl+V` to paste the command.
7. To connect to the database server, run the following command. A password was configured when the database was installed.
   ```bash
   mysql -u root --password='re:St@rt!9'
   ```
   - **Tip**: At any stage of the lab, if the Session Manager window is not responsive or if you need to reconnect to the database instance, follow these steps:
     - Close the Session Manager window, and try to reconnect using the previous steps.
     - Run the following commands in the terminal:
       ```bash
       sudo su
       cd /home/ec2-user/
       mysql -u root --password='re:St@rt!9'
       ```

---

## Task 2: Query the World Database
In this task, you will query the `world` database by using various `SELECT` statements and database functions.

### Steps:
1. To show the existing databases, run the following query:
   ```sql
   SHOW DATABASES;
   ```
   - Verify that a database named `world` is available. If the `world` database is not available, contact your instructor.
2. To review the table schema, data, and number of rows in the `country` table, run the following query:
   ```sql
   SELECT * FROM world.country;
   ```
3. To limit the number of records returned, use a `WHERE` clause to define the conditions that records must match. Use the `AND` operator to combine two conditions:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea, Population 
   FROM world.country 
   WHERE Population >= 50000000 AND Population <= 100000000;
   ```
   - This query returns records where the population is greater than or equal to 50,000,000 and less than or equal to 100,000,000.
4. To use the `BETWEEN` operator for a more readable query, run the following:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea, Population 
   FROM world.country 
   WHERE Population BETWEEN 50000000 AND 100000000;
   ```
   - The `BETWEEN` operator is inclusive, meaning it includes the beginning and ending values.
5. To search for a string pattern using the `LIKE` function, run the following query:
   ```sql
   SELECT SUM(Population) 
   FROM world.country 
   WHERE Region LIKE "%Europe%";
   ```
   - This query returns the total population of all European countries. The `%` wildcard represents any number of characters before or after the word "Europe."
6. To add a column alias for better readability, use the `AS` operator:
   ```sql
   SELECT SUM(Population) AS "Europe Population Total" 
   FROM world.country 
   WHERE Region LIKE "%Europe%";
   ```
   - The output column is now labeled "Europe Population Total."
7. To perform a case-sensitive search using the `LOWER` function, run the following query:
   ```sql
   SELECT Name, Capital, Region, SurfaceArea, Population 
   FROM world.country 
   WHERE LOWER(Region) LIKE "%central%";
   ```
   - This query converts the `Region` column to lowercase and searches for the string "central."

---

## Challenge
Write a query to return the sum of the surface area and sum of the population of North America.

### Solution:
```sql
SELECT SUM(SurfaceArea) AS "Total Surface Area", SUM(Population) AS "Total Population" 
FROM world.country 
WHERE Region = 'North America';
```

---

## Conclusion
Congratulations! You have now successfully:
1. Written a search condition using the `WHERE` clause.
2. Used the `BETWEEN` operator.
3. Used the `LIKE` operator with wildcard characters.
4. Created a column alias using the `AS` operator.
5. Used functions in a `SELECT` statement.
6. Used functions in a `WHERE` clause.

---

## Lab Complete
Choose **End Lab** at the top of this page, and then select **Yes** to confirm that you want to end the lab. An **Ended AWS Lab Successfully** message is briefly displayed indicating that the lab has ended.

---

## Additional Notes and Examples
### Notes:
1. **Wildcard Characters**: Use `%` in the `LIKE` operator to match any sequence of characters.
2. **Column Aliases**: Use the `AS` operator to make query results more readable.
3. **Case Sensitivity**: Use the `LOWER` or `UPPER` functions to perform case-insensitive searches.
4. **Aggregate Functions**: Use functions like `SUM`, `COUNT`, `AVG`, etc., to perform calculations on data.

### Examples:
1. **Filter by Region**:
   ```sql
   SELECT Name, Region 
   FROM world.country 
   WHERE Region LIKE "%Asia%";
   ```
2. **Sum of Population by Continent**:
   ```sql
   SELECT Continent, SUM(Population) AS "Total Population" 
   FROM world.country 
   GROUP BY Continent;
   ```
3. **Case-Insensitive Search**:
   ```sql
   SELECT Name, Region 
   FROM world.country 
   WHERE LOWER(Region) LIKE "%south%";
   ```

By following these steps and examples, you can confidently perform conditional searches and analyze data in a relational database using SQL.