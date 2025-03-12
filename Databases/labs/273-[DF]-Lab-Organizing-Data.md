# Organizing Data

## Scenario
The database operations team has created a relational database named `world` containing three tables: `city`, `country`, and `countrylanguage`. You will help write a few queries to group records for analysis by using both the `GROUP BY` and `OVER` clauses.

---

## Lab Overview and Objectives
This lab demonstrates how to use some common database functions with the `GROUP BY` and `OVER` clauses.

After completing this lab, you should be able to:
1. Use the `GROUP BY` clause with the aggregate function `SUM()`.
2. Use the `OVER` clause with the `RANK()` window function.
3. Use the `OVER` clause with the aggregate function `SUM()` and the `RANK()` window function.

When you start the lab, the following resources are already created for you:
- A **Command Host** instance and `world` database containing three tables (`city`, `country`, and `countrylanguage`).

At the end of this lab, you will have used both the `GROUP BY` and `OVER` clauses with some common database operators:
- A lab user is connected to a database instance. A database called `world` containing three tables (`city`, `country`, and `countrylanguage`) is created.
- It also displays some commonly used SQL clauses and database functions.

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
In this task, you query the `world` database using various `SELECT` statements and database functions.

### Steps:
1. To show the existing databases, enter the following command in the terminal:
   ```sql
   SHOW DATABASES;
   ```
   - Verify that a database named `world` is available. If the `world` database is not available, contact your instructor.
2. To review the table schema, data, and number of rows in the `country` table, enter the following query:
   ```sql
   SELECT * FROM world.country;
   ```
3. To return a list of records where the `Region` is "Australia and New Zealand," run the following query:
   ```sql
   SELECT Region, Name, Population 
   FROM world.country 
   WHERE Region = 'Australia and New Zealand' 
   ORDER BY Population DESC;
   ```
   - This query includes an `ORDER BY` clause to arrange the results by `Population` in descending order.
4. To use the `GROUP BY` clause with the `SUM()` function, run the following query:
   ```sql
   SELECT Region, SUM(Population) AS "Total Population" 
   FROM world.country 
   WHERE Region = 'Australia and New Zealand' 
   GROUP BY Region 
   ORDER BY SUM(Population) DESC;
   ```
   - This query groups records by `Region` and calculates the total population for the "Australia and New Zealand" region.
5. To use the `OVER` clause with the `SUM()` function to generate a running total, run the following query:
   ```sql
   SELECT Region, Name, Population, 
          SUM(Population) OVER (PARTITION BY Region ORDER BY Population) AS "Running Total" 
   FROM world.country 
   WHERE Region = 'Australia and New Zealand';
   ```
   - This query calculates a running total of the population for each country in the "Australia and New Zealand" region.
6. To use the `OVER` clause with the `RANK()` function, run the following query:
   ```sql
   SELECT Region, Name, Population, 
          SUM(Population) OVER (PARTITION BY Region ORDER BY Population) AS "Running Total", 
          RANK() OVER (PARTITION BY Region ORDER BY Population) AS "Ranked" 
   FROM world.country 
   WHERE Region = 'Australia and New Zealand';
   ```
   - This query ranks countries within the "Australia and New Zealand" region by their population.

---

## Challenge
Write a query to rank the countries in each region by their population from largest to smallest.

### Solution:
```sql
SELECT Region, Name, Population, 
       RANK() OVER (PARTITION BY Region ORDER BY Population DESC) AS "Ranked" 
FROM world.country 
ORDER BY Region, Ranked;
```

---

## Conclusion
Congratulations! You have now successfully:
1. Used the `GROUP BY` clause with the aggregate function `SUM()`.
2. Used the `OVER` clause with the `RANK()` window function.
3. Used the `OVER` clause with the aggregate function `SUM()` and the `RANK()` window function.

---

## Lab Complete
Choose **End Lab** at the top of this page, and then select **Yes** to confirm that you want to end the lab. An **Ended AWS Lab Successfully** message is briefly displayed indicating that the lab has ended.

---

## Additional Notes and Examples
### Notes:
1. **GROUP BY Clause**: Use the `GROUP BY` clause to group records and apply aggregate functions like `SUM()`, `AVG()`, `COUNT()`, etc.
2. **OVER Clause**: Use the `OVER` clause with window functions like `RANK()` and `SUM()` to perform calculations across a set of rows related to the current row.
3. **RANK() Function**: Use the `RANK()` function to assign a unique rank to each row within a partition of the result set.

### Examples:
1. **Total Population by Continent**:
   ```sql
   SELECT Continent, SUM(Population) AS "Total Population" 
   FROM world.country 
   GROUP BY Continent 
   ORDER BY SUM(Population) DESC;
   ```
2. **Running Total by Continent**:
   ```sql
   SELECT Continent, Name, Population, 
          SUM(Population) OVER (PARTITION BY Continent ORDER BY Population) AS "Running Total" 
   FROM world.country;
   ```
3. **Rank Countries by Population**:
   ```sql
   SELECT Name, Population, 
          RANK() OVER (ORDER BY Population DESC) AS "Ranked" 
   FROM world.country;
   ```

By following these steps and examples, you can confidently organize and analyze data in a relational database using SQL.