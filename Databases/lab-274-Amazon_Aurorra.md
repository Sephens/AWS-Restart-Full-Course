# Introduction to Amazon Aurora - Comprehensive Notes and Examples

This document provides a detailed summary of the "Introduction to Amazon Aurora" lab, including key concepts, steps, and examples.

---

## **Key Takeaways**
1. **Amazon Aurora**: A fully managed, MySQL-compatible relational database engine optimized for high performance and scalability.
2. **Key Features**:
   - **High Performance**: Up to 5x faster than MySQL.
   - **Scalability**: Automatically scales storage up to 128 TB.
   - **High Availability**: Multi-AZ deployments with automatic failover.
   - **Global Tables**: Replicate data across AWS Regions for low-latency access.
3. **Lab Objectives**:
   - Create an Aurora instance.
   - Connect to an Amazon EC2 instance.
   - Configure the EC2 instance to connect to Aurora.
   - Query the Aurora instance.

---

## **Lab Overview**

### **Topics Covered**
- **Creating an Aurora Instance**: Learn how to set up an Aurora database.
- **Connecting to an EC2 Instance**: Use an EC2 instance to interact with Aurora.
- **Configuring EC2 for Aurora**: Install the MariaDB client and connect to Aurora.
- **Querying Aurora**: Create tables, insert data, and run queries.

### **Duration**
- Approximately **40 minutes**.

---

## **Lab Steps**

### **Task 1: Create an Aurora Instance**
1. **Steps**:
   - Navigate to the **AWS Management Console** → **RDS** → **Databases** → **Create database**.
   - Choose **Standard create**.
   - Select **Aurora (MySQL Compatible)** as the engine type.
   - Choose the default version (e.g., **8.0**).
   - Select **Dev/Test** template.
   - Configure the following:
     - **DB cluster identifier**: `aurora`.
     - **Master username**: `admin`.
     - **Master password**: `admin123`.
     - **DB instance class**: `db.t3.medium`.
     - **Multi-AZ deployment**: Disabled (for lab purposes).
     - **VPC**: `LabVPC`.
     - **Subnet group**: `dbsubnetgroup`.
     - **Public access**: No.
     - **VPC security group**: `DBSecurityGroup`.
     - **Initial database name**: `world`.
     - **Encryption**: Disabled.
   - Click **Create database**.
2. **Result**:
   - An Aurora instance named `aurora` is created.

---

### **Task 2: Connect to an Amazon EC2 Instance**
1. **Steps**:
   - Navigate to the **AWS Management Console** → **EC2** → **Instances**.
   - Select the instance labeled **Command Host**.
   - Click **Connect** → **Session Manager** → **Connect**.
2. **Result**:
   - A terminal session is opened for the EC2 instance.

---

### **Task 3: Configure the EC2 Instance to Connect to Aurora**
1. **Install MariaDB Client**:
   - Run the following command:
     ```bash
     sudo yum install mariadb -y
     ```
   - **Expected Output**:
     ```plaintext
     Complete!
     ```
2. **Get Aurora Endpoint**:
   - Navigate to **RDS** → **Databases** → Select `aurora`.
   - Copy the **Endpoint** under **Connectivity & security**.
   - Example: `aurora.cluster-123456789012.us-west-2.rds.amazonaws.com`.
3. **Connect to Aurora**:
   - Run the following command (replace `<endpoint>` with the copied endpoint):
     ```bash
     mysql -u admin --password='admin123' -h <endpoint>
     ```
   - **Expected Output**:
     ```plaintext
     Welcome to the MariaDB monitor.
     MySQL [(none)]>
     ```

---

### **Task 4: Create a Table, Insert Data, and Query Records**
1. **List Databases**:
   - Run the following command:
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
2. **Switch to `world` Database**:
   - Run the following command:
     ```sql
     USE world;
     ```
   - **Expected Output**:
     ```plaintext
     Database changed
     ```
3. **Create a Table**:
   - Run the following SQL command:
     ```sql
     CREATE TABLE `country` (
       `Code` CHAR(3) NOT NULL DEFAULT '',
       `Name` CHAR(52) NOT NULL DEFAULT '',
       `Continent` ENUM('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') NOT NULL DEFAULT 'Asia',
       `Region` CHAR(26) NOT NULL DEFAULT '',
       `SurfaceArea` FLOAT(10,2) NOT NULL DEFAULT '0.00',
       `IndepYear` SMALLINT(6) DEFAULT NULL,
       `Population` INT(11) NOT NULL DEFAULT '0',
       `LifeExpectancy` FLOAT(3,1) DEFAULT NULL,
       `GNP` FLOAT(10,2) DEFAULT NULL,
       `GNPOld` FLOAT(10,2) DEFAULT NULL,
       `LocalName` CHAR(45) NOT NULL DEFAULT '',
       `GovernmentForm` CHAR(45) NOT NULL DEFAULT '',
       `Capital` INT(11) DEFAULT NULL,
       `Code2` CHAR(2) NOT NULL DEFAULT '',
       PRIMARY KEY (`Code`)
     );
     ```
   - **Expected Output**:
     ```plaintext
     Query OK, 0 rows affected, 7 warnings (0.02 sec)
     ```
4. **Insert Data**:
   - Run the following SQL commands:
     ```sql
     INSERT INTO `country` VALUES ('GAB','Gabon','Africa','Central Africa',267668.00,1960,1226000,50.1,5493.00,5279.00,'Le Gabon','Republic',902,'GA');
     INSERT INTO `country` VALUES ('IRL','Ireland','Europe','British Islands',70273.00,1921,3775100,76.8,75921.00,73132.00,'Ireland/Éire','Republic',1447,'IE');
     INSERT INTO `country` VALUES ('THA','Thailand','Asia','Southeast Asia',513115.00,1350,61399000,68.6,116416.00,153907.00,'Prathet Thai','Constitutional Monarchy',3320,'TH');
     INSERT INTO `country` VALUES ('CRI','Costa Rica','North America','Central America',51100.00,1821,4023000,75.8,10226.00,9757.00,'Costa Rica','Republic',584,'CR');
     INSERT INTO `country` VALUES ('AUS','Australia','Oceania','Australia and New Zealand',7741220.00,1901,18886000,79.8,351182.00,392911.00,'Australia','Constitutional Monarchy, Federation',135,'AU');
     ```
   - **Expected Output**:
     ```plaintext
     Query OK, 1 row affected (0.00 sec)
     ```
5. **Query Data**:
   - Run the following SQL command:
     ```sql
     SELECT * FROM country WHERE GNP > 35000 AND Population > 10000000;
     ```
   - **Expected Output**:
     ```plaintext
     +------+-----------+-----------+---------------------------+-------------+-----------+------------+----------------+-----------+-----------+--------------+------------------------------------+---------+-------+
     | Code | Name      | Continent | Region                    | SurfaceArea | IndepYear | Population | LifeExpectancy | GNP       | GNPOld    | LocalName    | GovernmentForm                      | Capital | Code2 |
     +------+-----------+-----------+---------------------------+-------------+-----------+------------+----------------+-----------+-----------+--------------+------------------------------------+---------+-------+
     | AUS  | Australia | Oceania   | Australia and New Zealand |  7741220.00 |      1901 |   18886000 |           79.8 | 351182.00 | 392911.00 | Australia    | Constitutional Monarchy,Federation |     135 | AU    |
     | THA  | Thailand  | Asia      | Southeast Asia            |   513115.00 |      1350 |   61399000 |           68.6 | 116416.00 | 153907.00 | Prathet Thai | Constitutional Monarchy             |    3320 | TH    |
     +------+-----------+-----------+---------------------------+-------------+-----------+------------+----------------+-----------+-----------+--------------+------------------------------------+---------+-------+
     2 rows in set (0.00 sec)
     ```

---

## **Conclusion**
- **Aurora Instance Created**: Successfully set up an Aurora database.
- **EC2 Connection**: Connected to an EC2 instance and configured it to interact with Aurora.
- **Data Operations**: Created a table, inserted data, and queried records in Aurora.

---

**Next Steps**:
- Explore **Multi-AZ deployments** for high availability.
- Experiment with **Aurora Global Tables** for cross-region replication.
- Test **Aurora Serverless** for automatic scaling.

--- 

Let me know if you need further assistance! 😊