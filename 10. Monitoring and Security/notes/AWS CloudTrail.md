# AWS CloudTrail - Comprehensive Guide

## Table of Contents
1. [Introduction to CloudTrail](#introduction-to-cloudtrail)
2. [Key Features](#key-features)
3. [CloudTrail Log Structure](#cloudtrail-log-structure)
4. [Configuration Steps](#configuration-steps)
5. [Security Monitoring](#security-monitoring)
6. [Key Takeaways](#key-takeaways)

---

## Introduction to CloudTrail

**Definition**: AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of AWS accounts by logging API activity across AWS infrastructure.

**Core Capabilities**:
- Records API calls for most AWS services
- Captures console, CLI, and SDK activity
- Delivers logs to S3 for long-term retention
- Supports integration with CloudWatch Logs

**Example Use Case**:
```mermaid
graph LR
    A[API Call] --> B[CloudTrail]
    B --> C[S3 Bucket]
    B --> D[CloudWatch Logs]
    D --> E[Alarms]
```

---

## Key Features

### 1. Comprehensive Logging
- **Management Events**: Operations performed on resources (create, modify, delete)
- **Data Events**: Resource operations (S3 object-level, Lambda execution)
- **Read/Write Tracking**: Distinguishes between read-only and modifying actions

### 2. Multi-Region Support
```bash
# Enable multi-region trail
aws cloudtrail create-trail \
  --name MyTrail \
  --s3-bucket-name my-cloudtrail-logs \
  --is-multi-region-trail
```

### 3. Security Enhancements
- Log file integrity validation
- Encryption with AWS KMS
- IAM-based access control

**Limitations**:
- Doesn't track OS-level activities within EC2 instances
- 90-day visibility for event history without trail configuration

---

## CloudTrail Log Structure

### Sample Log Entry Components:
```json
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE",
    "arn": "arn:aws:iam::123456789012:user/Alice",
    "accountId": "123456789012",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "userName": "Alice"
  },
  "eventTime": "2023-11-14T19:15:45Z",
  "eventSource": "ec2.amazonaws.com",
  "eventName": "RunInstances",
  "requestParameters": {
    "instanceType": "t2.micro",
    "imageId": "ami-0abcdef1234567890"
  },
  "responseElements": {
    "instancesSet": {
      "items": [
        {
          "instanceId": "i-1234567890abcdef0",
          "imageId": "ami-0abcdef1234567890"
        }
      ]
    }
  }
}
```

### Critical Fields:
| Field | Description | Example |
|-------|-------------|---------|
| `userIdentity` | Who performed the action | IAM user/role |
| `eventSource` | Which service was called | `s3.amazonaws.com` |
| `eventName` | Specific API operation | `PutObject` |
| `requestParameters` | Detailed request data | Instance type, AMI ID |
| `responseElements` | API response details | Created resource IDs |

---

## Configuration Steps

### 1. Create S3 Bucket
```bash
aws s3api create-bucket \
  --bucket my-cloudtrail-logs \
  --region us-east-1 \
  --create-bucket-configuration LocationConstraint=us-east-1
```

### 2. Set Up Trail
```bash
aws cloudtrail create-trail \
  --name SecurityAuditTrail \
  --s3-bucket-name my-cloudtrail-logs \
  --include-global-service-events \
  --is-multi-region-trail \
  --enable-log-file-validation
```

### 3. Configure Notifications
```bash
aws sns create-topic --name CloudTrail-Alerts
aws cloudtrail update-trail \
  --name SecurityAuditTrail \
  --sns-topic-name CloudTrail-Alerts
```

### 4. Enable CloudWatch Logs Integration
```bash
aws cloudtrail update-trail \
  --name SecurityAuditTrail \
  --cloud-watch-logs-log-group-arn arn:aws:logs:us-east-1:123456789012:log-group:CloudTrail/DefaultLogGroup:* \
  --cloud-watch-logs-role-arn arn:aws:iam::123456789012:role/CloudTrail_CloudWatchLogs_Role
```

**Best Practices**:
- Enable multi-region trails for comprehensive auditing
- Use separate S3 buckets for production/non-production
- Enable log file validation for integrity checking

---

## Security Monitoring

### Common Security Use Cases:

1. **Unauthorized Access Detection**
   ```sql
   # CloudWatch Logs Insights Query
   filter eventName = "ConsoleLogin" and errorMessage like /Failed/
   | stats count(*) by userIdentity.arn, sourceIPAddress
   | sort count(*) desc
   ```

2. **Resource Configuration Changes**
   ```bash
   # Find recent security group modifications
   aws cloudtrail lookup-events \
     --lookup-attributes AttributeKey=EventName,AttributeValue=AuthorizeSecurityGroupIngress \
     --start-time "2023-11-01T00:00:00Z" \
     --end-time "2023-11-15T00:00:00Z"
   ```

3. **Suspicious API Patterns**
   ```sql
   # Detect unusual instance launches
   filter eventName = "RunInstances" 
   | stats count(*) by userIdentity.arn, requestParameters.instanceType
   | sort count(*) desc
   ```

**Alerting Example**:
```bash
aws cloudwatch put-metric-alarm \
  --alarm-name "MultipleFailedLogins" \
  --metric-name "FailedConsoleLogins" \
  --namespace "CloudTrailMetrics" \
  --statistic Sum \
  --period 300 \
  --threshold 5 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 1 \
  --alarm-actions "arn:aws:sns:us-east-1:123456789012:Security-Alerts"
```

---

## Key Takeaways

1. **Compliance Foundation**:
   - Meets requirements for SOC, PCI DSS, HIPAA
   - Provides immutable audit trail

2. **Forensic Capabilities**:
   - Answers "who did what, when, and from where"
   - Tracks changes across all AWS services

3. **Integration Ecosystem**:
   - Works with SIEM tools (Splunk, Sumo Logic)
   - Feeds into AWS Security Hub

4. **Operational Visibility**:
   - Identifies misconfigurations
   - Tracks root causes of issues

**Implementation Checklist**:
- [ ] Enable organization-wide trails
- [ ] Configure log file validation
- [ ] Set up CloudWatch Logs integration
- [ ] Create security-focused metric filters
- [ ] Establish log retention policies (S3 lifecycle rules)

**Final Note**: CloudTrail forms the backbone of AWS security monitoring, processing over 100 million API events per second globally. Regular review of CloudTrail findings should be part of all security operations center (SOC) workflows.