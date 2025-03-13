# Amazon Elastic Compute Cloud (Amazon EC2) - Cloud Foundations

## What You Will Learn

### Core Objectives:
- **Explain the features and uses of Amazon EC2.**
- **Launch an EC2 instance.**
- **Describe the pricing options for Amazon EC2.**

---

## Introduction to AWS Compute Services

AWS provides a broad catalog of **Compute services**, which are foundational to building solutions. These services range from **application services** to **flexible virtual servers** and **serverless computing**. Whether you're building mobile apps or running massive clusters for genome sequencing, compute is the starting point.

### Key Compute Categories:
1. **Virtual Machines (VMs)**
   - **Amazon EC2**: Secure, resizable virtual servers in the cloud.
   - **Amazon Lightsail**: Cost-effective virtual private servers.

2. **Containers**
   - **Amazon Elastic Container Service (ECS)**: Run Docker container applications on AWS.

3. **Platform as a Service (PaaS)**
   - **AWS Elastic Beanstalk**: Runs web applications and services in various languages (Java, .NET, PHP, etc.).

4. **Serverless**
   - **AWS Lambda**: Runs code without provisioning servers.
   - **AWS Fargate**: Serverless compute platform for containers.

5. **Specialized Solutions**
   - **AWS Outposts**: Run AWS infrastructure on-premises.
   - **AWS Batch**: Run batch jobs at any scale.

---

## Amazon EC2 Overview

Amazon EC2 provides **virtual machines** (referred to as **EC2 instances**) in the cloud. These instances can support a variety of workloads, such as:

- **Application servers**
- **Web servers**
- **Database servers**
- **Game servers**
- **Mail servers**
- **Media servers**
- **Catalog servers**
- **File servers**
- **Computing servers**
- **Proxy servers**

### Key Features:
- **Elasticity**: Automatically scale the number of servers up or down.
- **Compute**: Host applications or process data using CPU and memory.
- **Cloud**: Instances are hosted in the cloud, providing flexibility and scalability.

### EC2 Instance Lifecycle:
- **Pending**: Instance is being launched or started.
- **Running**: Instance is fully booted and ready.
- **Rebooting**: Instance is being rebooted.
- **Stopping**: Instance is being stopped.
- **Stopped**: Instance is not running but can be restarted.
- **Terminated**: Instance is permanently deleted.

---

## Launching an EC2 Instance

When launching an EC2 instance, you need to make several key decisions:

### 1. Select an AMI (Amazon Machine Image)
- **AMI**: A template that contains the OS and pre-installed software.
- **AMI Types**:
  - **Quick Start**: Prebuilt AMIs provided by AWS.
  - **My AMIs**: AMIs you created.
  - **AWS Marketplace**: Preconfigured templates from third parties.
  - **Community AMIs**: Shared by others (use with caution).

### 2. Select an Instance Type
- **Instance Type**: Determines the hardware configuration (CPU, memory, storage, network).
- **Categories**:
  - **General Purpose**: Balanced CPU, memory, and storage.
  - **Compute Optimized**: High-performance CPUs.
  - **Memory Optimized**: High memory for in-memory databases.
  - **Storage Optimized**: High storage for distributed file systems.
  - **Accelerated Computing**: GPU-based instances for machine learning.

### 3. Specify Network Settings
- **VPC (Virtual Private Cloud)**: Define the network where the instance will run.
- **Subnet**: Choose a subnet within the VPC.
- **Public IP**: Decide if the instance should have a public IP address.

### 4. Attach an IAM Role (Optional)
- **IAM Role**: Grants permissions to interact with other AWS services.
- **Instance Profile**: Container for the IAM role.

### 5. User Data Script (Optional)
- **User Data**: Scripts that run when the instance starts (e.g., install software, update the OS).

### 6. Specify Storage
- **Root Volume**: Contains the OS.
- **Additional Volumes**: Attach extra storage if needed.
- **Volume Types**:
  - **Amazon EBS**: Durable block storage.
  - **Instance Store**: Ephemeral storage (data is lost if the instance stops).

### 7. Add Tags
- **Tags**: Key-value pairs for organizing and managing resources.
- **Example**: `Name: WebServer1`

### 8. Security Group Settings
- **Security Group**: Acts as a virtual firewall, controlling traffic to and from the instance.
- **Rules**: Define allowed traffic (e.g., SSH on port 22).

### 9. Identify or Create a Key Pair
- **Key Pair**: Used for secure SSH access to the instance.
- **Public Key**: Stored on AWS.
- **Private Key**: Stored locally (must be kept secure).

---

## Amazon EC2 Pricing Models

### 1. **On-Demand Instances**
   - **Pay-as-you-go**: No upfront costs, pay by the hour.
   - **Best for**: Short-term, spiky, or unpredictable workloads.

### 2. **Reserved Instances**
   - **Commitment**: 1-year or 3-year term with discounted rates.
   - **Best for**: Steady-state workloads with predictable usage.

### 3. **Spot Instances**
   - **Bid-based**: Run instances at a lower cost, but they can be interrupted.
   - **Best for**: Fault-tolerant, time-insensitive workloads.

### 4. **Dedicated Hosts**
   - **Physical Server**: Dedicated hardware for your use.
   - **Best for**: Licensing compliance or regulatory requirements.

### 5. **Dedicated Instances**
   - **Isolated Hardware**: Instances run on hardware dedicated to a single customer.
   - **Best for**: Security-sensitive workloads.

### 6. **Scheduled Reserved Instances**
   - **Recurring Schedule**: Reserve capacity on a daily, weekly, or monthly basis.
   - **Best for**: Predictable workloads with specific time requirements.

---

## Key Takeaways

- **Amazon EC2** allows you to run virtual machines in the cloud with full control over the OS.
- **AMI** provides the template for launching EC2 instances.
- **Instance Types** define the hardware configuration (CPU, memory, storage, network).
- **Pricing Models** include On-Demand, Reserved, Spot, and Dedicated Hosts.
- **Security Groups** act as firewalls, controlling traffic to and from instances.
- **Key Pairs** are used for secure SSH access to instances.

---

## Additional Notes and Examples

### Example: Launching an EC2 Instance via AWS CLI
```bash
aws ec2 run-instances \
--image-id ami-0abcdef1234567890 \
--count 1 \
--instance-type t2.micro \
--key-name MyKeyPair \
--security-group-ids sg-0abcdef1234567890 \
--subnet-id subnet-0abcdef1234567890 \
--region us-east-1
```
- **image-id**: The AMI ID.
- **instance-type**: The type of instance (e.g., t2.micro).
- **key-name**: The key pair for SSH access.
- **security-group-ids**: The security group ID.
- **subnet-id**: The subnet where the instance will be launched.

### Example: User Data Script for Linux
```bash
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
```
- This script updates the OS, installs the Apache web server, and starts it.

### Example: Security Group Rule
- **Type**: SSH
- **Protocol**: TCP
- **Port Range**: 22
- **Source**: My IP (72.21.198.87/32)
- This rule allows SSH access from the specified IP address.

### Example: Tagging
- **Key**: Environment
- **Value**: Production
- This tag helps identify the instance as part of the production environment.

---

## Conclusion

Amazon EC2 is a powerful and flexible service that allows you to run virtual machines in the cloud. By understanding the key concepts of AMIs, instance types, networking, security, and pricing models, you can effectively launch and manage EC2 instances to meet your specific workload requirements.