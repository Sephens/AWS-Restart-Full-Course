# Amazon Relational Database Service (Amazon RDS) - Comprehensive Notes and Examples

This document provides a detailed summary of the "Amazon RDS and Aurora" module, including key concepts, features, use cases, and examples.

---

## **Key Takeaways**
1. **Amazon RDS**: A fully managed relational database service for setting up, operating, and scaling databases in the cloud.
2. **Supported Engines**: MySQL, Aurora, Microsoft SQL Server, PostgreSQL, MariaDB, Oracle.
3. **High Availability**: Achieved through Multi-AZ deployments and automatic failover.
4. **Scalability**: Vertical scaling (instance class) and horizontal scaling (read replicas).
5. **Aurora**: A high-performance, cost-effective database engine compatible with MySQL/PostgreSQL, optimized for cloud workloads.

---

## **Amazon RDS Overview**

### **What is Amazon RDS?**
- A **managed database service** that automates setup, maintenance, backups, and scaling.
- Eliminates administrative tasks like hardware provisioning, patching, and backups.
- Use cases:
  - Web/mobile applications (high throughput, scalability).
  - E-commerce (low cost, security, fully managed).
  - Gaming (automatic scaling, high availability).

Amazon Relational Database Service (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while managing time-consuming database administration tasks, which allows you to focus on your applications and business. Amazon RDS provides you with six familiar database engines to choose from: Amazon Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL and MariaDB.

### **Key Features**
| Feature | Description |
|---------|-------------|
| **DB Instance** | Isolated database environment in the cloud. Configured via instance class (CPU, memory) and storage type (SSD/magnetic). |
| **Backup** | **Automatic** (daily snapshots + transaction logs) and **Manual** (on-demand snapshots). |
| **Multi-AZ** | Synchronous replication to a standby instance in another Availability Zone (AZ) for failover. |
| **Read Replicas** | Asynchronous replication for read-heavy workloads. Supports cross-region replication. |

---

## **Amazon RDS Components**

### **DB Instance**
- **Definition**: A database environment with compute, memory, and storage resources.
- **Configuration**:
  - **Instance Class**: Determines CPU, memory, and network performance (e.g., `db.t3.micro`).
  - **Storage**: General Purpose SSD (cost-effective), Provisioned IOPS (high performance).

### **Backup Options**
1. **Automatic Backups**:
   - Enabled by default.
   - Retained for 1–35 days.
   - Restores to any point within the retention period.
2. **Manual Snapshots**:
   - User-initiated, retained indefinitely.
   - Used for long-term backups or cloning databases.

### **High Availability with Multi-AZ**
- **How It Works**:
  - Primary DB instance in one AZ.
  - Standby replica in another AZ with **synchronous replication**.
  - Automatic failover during primary instance failure (no data loss).
- **Use Case**: Critical applications requiring minimal downtime.

### **Scalability**
1. **Vertical Scaling**:
   - Change instance class (e.g., `db.t3.small` → `db.r5.large`).
   - Requires downtime.
2. **Horizontal Scaling**:
   - **Read Replicas**: Offload read traffic (supports up to 5 replicas per instance).
   - **Aurora Replicas**: Up to 15 read replicas with automatic failover.

---

## **Amazon Aurora**

### **What is Aurora?**
- A MySQL/PostgreSQL-compatible database engine optimized for the cloud.
- **Key Benefits**:
  - **Performance**: 5x faster than standard MySQL and 3x faster than PostgreSQL.
  - **Scalability**: Storage auto-scales up to 128 TB.
  - **High Availability**: Multi-AZ by default with automatic failover.
  - **Cost-Effective**: Up to 90% lower costs than commercial databases.

### **Aurora Cluster Architecture**
| Component | Description |
|-----------|-------------|
| **Primary DB Instance** | Handles read/write operations. |
| **Aurora Replicas** | Read-only instances for scaling reads. |
| **Cluster Volume** | Distributed storage spanning multiple AZs (6 copies of data). |

![Aurora Cluster](https://docs.aws.amazon.com/images/rds/latest/userguide/images/aurora-architecture.png)

### **Aurora Use Cases**
1. **Enterprise Applications**: High availability and cost savings.
2. **SaaS Applications**: Focus on app development, not database management.
3. **Gaming**: High throughput and auto-scaling for unpredictable workloads.

---

## **Examples**

### **Creating a DB Instance (Easy Create Method)**
1. **Steps**:
   - Navigate to AWS Management Console → RDS → **Create database**.
   - Choose **Easy Create** → Select engine (e.g., MySQL).
   - Specify instance size (e.g., `db.t3.micro`) and DB identifier.
   - Click **Create**.
2. **Post-Creation**:
   - Connect using MySQL Workbench or `mysql` CLI:
     ```bash
     mysql -h <endpoint> -P 3306 -u <masteruser> -p
     ```

### **Configuring Multi-AZ Deployment**
1. **Steps**:
   - During DB creation, enable **Multi-AZ deployment**.
   - For existing instances: Modify → **Multi-AZ** → **Yes** → Apply.

### **Creating an Aurora Cluster**
1. **Steps**:
   - In RDS console, select **Amazon Aurora** → Choose compatibility (MySQL/PostgreSQL).
   - Configure instance class, cluster storage, and replicas.
   - Example cluster:
     - Primary instance: `db.r5.large`.
     - 2 Aurora Replicas in different AZs.

---

## **Checkpoint Questions**
1. **What is one database engine supported by Amazon RDS?**  
   - MySQL, Aurora, PostgreSQL, MariaDB, Oracle, or Microsoft SQL Server.

2. **What is Aurora?**  
   - A high-performance, fully managed database engine compatible with MySQL/PostgreSQL, optimized for cloud scalability and availability.

---

## **Key Takeaways**
- **Amazon RDS** simplifies database management with automated backups, scaling, and Multi-AZ redundancy.
- **Aurora** offers superior performance, auto-scaling storage, and cost efficiency for enterprise workloads.
- Use **Read Replicas** for read scaling and **Multi-AZ** for fault tolerance.

---

**Next Steps**: Explore hands-on labs for creating RDS instances, configuring backups, and testing failover scenarios in the AWS Management Console.


# LAB
Amazon Relational Database Service (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while managing time-consuming database administration tasks, which allows you to focus on your applications and business. Amazon RDS provides you with six familiar database engines to choose from: Amazon Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL and MariaDB.

After completing this lab, you can:
- Launch an Amazon RDS DB instance with high availability.
- Configure the DB instance to permit connections from your web server.
- Open a web application and interact with your database.

## Task 1: Create a Security Group for the RDS DB Instance
In this task, you will create a security group to allow your web server to access your RDS DB instance. The security group will be used when you launch the database instance.

1. In the AWS Management Console, select the  Services menu, and then select VPC under Networking & Content Delivery.

2. In the left navigation pane, click Security Groups.

3. Click Create security group and then configure:

- Security group name: DB Security Group

- Description: Permit access from Web Security Group

- VPC: Lab VPC

>You will now add a rule to the security group to permit inbound database requests. The security group currently has no rules. You will add a rule to permit access from the Web Security Group.

4. In the Inbound rules section, click Add rule, then configure:

- Type: MySQL/Aurora (3306)

- Source: Type sg in the search field and then select Web Security Group.

>This configures the Database security group to permit inbound traffic on port 3306 from any EC2 instance that is associated with the Web Security Group.

5. Scroll to the bottom of the screen, then click Create security group

You will use this security group when launching the Amazon RDS database.

## Task 2: Create a DB Subnet Group
In this task, you will create a DB subnet group that is used to tell RDS which subnets can be used for the database. Each DB subnet group requires subnets in at least two Availability Zones.

1. In the AWS Management Console, select the  Services menu, and then select RDS under Database.

2. In the left navigation pane, click Subnet groups.

 If the navigation pane is not visible, click the  menu icon in the top-left corner.

3. Click Create DB Subnet Group then configure:

- Name: DB Subnet Group

- Description: DB Subnet Group

- VPC ID: Lab VPC

4. In the Add subnets section for Availability zones, click the , then:

- Select  the first Availability zone

- Select  the second Availability zone

5. For Subnets, click the , then:

- For the first Availability zone, select  10.0.1.0/24

- For the second Availability zone, select  10.0.3.0/24

Click Create

This adds Private Subnet 1 (10.0.1.0/24) and Private Subnet 2 (10.0.3.0/24). You will use this DB subnet group when creating the database in the next task.

## Task 3: Create an Amazon RDS DB Instance
In this task, you will configure and launch a Multi-AZ Amazon RDS for MySQL database instance.

Amazon RDS Multi-AZ deployments provide enhanced availability and durability for Database (DB) instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB instance, Amazon RDS automatically creates a primary DB instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ).

1. In the left navigation pane, click Databases.

2. Click Create database

 If you see Switch to the new database creation flow at the top of the screen, please click it.

3. Choose Create database, then choose Standard create.

4. Under the Engine options section, for Engine type, choose MySQL.

5. For Engine version, choose the latest version.

6. For Templates, choose Dev/Test.

7. For Availability and durability, choose Multi-AZ DB Instance.

8. Under Settings, configure the following:

- DB instance identifier: lab-db

- Master username: main

- Master password: lab-password

- Confirm password: lab-password

9. Under Instance configuration, configure the following for DB instance class:

- Select  Burstable classes (includes t classes).

- Select db.t3.medium. 

10. Under Storage, configure:

- Select General Purpose (SSD) under Storage type.

11. Under Connectivity, configure:

- Virtual Private Cloud (VPC): Lab VPC

12. Under VPC security group select Choose existing

13. Under Existing VPC security groups

- Use X to Remove default.

- Select DB Security Group to highlight it in blue.

14. Under Monitoring, expand Additional configuration and then configure the following:

- For Enhanced Monitoring, uncheck  Enable Enhanced monitoring.

15. Scroll down to the  Additional configuration section and expand this option. Then configure:

- Initial database name: lab

- Under Backup, uncheck  Enable automated backups.

 This will turn off backups, which is not normally recommended, but will make the database deploy faster for this lab.

16. Scroll to the bottom of the screen, then click Create database

Your database will now be launched.

17. Click lab-db (click the link itself).

You will now need to wait approximately 4 minutes for the database to be available. The deployment process is deploying a database in two different Availability zones.

 Note: If you are prompted with the Suggested add-ons for lab-db window, choose Close

 While you are waiting, you might want to review the Amazon RDS FAQs or grab a cup of coffee.

18. Wait until the Status changes to Modifying or Available.

19. Scroll down to the Connectivity & Security section and copy the Endpoint field.

It will look similar to: lab-db.cggq8lhnxvnv.us-west-2.rds.amazonaws.com

20. Paste the Endpoint value into a text editor. You will use it later in the lab.


## Task 4: Interact with Your Database

In this task, you will open a web application running on your web server and configure it to use the database.

1. Copy the WebServer IP address by selecting i AWS Details above these instructions you are currently reading.

2. Open a new web browser tab, paste the WebServer IP address and press Enter.

The web application will be displayed, showing information about the EC2 instance.

3. At the top of the web application page, click the RDS link.
You will now configure the application to connect to your database.

4. Configure the following settings:

- Endpoint: Paste the Endpoint you copied to a text editor earlier

- Database: lab

- Username: main

- Password: lab-password

- Click Submit

A message will appear explaining that the application is running a command to copy information to the database. After a few seconds the application will display an Address Book.

The Address Book application is using the RDS database to store information.

5. Test the web application by adding, editing and removing contacts.

The data is being persisted to the database and is automatically replicating to the second Availability Zone.

