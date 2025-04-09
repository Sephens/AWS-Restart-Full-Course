# **Comprehensive Lab Guide: Building a Serverless Sales Reporting System with AWS Lambda**

## **Lab Overview and Objectives**
This lab provides hands-on experience creating a complete serverless architecture for generating and distributing daily sales reports. You'll learn to:

- Configure IAM roles with least-privilege permissions
- Create Lambda layers for shared dependencies
- Develop Lambda functions that interact with databases
- Implement scheduled executions with CloudWatch Events
- Distribute reports via SNS email notifications
- Troubleshoot using CloudWatch Logs

## **Detailed Task Walkthrough**

### **Task 1: IAM Role Configuration**
#### **1.1 salesAnalysisReportRole Analysis**
- **Trust Relationship**: Allows Lambda service to assume the role
- **Critical Policies**:
  - `AmazonSNSFullAccess`: Enables report distribution
  - `AmazonSSMReadOnlyAccess`: Reads database credentials from Parameter Store
  - `AWSLambdaBasicRunRole`: Standard logging permissions
  - `AWSLambdaRole`: Permissions to invoke other Lambda functions

#### **1.2 salesAnalysisReportDERole Analysis**
- **Trust Relationship**: Lambda service trust
- **Essential Permissions**:
  - Basic execution role for logging
  - VPC access role for database connectivity

**Best Practice**: Always review IAM policies before attaching them to functions.

### **Task 2: Lambda Layer and Data Extractor Setup**
#### **2.1 Creating the PyMySQL Layer**
1. Navigate to Lambda > Layers
2. Upload `pymysql-v3.zip` with proper Python package structure
3. Configure for Python 3.9 compatibility

#### **2.2 Building the Data Extractor Function**
1. **Basic Configuration**:
   - Runtime: Python 3.9
   - Existing role: `salesAnalysisReportDERole`
   - Timeout: Increase to 1 minute (default 3 seconds often insufficient)

2. **Layer Attachment**:
   - Select the created `pymysqlLibrary`
   - Verify layer appears in function configuration

3. **Network Configuration**:
   - VPC: `Cafe VPC`
   - Subnet: `Cafe Public Subnet 1`
   - Security Group: `CafeSecurityGroup` (confirm MySQL port 3306 access)

**Troubleshooting Tip**: If function times out, check:
- Security group inbound rules
- Database accessibility from the subnet
- CloudWatch logs for connection errors

### **Task 3: Testing the Data Pipeline**
#### **3.1 Initial Test Execution**
```json
{
  "dbUrl": "cafe-db.example.com",
  "dbName": "cafe_db",
  "dbUser": "report_user",
  "dbPassword": "securepassword123"
}
```

#### **3.2 Generating Test Data**
1. Access the café web interface at `http://<CafePublicIP>/cafe`
2. Place several test orders for different menu items
3. Verify orders appear in database before retesting

**Expected Output**:
```json
{
  "statusCode": 200,
  "body": [
    {
      "product_group_number": 1,
      "product_name": "Croissant",
      "quantity": 2
    }
  ]
}
```

### **Task 4: Notification System Setup**
#### **4.1 SNS Topic Creation**
1. Standard topic type
2. Name: `salesAnalysisReportTopic`
3. Display name: `SARTopic` (appears in email sender)

#### **4.2 Email Subscription**
1. Protocol: Email
2. Endpoint: Your verified email address
3. Confirm subscription via confirmation email

**Pro Tip**: Use AWS SES for production email delivery.

### **Task 5: Main Report Function Deployment**
#### **5.1 CLI Deployment**
```bash
aws lambda create-function \
  --function-name salesAnalysisReport \
  --runtime python3.9 \
  --zip-file fileb://salesAnalysisReport-v2.zip \
  --handler salesAnalysisReport.lambda_handler \
  --role arn:aws:iam::123456789012:role/salesAnalysisReportRole \
  --timeout 60 \
  --region us-west-2
```

#### **5.2 Environment Configuration**
- Key: `topicARN`
- Value: `arn:aws:sns:us-west-2:123456789012:salesAnalysisReportTopic`

#### **5.3 Scheduled Execution**
1. Trigger type: EventBridge (CloudWatch Events)
2. Rule type: Schedule expression
3. Cron expression: `cron(0 20 ? * MON-SAT *)` (8 PM UTC, Mon-Sat)
4. Test with immediate execution: `cron(5 * * * ? *)` (next 5th minute)

**Cron Expression Cheat Sheet**:
```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (1 - 7)
│ │ │ │ │
│ │ │ │ │
* * * * *
```

## **Production Considerations**
1. **Error Handling**:
   - Implement retry logic for database connections
   - Add dead-letter queues for failed invocations

2. **Security**:
   - Encrypt sensitive parameters in Parameter Store
   - Rotate database credentials regularly

3. **Monitoring**:
   - Set up CloudWatch alarms for function errors
   - Create dashboards for invocation metrics

4. **Cost Optimization**:
   - Right-size memory allocation
   - Consider provisioned concurrency for predictable loads

## **Conclusion**
This lab has guided you through building a complete serverless reporting system that:
- Securely accesses database resources
- Processes and formats sales data
- Distributes reports via email
- Runs on a automated schedule

**Key Architecture Benefits**:
- **Scalability**: Automatically handles variable loads
- **Reliability**: Built-in retries and failover
- **Cost-Effectiveness**: Pay-per-use pricing model
- **Maintainability**: Separation of concerns between components

**Next Steps for Enhancement**:
1. Add report formatting (PDF generation)
2. Implement historical data archiving
3. Create a frontend for report customization
4. Set up multi-channel notifications (SMS, Slack)