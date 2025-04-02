# Amazon Elastic File System (EFS) - Comprehensive Guide

## Table of Contents
- [Amazon Elastic File System (EFS) - Comprehensive Guide](#amazon-elastic-file-system-efs---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction to Amazon EFS](#introduction-to-amazon-efs)
  - [Key Features](#key-features)
  - [Benefits of Amazon EFS](#benefits-of-amazon-efs)
  - [Performance Attributes](#performance-attributes)
    - [Storage Classes](#storage-classes)
    - [Performance Modes](#performance-modes)
    - [Throughput Modes](#throughput-modes)
  - [Use Cases](#use-cases)
  - [Architecture](#architecture)
    - [Core Components:](#core-components)
    - [Typical Deployment:](#typical-deployment)
  - [Implementation Steps](#implementation-steps)
    - [1. Create EFS File System](#1-create-efs-file-system)
    - [2. Configure EC2 Resources](#2-configure-ec2-resources)
    - [3. Create Mount Targets](#3-create-mount-targets)
    - [4. Mount EFS](#4-mount-efs)
    - [5. Cleanup](#5-cleanup)
  - [Checkpoint Questions \& Answers](#checkpoint-questions--answers)
  - [Key Takeaways](#key-takeaways)

---

## Introduction to Amazon EFS

**Definition**: Amazon Elastic File System (EFS) is a scalable, fully managed, elastic Network File System (NFS) storage service for use with AWS Cloud services and on-premises resources.

**Key Characteristics**:
- **Shared File Storage**: Multiple instances can access files simultaneously.
- **Elastic Capacity**: Automatically scales to petabytes as needed.
- **Fully Managed**: No infrastructure to provision or maintain.

**Example**: A media company uses EFS to store video assets that need to be accessed by multiple rendering servers simultaneously during post-production.

---

## Key Features

1. **NFS Support**: Compatible with NFSv4 protocol.
2. **Multi-Service Compatibility**: Works with EC2, Lambda, ECS, and on-premises servers.
3. **Linux Compatibility**: Supports all Linux-based AMIs and distributions.
4. **Tagging**: Enables resource organization and cost allocation.
5. **Security**: Integrates with IAM, VPC security groups, and encryption at rest/in-transit.

**Additional Notes**:
- Uses standard NFS mount commands (`mount -t nfs4...`)
- Supports POSIX file permissions (user/group/others)

---

## Benefits of Amazon EFS

| Benefit | Description | Example Use Case |
|---------|------------|------------------|
| **High Availability** | Data stored redundantly across multiple AZs | Mission-critical applications requiring 24/7 access |
| **Dynamic Elasticity** | Automatically scales with file additions/deletions | Unpredictable storage needs like user uploads |
| **Fully Managed** | No file server maintenance required | Teams without dedicated storage administrators |
| **Shared Access** | Multiple instances can read/write simultaneously | CI/CD pipelines with parallel build processes |

**Cost Advantage**: Pay only for storage used (no pre-provisioning required)

---

## Performance Attributes

### Storage Classes
| Class | Description | Ideal For |
|-------|-------------|-----------|
| **Standard** | Frequently accessed files | Active workloads |
| **Standard-IA** | Infrequently accessed files (lower cost) | Archived data with occasional access |
| **One Zone** | Single AZ storage (lower cost) | Non-critical, recreatable data |
| **One Zone-IA** | Single AZ infrequent access | Secondary backups |

### Performance Modes
- **General Purpose**: Default for most workloads (low latency)
- **Max I/O**: Higher throughput for parallel applications (big data)

### Throughput Modes
- **Bursting**: Baseline + burst capability (default)
- **Provisioned**: Guaranteed throughput for consistent workloads

**Example**: A scientific research team uses Max I/O mode with Standard storage for their parallel data processing workloads.

---

## Use Cases

1. **Home Directories**: Centralized storage for user profiles.
2. **Enterprise Applications**: Shared storage for SAP, Oracle, etc.
3. **Development/Testing**: Shared code repositories.
4. **Database Backups**: Central location for DB dumps.
5. **Web Serving**: Shared content for web farms.
6. **Media Workflows**: Collaborative video editing.
7. **Big Data**: Shared datasets for analytics.

**Implementation Example**:
```bash
# Mount command example
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 \
fs-12345678.efs.us-west-2.amazonaws.com:/ /mnt/efs
```

---

## Architecture

### Core Components:
1. **File System**: Primary EFS resource (regional service)
2. **Mount Targets**: ENIs in each AZ (1 per subnet)
3. **Access Points**: Application-specific entry points

### Typical Deployment:
```
AWS Region
├── VPC
│   ├── AZ1
│   │   ├── Private Subnet
│   │   │   └── Mount Target (10.0.1.32)
│   │   └── EC2 Instance (mounts EFS)
│   ├── AZ2
│   │   ├── Private Subnet
│   │   │   └── Mount Target (10.0.3.45)
│   │   └── EC2 Instance
│   └── AZ3
│       ├── Private Subnet
│       │   └── Mount Target (10.0.4.15)
│       └── EC2 Instance
└── EFS File System (shared across all AZs)
```

**Best Practice**: Create mount targets in private subnets for security

---

## Implementation Steps

### 1. Create EFS File System
- Console: EFS > Create file system
- CLI:
  ```bash
  aws efs create-file-system --creation-token "my-efs" \
  --performance-mode generalPurpose --throughput-mode bursting
  ```

### 2. Configure EC2 Resources
- Launch Linux instances in multiple AZs
- Ensure proper VPC networking (security groups)

### 3. Create Mount Targets
- One per AZ in your VPC
- Requires proper security group rules (NFS port 2049)

### 4. Mount EFS
- Install NFS client: `sudo yum install -y nfs-utils`
- Create mount point: `sudo mkdir /mnt/efs`
- Add to /etc/fstab for automatic mounting

### 5. Cleanup
- Unmount before deletion: `sudo umount /mnt/efs`
- Delete mount targets before file system

---

## Checkpoint Questions & Answers

1. **Which file system protocol does Amazon EFS support?**
   - **Answer**: Network File System (NFS) version 4.0 and 4.1 (NFSv4)

2. **Which AWS services are able to access Amazon EFS concurrently?**
   - **Answer**: 
     - Amazon EC2
     - AWS Lambda (when configured with EFS access)
     - Amazon ECS
     - On-premises servers (via AWS Direct Connect/VPN)

3. **What are the main benefits of using Amazon EFS in your cloud environment?**
   - **Answer**:
     1. Shared access across multiple instances
     2. Automatic scaling without provisioning
     3. High availability across AZs
     4. Fully managed service
     5. Integration with Linux workloads

---

## Key Takeaways

1. **Shared Storage**: EFS enables multiple instances to access files simultaneously.
2. **Elastic Scaling**: Grows and shrinks automatically with your data.
3. **High Availability**: Data replicated across multiple AZs by default.
4. **Performance Options**: Choose between General Purpose and Max I/O modes.
5. **Security**: Encryption at rest/in-transit with IAM and security group controls.

**Final Example**: A game development studio uses EFS to store game assets, allowing their render farm (50+ EC2 instances) to simultaneously access texture files during compilation, while their web servers use the same EFS to serve downloadable content to players.