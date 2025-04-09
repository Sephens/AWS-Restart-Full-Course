# **Lab Guide: Introduction to Amazon Aurora**  

## **Lab Overview**  
This lab introduces **Amazon Aurora**, a high-performance MySQL-compatible database engine. You will:  
✔ **Create an Aurora DB cluster**  
✔ **Connect to an EC2 instance**  
✔ **Configure the EC2 instance to interact with Aurora**  
✔ **Run SQL queries on Aurora**  

### **Technologies Covered**  
🔹 **Amazon Aurora** – A MySQL-compatible, high-performance managed database.  
🔹 **Amazon EC2** – Virtual servers in the cloud.  
🔹 **Amazon RDS** – Managed relational database service.  

---

## **Task 1: Create an Aurora Instance**  

### **Objective**  
Launch an **Aurora MySQL DB cluster** in **Dev/Test** mode.  

### **Step-by-Step Instructions**  

1. **Navigate to RDS Console:**  
   - Open the **AWS Management Console** and search for **RDS**.  
   - Click **Databases** in the left menu.  

2. **Start Database Creation:**  
   - Click **Create database**.  
   - Choose **Standard create**.  
   - Select **Aurora (MySQL Compatible)** for **Engine type**.  
   - Keep the default **Engine version (8.0+)**.  
   - Under **Templates**, select **Dev/Test**.  

3. **Configure DB Settings:**  
   - **DB cluster identifier:** `aurora`  
   - **Master username:** `admin`  
   - **Master password:** `admin123`  
   - **Confirm password:** `admin123`  

4. **Choose Instance & Deployment:**  
   - **DB instance class:** `db.t3.medium` (Burstable)  
   - **Multi-AZ deployment:** `Don't create an Aurora Replica` *(For production, enable Multi-AZ!)*  

5. **Set Networking & Security:**  
   - **VPC:** `LabVPC`  
   - **Subnet group:** `dbsubnetgroup` *(Pre-created by CloudFormation)*  
   - **Public access:** `No` *(Private DB for security)*  
   - **VPC security group:** Remove **default**, select **DBSecurityGroup**.  

6. **Additional Configuration:**  
   - **Initial database name:** `world`  
   - **Disable encryption** *(Not recommended for production!)*  
   - **Disable auto minor version upgrade** *(For lab simplicity)*  

7. **Launch the Database:**  
   - Click **Create database**.  
   - Wait ~5 minutes for the DB to initialize.  

### **Key Notes**  
📌 **Aurora Endpoint:** After creation, note the **Writer Endpoint** (e.g., `aurora.cluster-abc123.us-west-2.rds.amazonaws.com`).  
📌 **No Multi-AZ in Lab:** For production, always enable **Multi-AZ** for high availability.  

---

## **Task 2: Connect to an Amazon EC2 Instance**  

### **Objective**  
Access the **pre-configured EC2 instance** (Command Host) to interact with Aurora.  

### **Step-by-Step Instructions**  

1. **Navigate to EC2 Console:**  
   - Search for **EC2** in the AWS Console.  
   - Click **Instances** in the left menu.  

2. **Locate the Command Host:**  
   - Find the instance named **Command Host**.  
   - Select it and click **Connect**.  

3. **Connect via Session Manager:**  
   - Choose **Session Manager**.  
   - Click **Connect** to open a terminal.  

### **Troubleshooting**  
🔹 If **Connect** is unavailable, wait a few minutes and retry.  
🔹 Ensure the **Command Host** instance is running.  

---

## **Task 3: Configure EC2 to Connect to Aurora**  

### **Objective**  
Install the **MySQL client** and connect to Aurora from EC2.  

### **Step-by-Step Instructions**  

1. **Install MariaDB Client:**  
   ```bash
   sudo yum install mariadb -y
   ```
   *(MariaDB is MySQL-compatible and used to interact with Aurora.)*  

2. **Get Aurora Endpoint:**  
   - Go back to **RDS > Databases**.  
   - Select the `aurora` cluster.  
   - Under **Connectivity & security**, copy the **Writer Endpoint**.  

3. **Connect to Aurora:**  
   ```bash
   mysql -u admin --password='admin123' -h <aurora-endpoint>
   ```
   *(Replace `<aurora-endpoint>` with the copied Writer Endpoint.)*  

4. **Verify Connection:**  
   - You should see:  
     ```sql
     Welcome to the MariaDB monitor...
     MySQL [(none)]>
     ```

### **Key Notes**  
📌 **Writer Endpoint vs. Reader Endpoint:**  
- **Writer Endpoint:** For **read/write** operations (connects to the primary DB).  
- **Reader Endpoint:** For **read-only** queries (load-balanced across replicas).  

---

## **Task 4: Create a Table and Query Data**  

### **Objective**  
Create a `country` table, insert data, and run queries.  

### **Step-by-Step Instructions**  

1. **List Databases:**  
   ```sql
   SHOW DATABASES;
   ```
   - Should display `world` (created earlier).  

2. **Switch to `world` Database:**  
   ```sql
   USE world;
   ```

3. **Create the `country` Table:**  
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

4. **Insert Sample Data:**  
   ```sql
   INSERT INTO `country` VALUES ('GAB','Gabon','Africa','Central Africa',267668.00,1960,1226000,50.1,5493.00,5279.00,'Le Gabon','Republic',902,'GA');
   INSERT INTO `country` VALUES ('IRL','Ireland','Europe','British Islands',70273.00,1921,3775100,76.8,75921.00,73132.00,'Ireland/Éire','Republic',1447,'IE');
   INSERT INTO `country` VALUES ('THA','Thailand','Asia','Southeast Asia',513115.00,1350,61399000,68.6,116416.00,153907.00,'Prathet Thai','Constitutional Monarchy',3320,'TH');
   INSERT INTO `country` VALUES ('CRI','Costa Rica','North America','Central America',51100.00,1821,4023000,75.8,10226.00,9757.00,'Costa Rica','Republic',584,'CR');
   INSERT INTO `country` VALUES ('AUS','Australia','Oceania','Australia and New Zealand',7741220.00,1901,18886000,79.8,351182.00,392911.00,'Australia','Constitutional Monarchy, Federation',135,'AU');
   ```

5. **Run a Query:**  
   ```sql
   SELECT * FROM country WHERE GNP > 35000 AND Population > 10000000;
   ```
   - Should return **Australia** and **Thailand**.  

### **Key Notes**  
📌 **Aurora Performance:**  
- **5x faster than MySQL** without code changes.  
- **Auto-scaling storage** (up to 128TB).  

---

## **Conclusion**  
✅ **Created an Aurora MySQL DB cluster**  
✅ **Connected to an EC2 instance via Session Manager**  
✅ **Configured MySQL client for Aurora access**  
✅ **Ran SQL queries on Aurora**  

### **Next Steps for Production**  
🔹 **Enable Multi-AZ** for high availability.  
🔹 **Enable encryption** for data security.  
🔹 **Set up automated backups**.  

🚀 **You’re now ready to use Aurora in real-world applications!**