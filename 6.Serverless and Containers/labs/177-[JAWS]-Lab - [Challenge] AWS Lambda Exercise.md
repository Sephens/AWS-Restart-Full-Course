# **AWS Lambda Word Counter - Complete Lab Guide**

## **Lab Overview**
This challenge lab teaches you to build a serverless word counter that automatically processes text files uploaded to Amazon S3 and sends word count results via email/SMS. You'll create three key AWS components that work together:

1. **AWS Lambda Function** (Python code to count words)
2. **Amazon S3 Bucket** (Stores files and triggers Lambda)
3. **Amazon SNS Topic** (Sends notifications)


## **Detailed Step-by-Step Instructions**

### **1. Setting Up Your Environment**
**Time Estimate**: 5 minutes

1. **Start the Lab Environment**
   - Click "Start Lab" at the top of these instructions
   - Wait for status to show "ready"

2. **Access AWS Console**
   - Click "AWS" to open the management console
   - Ensure you're in the correct region (us-east-1 recommended)

### **2. Creating the S3 Bucket**
**Time Estimate**: 10 minutes

1. **Navigate to S3 Service**
   - Search for "S3" in AWS services
   - Click "Create bucket"

2. **Configure Bucket**
   ```yaml
   Bucket name: word-count-[your-name]-[date]  # e.g., word-count-john-20230501
   Region: Same as your Lambda will be in
   Block all public access: Enabled (checked)
   Bucket Versioning: Disabled (for this lab)
   ```

3. **Enable Event Notifications**
   - Go to bucket → Properties → Event notifications
   - Click "Create event notification"
   - Configure:
     ```yaml
     Event name: WordCountTrigger
     Event types: All object create events
     Destination: Lambda function
     Lambda function: [Will select after creating it]
     ```

**Important Notes**:
- Bucket names must be globally unique
- Avoid spaces and uppercase letters
- For production, enable versioning and logging

### **3. Creating the SNS Topic**
**Time Estimate**: 10 minutes

1. **Navigate to SNS Service**
   - Search for "SNS" in AWS services
   - Click "Topics" → "Create topic"

2. **Configure Topic**
   ```yaml
   Type: Standard
   Name: WordCountTopic
   Display name: WordCount  # Shows in email "From" field
   ```

3. **Create Subscription**
   - Click "Create subscription"
   - Configure:
     ```yaml
     Protocol: Email
     Endpoint: your-email@example.com
     ```

4. **Confirm Subscription**
   - Check your email inbox
   - Click confirmation link in AWS notification email

**Pro Tip**: For SMS notifications, choose "SMS" protocol and enter your phone number with country code.

### **4. Creating the Lambda Function**
**Time Estimate**: 25 minutes

#### **4.1 Basic Configuration**
1. **Navigate to Lambda Service**
   - Search for "Lambda" in AWS services
   - Click "Create function"

2. **Configure Function**
   ```yaml
   Function name: WordCounter
   Runtime: Python 3.9
   Architecture: x86_64
   Execution role: Use existing role
   Existing role: LambdaAccessRole
   ```

#### **4.2 Add Environment Variable**
1. Go to Configuration → Environment variables
2. Add:
   ```yaml
   Key: SNS_TOPIC_ARN
   Value: [Paste your SNS Topic ARN]
   ```

#### **4.3 Paste the Function Code**
Replace the default code with:

```python
import boto3
import os
import json

def lambda_handler(event, context):
    try:
        print("Raw event received:", json.dumps(event))
        
        # Parse event from different sources
        if 'Records' not in event:
            if 'key' in event and 'bucket' in event:  # Manual test format
                print("Processing manual test event")
                bucket = event['bucket']
                key = event['key']
            else:
                return {
                    'statusCode': 400,
                    'body': 'Invalid event format. Expected S3 event with Records or manual test format with bucket/key.'
                }
        else:  # Real S3 event
            print("Processing S3 event")
            if len(event['Records']) == 0:
                return {
                    'statusCode': 400,
                    'body': 'Empty Records array in event'
                }
                
            record = event['Records'][0]
            if 's3' not in record:
                return {
                    'statusCode': 400,
                    'body': 'Missing s3 in Record'
                }
                
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']

        print(f"Processing file: {key} from bucket: {bucket}")
        
        # Validate file type
        if not key.lower().endswith('.txt'):
            return {
                'statusCode': 400,
                'body': 'Only .txt files are supported'
            }
        
        # Download file
        tmp_file = '/tmp/' + os.path.basename(key)
        s3 = boto3.client('s3')
        s3.download_file(bucket, key, tmp_file)
        
        # Count words
        with open(tmp_file, 'r', encoding='utf-8') as f:
            content = f.read()
            word_count = len(content.split())
        
        # Publish to SNS
        sns = boto3.client('sns')
        message = f"The word count in the {key} file is {word_count}."
        response = sns.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Subject="Word Count Result",
            Message=message
        )
        
        # Clean up
        os.remove(tmp_file)
        
        return {
            'statusCode': 200,
            'body': message
        }
        
    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': f"Error processing file: {str(e)}"
        }
```

#### **4.4 Configure Function Settings**
1. Go to Configuration → General configuration
2. Set:
   ```yaml
   Timeout: 30 seconds
   Memory: 512 MB
   ```

### **5. Connecting Components**
**Time Estimate**: 10 minutes

1. **Complete S3 Trigger Setup**
   - Return to your S3 bucket's event notifications
   - Select your Lambda function as the destination
   - Save changes

2. **Verify Permissions**
   - LambdaAccessRole should have:
     - `AWSLambdaBasicExecutionRole`
     - `AmazonS3FullAccess`
     - `AmazonSNSFullAccess`

### **6. Testing Your Solution**
**Time Estimate**: 15 minutes

#### **6.1 Manual Test**
1. In Lambda console, go to your function
2. Click "Test" tab
3. Create new test event:
   ```json
   {
     "bucket": "your-bucket-name",
     "key": "test.txt"
   }
   ```
4. Run test and check:
   - Execution results
   - CloudWatch logs
   - Email notification

#### **6.2 Real S3 Upload Test**
1. Create a sample text file:
   ```bash
   echo "This is a test file with seven words" > test.txt
   ```
2. Upload to your S3 bucket
3. Verify:
   - Lambda was triggered (check logs)
   - Email received with correct count

### **7. Troubleshooting Guide**

| Symptom | Solution |
|---------|----------|
| No Lambda invocation | Check S3 event notification configuration |
| Permission denied | Verify Lambda execution role policies |
| No email received | Confirm SNS subscription is confirmed |
| Wrong word count | Check file encoding (use UTF-8) |
| Timeout errors | Increase Lambda timeout setting |

**Debugging Tips**:
1. Always check CloudWatch logs first
2. Test with simple files (known word count)
3. Verify all ARNs are correct

## **Complete Solution Explained**

### **Event Handling**
The Lambda function processes two event formats:
1. **Real S3 Trigger** (Production):
   ```json
   {
     "Records": [{
       "s3": {
         "bucket": {"name": "your-bucket"},
         "object": {"key": "file.txt"}
       }
     }]
   }
   ```
2. **Manual Test** (Console Testing):
   ```json
   {
     "bucket": "your-bucket",
     "key": "file.txt"
   }
   ```

### **Word Counting Logic**
1. Downloads file to `/tmp` (Lambda's ephemeral storage)
2. Reads content with UTF-8 encoding
3. Splits text by whitespace and counts elements
4. Formats result message as specified

### **SNS Notification**
- Uses environment variable for topic ARN
- Formats message: "The word count in [filename] is [count]."
- Subject: "Word Count Result"

### **Error Handling**
- Validates file type (.txt only)
- Checks event structure
- Handles download/processing failures
- Provides clear error messages

## **Best Practices Implemented**

1. **Security**
   - Least privilege permissions
   - No hardcoded credentials
   - Environment variables for configuration

2. **Reliability**
   - Comprehensive error handling
   - Resource cleanup (deletes temp files)
   - Input validation

3. **Maintainability**
   - Clear logging
   - Modular structure
   - Comments explaining logic

## **Submission Requirements**

1. **Email Forwarding**
   - Forward one test result email to your instructor
   - Subject should be "Word Count Result"

2. **Screenshot**
   - Capture your Lambda function configuration
   - Include: Code, triggers, and environment variables

3. **Verification**
   - Confirm you received notifications
   - Check word counts are accurate

## **Final Checklist**

✅ S3 bucket created and configured  
✅ SNS topic created with verified subscription  
✅ Lambda function deployed with correct code  
✅ Environment variable set (SNS_TOPIC_ARN)  
✅ S3 trigger properly configured  
✅ Tested with both manual and real uploads  
✅ Received email notifications  
✅ Submitted required materials  

This lab provides hands-on experience with key AWS serverless services while following AWS best practices. The skills learned are directly applicable to real-world serverless application development.