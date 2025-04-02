# AWS VPC Troubleshooting Lab Guide

## Table of Contents
- [AWS VPC Troubleshooting Lab Guide](#aws-vpc-troubleshooting-lab-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Business Scenario](#business-scenario)
  - [Technical Requirements](#technical-requirements)
    - [Recommended Troubleshooting Steps:](#recommended-troubleshooting-steps)
  - [Lab Tasks Overview](#lab-tasks-overview)
    - [Step-by-Step Activities:](#step-by-step-activities)
  - [Café Web Server Architecture](#café-web-server-architecture)
    - [Network Diagram:](#network-diagram)
  - [Troubleshooting Steps](#troubleshooting-steps)
    - [1. Verify Route Tables](#1-verify-route-tables)
    - [2. Check Security Groups](#2-check-security-groups)
    - [3. Review Network ACLs](#3-review-network-acls)
    - [4. Analyze Flow Logs](#4-analyze-flow-logs)
  - [Checkpoint Questions \& Answers](#checkpoint-questions--answers)
  - [Key Takeaways](#key-takeaways)

---

## Introduction

**Objective**: This lab guides you through troubleshooting network connectivity issues in an Amazon Virtual Private Cloud (VPC) environment, focusing on a café web server that has become inaccessible after security updates.

**Key Concepts**:
- VPC networking components
- Flow logs for traffic analysis
- Security group and NACL configurations

---

## Business Scenario

**Situation**: 
- Security improvements were made to the café's VPC
- Customers can no longer access the website
- SSH connections to the web server are failing

**Team Members**:
- Martha: Project lead
- Nikhil & Sofia: Engineers who implemented changes
- Mateo & Olivia: Networking specialists

**Problem Statement**: The security changes inadvertently caused network misconfigurations that need to be diagnosed and fixed.

---

## Technical Requirements

### Recommended Troubleshooting Steps:
1. **Verify Network Components**:
   - Route tables
   - Network ACLs (stateless firewall)
   - Security groups (stateful firewall)

2. **Enable VPC Flow Logs**:
   - Capture all IP traffic
   - Analyze for blocked connections

3. **Analyze Flow Data**:
   - Identify rejected packets
   - Trace communication paths

**Example**: If SSH connections are failing, flow logs might show that TCP port 22 traffic is being blocked by a network ACL.

---

## Lab Tasks Overview

### Step-by-Step Activities:
1. **Create S3 Bucket**:
   - Storage destination for flow logs
   - Requires proper IAM permissions

2. **Enable VPC Flow Logs**:
   - Configure to capture all traffic
   - Specify S3 bucket as destination

3. **Troubleshoot Configurations**:
   - Check route tables for proper internet gateway routes
   - Verify security group inbound/outbound rules
   - Review network ACL allow/deny rules

4. **Analyze Flow Logs**:
   - Download logs from S3
   - Identify REJECT entries

**CLI Example**:
```bash
aws ec2 create-flow-logs \
--resource-type VPC \
--resource-id vpc-12345678 \
--traffic-type ALL \
--log-destination-type s3 \
--log-destination arn:aws:s3:::my-flow-log-bucket
```

---

## Café Web Server Architecture

### Network Diagram:
```
Region
├── VPC 1 (10.0.0.0/16)
│   ├── Public Subnet (10.0.1.0/24)
│   │   ├── Internet Gateway
│   │   ├── Route Table
│   │   ├── Network ACL
│   │   └── Café Web Server (EC2 Instance)
│   └── Flow Logs
└── VPC 2 (192.168.0.0/16)
    ├── Public Subnet
    ├── CLI Host
    └── S3 Flow Logs Bucket
```

**Critical Components**:
- **Internet Gateway**: Provides internet access
- **Route Table**: Must have 0.0.0.0/0 route to IGW
- **Security Group**: Should allow HTTP/80, HTTPS/443, and SSH/22
- **Network ACL**: Must have proper inbound/outbound rules

---

## Troubleshooting Steps

### 1. Verify Route Tables
- Check if public subnet route table has:
  ```
  Destination: 0.0.0.0/0 
  Target: igw-123456 (Internet Gateway)
  ```

### 2. Check Security Groups
- Web server security group needs:
  - Inbound: HTTP (80), HTTPS (443), SSH (22)
  - Outbound: All traffic (or restricted as needed)

### 3. Review Network ACLs
- Network ACLs are stateless - need explicit allow rules in both directions:
  ```
  Rule # | Type | Protocol | Port | Source/Dest | Allow/Deny
  100    | HTTP | TCP      | 80   | 0.0.0.0/0   | ALLOW
  110    | SSH  | TCP      | 22   | <your IP>   | ALLOW
  *      | ALL  | ALL      | ALL  | 0.0.0.0/0   | DENY
  ```

### 4. Analyze Flow Logs
Sample log entry showing blocked SSH:
```
version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status
2 123456789012 eni-123456 203.0.113.12 10.0.1.5 54321 22 6 1 40 1432820000 1432820000 REJECT OK
```

---

## Checkpoint Questions & Answers

1. **What are four common tasks for troubleshooting network connectivity on AWS?**
   - **Answer**:
     1. Verify route tables
     2. Check security group rules
     3. Review network ACL configurations
     4. Examine VPC flow logs

2. **Where can a systems operator publish a VPC flow log?**
   - **Answer**: 
     - Amazon S3 bucket
     - Amazon CloudWatch Logs
     - Amazon Kinesis Data Firehose

3. **Which AWS CLI command do you use to create a VPC flow log?**
   - **Answer**:
   ```bash
   aws ec2 create-flow-logs \
   --resource-type VPC \
   --resource-id vpc-12345678 \
   --traffic-type ALL \
   --log-destination-type s3 \
   --log-destination arn:aws:s3:::my-flow-log-bucket
   ```

---

## Key Takeaways

1. **Layered Security**: AWS provides multiple security layers (NACLs, SGs) that must work together.
2. **Diagnostic Tools**: VPC flow logs are essential for visibility into network traffic.
3. **Configuration Order**:
   - Route tables direct traffic
   - NACLs filter at subnet level
   - Security groups filter at instance level

**Final Example**: After analysis, the team discovers the network ACL was missing an outbound rule for ephemeral ports (32768-61000) needed for TCP responses, explaining why SSH connections timed out.