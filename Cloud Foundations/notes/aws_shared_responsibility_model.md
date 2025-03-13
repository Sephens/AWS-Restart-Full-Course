# AWS Shared Responsibility Model - Cloud Foundations

## What You Will Learn

### Core Objectives:
- **Describe AWS Cloud security and the shared responsibility model.**
- **Identify the security responsibilities of AWS compared to the customer.**

---

## Introduction to the AWS Shared Responsibility Model

Security is a **shared responsibility** between AWS and the customer. AWS is responsible for the **security of the cloud**, while the customer is responsible for **security in the cloud**. This model ensures that both parties work together to maintain a secure cloud environment.

### Key Concepts:
- **AWS Responsibility**: Protects the infrastructure that runs AWS services (e.g., hardware, software, networking, and facilities).
- **Customer Responsibility**: Manages the security of the data, applications, and configurations they deploy on AWS.

---

## AWS Security Responsibilities: Security **OF** the Cloud

AWS is responsible for the **security of the cloud**, which includes:

### 1. **Physical Security of Data Centers**
   - **Controlled Access**: Data centers are secured with 24/7 guards, two-factor authentication, and video surveillance.
   - **Disk Degaussing and Destruction**: Ensures data is securely erased from storage devices.

### 2. **Hardware and Software Infrastructure**
   - **Host OS Access Logging and Auditing**: AWS monitors and logs access to the host operating systems.
   - **Storage Decommissioning**: Ensures data is securely wiped from storage devices.

### 3. **Network Infrastructure**
   - **Intrusion Detection**: AWS continuously monitors the network for unauthorized access.
   - **Redundant Infrastructure**: Ensures high availability and fault tolerance.

### 4. **Virtualization Infrastructure**
   - **Instance Isolation**: Ensures that virtual machines (VMs) are isolated from each other to prevent unauthorized access.

### Example:
- **AWS Global Infrastructure**: AWS manages the physical security of data centers, hardware, and networking across **Regions**, **Availability Zones**, and **Edge Locations**.

---

## Customer Security Responsibilities: Security **IN** the Cloud

The customer is responsible for **security in the cloud**, which includes:

### 1. **Operating System (OS) Management**
   - **Patching and Maintenance**: Customers must apply security patches and updates to the guest OS running on EC2 instances.
   - **Example**: If you run a Linux-based EC2 instance, you are responsible for applying OS updates and security patches.

### 2. **Application Security**
   - **Passwords and Access Control**: Customers must manage passwords, role-based access, and other application-level security measures.
   - **Example**: If you deploy a web application on EC2, you must ensure that the application is secure (e.g., using HTTPS, secure authentication).

### 3. **Security Group Configuration**
   - **Firewall Rules**: Customers must configure security groups to control inbound and outbound traffic to EC2 instances.
   - **Example**: If you want to allow SSH access to an EC2 instance, you must configure the security group to allow traffic on port 22.

### 4. **Data Encryption**
   - **Client-Side and Server-Side Encryption**: Customers are responsible for encrypting data at rest and in transit.
   - **Example**: If you store sensitive data in Amazon S3, you should enable server-side encryption (SSE) to protect the data.

### 5. **Network Configuration**
   - **VPC Configuration**: Customers must configure Virtual Private Clouds (VPCs) to control network traffic.
   - **Example**: If you want to isolate your EC2 instances from the public internet, you can configure a private subnet within a VPC.

### 6. **Account Management**
   - **IAM Roles and Permissions**: Customers must manage IAM roles and permissions to control access to AWS resources.
   - **Example**: If you want to grant an application access to an S3 bucket, you must create an IAM role with the appropriate permissions.

---

## Service Characteristics and Security Responsibility

### 1. **Infrastructure as a Service (IaaS)**
   - **Customer Responsibility**: The customer has more control over the configuration of networking, storage, and security settings.
   - **Examples**: Amazon EC2, Amazon EBS, Amazon VPC.
   - **Security Tasks**:
     - Manage guest OS updates and patches.
     - Configure security groups and firewalls.
     - Manage application-level security.

### 2. **Platform as a Service (PaaS)**
   - **AWS Responsibility**: AWS manages the underlying infrastructure, including OS updates, database patching, and disaster recovery.
   - **Examples**: AWS Lambda, Amazon RDS, AWS Elastic Beanstalk.
   - **Security Tasks**:
     - Customers focus on managing code and data.
     - AWS handles OS and database patching, firewall configuration, and DR.

### 3. **Software as a Service (SaaS)**
   - **AWS Responsibility**: AWS manages the entire infrastructure, including software updates and security.
   - **Examples**: AWS Trusted Advisor, AWS Shield, Amazon Chime.
   - **Security Tasks**:
     - Customers do not need to manage the infrastructure.
     - AWS handles all security aspects, including DDoS protection and software updates.

---

## Activity: AWS Shared Responsibility Model

### Scenario:
- **AWS Cloud**: VPC, Amazon S3, Amazon EC2, Oracle instance.
- **Oracle**: Oracle instance running on EC2 or Amazon RDS.

### Questions:
1. **Upgrades and patches to the OS on the EC2 instance**:
   - **Answer**: Customer.
   - **Explanation**: The customer is responsible for managing the guest OS, including applying patches and updates.

2. **Physical security of the data center**:
   - **Answer**: AWS.
   - **Explanation**: AWS is responsible for the physical security of data centers.

3. **Virtualization infrastructure**:
   - **Answer**: AWS.
   - **Explanation**: AWS manages the virtualization layer, ensuring instance isolation and security.

4. **Amazon EC2 security group settings**:
   - **Answer**: Customer.
   - **Explanation**: The customer must configure security groups to control traffic to and from EC2 instances.

5. **Configuration of applications running on the EC2 instance**:
   - **Answer**: Customer.
   - **Explanation**: The customer is responsible for securing and configuring applications deployed on EC2.

6. **Oracle upgrades or patches if the Oracle instance runs as an Amazon RDS instance**:
   - **Answer**: AWS.
   - **Explanation**: Amazon RDS is a managed service, so AWS handles database patching and updates.

7. **Oracle upgrades or patches if Oracle runs on an EC2 instance**:
   - **Answer**: Customer.
   - **Explanation**: If Oracle runs on an EC2 instance, the customer is responsible for applying patches and updates.

8. **Configuration of S3 bucket access**:
   - **Answer**: Customer.
   - **Explanation**: The customer must configure access policies and permissions for S3 buckets.

---

## Key Takeaways

- **Shared Responsibility**: AWS and the customer share security responsibilities.
  - **AWS**: Security **OF** the cloud (infrastructure, hardware, software, networking).
  - **Customer**: Security **IN** the cloud (data, applications, configurations).

- **IaaS**: Customers have more control and responsibility for security (e.g., EC2, EBS, VPC).
- **PaaS**: AWS manages the underlying infrastructure, while customers focus on code and data (e.g., Lambda, RDS).
- **SaaS**: AWS manages the entire infrastructure and security (e.g., Trusted Advisor, Shield).

---

## Additional Notes and Examples

### Example: Securing an EC2 Instance
1. **OS Updates**: Apply the latest security patches to the guest OS.
2. **Security Groups**: Configure security groups to allow only necessary traffic (e.g., SSH on port 22).
3. **IAM Roles**: Assign IAM roles to the EC2 instance to grant it access to other AWS resources (e.g., S3).
4. **Data Encryption**: Enable encryption for data at rest (e.g., EBS volumes) and in transit (e.g., HTTPS).

### Example: Securing an S3 Bucket
1. **Bucket Policies**: Configure bucket policies to restrict access to authorized users.
2. **Encryption**: Enable server-side encryption (SSE) to protect data at rest.
3. **Versioning**: Enable versioning to protect against accidental deletions or overwrites.
4. **Access Logs**: Enable access logging to monitor who accesses the bucket.

### Example: Using AWS Trusted Advisor
- **AWS Trusted Advisor** provides recommendations to optimize your AWS environment.
- **Example**: If Trusted Advisor identifies an S3 bucket with public access, you can modify the bucket policy to restrict access.

---

## Conclusion

The AWS Shared Responsibility Model ensures that both AWS and the customer work together to maintain a secure cloud environment. By understanding the division of responsibilities, customers can effectively secure their data, applications, and configurations while leveraging AWS's robust infrastructure security.