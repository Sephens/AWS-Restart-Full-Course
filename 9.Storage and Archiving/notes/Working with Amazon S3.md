# Working with Amazon S3 - Comprehensive Lab Guide

## Table of Contents
- [Working with Amazon S3 - Comprehensive Lab Guide](#working-with-amazon-s3---comprehensive-lab-guide)
  - [Table of Contents](#table-of-contents)
  - [Business Scenario](#business-scenario)
  - [Technical Requirements](#technical-requirements)
    - [Core Components:](#core-components)
  - [Lab Tasks Overview](#lab-tasks-overview)
    - [Task 1: S3 Bucket Setup](#task-1-s3-bucket-setup)
    - [Task 2: Permission Verification](#task-2-permission-verification)
    - [Task 3: Event Notifications](#task-3-event-notifications)
  - [Architecture](#architecture)
    - [Component Diagram:](#component-diagram)
  - [Implementation Steps](#implementation-steps)
    - [1. Create S3 Bucket](#1-create-s3-bucket)
    - [2. Configure IAM Permissions](#2-configure-iam-permissions)
    - [3. Set Up Notifications](#3-set-up-notifications)
  - [Checkpoint Questions \& Answers](#checkpoint-questions--answers)
  - [Key Takeaways](#key-takeaways)

---

## Business Scenario

**Situation**: 
- Café is expanding product catalog
- External media company creating product images
- Need secure file sharing solution with notification system

**Requirements**:
- Centralized storage for large image files
- Email notifications on upload
- Secure access for external partner
- Review workflow before website deployment

**Solution Components**:
- Amazon S3 for file storage
- IAM for access control
- SNS for notifications

**Example Flow**:
1. Media company uploads images to S3
2. S3 triggers SNS notification
3. Café team reviews images
4. Approved images deployed to website

---

## Technical Requirements

### Core Components:
1. **EC2 Instance Connect**:
   - Secure CLI access point
   - AWS CLI configuration

2. **S3 Bucket**:
   - Dedicated bucket for media files
   - Proper permissions structure

3. **IAM Permissions**:
   - `mediaco` user group
   - Fine-grained bucket access

4. **SNS Notifications**:
   - Bucket event triggers
   - Email subscription

**Implementation Example**:
```bash
# Create S3 bucket
aws s3api create-bucket --bucket café-media-uploads --region us-west-2

# Configure notification
aws s3api put-bucket-notification-configuration \
  --bucket café-media-uploads \
  --notification-configuration file://notification.json
```

---

## Lab Tasks Overview

### Task 1: S3 Bucket Setup
- Create bucket using AWS CLI
- Configure bucket policies
- Set lifecycle rules (if needed)

### Task 2: Permission Verification
- Test IAM user access
- Validate write permissions
- Restrict public access

### Task 3: Event Notifications
- Create SNS topic
- Configure bucket events
- Test notification flow

**Detailed Example**:
```bash
# Verify permissions
aws s3api put-object --bucket café-media-uploads --key test.txt --body test.txt

# Create SNS topic
aws sns create-topic --name s3-upload-notifications
```

---

## Architecture

### Component Diagram:
```
AWS Cloud (us-west-2)
├── VPC
│   └── CLI Host (EC2 Instance)
│       ├── EC2 Instance Connect
│       └── AWS CLI Configuration
│
└── S3 Bucket (café-media-uploads)
    ├── IAM Policies
    │   └── mediaco User Group
    └── SNS Topic (s3NotificationTopic)
        └── Email Subscriptions
```

**Data Flow**:
1. Media company → S3 Upload
2. S3 → SNS Notification
3. SNS → Email to Café team

---

## Implementation Steps

### 1. Create S3 Bucket
```bash
aws s3api create-bucket \
  --bucket café-media-uploads \
  --region us-west-2 \
  --create-bucket-configuration LocationConstraint=us-west-2
```

**Best Practices**:
- Enable versioning
- Configure encryption
- Set lifecycle policies

### 2. Configure IAM Permissions
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowListBuckets",
      "Effect": "Allow",
      "Action": ["s3:ListAllMyBuckets"],
      "Resource": "*"
    },
    {
      "Sid": "AllowMediaUploads",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::café-media-uploads/*"
    }
  ]
}
```

### 3. Set Up Notifications
```bash
# Create SNS topic
aws sns create-topic --name s3-upload-notifications

# Add email subscription
aws sns subscribe \
  --topic-arn arn:aws:sns:us-west-2:123456789012:s3-upload-notifications \
  --protocol email \
  --notification-endpoint admin@cafe.example.com

# Configure bucket notifications
aws s3api put-bucket-notification-configuration \
  --bucket café-media-uploads \
  --notification-configuration '{
    "TopicConfigurations": [{
      "TopicArn": "arn:aws:sns:us-west-2:123456789012:s3-upload-notifications",
      "Events": ["s3:ObjectCreated:*"]
    }]
  }'
```

---

## Checkpoint Questions & Answers

1. **What are two benefits of using Amazon S3 to share files?**
   - **Answer**:
     1. **Scalability**: Automatically handles large files and high request volumes
     2. **Security**: Fine-grained access control through IAM policies and bucket policies

2. **Which AWS CLI command creates an S3 bucket?**
   - **Answer**:
     ```bash
     aws s3api create-bucket --bucket my-bucket --region us-west-2
     ```

3. **For IAM user group permissions, which SID key name defines permissions that allow the user to use the Amazon S3 console to view the list of S3 buckets in the account?**
   - **Answer**: `AllowListBuckets` (typically includes `s3:ListAllMyBuckets` permission)

4. **Which Amazon SNS resource sends an email notification to its subscribed users?**
   - **Answer**: An **SNS Topic** with email subscriptions configured

---

## Key Takeaways

1. **Secure File Sharing**: S3 provides robust access controls for external collaboration
2. **Automated Workflows**: Event notifications enable real-time processing
3. **CLI Management**: AWS CLI offers powerful bucket management capabilities
4. **Cost-Effective**: Only pay for storage used and requests made
5. **Integration**: Seamless connection with other AWS services (SNS, IAM)

**Final Implementation**:
- Bucket name: `café-media-uploads`
- IAM group: `mediaco` with write permissions
- SNS topic: `s3-upload-notifications`
- Notification: Triggers on all object creations
- Lifecycle: Transition older versions to S3-IA after 30 days