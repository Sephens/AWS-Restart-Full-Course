# **Challenge Lab: Build Your DB Server and Interact With Your DB**  
### **A Step-by-Step Guide to Launching RDS and Querying Data**  

---

## **Lab Overview**  
This challenge lab requires you to:  
✅ **Launch an Amazon RDS instance** (Aurora or MySQL)  
✅ **Connect to a Linux server and install MySQL client**  
✅ **Create tables, insert data, and run queries**  
✅ **Capture required screenshots for submission**  

---

## **Task 1: Launch an Amazon RDS Instance**  

### **Step-by-Step Instructions**  

1. **Go to RDS Console:**  
   - Open **AWS Management Console** > **RDS**.  

2. **Create Database:**  
   - Click **Create database** > **Standard create**.  
   - **Engine options:**  
     - Choose **Amazon Aurora (MySQL-Compatible)** or **MySQL**.  
     - Select the latest **Engine version**.  
   - **Templates:**  
     - Choose **Dev/Test** (or **Free tier** if available).  
   - **Settings:**  
     - **DB instance identifier:** `challenge-db`  
     - **Master username:** `admin`  
     - **Master password:** `your-password` *(Note this down!)*  
   - **DB instance class:**  
     - **Burstable classes (db.t3)** > Choose **db.t3.medium**.  
   - **Storage:**  
     - **General Purpose SSD (gp2)** (Max **100 GB**).  
   - **Connectivity:**  
     - **VPC:** `Lab VPC`  
     - **Security group:**  
       - Remove **default**, add a **new SG** allowing MySQL (port **3306**) from **LinuxServer**.  
   - **Additional configuration:**  
     - **Initial DB name:** `studentdb`  
     - **Disable Enhanced Monitoring** (for MySQL).  
   - Click **Create database**.  

3. **Wait for DB to Initialize (~5-10 mins)**  
   - Note the **Endpoint** (e.g., `challenge-db.abc123.us-west-2.rds.amazonaws.com`).  

---

## **Task 2: Connect to Linux Server & Install MySQL Client**  

### **Step-by-Step Instructions**  

1. **Download SSH Key:**  
   - Under **AWS Details**, click **Download PEM** (Linux/macOS) or **PPK** (Windows).  

2. **Connect via SSH:**  
   - Use **Terminal (Linux/macOS)** or **PuTTY (Windows)**.  
   - Example (Linux/macOS):  
     ```bash
     chmod 400 your-key.pem  
     ssh -i your-key.pem ec2-user@<LinuxServer-IP>
     ```

3. **Install MySQL Client:**  
   ```bash
   sudo yum install mysql -y
   ```

4. **Connect to RDS:**  
   ```bash
   mysql -h <RDS-Endpoint> -u admin -p
   ```
   - Enter password when prompted.  

---

## **Task 3: Create Tables & Insert Data**  

### **Step 1: Create `RESTART` Table**  
```sql
CREATE TABLE RESTART (
  StudentID INT PRIMARY KEY,
  StudentName VARCHAR(50),
  RestartCity VARCHAR(50),
  GraduationDate DATETIME
);
```

### **Step 2: Insert 10 Rows**  
```sql
INSERT INTO RESTART VALUES 
(1, 'John Doe', 'New York', '2023-12-15'),
(2, 'Jane Smith', 'London', '2023-11-20'),
(3, 'Alex Brown', 'Berlin', '2024-01-10'),
(4, 'Emily Davis', 'Tokyo', '2023-10-05'),
(5, 'Michael Lee', 'Sydney', '2024-02-28'),
(6, 'Sarah Wilson', 'Paris', '2023-09-12'),
(7, 'David Clark', 'Toronto', '2024-03-15'),
(8, 'Lisa Johnson', 'Dubai', '2023-08-30'),
(9, 'Robert White', 'Mumbai', '2024-04-20'),
(10, 'Anna Garcia', 'Singapore', '2023-07-25');
```

### **Step 3: Create `CLOUD_PRACTITIONER` Table**  
```sql
CREATE TABLE CLOUD_PRACTITIONER (
  StudentID INT,
  CertificationDate DATETIME,
  FOREIGN KEY (StudentID) REFERENCES RESTART(StudentID)
);
```

### **Step 4: Insert 5 Rows**  
```sql
INSERT INTO CLOUD_PRACTITIONER VALUES 
(1, '2023-12-20'),
(2, '2023-11-25'),
(4, '2023-10-10'),
(7, '2024-03-20'),
(9, '2024-04-25');
```

---

## **Task 4: Run Queries & Capture Screenshots**  

### **Screenshot 1: `RESTART` Table Structure**  
```sql
DESCRIBE RESTART;
```

### **Screenshot 2: All Rows in `RESTART`**  
```sql
SELECT * FROM RESTART;
```

### **Screenshot 3: `CLOUD_PRACTITIONER` Table Structure**  
```sql
DESCRIBE CLOUD_PRACTITIONER;
```

### **Screenshot 4: All Rows in `CLOUD_PRACTITIONER`**  
```sql
SELECT * FROM CLOUD_PRACTITIONER;
```

### **Screenshot 5: Inner Join Query**  
```sql
SELECT R.StudentID, R.StudentName, C.CertificationDate  
FROM RESTART R  
INNER JOIN CLOUD_PRACTITIONER C ON R.StudentID = C.StudentID;
```

---

## **Task 5: Clean Up (Optional)**  
To avoid unnecessary charges:  
1. **Delete RDS Instance:**  
   - Go to **RDS** > **Databases** > Select `challenge-db` > **Actions** > **Delete**.  
2. **Terminate Linux Server (if needed).**  

---

## **Conclusion**  
✅ **Launched RDS instance** (Aurora/MySQL)  
✅ **Connected via MySQL client**  
✅ **Created tables & inserted sample data**  
✅ **Ran queries & captured screenshots**  

### **Key Takeaways**  
🔹 **RDS simplifies DB management** (no server maintenance).  
🔹 **Security groups control access** (only allow trusted sources).  
🔹 **SQL skills are essential** for querying relational data.  

🚀 **You’ve completed the challenge! Submit your screenshots for verification.**