# Amazon S3 Glacier - Comprehensive Guide

## Table of Contents
- [Amazon S3 Glacier - Comprehensive Guide](#amazon-s3-glacier---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction to Amazon S3 Glacier](#introduction-to-amazon-s3-glacier)
  - [Storage Classes](#storage-classes)
  - [Data Model Concepts](#data-model-concepts)
    - [1. **Vault**](#1-vault)
    - [2. **Archive**](#2-archive)
    - [3. **Job**](#3-job)
    - [4. **Notifications**](#4-notifications)
  - [Retrieval Options](#retrieval-options)
  - [Security Features](#security-features)
  - [Comparison with Amazon S3](#comparison-with-amazon-s3)
  - [Access Methods](#access-methods)
  - [Checkpoint Questions \& Answers](#checkpoint-questions--answers)
  - [Key Takeaways](#key-takeaways)

---

## Introduction to Amazon S3 Glacier

**Definition**: Amazon S3 Glacier is a secure, durable, and extremely low-cost cloud storage service for data archiving and long-term backup.

**Key Characteristics**:
- **Purpose-built for archiving**: Optimized for rarely accessed data
- **Low-cost storage**: Costs as low as $1 per TB per month
- **High durability**: 99.999999999% (11 9's) durability
- **Automated encryption**: All data encrypted by default with AES-256

**Example**: A financial institution uses Glacier to store 7+ years of transaction records for compliance purposes at 1/5th the cost of on-premises tape storage.

---

## Storage Classes

| Class | Retrieval Time | Cost | Ideal Use Case |
|-------|---------------|------|---------------|
| **Instant Retrieval** | Milliseconds | $$ | Rarely accessed data needing fast retrieval |
| **Flexible Retrieval** | 3-5 hours (Standard), 5-12 hours (Bulk) | $ | Yearly accessed archives (e.g., financial records) |
| **Deep Archive** | 12-48 hours | $ | Long-term preservation (e.g., medical records, media archives) |

**Cost Comparison Example**:
- Storing 100TB for 5 years:
  - Standard S3: ~$15,000
  - Glacier Deep Archive: ~$1,200

---

## Data Model Concepts

### 1. **Vault**
- Container for archives
- **URI Format**: `https://glacier.region.amazonaws.com/account-id/vaults/vault-name`
- **Example**: 
  ```bash
  aws glacier create-vault --account-id 111122223333 --vault-name "financial-archives"
  ```

### 2. **Archive**
- Any stored object (documents, media, backups)
- **URI Format**: `.../vaults/vault-name/archives/archive-id`
- **Upload Example**:
  ```bash
  aws glacier upload-archive --vault-name financial-archives --body largebackup.zip
  ```

### 3. **Job**
- Retrieval or inventory request
- **URI Format**: `.../vaults/vault-name/jobs/job-id`
- **Initiate Job**:
  ```bash
  aws glacier initiate-job --vault-name financial-archives --job-parameters '{"Type": "archive-retrieval", "ArchiveId": "Nk...!qrEXAMPLE"}'
  ```

### 4. **Notifications**
- SNS alerts for job completion
- **Configuration Example**:
  ```json
  {
    "Topic": "arn:aws:sns:us-west-2:111122223333:glacier-alerts",
    "Events": ["ArchiveRetrievalCompleted"]
  }
  ```

---

## Retrieval Options

| Option | Timeframe | Cost | Use When... |
|--------|----------|------|-------------|
| **Expedited** | 1-5 minutes | $$$ | Emergency access (e.g., legal discovery) |
| **Standard** | 3-5 hours | $$ | Planned retrievals (e.g., quarterly audits) |
| **Bulk** | 5-12 hours | $ | Large datasets (e.g., yearly compliance checks) |

**Real-World Scenario**: A law firm pays for expedited retrieval when responding to urgent subpoenas, but uses bulk retrieval for routine case file reviews.

---

## Security Features

1. **IAM Policies**:
   - Fine-grained access control
   - Example policy allowing only archive uploads:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [{
         "Effect": "Allow",
         "Action": ["glacier:UploadArchive"],
         "Resource": "*"
       }]
     }
     ```

2. **Encryption**:
   - AES-256 encryption at rest
   - SSL/TLS for data in transit

3. **Vault Lock**:
   - WORM (Write Once Read Many) compliance
   - Immutable policies for regulatory requirements

---

## Comparison with Amazon S3

| Feature | S3 Standard | S3 Glacier |
|---------|------------|------------|
| **Storage Cost** | $0.023/GB | $0.004/GB (Deep Archive) |
| **Retrieval Time** | Milliseconds | Minutes to hours |
| **Max Object Size** | 5TB | 40TB |
| **Encryption** | Optional | Always on |
| **Best For** | Frequently accessed data | Long-term archives |

**Migration Example**: Use S3 Lifecycle Policies to automatically transition objects:
```bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket my-bucket \
  --lifecycle-configuration '{
    "Rules": [{
      "ID": "MoveToGlacier",
      "Prefix": "archive/",
      "Status": "Enabled",
      "Transitions": [{
        "Days": 90,
        "StorageClass": "GLACIER"
      }]
    }]
  }'
```

---

## Access Methods

1. **AWS Management Console**:
   - Visual interface for vault management
   - Limited functionality (use CLI/SDK for full features)

2. **AWS CLI**:
   - Full control over operations
   - Example inventory retrieval:
     ```bash
     aws glacier initiate-job --vault-name my-vault --job-parameters '{"Type": "inventory-retrieval"}'
     ```

3. **SDKs (Java/.NET)**:
   - Programmatic integration
   - Example Java code:
     ```java
     InitiateJobRequest request = new InitiateJobRequest()
       .withVaultName("my-vault")
       .withJobParameters(new JobParameters()
         .withType("archive-retrieval"));
     ```

4. **S3 Lifecycle Policies**:
   - Automated tier transitions
   - Set rules based on object age/prefix

---

## Checkpoint Questions & Answers

1. **What are the three storage classes that make up Amazon S3 Glacier?**
   - **Answer**: 
     1. S3 Glacier Instant Retrieval
     2. S3 Glacier Flexible Retrieval
     3. S3 Glacier Deep Archive

2. **What is created in order to retrieve an archive or create an inventory of a vault?**
   - **Answer**: A *job* must be initiated, which generates a unique job ID for tracking the retrieval or inventory process.

3. **Which information does the vault description provide?**
   - **Answer**: 
     - Vault ARN
     - Creation date
     - Number of archives
     - Total archive size
     - Last inventory date
     - Associated notification configuration

---

## Key Takeaways

1. **Cost-Effective Archiving**: Glacier provides the lowest-cost storage in AWS for long-term retention.
2. **Flexible Retrieval**: Multiple retrieval options balance speed and cost.
3. **Enterprise-Grade Security**: Always-on encryption and IAM integration.
4. **Compliance Ready**: Vault Lock meets strict regulatory requirements.
5. **Automation Friendly**: Integrates with S3 Lifecycle for hands-off archiving.

**Final Example**: A media company:
- Uses *Instant Retrieval* for recent raw footage ($0.004/GB)
- Stores finished projects in *Flexible Retrieval* ($0.0025/GB)
- Archives unused footage in *Deep Archive* ($0.00099/GB)
- Automates everything via S3 Lifecycle policies
- Retrieves content via CLI when needed for remastering