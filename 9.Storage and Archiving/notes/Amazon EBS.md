# Amazon Elastic Block Store (EBS) - Comprehensive Guide

## Table of Contents
- [Amazon Elastic Block Store (EBS) - Comprehensive Guide](#amazon-elastic-block-store-ebs---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction to Amazon EBS](#introduction-to-amazon-ebs)
  - [Key Features of Amazon EBS](#key-features-of-amazon-ebs)
  - [EBS Volume Types](#ebs-volume-types)
    - [SSD Volumes (Optimized for IOPS)](#ssd-volumes-optimized-for-iops)
    - [HDD Volumes (Optimized for Throughput)](#hdd-volumes-optimized-for-throughput)
  - [EBS Use Cases](#ebs-use-cases)
    - [Volume Use Cases:](#volume-use-cases)
    - [Snapshot Use Cases:](#snapshot-use-cases)
  - [Working with EBS Volumes](#working-with-ebs-volumes)
    - [Creating and Attaching a Volume (AWS CLI)](#creating-and-attaching-a-volume-aws-cli)
  - [EBS Snapshots](#ebs-snapshots)
    - [Key Concepts:](#key-concepts)
    - [Creating and Restoring Snapshots:](#creating-and-restoring-snapshots)
  - [Data Lifecycle Management](#data-lifecycle-management)
    - [Amazon Data Lifecycle Manager (DLM):](#amazon-data-lifecycle-manager-dlm)
    - [Setup Steps:](#setup-steps)
  - [Checkpoint Questions and Answers](#checkpoint-questions-and-answers)
  - [Key Takeaways](#key-takeaways)

---

## Introduction to Amazon EBS

**Definition**: Amazon Elastic Block Store (EBS) provides persistent block-level storage volumes for use with Amazon EC2 instances. 

**Key Characteristics**:
- **Persistent Storage**: Data persists independently of EC2 instance lifecycles.
- **High Availability**: Automatically replicated within its Availability Zone (AZ).
- **Scalability**: Can scale capacity up or down within minutes.
- **Performance**: Offers SSD and HDD options for different workload needs.

**Example**: When running a database on EC2, EBS provides durable storage that remains intact even if the EC2 instance is stopped or terminated.

---

## Key Features of Amazon EBS

1. **Multiple Volume Types**: SSDs for high IOPS, HDDs for throughput-intensive workloads.
2. **Snapshots**: Point-in-time backups stored in Amazon S3.
3. **Encryption**: Data encrypted at rest using AWS Key Management Service (KMS).
4. **Elastic Volumes**: Modify volume type, size, or IOPS without downtime.

**Additional Notes**:
- Snapshots are incremental, saving only changed blocks since the last snapshot.
- Encryption is transparent and requires no additional setup for applications.

---

## EBS Volume Types

### SSD Volumes (Optimized for IOPS)
| Type | Description | Max IOPS | Use Cases |
|------|-------------|----------|-----------|
| **Provisioned IOPS (io2 Block Express)** | Highest performance | 256,000 | Mission-critical databases (Oracle, SAP) |
| **Provisioned IOPS (io1/io2)** | High performance | 64,000 | Production databases (MySQL, PostgreSQL) |
| **General Purpose (gp3)** | Balanced performance | 16,000 | Boot volumes, development environments |
| **General Purpose (gp2)** | Legacy option | 16,000 | Older applications (being phased out) |

### HDD Volumes (Optimized for Throughput)
| Type | Description | Max Throughput | Use Cases |
|------|-------------|---------------|-----------|
| **Throughput Optimized (st1)** | Low-cost, high throughput | 500 MBps | Big data, log processing |
| **Cold HDD (sc1)** | Lowest cost | 250 MBps | Infrequently accessed data |

**Example**: A financial analytics platform uses `io2` volumes for its high-frequency trading database and `st1` volumes for storing historical transaction logs.

---

## EBS Use Cases

### Volume Use Cases:
- **Boot Volumes**: Store OS and applications for EC2 instances.
- **Primary Storage**: Host file systems (e.g., ext4, NTFS).
- **Databases**: Provide low-latency storage for MySQL, MongoDB, etc.

### Snapshot Use Cases:
- **Backups**: Create point-in-time backups of critical data.
- **Disaster Recovery**: Restore volumes in case of failures.
- **Data Sharing**: Copy snapshots across AWS accounts/regions.

**Example**: A gaming company uses EBS snapshots to back up player progress daily and replicates them to another region for disaster recovery.

---

## Working with EBS Volumes

### Creating and Attaching a Volume (AWS CLI)
1. **Create a Volume**:
   ```bash
   aws ec2 create-volume \
   --size 80 \
   --availability-zone us-east-1a \
   --volume-type gp2
   ```
   - `size`: Size in GiB.
   - `availability-zone`: Must match the EC2 instance's AZ.
   - `volume-type`: Choose based on workload (e.g., `gp3` for general use).

2. **Attach to an EC2 Instance**:
   ```bash
   aws ec2 attach-volume \
   --volume-id vol-1234567890abcdef0 \
   --instance-id i-01474ef662b89480 \
   --device /dev/sdf
   ```
   - `device`: Specify a device name (e.g., `/dev/sdf`).

**Note**: After attaching, format and mount the volume on the EC2 instance (e.g., using `mkfs` and `mount` commands).

---

## EBS Snapshots

### Key Concepts:
- **Incremental Backups**: Only changed blocks are saved, reducing costs.
- **Cross-Region Copy**: Enhance disaster recovery by copying snapshots to other regions.
- **Encryption**: Snapshots inherit the encryption status of the parent volume.

### Creating and Restoring Snapshots:
1. **Create a Snapshot**:
   ```bash
   aws ec2 create-snapshot \
   --volume-id vol-1234567890abcdef0 \
   --description "Daily backup"
   ```

2. **Restore a Snapshot**:
   ```bash
   aws ec2 create-volume \
   --snapshot-id snap-1234567890abcdef0 \
   --availability-zone us-east-1a
   ```

**Example**: A healthcare provider encrypts EBS volumes storing patient records and uses snapshots to comply with data retention policies.

---

## Data Lifecycle Management

### Amazon Data Lifecycle Manager (DLM):
- Automates snapshot creation, retention, and deletion.
- Uses IAM roles and policies to manage permissions.

### Setup Steps:
1. **Create an IAM Role**:
   ```bash
   aws dlm create-default-role
   ```
2. **Define a Lifecycle Policy** (JSON):
   ```json
   {
     "ResourceTypes": ["VOLUME"],
     "TargetTags": [{"Key": "env", "Value": "production"}],
     "Schedules": [{"Name": "Daily", "RetainRule": {"Count": 7}}]
   }
   ```
3. **Apply the Policy**:
   ```bash
   aws dlm create-lifecycle-policy \
   --description "Daily backups" \
   --policy-details file://policy.json
   ```

**Example**: An e-commerce platform automates daily snapshots of production databases, retaining them for 14 days.

---

## Checkpoint Questions and Answers

1. **A cloud engineer wants to choose a volume type for additional storage on a virtual desktop. Which volume type should the engineer use?**
   - **Answer**: `General Purpose SSD (gp3)` – Balanced performance for interactive workloads like virtual desktops.

2. **A cloud engineer has restored the EBS volume of an unresponsive instance from a recent snapshot. The engineer is concerned about the initial latency of the restored snapshot. What can the engineer do to prevent this latency?**
   - **Answer**: Use **Fast Snapshot Restore (FSR)** to pre-warm the snapshot and eliminate latency on first access.

3. **Which IAM role do you need to create before you can use Amazon Data Lifecycle Manager?**
   - **Answer**: `AWSDataLifecycleManagerDefaultRole` – Grants DLM permissions to manage snapshots.

---

## Key Takeaways

- **Persistence**: EBS volumes outlive EC2 instances, ensuring data durability.
- **Flexibility**: Choose between SSD (high IOPS) and HDD (high throughput) volumes.
- **Backups**: Snapshots provide cost-efficient, incremental backups stored in S3.
- **Automation**: Use DLM to simplify snapshot management.

**Final Example**: A media company uses `gp3` volumes for video editing workstations, `io2` for rendering servers, and automated snapshots to protect project files.