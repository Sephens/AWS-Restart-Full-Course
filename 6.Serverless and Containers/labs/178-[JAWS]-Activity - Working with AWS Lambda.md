# **AWS Lambda Sales Analysis Report - Comprehensive Lab Guide**

## **Lab Overview**
This lab demonstrates how to build a **serverless sales reporting system** using:
- **AWS Lambda** (Python functions)
- **Amazon RDS/MySQL** (Database)
- **Amazon SNS** (Email notifications)
- **AWS Systems Manager Parameter Store** (Secure configuration)
- **Amazon CloudWatch Events** (Scheduled triggers)

### **Architecture Flow**
1. **CloudWatch Event** triggers `salesAnalysisReport` Lambda daily at 8 PM.
2. `salesAnalysisReport` invokes `salesAnalysisReportDataExtractor` Lambda.
3. `salesAnalysisReportDataExtractor` queries **MySQL database** (`cafe_db`).
4. Results are returned to `salesAnalysisReport`.
5. Report is formatted and sent via **SNS** to administrators.

---

## **Task 1: Observing IAM Roles**
### **Objective**:  
Understand IAM permissions required for Lambda functions.

### **1.1 `salesAnalysisReportRole` Permissions**
- **Trust Relationship**: Allows Lambda service to assume the role.
- **Policies**:
  - `AmazonSNSFullAccess`: Publish to SNS topics.
  - `AmazonSSMReadOnlyAccess`: Read Parameter Store values.
  - `AWSLambdaBasicRunRole`: Write CloudWatch logs.
  - `AWSLambdaRole`: Invoke other Lambda functions.

### **1.2 `salesAnalysisReportDERole` Permissions**
- **Trust Relationship**: Lambda service.
- **Policies**:
  - `AWSLambdaBasicRunRole`: CloudWatch logs.
  - `AWSLambdaVPCAccessRunRole`: Access VPC resources (MySQL).

### **Key Notes**:
- **Least privilege principle**: Each role has only necessary permissions.
- **VPC Access**: Required for Lambda to connect to RDS/EC2-hosted databases.

---

## **Task 2: Creating Lambda Layer & Data Extractor Function**
### **Objective**:  
Create a **Lambda layer** for PyMySQL library and deploy the data extraction function.

### **2.1 Create Lambda Layer (`pymysqlLibrary`)**
1. **Download `pymysql-v3.zip`** (Pre-built PyMySQL package).
2. **AWS Lambda Console** → **Layers** → **Create Layer**:
   - **Name**: `pymysqlLibrary`
   - **Upload**: `pymysql-v3.zip`
   - **Compatible Runtimes**: Python 3.9

### **2.2 Create `salesAnalysisReportDataExtractor` Function**
1. **Lambda Console** → **Create Function**:
   - **Name**: `salesAnalysisReportDataExtractor`
   - **Runtime**: Python 3.9
   - **Role**: `salesAnalysisReportDERole`
2. **Add Layer**:
   - Attach `pymysqlLibrary` (v1).

### **2.3 Upload Function Code**
1. **Download `salesAnalysisReportDataExtractor-v3.zip`**.
2. **Upload ZIP** in Lambda console.
3. **Handler**: `salesAnalysisReportDataExtractor.lambda_handler`

### **2.4 Configure VPC Settings**
- **VPC**: `Cafe VPC`
- **Subnet**: `Cafe Public Subnet 1`
- **Security Group**: `CafeSecurityGroup`

### **Why?**
- **Lambda Layer**: Shared libraries reduce deployment package size.
- **VPC Access**: Required to connect to MySQL on EC2.

---

## **Task 3: Testing the Data Extractor Function**
### **Objective**:  
Verify the function can query MySQL and return sales data.

### **3.1 Prepare Test Event**
1. **Retrieve DB Parameters** (Systems Manager → Parameter Store):
   - `/cafe/dbUrl`
   - `/cafe/dbName`
   - `/cafe/dbUser`
   - `/cafe/dbPassword`
2. **Test Event JSON**:
   ```json
   {
     "dbUrl": "cafe-db.example.com",
     "dbName": "cafe_db",
     "dbUser": "admin",
     "dbPassword": "password123"
   }
   ```

### **3.2 First Test (Failure)**
- **Error**: `Task timed out after 3.00 seconds`
- **Cause**: Security group blocks MySQL port (`3306`).

### **3.3 Fix Security Group**
1. **EC2 Console** → **Security Groups** → `CafeSecurityGroup`.
2. **Add Inbound Rule**:
   - **Type**: MySQL/Aurora
   - **Port**: 3306
   - **Source**: `CafeSecurityGroup` (or Lambda’s SG).

### **3.4 Second Test (Success)**
- **Output**:
  ```json
  {
    "statusCode": 200,
    "body": []
  }
  ```
  (Empty until orders are placed.)

### **3.5 Populate Test Data**
1. Access **Café Website** (`http://<CafePublicIP>/cafe`).
2. **Place Orders** (Menu → Submit Order).
3. **Re-test Lambda**:
   ```json
   {
     "statusCode": 200,
     "body": [
       {
         "product_group_name": "Pastries",
         "product_name": "Croissant",
         "quantity": 2
       }
     ]
   }
   ```

### **Troubleshooting Tips**:
- **Timeout Issues**: Increase Lambda timeout (default: 3s → 10s).
- **Connection Errors**: Verify VPC/subnet/SG settings.

---

## **Task 4: Configuring SNS Notifications**
### **Objective**:  
Set up email alerts for the sales report.

### **4.1 Create SNS Topic**
1. **SNS Console** → **Topics** → **Create Topic**:
   - **Name**: `salesAnalysisReportTopic`
   - **Display Name**: `SARTopic`
2. **Note ARN** (e.g., `arn:aws:sns:us-west-2:123456789012:salesAnalysisReportTopic`).

### **4.2 Subscribe Email**
1. **Create Subscription**:
   - **Protocol**: Email
   - **Endpoint**: `your-email@example.com`
2. **Confirm Subscription** (Check email inbox).

### **Why?**
- **Decoupling**: Lambda publishes to SNS → SNS handles email delivery.
- **Scalability**: Add SMS/Slack endpoints later.

---

## **Task 5: Creating the Main Lambda Function**
### **Objective**:  
Deploy the orchestrator Lambda (`salesAnalysisReport`) that:
1. Fetches DB params from **Parameter Store**.
2. Invokes `salesAnalysisReportDataExtractor`.
3. Formats and emails report via **SNS**.

### **5.1 Deploy via AWS CLI**
1. **Connect to CLI Host** (EC2 Instance Connect).
2. **Configure AWS CLI**:
   ```bash
   aws configure
   ```
   - Enter **Access Key**, **Secret Key**, **Region** (`us-west-2`).
3. **Create Function**:
   ```bash
   aws lambda create-function \
   --function-name salesAnalysisReport \
   --runtime python3.9 \
   --zip-file fileb://salesAnalysisReport-v2.zip \
   --handler salesAnalysisReport.lambda_handler \
   --role arn:aws:iam::123456789012:role/salesAnalysisReportRole
   ```

### **5.2 Configure Environment Variables**
- **Key**: `topicARN`
- **Value**: `arn:aws:sns:us-west-2:123456789012:salesAnalysisReportTopic`

### **5.3 Test Manually**
- **Test Event**: `{}` (No input needed).
- **Expected Output**:
  ```json
  {
    "statusCode": 200,
    "body": "Sales Analysis Report sent."
  }
  ```
- **Verify Email Received**.

### **5.4 Schedule with CloudWatch Events**
1. **Add Trigger**:
   - **Trigger Type**: EventBridge (CloudWatch Events).
   - **Rule**: `salesAnalysisReportDailyTrigger`.
   - **Schedule Expression**:
     ```plaintext
     cron(0 20 ? * MON-SAT *)
     ```
     (Runs at 8 PM UTC Mon-Sat.)

### **Cron Expression Tips**:
- **Format**: `cron(Minutes Hours Day Month Weekday Year)`
- **Example**: `cron(0 14 ? * MON-FRI *)` = 2 PM UTC weekdays.

---

## **Task 6: Testing End-to-End Flow**
### **Steps**:
1. **Wait for Scheduled Run** (Or trigger manually).
2. **Check Email** for report:
   ```
   Daily Sales Analysis Report
   --------------------------
   Product: Croissant, Quantity: 2
   Product: Hot Chocolate, Quantity: 1
   ```
3. **CloudWatch Logs**:
   - Debug errors in `/aws/lambda/salesAnalysisReport`.

### **Common Issues & Fixes**:
| Issue | Solution |
|-------|----------|
| Timeout | Increase Lambda timeout (up to 15 mins). |
| No Email | Check SNS subscription is **confirmed**. |
| Empty Report | Place orders in café website. |

---

## **Conclusion**
### **What You Built**:
✅ **Serverless ETL Pipeline**:  
   - Lambda extracts data → SNS emails reports.  
✅ **Secure Configuration**:  
   - DB credentials in **Parameter Store** (not hardcoded).  
✅ **Scheduled Automation**:  
   - CloudWatch triggers daily reports.  

### **Real-World Applications**:
- **Daily Business Reports** (Sales, Inventory).  
- **Database Maintenance Tasks** (Backups, Cleanups).  
- **Alerting Systems** (Error notifications).  

### **Best Practices**:
✔ **Least Privilege IAM Roles**.  
✔ **Environment Variables** for configuration.  
✔ **CloudWatch Logs** for monitoring.  

This lab provides hands-on experience with **serverless orchestration**—key for AWS SysOps! 🚀