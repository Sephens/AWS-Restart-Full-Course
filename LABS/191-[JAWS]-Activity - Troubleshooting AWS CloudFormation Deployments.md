# Troubleshooting CloudFormation - Comprehensive Lab Guide

## Table of Contents
- [Troubleshooting CloudFormation - Comprehensive Lab Guide](#troubleshooting-cloudformation---comprehensive-lab-guide)
  - [Table of Contents](#table-of-contents)
  - [Lab Overview](#lab-overview)
  - [Objectives](#objectives)
  - [Duration](#duration)
  - [Task 1: Querying JSON with JMESPath](#task-1-querying-json-with-jmespath)
    - [Step-by-Step Instructions:](#step-by-step-instructions)
  - [Task 2: Troubleshooting CloudFormation](#task-2-troubleshooting-cloudformation)
    - [Task 2.1: Connect to CLI Host](#task-21-connect-to-cli-host)
      - [Windows Users:](#windows-users)
      - [Mac/Linux Users:](#maclinux-users)
    - [Task 2.2: Configure AWS CLI](#task-22-configure-aws-cli)
    - [Task 2.3: First Stack Creation Attempt](#task-23-first-stack-creation-attempt)
    - [Task 2.4: Prevent Rollback](#task-24-prevent-rollback)
    - [Task 2.5: Fix and Redeploy](#task-25-fix-and-redeploy)
  - [Task 3: Manual Modifications and Drift Detection](#task-3-manual-modifications-and-drift-detection)
    - [Task 3.1: Modify Security Group](#task-31-modify-security-group)
    - [Task 3.2: Add S3 Object](#task-32-add-s3-object)
    - [Task 3.3: Detect Drift](#task-33-detect-drift)
  - [Task 4: Stack Deletion Challenge](#task-4-stack-deletion-challenge)
    - [Initial Attempt](#initial-attempt)
    - [Solution: Retain Resources](#solution-retain-resources)
  - [Conclusion](#conclusion)
  - [Additional Notes and FAQs](#additional-notes-and-faqs)
    - [Best Practices](#best-practices)
    - [Advanced Topics](#advanced-topics)
    - [Frequently Asked Questions](#frequently-asked-questions)

## Lab Overview
This lab focuses on troubleshooting AWS CloudFormation deployments through hands-on exercises that simulate real-world scenarios.

**Key Components**:
- **CLI Host**: EC2 instance for running AWS CLI commands
- **Web Server**: EC2 instance created by CloudFormation
- **VPC and Security Groups**: Network infrastructure
- **S3 Bucket**: Storage resource created by CloudFormation

## Objectives
By completing this lab, you will be able to:
1. Use JMESPath to query JSON data
2. Troubleshoot failed CloudFormation deployments
3. Detect and analyze configuration drift
4. Resolve stack deletion issues

## Duration
Approximately 75 minutes (time may vary based on experience)

## Task 1: Querying JSON with JMESPath

### Step-by-Step Instructions:
1. Visit [jmespath.org](https://jmespath.org/)
2. Replace the default JSON with:
```json
{
  "desserts": [
    {"name": "Chocolate cake", "price": "20.00"},
    {"name": "Ice cream", "price": "15.00"},
    {"name": "Carrot cake", "price": "22.00"}
  ]
}
```
3. Practice queries:
   - `desserts` - Returns all desserts
   - `desserts[1]` - Returns second dessert
   - `desserts[0].name` - Returns "Chocolate cake"
   - `desserts[?name=='Carrot cake']` - Filters by name

**Technical Details**:
- JMESPath is a query language for JSON
- Used in AWS CLI with `--query` parameter
- Supports filtering, projections, and functions

## Task 2: Troubleshooting CloudFormation

### Task 2.1: Connect to CLI Host

#### Windows Users:
1. Download PPK file from lab credentials
2. Use PuTTY to connect to PublicIP
3. Login as `ec2-user`

#### Mac/Linux Users:
1. Download PEM file
2. Set permissions: `chmod 400 labsuser.pem`
3. Connect: `ssh -i labsuser.pem ec2-user@<PublicIP>`

### Task 2.2: Configure AWS CLI
```bash
aws configure
```
- Enter AccessKey and SecretKey from lab credentials
- Region: `us-west-2` (or your lab region)
- Output format: `json`

### Task 2.3: First Stack Creation Attempt
1. View template:
```bash
less template1.yaml
```
2. Create stack:
```bash
aws cloudformation create-stack \
  --stack-name myStack \
  --template-body file://template1.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameters ParameterKey=KeyName,ParameterValue=vockey
```
3. Monitor status:
```bash
watch -n 5 -d aws cloudformation describe-stack-resources \
  --stack-name myStack \
  --query 'StackResources[*].[ResourceType,ResourceStatus]' \
  --output table
```
4. Identify failure:
```bash
aws cloudformation describe-stack-events \
  --stack-name myStack \
  --query "StackEvents[?ResourceStatus == 'CREATE_FAILED']"
```
**Root Cause**: WaitCondition timeout due to "http" package not found in userdata script

### Task 2.4: Prevent Rollback
```bash
aws cloudformation create-stack \
  --stack-name myStack \
  --template-body file://template1.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --on-failure DO_NOTHING \
  --parameters ParameterKey=KeyName,ParameterValue=vockey
```
**Key Difference**: `--on-failure DO_NOTHING` prevents automatic rollback

### Task 2.5: Fix and Redeploy
1. Edit template:
```bash
vim template1.yaml
```
- Change `http` to `httpd` in UserData section
2. Delete failed stack:
```bash
aws cloudformation delete-stack --stack-name myStack
```
3. Create fixed stack:
```bash
aws cloudformation create-stack \
  --stack-name myStack \
  --template-body file://template1.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --on-failure DO_NOTHING \
  --parameters ParameterKey=KeyName,ParameterValue=vockey
```
4. Verify web server:
- Get public IP from stack outputs
- Access in browser to see "Hello from your web server!"

## Task 3: Manual Modifications and Drift Detection

### Task 3.1: Modify Security Group
1. In AWS Console:
   - Navigate to EC2 > Instances
   - Select "Web Server"
   - Security tab > "WebServerSG"
   - Edit inbound rules
   - Change SSH source from 0.0.0.0/0 to "My IP"

### Task 3.2: Add S3 Object
```bash
bucketName=$(aws cloudformation describe-stacks \
  --stack-name myStack \
  --query "Stacks[*].Outputs[?OutputKey == 'BucketName'].[OutputValue]" \
  --output text)
touch myfile
aws s3 cp myfile s3://$bucketName/
```

### Task 3.3: Detect Drift
1. Initiate detection:
```bash
aws cloudformation detect-stack-drift --stack-name myStack
```
2. Check status:
```bash
aws cloudformation describe-stack-drift-detection-status \
  --stack-drift-detection-id <detection-id>
```
3. View drifted resources:
```bash
aws cloudformation describe-stack-resource-drifts \
  --stack-name myStack \
  --stack-resource-drift-status-filters MODIFIED
```
**Expected Result**: Security group shows as MODIFIED due to manual change

## Task 4: Stack Deletion Challenge

### Initial Attempt
```bash
aws cloudformation delete-stack --stack-name myStack
```
**Failure Reason**: S3 bucket contains objects and cannot be deleted

### Solution: Retain Resources
1. Get bucket logical ID:
```bash
aws cloudformation describe-stack-resources \
  --stack-name myStack \
  --query "StackResources[?ResourceType=='AWS::S3::Bucket'].LogicalResourceId" \
  --output text
```
2. Delete stack while retaining bucket:
```bash
aws cloudformation delete-stack \
  --stack-name myStack \
  --retain-resources MyBucket
```
**Key Parameter**: `--retain-resources` specifies resources to keep

## Conclusion

In this lab you successfully:
1. Practiced JMESPath queries
2. Troubleshot a failed CloudFormation deployment
3. Detected and analyzed configuration drift
4. Resolved stack deletion issues while retaining resources

**Key Takeaways**:
- CloudFormation provides infrastructure as code capabilities
- Detailed logging is essential for troubleshooting
- Drift detection helps identify manual changes
- Resource retention prevents accidental data loss

## Additional Notes and FAQs

### Best Practices
1. **Templates**: Use version control for CloudFormation templates
2. **Changes**: Always modify infrastructure through templates
3. **Testing**: Implement CI/CD pipelines for stack updates
4. **Monitoring**: Set up alerts for stack events and drift

### Advanced Topics
- **Nested Stacks**: Break complex templates into modular components
- **Custom Resources**: Extend functionality with Lambda
- **Change Sets**: Preview changes before execution
- **Stack Policies**: Control update behaviors

### Frequently Asked Questions

**Q: How can I prevent manual changes to CloudFormation resources?**
A: Use IAM policies to restrict direct access to resources managed by CloudFormation

**Q: What's the difference between DO_NOTHING and ROLLBACK?**
A: DO_NOTHING leaves failed resources for inspection while ROLLBACK attempts to delete them

**Q: How often should I check for drift?**
A: For production environments, consider weekly checks or event-based triggers

**Q: Can I recover a deleted stack?**
A: No, but you can recreate it from the original template if you have it

**Q: What happens to retained resources after stack deletion?**
A: They remain in your account but are no longer managed by CloudFormation