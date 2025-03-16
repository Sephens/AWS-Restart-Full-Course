# Challenge Lab: Build Your DB Server and Interact With Your DB

## Overview

This lab is designed to reinforce the concept of leveraging an **AWS-managed database instance** to solve relational database needs. You will use **Amazon Relational Database Service (Amazon RDS)** to create a database instance, interact with it using a MySQL client, and perform various database operations.

### Key Concepts:
- **Amazon RDS**: A managed relational database service that simplifies database setup, operation, and scaling.
- **Database Engines**: Amazon RDS supports multiple database engines, including **Amazon Aurora**, **MySQL**, **PostgreSQL**, **Oracle**, **MariaDB**, and **Microsoft SQL Server**.
- **Query Editor**: Use the Amazon RDS Query Editor to interact with your database.

---

## Lab Objectives

After completing this lab, you will be able to:
1. **Create an RDS instance** using Amazon Aurora or MySQL.
2. **Use the Amazon RDS Query Editor** to query data.
3. **Install a MySQL client** on a Linux server and connect to the RDS instance.
4. **Create tables**, **insert data**, and **perform queries** on the database.

---

## Duration

This lab takes approximately **45 minutes**.

---

## Accessing the AWS Management Console

1. **Start the Lab**:
   - At the top of these instructions, click **Start Lab** to launch your lab.
   - Wait until you see the message **"Lab status: ready"**, then close the **Start Lab** panel.

2. **Open the AWS Management Console**:
   - Click **AWS** to open the AWS Management Console in a new browser tab.
   - If a pop-up blocker prevents the tab from opening, allow pop-ups for the site.

3. **Arrange Browser Tabs**:
   - Arrange the AWS Management Console tab alongside these instructions for easier navigation.

---

## Your Challenge

### Step 1: Launch an Amazon RDS DB Instance

1. **Navigate to Amazon RDS**:
   - In the AWS Management Console, search for **RDS** and select **Amazon RDS**.

2. **Create a Database**:
   - Click **Create database**.
   - Choose **Standard create**.
   - Select the **Database Engine**:
     - Choose either **Amazon Aurora** or **MySQL**.
     - **Note**: Amazon Aurora Serverless is not available for this lab.
   - Under **Templates**, select **Dev/Test** or **Free tier**.

3. **Configure DB Instance**:
   - **DB instance size**: Choose **Burstable classes** (e.g., `db.t3.micro` to `db.t3.medium`).
   - **Storage**: Select **General Purpose SSD (gp2)** with a size of up to **100 GB**.
   - **Availability and durability**: Do **not** create a standby instance.
   - **Amazon VPC**: Use the **Lab VPC**.
   - **Security Group**: Ensure the security group allows the **LinuxServer** to connect to the RDS instance.

4. **Additional Configuration**:
   - For **MySQL**, disable **Enhanced monitoring** under **Additional configuration**.
   - **Purchasing Options**: Use **On-Demand instances**. Other purchasing options are disabled.

5. **Set Credentials**:
   - Provide a **Master username** and **Master password**. Make a note of these credentials as they will be needed later.

6. **Create the Database**:
   - Click **Create database**.
   - Wait for the database status to change to **Available**.

---

### Step 2: Connect to the Linux Server

1. **Download PEM/PPK File**:
   - Click **Details** followed by **Show**.
   - Download the **PEM** file (for Linux/macOS) or **PPK** file (for Windows).

2. **Note the LinuxServer Address**:
   - Make a note of the **LinuxServer address** provided in the lab.

3. **Connect via SSH**:
   - Use an SSH client (e.g., PuTTY for Windows or Terminal for Linux/macOS) to connect to the LinuxServer.
   - Use the downloaded PEM/PPK file for authentication.

---

### Step 3: Install MySQL Client and Connect to the RDS Instance

1. **Install MySQL Client**:
   - On the LinuxServer, run the following command to install the MySQL client:
     ```bash
     sudo yum install mysql -y
     ```

2. **Connect to the RDS Instance**:
   - Use the following command to connect to your RDS instance:
     ```bash
     mysql -h <RDS-Endpoint> -u <Master-Username> -p
     ```
   - Replace `<RDS-Endpoint>` with the endpoint of your RDS instance and `<Master-Username>` with the master username you created earlier.
   - Enter the **Master password** when prompted.

---

### Step 4: Create Tables and Insert Data

1. **Create the `RESTART` Table**:
   - Run the following SQL command to create the `RESTART` table:
     ```sql
     CREATE TABLE RESTART (
         StudentID INT PRIMARY KEY,
         StudentName VARCHAR(100),
         RestartCity VARCHAR(100),
         GraduationDate DATETIME
     );
     ```
   - **Capture a screenshot** of the table creation for submission.

2. **Insert 10 Sample Rows**:
   - Insert 10 sample rows into the `RESTART` table using the following command:
     ```sql
     INSERT INTO RESTART (StudentID, StudentName, RestartCity, GraduationDate) VALUES
     (1, 'John Doe', 'New York', '2023-12-15 10:00:00'),
     (2, 'Jane Smith', 'Los Angeles', '2023-12-16 11:00:00'),
     (3, 'Alice Johnson', 'Chicago', '2023-12-17 12:00:00'),
     (4, 'Bob Brown', 'Houston', '2023-12-18 13:00:00'),
     (5, 'Charlie Davis', 'Phoenix', '2023-12-19 14:00:00'),
     (6, 'Eve White', 'Philadelphia', '2023-12-20 15:00:00'),
     (7, 'Frank Wilson', 'San Antonio', '2023-12-21 16:00:00'),
     (8, 'Grace Lee', 'San Diego', '2023-12-22 17:00:00'),
     (9, 'Henry Martinez', 'Dallas', '2023-12-23 18:00:00'),
     (10, 'Ivy Garcia', 'San Jose', '2023-12-24 19:00:00');
     ```
   - **Capture a screenshot** of the inserted rows for submission.

3. **Select All Rows from `RESTART` Table**:
   - Run the following SQL command to select all rows from the `RESTART` table:
     ```sql
     SELECT * FROM RESTART;
     ```
   - **Capture a screenshot** of the output for submission.

---

### Step 5: Create the `CLOUD_PRACTITIONER` Table and Insert Data

1. **Create the `CLOUD_PRACTITIONER` Table**:
   - Run the following SQL command to create the `CLOUD_PRACTITIONER` table:
     ```sql
     CREATE TABLE CLOUD_PRACTITIONER (
         StudentID INT,
         CertificationDate DATETIME
     );
     ```
   - **Capture a screenshot** of the table creation for submission.

2. **Insert 5 Sample Rows**:
   - Insert 5 sample rows into the `CLOUD_PRACTITIONER` table using the following command:
     ```sql
     INSERT INTO CLOUD_PRACTITIONER (StudentID, CertificationDate) VALUES
     (1, '2023-01-15 10:00:00'),
     (2, '2023-02-16 11:00:00'),
     (3, '2023-03-17 12:00:00'),
     (4, '2023-04-18 13:00:00'),
     (5, '2023-05-19 14:00:00');
     ```
   - **Capture a screenshot** of the inserted rows for submission.

3. **Select All Rows from `CLOUD_PRACTITIONER` Table**:
   - Run the following SQL command to select all rows from the `CLOUD_PRACTITIONER` table:
     ```sql
     SELECT * FROM CLOUD_PRACTITIONER;
     ```
   - **Capture a screenshot** of the output for submission.

---

### Step 6: Perform an Inner Join Between the Two Tables

1. **Inner Join Query**:
   - Run the following SQL command to perform an inner join between the `RESTART` and `CLOUD_PRACTITIONER` tables:
     ```sql
     SELECT R.StudentID, R.StudentName, C.CertificationDate
     FROM RESTART R
     INNER JOIN CLOUD_PRACTITIONER C
     ON R.StudentID = C.StudentID;
     ```
   - **Capture a screenshot** of the output for submission.

---

## Submission

Submit the following screenshots:
1. **Creation of the `RESTART` table**.
2. **Insertion of 10 rows into the `RESTART` table**.
3. **Selection of all rows from the `RESTART` table**.
4. **Creation of the `CLOUD_PRACTITIONER` table**.
5. **Insertion of 5 rows into the `CLOUD_PRACTITIONER` table**.
6. **Selection of all rows from the `CLOUD_PRACTITIONER` table**.
7. **Inner join query result** between the two tables.

---

## Conclusion

By completing this lab, you have gained hands-on experience with **Amazon RDS**, including creating a database instance, connecting to it, and performing various database operations. This lab reinforces the importance of using managed database services to simplify database administration and focus on application development.