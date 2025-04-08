# Comprehensive Lab Guide: Building a VPC and Launching a Web Server

## Introduction
This lab provides a complete walkthrough for creating a secure, functional VPC infrastructure with public and private subnets, and deploying a web server in AWS. You'll learn VPC architecture fundamentals and practical implementation.

## Task 1: Creating the VPC

### Step 1: Access VPC Console
1. Open AWS Management Console
2. Search for and select "VPC" service

### Step 2: Configure VPC Using Wizard
1. Select "Create VPC" → "VPC and more"
2. Configure settings:
   ```yaml
   Name tag: Lab VPC
   IPv4 CIDR: 10.0.0.0/16
   IPv6: No IPv6 CIDR block
   Tenancy: Default
   Availability Zones: 1
   Public subnets: 1 (10.0.0.0/24)
   Private subnets: 1 (10.0.1.0/24)
   NAT gateway: In 1 AZ
   ```

3. Name resources:
   ```yaml
   VPC: Lab VPC
   Public Subnet: Public Subnet 1
   Private Subnet: Private Subnet 1
   Public Route Table: Public Route Table
   Private Route Table: Private Route Table
   ```

**Key Components Created:**
- VPC with 65,536 IP addresses (10.0.0.0/16)
- Internet Gateway (for public subnet)
- NAT Gateway (for private subnet)
- Route tables with proper routes

## Task 2: Creating Additional Subnets

### Step 1: Create Second Public Subnet
1. Navigate to "Subnets" → "Create subnet"
2. Configure:
   ```yaml
   VPC: Lab VPC
   Name: Public Subnet 2
   AZ: No preference
   CIDR: 10.0.2.0/24
   ```

### Step 2: Create Second Private Subnet
1. Navigate to "Subnets" → "Create subnet"
2. Configure:
   ```yaml
   VPC: Lab VPC
   Name: Private Subnet 2
   AZ: No preference
   CIDR: 10.0.3.0/24
   ```

**Subnet Strategy:**
- Public subnets: 10.0.0.0/24, 10.0.2.0/24
- Private subnets: 10.0.1.0/24, 10.0.3.0/24
- Enables multi-AZ deployment for high availability

## Task 3: Configuring Route Tables

### Step 1: Associate Public Subnet
1. Navigate to "Route Tables"
2. Select "Public Route Table"
3. Under "Subnet associations":
   - Edit associations
   - Add "Public Subnet 2"
   - Save

### Step 2: Associate Private Subnet
1. Select "Private Route Table"
2. Under "Subnet associations":
   - Edit associations
   - Add "Private Subnet 2"
   - Save

**Verification:**
- Public subnets route 0.0.0.0/0 → Internet Gateway
- Private subnets route 0.0.0.0/0 → NAT Gateway

## Task 4: Creating Security Group

### Step 1: Configure Web Security Group
1. Navigate to "Security Groups" → "Create security group"
2. Configure:
   ```yaml
   Name: Web Security Group
   Description: Enable HTTP access
   VPC: Lab VPC
   Inbound rules:
     - Type: HTTP
     - Source: 0.0.0.0/0
     - Description: Permit web requests
   ```

**Security Best Practices:**
- Only open necessary ports (HTTP/80)
- Restrict source IP ranges in production
- Use descriptive names and tags

## Task 5: Launching Web Server

### Step 1: Configure EC2 Instance
1. Navigate to EC2 → "Launch instances"
2. Configure:
   ```yaml
   Name: Web Server 1
   AMI: Amazon Linux 2
   Instance type: t3.micro
   Key pair: vockey
   Network:
     - VPC: Lab VPC
     - Subnet: Public Subnet 2
     - Auto-assign public IP: Enable
     - Security group: Web Security Group
   User data:
     #!/bin/bash
     yum install -y httpd mysql php
     wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/.../lab-app.zip
     unzip lab-app.zip -d /var/www/html/
     chkconfig httpd on
     service httpd start
   ```

### Step 2: Verify Deployment
1. Wait for instance status checks (2/2)
2. Copy "Public IPv4 DNS" from instance details
3. Open in web browser

**Expected Result:**
- Apache web server welcome page
- PHP application files deployed
- Successful internet connectivity

## Architecture Overview

### Final VPC Configuration
| Resource | Configuration |
|----------|--------------|
| VPC | 10.0.0.0/16 |
| Public Subnets | 10.0.0.0/24, 10.0.2.0/24 |
| Private Subnets | 10.0.1.0/24, 10.0.3.0/24 |
| Internet Gateway | Attached to VPC |
| NAT Gateway | us-west-2a |
| Security Group | HTTP access from anywhere |

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| Instance not reachable | Check security group rules |
| No internet access | Verify route table IGW route |
| User data not executing | Check instance system logs |
| HTTP timeout | Verify NACL allows ephemeral ports |

## Best Practices

1. **Naming Conventions**:
   - Consistent, descriptive names (e.g., "prod-web-sg")
   - Include environment tags

2. **Security**:
   - Restrict SSH access to known IPs
   - Implement least privilege security groups
   - Monitor security group changes

3. **High Availability**:
   - Deploy across multiple AZs
   - Use Auto Scaling groups in production
   - Consider Application Load Balancer

## Common Questions

**Q: Why use both public and private subnets?**
A: Public subnets for internet-facing resources, private subnets for databases/internal services

**Q: How to make my web server highly available?**
A: Deploy identical instances in multiple AZs behind a load balancer

**Q: What's the difference between NAT Gateway and Internet Gateway?**
A: IGW provides bidirectional internet access, NAT Gateway allows outbound-only internet for private subnets

This comprehensive guide provides all steps needed to build a secure, functional VPC with web server deployment, following AWS best practices for network architecture and security.