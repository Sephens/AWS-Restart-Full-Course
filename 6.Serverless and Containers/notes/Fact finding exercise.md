# AWS re/Start Fact-Finding Exercises - Comprehensive Guide

## Table of Contents
- [AWS re/Start Fact-Finding Exercises - Comprehensive Guide](#aws-restart-fact-finding-exercises---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Python](#python)
    - [Questions \& Answers with Examples](#questions--answers-with-examples)
  - [Databases](#databases)
    - [Questions \& Answers with Examples](#questions--answers-with-examples-1)
  - [AWS Cloud Foundations Part 1](#aws-cloud-foundations-part-1)
    - [Questions \& Answers with Examples](#questions--answers-with-examples-2)
  - [AWS Cloud Foundations Part 2](#aws-cloud-foundations-part-2)
    - [Questions \& Answers with Examples](#questions--answers-with-examples-3)
  - [AWS Well-Architected Framework](#aws-well-architected-framework)
    - [Questions \& Answers with Examples](#questions--answers-with-examples-4)
  - [AWS CloudFormation](#aws-cloudformation)
    - [Questions \& Answers with Examples](#questions--answers-with-examples-5)
  - [AWS Billing](#aws-billing)
    - [Questions \& Answers with Examples](#questions--answers-with-examples-6)
  - [Key Takeaways](#key-takeaways)

---

## Python

### Questions & Answers with Examples

1. **What are a list and tuple in Python?**  
   - **List**: Mutable, ordered collection. Example: `fruits = ["apple", "banana"]`.  
   - **Tuple**: Immutable, ordered collection. Example: `colors = ("red", "green")`.  

2. **What is a namespace in Python?**  
   A system to ensure unique names for objects (e.g., variables). Types:  
   - **Local**: Inside a function.  
   - **Global**: Defined at the script level.  

3. **Local vs. Global Variable**  
   - **Local**: Accessible only within its function.  
     ```python
     def greet():
         message = "Hello"  # Local
     ```
   - **Global**: Accessible everywhere.  
     ```python
     message = "Hello"  # Global
     ```

4. **What is an IDE?**  
   Integrated Development Environment (e.g., PyCharm, VS Code).  

5. **What are modules?**  
   Reusable Python files (e.g., `math.py`). Example:  
   ```python
   import math
   print(math.sqrt(16))  # Output: 4.0
   ```

6. **Array vs. List**  
   - **Array**: Homogeneous (fixed type, from `array` module).  
     ```python
     import array
     arr = array.array('i', [1, 2, 3])
     ```
   - **List**: Heterogeneous (any type).  

7. **What are operators?**  
   Symbols to perform operations (e.g., `+`, `==`, `and`).  

---

## Databases

### Questions & Answers with Examples

1. **Relational vs. Non-Relational DB**  
   - **Relational**: Tables with schemas (e.g., MySQL).  
   - **Non-Relational**: Flexible (e.g., MongoDB).  

2. **What are indexes?**  
   Structures to speed up queries (e.g., `CREATE INDEX idx_name ON users(name)`).  

3. **Primary vs. Secondary Keys**  
   - **Primary**: Unique identifier (e.g., `user_id`).  
   - **Secondary**: Non-unique (e.g., `email` for faster searches).  

4. **Inner vs. Outer Joins**  
   - **Inner**: Returns matching rows.  
     ```sql
     SELECT * FROM orders INNER JOIN customers ON orders.customer_id = customers.id;
     ```
   - **Outer**: Includes non-matching rows (LEFT, RIGHT, FULL).  

5. **DROP TABLE vs. TRUNCATE TABLE**  
   - **DROP**: Deletes table + structure.  
   - **TRUNCATE**: Deletes data only (faster).  

6. **SQL Data Types**  
   `INT`, `VARCHAR`, `DATE`, `BOOLEAN`.  

7. **WHERE vs. HAVING**  
   - **WHERE**: Filters rows before grouping.  
   - **HAVING**: Filters after grouping.  

---

## AWS Cloud Foundations Part 1

### Questions & Answers with Examples

1. **IaaS, PaaS, SaaS**  
   - **IaaS**: Raw compute (e.g., EC2).  
   - **PaaS**: Platform (e.g., Elastic Beanstalk).  
   - **SaaS**: Software (e.g., Gmail).  

2. **Cloud Advantages**  
   Cost savings, scalability, global reach.  

3. **AWS Region vs. AZ**  
   - **Region**: Geographic area (e.g., `us-east-1`).  
   - **AZ**: Isolated data centers within a region.  

4. **AWS Services Categories**  
   Compute, Storage, Database, Networking.  

5. **Object vs. Block Storage**  
   - **Object**: S3 (files).  
   - **Block**: EBS (volumes for EC2).  

6. **Compute Services**  
   - **EC2**: Virtual servers.  
   - **Lambda**: Serverless functions.  

7. **Storage Services**  
   - **S3**: Object storage.  
   - **EBS**: Block storage.  

---

## AWS Cloud Foundations Part 2

### Questions & Answers with Examples

1. **Shared Responsibility Model**  
   AWS manages the cloud; customers manage in-cloud resources.  

2. **IAM Role vs. Policy**  
   - **Role**: Temporary permissions (e.g., EC2 to access S3).  
   - **Policy**: JSON permissions document.  

3. **AMI**  
   Template for EC2 instances (e.g., `ami-0abcdef1234567890`).  

4. **EC2 Instance Types**  
   - **t2.micro**: Free tier (low traffic).  
   - **m5.large**: Memory-optimized.  

5. **VPC & Subnets**  
   - **Public Subnet**: Internet access (e.g., web servers).  
   - **Private Subnet**: No direct internet access (e.g., databases).  

---

## AWS Well-Architected Framework

### Questions & Answers with Examples

1. **Pillars**  
   Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.  

2. **Operational Excellence**  
   Automate changes (e.g., CloudFormation).  

3. **Security Principles**  
   Least privilege, encryption (e.g., KMS).  

4. **Reliability**  
   Multi-AZ deployments (e.g., RDS).  

5. **Performance Efficiency**  
   Right-sizing (e.g., EC2 instance types).  

6. **Cost Optimization**  
   Reserved Instances, Spot Instances.  

7. **Sustainability**  
   Energy-efficient regions (e.g., `eu-west-1`).  

---

## AWS CloudFormation

### Questions & Answers with Examples

1. **Configuration Orchestration**  
   Automating resource deployment (e.g., `AWS::EC2::Instance`).  

2. **Configuration Management Tools**  
   Ansible, Chef, Puppet.  

3. **CI/CD**  
   - **CI**: Automated testing (e.g., CodePipeline).  
   - **CD**: Automated deployments.  

4. **CloudFormation Advantages**  
   Infrastructure as Code (IaC), repeatability, rollback.  

5. **JSON vs. YAML**  
   - **JSON**: Strict syntax.  
   - **YAML**: Human-readable (preferred for CFN).  

6. **Stack**  
   Collection of AWS resources defined in a template.  

---

## AWS Billing

### Questions & Answers with Examples

1. **Support Plans**  
   Basic, Developer, Business, Enterprise.  

2. **AWS Pricing Calculator**  
   Estimates costs (e.g., `t2.micro` = ~$8.50/month).  

3. **EC2 Pricing Models**  
   - **On-Demand**: Pay-as-you-go.  
   - **Reserved**: Discount for commitment.  
   - **Spot**: Bid for unused capacity.  

---

## Key Takeaways

- **Python**: Lists (mutable), tuples (immutable), modules.  
- **Databases**: Relational (SQL) vs. non-relational (NoSQL).  
- **AWS Basics**: Regions, AZs, IAM, VPC.  
- **Well-Architected**: Six pillars for robust cloud design.  
- **CloudFormation**: IaC for automated deployments.  
- **Billing**: Optimize costs with Reserved/Spot Instances.  

**Example Scenario**:  
A startup uses CloudFormation to deploy a VPC with public/private subnets, EC2 instances, and RDS, following Well-Architected principles.  

**Feedback**: Contact [AWS Support](https://support.aws.amazon.com).  

© 2022, Amazon Web Services, Inc. or its affiliates. All rights reserved.