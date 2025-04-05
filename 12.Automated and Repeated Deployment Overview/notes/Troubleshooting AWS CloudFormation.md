---
title: "Troubleshooting AWS CloudFormation"
author: "Steven Odhiambo"
company: "RiseTechnon Inc."
copyright: "© 2025 RiseTechnon Inc. All rights reserved."
license: "Proprietary"
version: "1.2"
date: "2025-04-02"
repo: "github.com/open-cloud/aws-re/start"
contribute: "Contributions welcome via pull requests"
disclaimer: "This document contains proprietary techniques of RiseTechnon Inc. Unauthorized distribution prohibited."
---
# Troubleshooting AWS CloudFormation - Comprehensive Guide

## Overview
This guide provides detailed troubleshooting techniques for common AWS CloudFormation issues, including template errors, resource creation failures, WaitCondition problems, and log analysis methods.

## Common Error Categories

### 1. Template Validation Errors
**Symptoms**: Stack creation fails immediately with validation errors

**Common Causes**:
- Invalid JSON/YAML syntax
- Missing required properties
- Incorrect resource types
- Invalid parameter values

**Troubleshooting Steps**:
1. **Validate template**:
   ```bash
   aws cloudformation validate-template --template-body file://template.yaml
   ```
2. Check for:
   - Matching braces/brackets in JSON
   - Correct indentation in YAML
   - Valid resource property combinations

**Example**: Fixing a malformed template
```yaml
# Before (error - missing colon)
Resources:
  MyBucket
    Type: AWS::S3::Bucket

# After (fixed)
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
```

### 2. S3 Template URL Issues
**Error Message**: "TemplateURL must reference a valid S3 bucket"

**Solutions**:
1. Verify bucket exists:
   ```bash
   aws s3 ls s3://my-bucket-name
   ```
2. Check permissions:
   - Bucket policy allows read access
   - IAM user has `s3:GetObject` permission
3. Ensure URL format is correct:
   ```
   https://s3.amazonaws.com/mybucket/my-template.yaml
   ```

**Best Practice**: Use versioned S3 objects for templates in production:
```bash
aws s3 cp template.yaml s3://my-bucket/templates/v1.0.0/template.yaml
```

### 3. Resource Creation Failures

#### A. IAM Permission Issues
**Symptoms**: "API: iam:CreateRole User is not authorized"

**Solution**:
1. Verify IAM permissions for CloudFormation:
   - `cloudformation:*` actions
   - Permissions for resources being created
2. Use a CloudFormation service role with sufficient privileges

**Example IAM Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:*",
        "s3:*"
      ],
      "Resource": "*"
    }
  ]
}
```

#### B. Service Limit Exceeded
**Symptoms**: "LimitExceededException"

**Solutions**:
1. Check current limits:
   ```bash
   aws service-quota list-service-quotas --service-code ec2
   ```
2. Request limit increases via AWS Support
3. Implement staggered creation for large deployments

#### C. Resource-Specific Configuration
**Example EC2 Instance Error**:
- Missing required properties (ImageId, InstanceType)
- Invalid AMI for region
- Insufficient instance capacity in AZ

**Troubleshooting**:
1. Compare with working templates
2. Consult AWS documentation for required properties
3. Use AWS::EC2::Image::Id parameter type for AMIs

### 4. WaitCondition Failures
**Symptoms**: Stack stuck in CREATE_IN_PROGRESS, then fails with WaitCondition timeout

**Debugging Process**:
1. **Preserve instance**:
   ```bash
   aws cloudformation create-stack --stack-name my-stack \
     --template-body file://template.yaml \
     --on-failure DO_NOTHING
   ```
2. **Check logs**:
   - Linux: `/var/log/cfn-init.log`, `/var/log/cloud-init-output.log`
   - Windows: `C:\cfn\log\cfn-init.log`
3. **Common Issues**:
   - Invalid cfn-signal command
   - Scripts failing with non-zero exit codes
   - Network connectivity problems

**Example Fix**:
```bash
#!/bin/bash
# Before (missing proper signal)
yum install -y httpd

# After (proper signal)
yum install -y httpd
if [ $? -eq 0 ]; then
  /opt/aws/bin/cfn-signal -e 0 --stack ${AWS::StackName} \
    --resource WebServerWaitHandle --region ${AWS::Region}
else
  /opt/aws/bin/cfn-signal -e 1 --stack ${AWS::StackName} \
    --resource WebServerWaitHandle --region ${AWS::Region}
  exit 1
fi
```

### 5. Update Failures
**Symptoms**: Stack update fails, stuck in UPDATE_ROLLBACK_FAILED state

**Resolution Options**:
1. **Continue rollback**:
   ```bash
   aws cloudformation continue-update-rollback --stack-name my-stack
   ```
2. **Skip resources**:
   ```bash
   aws cloudformation continue-update-rollback --stack-name my-stack \
     --resources-to-skip LogicalResourceId1 LogicalResourceId2
   ```
3. **Manual intervention**:
   - Fix resource outside CloudFormation
   - Protect resources with DeletionPolicy: Retain

## Log Analysis Techniques

### CloudFormation Event Logs
1. View in AWS Console:
   - CloudFormation → Stacks → Events tab
2. Filter for failed events
3. Examine "Status Reason" messages

### EC2 Instance Logs
**Access Methods**:
1. **Direct access**:
   ```bash
  ssh -i key.pem ec2-user@public-ip
  sudo tail -f /var/log/cfn-init.log
  ```
2. **Systems Manager Session Manager** (no SSH needed)
3. **CloudWatch Logs** (configure in template):
```yaml
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Metadata:
      AWS::CloudFormation::Init:
        config:
          files:
            "/etc/awslogs/awslogs.conf":
              content: !Sub |
                [general]
                state_file = /var/lib/awslogs/agent-state
                
                [/var/log/cfn-init.log]
                file = /var/log/cfn-init.log
                log_group_name = /aws/cloudformation/${AWS::StackName}
                log_stream_name = {instance_id}/cfn-init.log
```

## Advanced Troubleshooting Scenarios

### 1. Circular Dependencies
**Symptoms**: "Circular dependency between resources"

**Solution**:
1. Identify dependency chain (A→B→C→A)
2. Restructure using:
   - AWS::CloudFormation::WaitCondition
   - Fn::GetAtt instead of explicit DependsOn
   - Custom Resources to break cycles

### 2. Drift Detection
**Symptoms**: Unexpected behavior after manual resource changes

**Resolution**:
1. Detect drift:
   ```bash
   aws cloudformation detect-stack-drift --stack-name my-stack
   ```
2. View drift results:
   ```bash
   aws cloudformation describe-stack-resource-drifts --stack-name my-stack
   ```
3. Remediate by:
   - Updating stack to match template
   - Importing changed resources
   - Documenting exceptions

### 3. Nested Stack Failures
**Symptoms**: Parent stack fails due to child stack error

**Debugging**:
1. Check nested stack events separately
2. Examine outputs from child stacks
3. Use detailed logging in nested templates

## Best Practices for Prevention

### 1. Development Practices
- **Use change sets** before updates:
  ```bash
  aws cloudformation create-change-set --stack-name my-stack \
    --template-body file://template.yaml --change-set-name my-change
  ```
- **Implement CI/CD** for templates
- **Validate templates** in pipeline:
  ```bash
  aws cloudformation validate-template --template-body file://template.yaml
  ```

### 2. Monitoring and Alerting
- Configure CloudWatch Alarms for stack events
- Use AWS Config to monitor compliance
- Implement SNS notifications for stack failures

### 3. Template Design
- **Modularize** with nested stacks
- **Parameterize** all environment-specific values
- **Validate inputs** with constraints:
```yaml
Parameters:
  InstanceType:
    Type: String
    AllowedValues: [t2.micro, t2.small, t2.medium]
    ConstraintDescription: Must be a valid EC2 instance type
```

## FAQ Section

**Q: How do I troubleshoot a stack stuck in DELETE_FAILED state?**
A: 
1. Identify which resource failed to delete
2. Check IAM permissions for deletion
3. Manually delete the resource if safe
4. Retry stack deletion with:
   ```bash
   aws cloudformation delete-stack --stack-name my-stack
   ```

**Q: Why does my stack fail randomly in different regions?**
A: Common causes:
- Region-specific service availability
- Different AMI IDs per region (use Mappings)
- Varying service limits across regions

**Q: How can I debug Lambda functions in CloudFormation?**
A: 
1. Check CloudWatch Logs for the Lambda function
2. Implement detailed logging in function code
3. Use test events before stack deployment

**Q: What's the best way to handle sensitive data in templates?**
A: 
1. Use AWS Systems Manager Parameter Store:
   ```yaml
   Parameters:
     DBPassword:
       Type: AWS::SSM::Parameter::Value<SecureString>
       Default: /myapp/db/password
   ```
2. Never store secrets in template or parameter files

## Conclusion

Effective troubleshooting of AWS CloudFormation requires:
1. **Systematic approach**: Start with event logs, then instance logs
2. **Deep AWS knowledge**: Understand service limits and IAM
3. **Defensive design**: Implement validation and monitoring
4. **Proper tools**: Use AWS CLI, CloudWatch, and Systems Manager

By following these practices and utilizing the techniques outlined in this guide, you can significantly reduce resolution time for CloudFormation issues and build more reliable infrastructure deployments.