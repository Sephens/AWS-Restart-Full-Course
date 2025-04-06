# Working with Amazon S3 - Comprehensive Lab Guide

## Table of Contents
- [Working with Amazon S3 - Comprehensive Lab Guide](#working-with-amazon-s3---comprehensive-lab-guide)
  - [Table of Contents](#table-of-contents)
  - [Lab Overview](#lab-overview)
  - [Objectives](#objectives)
  - [Duration](#duration)
  - [Accessing the AWS Management Console](#accessing-the-aws-management-console)
  - [Task 1: Connecting to the CLI Host EC2 Instance](#task-1-connecting-to-the-cli-host-ec2-instance)
    - [Task 1.1: Connecting to CLI Host](#task-11-connecting-to-cli-host)
      - [Step-by-Step Instructions:](#step-by-step-instructions)
    - [Task 1.2: Configuring AWS CLI](#task-12-configuring-aws-cli)
      - [Step-by-Step Instructions:](#step-by-step-instructions-1)
  - [Task 2: Creating and Initializing the S3 Share Bucket](#task-2-creating-and-initializing-the-s3-share-bucket)
      - [Step-by-Step Instructions:](#step-by-step-instructions-2)
  - [Task 3: Reviewing IAM Group and User Permissions](#task-3-reviewing-iam-group-and-user-permissions)
    - [Task 3.1: Reviewing mediaco IAM Group](#task-31-reviewing-mediaco-iam-group)
      - [Step-by-Step Instructions:](#step-by-step-instructions-3)
    - [Task 3.2: Reviewing mediacouser IAM User](#task-32-reviewing-mediacouser-iam-user)
      - [Step-by-Step Instructions:](#step-by-step-instructions-4)
    - [Task 3.3: Testing mediacouser Permissions](#task-33-testing-mediacouser-permissions)
      - [Step-by-Step Instructions:](#step-by-step-instructions-5)
  - [Task 4: Configuring Event Notifications](#task-4-configuring-event-notifications)
    - [Task 4.1: Creating SNS Topic](#task-41-creating-sns-topic)
      - [Step-by-Step Instructions:](#step-by-step-instructions-6)
    - [Task 4.2: Adding Event Notification](#task-42-adding-event-notification)
      - [Step-by-Step Instructions:](#step-by-step-instructions-7)
  - [Task 5: Testing Event Notifications](#task-5-testing-event-notifications)
      - [Step-by-Step Instructions:](#step-by-step-instructions-8)
  - [Conclusion](#conclusion)
  - [Additional Notes and FAQs](#additional-notes-and-faqs)
    - [Best Practices](#best-practices)
    - [Advanced Topics](#advanced-topics)
    - [Frequently Asked Questions](#frequently-asked-questions)

## Lab Overview
This lab demonstrates how to securely configure an S3 bucket for file sharing with external users while monitoring changes through event notifications.

**Key Components**:
- **S3 Bucket**: Stores product images with restricted access
- **mediacouser**: External IAM user with limited permissions
- **SNS Topic**: Sends email notifications for bucket changes

## Objectives
By completing this lab, you will be able to:
1. Create and configure S3 buckets using AWS CLI
2. Implement secure file sharing with IAM permissions
3. Configure S3 event notifications via SNS
4. Test and validate the complete workflow

## Duration
Approximately 90 minutes (timer may vary based on experience level)

## Accessing the AWS Management Console
1. Click **Start Lab** to begin your session
2. Wait for the "Lab status: ready" message
3. Click the **AWS** button to open the console
4. Copy the AccessKey and SecretKey from the Details panel

## Task 1: Connecting to the CLI Host EC2 Instance

### Task 1.1: Connecting to CLI Host

#### Step-by-Step Instructions:
1. Open EC2 Console:
   - Search for "EC2" in AWS console
   - Click "EC2" to open the service

2. Connect to CLI Host:
   - Select "CLI Host" instance
   - Click "Connect"
   - Choose "EC2 Instance Connect"
   - Click "Connect"

**Note**: This opens a terminal in your browser where you'll run AWS CLI commands

### Task 1.2: Configuring AWS CLI

#### Step-by-Step Instructions:
1. Configure AWS CLI:
   ```bash
   aws configure
   ```
   - Enter the AccessKey and SecretKey you copied
   - Region: `us-west-2`
   - Output format: `json`

**Technical Details**:
- AWS CLI stores credentials in `~/.aws/credentials`
- Configuration is stored in `~/.aws/config`
- The json format makes output machine-readable

## Task 2: Creating and Initializing the S3 Share Bucket

#### Step-by-Step Instructions:
1. Create S3 bucket:
   ```bash
   aws s3 mb s3://cafe-xxxnnn --region us-west-2
   ```
   - Replace `xxxnnn` with unique characters/numbers

2. Sync sample images:
   ```bash
   aws s3 sync ~/initial-images/ s3://cafe-xxxnnn/images
   ```

3. Verify upload:
   ```bash
   aws s3 ls s3://cafe-xxxnnn/images/ --human-readable --summarize
   ```

**Technical Details**:
- Bucket names must be globally unique
- The `sync` command efficiently uploads changed files only
- `--human-readable` shows sizes in KB/MB/GB instead of bytes

## Task 3: Reviewing IAM Group and User Permissions

### Task 3.1: Reviewing mediaco IAM Group

#### Step-by-Step Instructions:
1. Open IAM Console:
   - Search for "IAM" in AWS console
   - Click "IAM" to open the service

2. Review mediaco group:
   - Navigate to "User groups"
   - Select "mediaco"
   - Examine "mediaCoPolicy" permissions

**Key Permissions**:
- View bucket lists
- List objects in specific bucket
- Read/write/delete in `images/` prefix only

### Task 3.2: Reviewing mediacouser IAM User

#### Step-by-Step Instructions:
1. Navigate to "Users"
2. Select "mediacouser"
3. Create access key:
   - Security credentials tab
   - "Create access key"
   - Download CSV file
4. Copy console sign-in link

### Task 3.3: Testing mediacouser Permissions

#### Step-by-Step Instructions:
1. Sign in as mediacouser:
   - Use incognito/private browser
   - Paste console sign-in link
   - Username: `mediacouser`
   - Password: `Training1!`

2. Test permissions:
   - View images (should work)
   - Upload new image (should work)
   - Delete image (should work)
   - Modify bucket permissions (should fail)

**Security Principle**:
- Follows principle of least privilege
- User can only modify contents in `images/` prefix
- No bucket configuration permissions

## Task 4: Configuring Event Notifications

### Task 4.1: Creating SNS Topic

#### Step-by-Step Instructions:
1. Open SNS Console:
   - Search for "SNS"
   - Click "Simple Notification Service"

2. Create topic:
   - Name: `s3NotificationTopic`
   - Type: Standard
   - Click "Create topic"

3. Configure access policy:
   ```json
   {
     "Version": "2008-10-17",
     "Id": "S3PublishPolicy",
     "Statement": [
       {
         "Sid": "AllowPublishFromS3",
         "Effect": "Allow",
         "Principal": {
           "Service": "s3.amazonaws.com"
         },
         "Action": "SNS:Publish",
         "Resource": "<ARN>",
         "Condition": {
           "ArnLike": {
             "aws:SourceArn": "arn:aws:s3:*:*:<bucket>"
           }
         }
       }
     ]
   }
   ```

4. Create subscription:
   - Protocol: Email
   - Endpoint: Your email address
   - Confirm subscription via email

### Task 4.2: Adding Event Notification

#### Step-by-Step Instructions:
1. Create notification config:
   ```bash
   vi s3EventNotification.json
   ```
   ```json
   {
     "TopicConfigurations": [
       {
         "TopicArn": "<ARN>",
         "Events": ["s3:ObjectCreated:*","s3:ObjectRemoved:*"],
         "Filter": {
           "Key": {
             "FilterRules": [
               {
                 "Name": "prefix",
                 "Value": "images/"
               }
             ]
           }
         }
       }
     ]
   }
   ```

2. Apply configuration:
   ```bash
   aws s3api put-bucket-notification-configuration \
     --bucket cafe-xxxnnn \
     --notification-configuration file://s3EventNotification.json
   ```

**Technical Details**:
- Notifications are filtered to only `images/` prefix
- Both object creation and deletion events are tracked
- S3 automatically sends a test notification

## Task 5: Testing Event Notifications

#### Step-by-Step Instructions:
1. Configure mediacouser credentials:
   ```bash
   aws configure
   ```
   - Use access keys from downloaded CSV

2. Test upload:
   ```bash
   aws s3api put-object \
     --bucket cafe-xxxnnn \
     --key images/Caramel-Delight.jpg \
     --body ~/new-images/Caramel-Delight.jpg
   ```
   - Verify email notification

3. Test delete:
   ```bash
   aws s3api delete-object \
     --bucket cafe-xxxnnn \
     --key images/Strawberry-Tarts.jpg
   ```
   - Verify email notification

4. Test unauthorized action:
   ```bash
   aws s3api put-object-acl \
     --bucket cafe-xxxnnn \
     --key images/Donuts.jpg \
     --acl public-read
   ```
   - Should fail with AccessDenied

**Notification Details**:
- Notifications include:
  - Event type (create/delete)
  - Object key
  - Timestamp
  - Bucket name

## Conclusion

In this lab you successfully:
1. Created a secure S3 file sharing solution
2. Configured granular IAM permissions
3. Implemented change notifications via SNS
4. Validated the complete workflow

**Key Takeaways**:
- S3 provides robust access control mechanisms
- Event notifications enable real-time monitoring
- IAM policies should follow least privilege principle
- SNS provides flexible notification delivery

## Additional Notes and FAQs

### Best Practices
1. **Bucket Naming**: Use consistent naming conventions
2. **Access Control**: Regularly review IAM permissions
3. **Monitoring**: Set up CloudWatch alarms for notifications
4. **Versioning**: Consider enabling for critical buckets

### Advanced Topics
- **Cross-Account Access**: Share buckets between AWS accounts
- **Lifecycle Policies**: Automate transition to Glacier
- **Replication**: Maintain copies in different regions
- **Presigned URLs**: Temporary access without IAM users

### Frequently Asked Questions

**Q: How can I restrict access to specific IP addresses?**
A: Add an IP condition to the bucket policy using `aws:SourceIp`

**Q: What's the difference between S3 events and SNS notifications?**
A: S3 events can trigger multiple services (SNS, SQS, Lambda) while SNS is specifically for pub/sub messaging

**Q: How do I troubleshoot failed notifications?**
A: Check CloudTrail logs and SNS delivery status metrics

**Q: Can I get notifications for specific file types only?**
A: Yes, add a suffix filter to your notification configuration

**Q: How do I handle large numbers of notifications?**
A: Consider using SQS instead of email for high-volume notifications