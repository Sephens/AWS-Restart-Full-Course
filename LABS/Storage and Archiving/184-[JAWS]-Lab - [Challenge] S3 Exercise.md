# Amazon S3 Challenge Lab - Comprehensive Guide

## Table of Contents
1. [Lab Overview](#lab-overview)
2. [Objectives](#objectives)
3. [Duration](#duration)
4. [Accessing the AWS Management Console](#accessing-the-aws-management-console)
5. [Task 1: Connecting to the CLI Host Instance](#task-1-connecting-to-the-cli-host-instance)
6. [Task 2: Configuring the AWS CLI](#task-2-configuring-the-aws-cli)
7. [Task 3: Challenge Tasks](#task-3-challenge-tasks)
8. [Conclusion](#conclusion)
9. [Additional Notes and FAQs](#additional-notes-and-faqs)

## Lab Overview
This challenge lab tests your ability to work with Amazon S3 by completing a series of practical tasks including bucket creation, object uploads, permission management, and CLI operations.

**Key Components**:
- **S3 Bucket**: Storage container for your objects
- **CLI Host**: EC2 instance for running AWS CLI commands
- **Public Access**: Configuring objects for web access

## Objectives
By completing this challenge, you will demonstrate ability to:
1. Create and configure S3 buckets
2. Upload and manage objects
3. Configure public access permissions
4. Use AWS CLI for S3 operations

## Duration
Approximately 45 minutes (time may vary based on experience)

## Accessing the AWS Management Console
1. Click **Start Lab** to begin your session
2. Wait for the "Lab status: ready" message
3. Click the **AWS** button to open the console
4. Copy these values from the Details panel:
   - SecretKey
   - PublicIP (of your Linux instance)
   - AccessKey

## Task 1: Connecting to the CLI Host Instance

### Step-by-Step Instructions:
1. Open EC2 Console:
   - Search for "EC2" in AWS console
   - Click "EC2" to open the service

2. Connect to CLI Host:
   - Select "CLI Host" instance
   - Click "Connect"
   - Choose "EC2 Instance Connect"
   - Click "Connect"

**Note**: This opens a terminal in your browser where you'll run AWS CLI commands

## Task 2: Configuring the AWS CLI

### Step-by-Step Instructions:
1. Configure AWS CLI:
   ```bash
   aws configure
   ```
   - AWS Access Key ID: Paste your AccessKey
   - AWS Secret Access Key: Paste your SecretKey
   - Default region name: `us-west-2`
   - Default output format: `json`

**Verification**:
```bash
aws sts get-caller-identity
```
Should return your IAM user details

## Task 3: Challenge Tasks

### 1. Create an S3 Bucket

#### Solution:
```bash
aws s3 mb s3://my-unique-bucket-name-123 --region us-west-2
```
**Notes**:
- Bucket names must be globally unique
- Avoid using personal info in bucket names
- Region should match your lab region (us-west-2)

### 2. Upload an Object

#### Solution:
1. First create a test file:
```bash
echo "This is my test object" > testfile.txt
```

2. Upload to S3:
```bash
aws s3 cp testfile.txt s3://my-unique-bucket-name-123/
```

**Verification**:
```bash
aws s3 ls s3://my-unique-bucket-name-123/
```

### 3. Attempt Browser Access (Should Fail)

#### Solution:
1. Construct URL:
   ```
   http://my-unique-bucket-name-123.s3.us-west-2.amazonaws.com/testfile.txt
   ```
2. Attempt access - should get Access Denied

### 4. Make Object Publicly Accessible

#### Solution:
```bash
aws s3api put-object-acl \
  --bucket my-unique-bucket-name-123 \
  --key testfile.txt \
  --acl public-read
```

**Alternative Method** (via bucket policy):
```bash
cat > policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-unique-bucket-name-123/testfile.txt"
    }
  ]
}
EOF

aws s3api put-bucket-policy \
  --bucket my-unique-bucket-name-123 \
  --policy file://policy.json
```

### 5. Verify Browser Access (Should Work)

#### Solution:
1. Refresh browser with same URL
2. Should now see file contents

### 6. List Bucket Contents via CLI

#### Solution:
```bash
aws s3 ls s3://my-unique-bucket-name-123/
```

**Enhanced Listing**:
```bash
aws s3api list-objects-v2 --bucket my-unique-bucket-name-123
```

## Conclusion

You've successfully completed the challenge by:
1. Creating an S3 bucket
2. Uploading an object
3. Configuring public access
4. Verifying access through browser
5. Listing contents via CLI

**Key Takeaways**:
- S3 provides highly available object storage
- Permissions can be set at bucket or object level
- CLI offers powerful management capabilities
- Public access requires explicit configuration

## Additional Notes and FAQs

### Best Practices
1. **Naming Conventions**: Use consistent, meaningful bucket names
2. **Access Control**: Prefer IAM policies over bucket policies for AWS users
3. **Public Access**: Only make objects public when absolutely necessary
4. **Monitoring**: Enable access logging for security auditing

### Advanced Topics
- **Versioning**: Protect against accidental deletions
- **Lifecycle Policies**: Automate transition to cheaper storage classes
- **Encryption**: Enable server-side encryption for sensitive data
- **Static Website Hosting**: Configure S3 to host static websites

### Frequently Asked Questions

**Q: Why did my first browser access fail?**
A: S3 objects are private by default. You must explicitly grant public access.

**Q: What's the difference between --acl and bucket policy?**
A: ACLs are simpler but less flexible. Policies allow more granular control.

**Q: How do I delete the bucket when finished?**
A: First empty the bucket, then run:
```bash
aws s3 rb s3://my-unique-bucket-name-123 --force
```

**Q: Can I make the entire bucket public?**
A: Yes, but this is strongly discouraged for security reasons.

**Q: How do I upload an entire folder?**
A: Use `aws s3 sync local_folder s3://bucket-name/`

**Q: What if my bucket name isn't available?**
A: Try adding numbers or different prefixes/suffixes to make it unique.