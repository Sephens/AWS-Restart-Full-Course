# Lab Guide: Build Your DB Server and Interact With Your DB Using an App  

## **Lab Overview**  
This lab focuses on leveraging **Amazon RDS (Relational Database Service)** to set up a highly available database instance and interact with it using a web application.  

### **Objectives**  
After completing this lab, you will be able to:  
1. **Launch an Amazon RDS DB instance with high availability (Multi-AZ).**  
2. **Configure the DB instance to allow connections from a web server.**  
3. **Interact with the database using a web application.**  

---

## **Task 1: Create a Security Group for the RDS DB Instance**  

### **Objective**  
Create a security group that allows the **web server** to connect to the **RDS database** securely.  

### **Step-by-Step Instructions**  

1. **Navigate to the VPC Console:**  
   - Open the **AWS Management Console**.  
   - Click **Services** > **VPC** (under *Networking & Content Delivery*).  

2. **Create a New Security Group:**  
   - In the left navigation pane, click **Security Groups**.  
   - Click **Create security group** and configure:  
     - **Security group name:** `DB Security Group`  
     - **Description:** `Permit access from Web Security Group`  
     - **VPC:** `Lab VPC`  

3. **Add an Inbound Rule:**  
   - In the **Inbound rules** section, click **Add rule** and configure:  
     - **Type:** `MySQL/Aurora (3306)`  
     - **Source:** Type `sg` and select **Web Security Group** (this allows MySQL traffic from the web server).  

4. **Finalize the Security Group:**  
   - Scroll down and click **Create security group**.  

### **Why This Step Matters**  
- Security groups act as virtual firewalls.  
- By allowing **MySQL/Aurora (port 3306)** from the **Web Security Group**, we ensure only the web server can connect to the database.  

---

## **Task 2: Create a DB Subnet Group**  

### **Objective**  
Define which **subnets** RDS can use (required for **Multi-AZ deployments**).  

### **Step-by-Step Instructions**  

1. **Navigate to the RDS Console:**  
   - Click **Services** > **RDS** (under *Database*).  

2. **Create a DB Subnet Group:**  
   - In the left navigation pane, click **Subnet groups**.  
   - Click **Create DB Subnet Group** and configure:  
     - **Name:** `DB Subnet Group`  
     - **Description:** `DB Subnet Group`  
     - **VPC ID:** `Lab VPC`  

3. **Select Subnets:**  
   - Under **Add subnets**, select:  
     - **Availability Zone 1:** `10.0.1.0/24`  
     - **Availability Zone 2:** `10.0.3.0/24`  

4. **Finalize the Subnet Group:**  
   - Click **Create**.  

### **Why This Step Matters**  
- A **DB Subnet Group** tells RDS which subnets to use.  
- **Multi-AZ deployments** require subnets in **at least two Availability Zones** for high availability.  

---

## **Task 3: Create an Amazon RDS DB Instance**  

### **Objective**  
Launch a **Multi-AZ MySQL RDS database**.  

### **Step-by-Step Instructions**  

1. **Navigate to the RDS Database Creation Page:**  
   - In the left navigation pane, click **Databases**.  
   - Click **Create database**.  

2. **Choose Database Configuration:**  
   - **Engine type:** `MySQL`  
   - **Engine version:** (Choose the latest)  
   - **Templates:** `Dev/Test`  
   - **Availability & durability:** `Multi-AZ DB Instance`  

3. **Set Database Credentials:**  
   - **DB instance identifier:** `lab-db`  
   - **Master username:** `main`  
   - **Master password:** `lab-password`  

4. **Configure Instance & Storage:**  
   - **DB instance class:** `db.t3.medium` (Burstable)  
   - **Storage type:** `General Purpose (SSD)`  

5. **Set Networking & Security:**  
   - **VPC:** `Lab VPC`  
   - **Security group:** Remove default, select **DB Security Group**.  

6. **Additional Configuration:**  
   - **Initial database name:** `lab`  
   - **Disable automated backups** (for lab speed).  

7. **Finalize & Launch:**  
   - Click **Create database**.  

8. **Wait for Database to Initialize (~4 minutes):**  
   - Once the status changes to **Available**, note the **Endpoint** (e.g., `lab-db.cggq8lhnxvnv.us-west-2.rds.amazonaws.com`).  

### **Why This Step Matters**  
- **Multi-AZ deployment** ensures **high availability** (if one AZ fails, RDS fails over to the standby).  
- The **Endpoint** is the connection string for applications to access the database.  

---

## **Task 4: Interact with Your Database**  

### **Objective**  
Configure the web app to connect to the RDS database and test CRUD operations.  

### **Step-by-Step Instructions**  

1. **Access the Web Application:**  
   - Copy the **WebServer IP** from **AWS Details**.  
   - Open a new browser tab and paste the IP.  

2. **Configure Database Connection:**  
   - Click the **RDS** link in the web app.  
   - Enter:  
     - **Endpoint:** (Paste the RDS endpoint)  
     - **Database:** `lab`  
     - **Username:** `main`  
     - **Password:** `lab-password`  
   - Click **Submit**.  

3. **Test the Application:**  
   - Add, edit, and delete contacts.  
   - Verify data persists (stored in RDS).  

### **Why This Step Matters**  
- Confirms the **web server can connect to RDS**.  
- Validates **Multi-AZ replication** (data is synced across AZs).  

---

## **Final Notes**  
✅ **Security Best Practice:** In production, always enable **automated backups** and **Enhanced Monitoring**.  
✅ **Multi-AZ Benefit:** Provides **failover support** in case of AZ outages.  
✅ **Connection Security:** Only the **Web Security Group** can access the database.  

### **Troubleshooting Tips**  
❌ **Can’t connect?** Check:  
- Security group rules (must allow **MySQL/Aurora on 3306**).  
- Database endpoint is correct.  
- Database is in **Available** state.  

---

## **Conclusion**  
You have successfully:  
✔ Launched a **Multi-AZ RDS MySQL** database.  
✔ Configured **security groups & subnet groups**.  
✔ Connected a **web app** and tested database operations.  

This setup is ideal for **production workloads** requiring **high availability**. 🚀