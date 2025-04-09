# **Comprehensive Lab Guide: AWS Lambda Word Counter Challenge**

## **Lab Overview**
This challenge lab teaches you to build a serverless word counting system that:
✅ Processes text files uploaded to S3  
✅ Calculates word counts  
✅ Sends results via SNS email/SMS  
✅ Demonstrates event-driven architecture  

## **Step-by-Step Implementation**

### **1. Create S3 Bucket**
1. Navigate to **S3 Console**
2. Choose **Create bucket**
3. Configure:
   - **Bucket name**: `word-count-bucket-[your-initials]` (must be globally unique)
   - **Region**: Same as all other resources (e.g., us-east-1)
4. Leave all other settings default
5. Click **Create bucket**

### **2. Create SNS Topic**
1. Go to **SNS Console**
2. Select **Topics** > **Create topic**
3. Configure:
   - **Type**: Standard
   - **Name**: `WordCountResults`
   - **Display name**: `WordCountAlert`
4. Click **Create topic**
5. Create subscription:
   - **Protocol**: Email
   - **Endpoint**: Your email address
   - Click **Create subscription**
6. Confirm subscription via email

*Optional SMS Setup*:  
Add another subscription with protocol "SMS" and your mobile number.

### **3. Create Lambda Function**
1. Navigate to **Lambda Console**
2. Choose **Create function**
3. Configure:
   - **Function name**: `WordCounter`
   - **Runtime**: Python 3.9
   - **Execution role**: Use existing role
   - **Existing role**: `LambdaAccessRole`
4. Click **Create function**

### **4. Implement Function Code**
Replace the default code with:

```python
import boto3
import os

def lambda_handler(event, context):
    # Get bucket and file details from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Get the file content
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    
    # Count words
    word_count = len(content.split())
    
    # Publish to SNS
    sns = boto3.client('sns')
    message = f"The word count in the {key} file is {word_count}."
    sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=message,
        Subject="Word Count Result"
    )
    
    return {
        'statusCode': 200,
        'body': message
    }
```

### **5. Configure Environment Variables**
1. In Lambda function console, go to **Configuration** > **Environment variables**
2. Add variable:
   - **Key**: `SNS_TOPIC_ARN`
   - **Value**: [Your SNS Topic ARN] (copy from SNS Topic details)

### **6. Set Up S3 Trigger**
1. In Lambda function, go to **Configuration** > **Triggers**
2. Click **Add trigger**
3. Select **S3**
4. Configure:
   - **Bucket**: Select your created bucket
   - **Event type**: `Put`
   - **Prefix**: `text-files/` (optional for organization)
5. Click **Add**

### **7. Test the System**
1. Upload a text file to your S3 bucket:
   - Either use AWS Console drag-and-drop
   - Or AWS CLI: `aws s3 cp sample.txt s3://word-count-bucket-[your-initials]/`
2. Check your email for the word count result
3. Verify CloudWatch logs for execution details

## **Troubleshooting Guide**

| **Issue**                  | **Solution** |
|----------------------------|-------------|
| No email received          | Check SNS subscription confirmation status |
| Permission errors          | Verify LambdaAccessRole has all required policies |
| File not processed         | Confirm trigger is configured for correct bucket/prefix |
| Incorrect word count       | Review Python splitting logic (may need regex for complex files) |

## **Advanced Enhancements**
1. **File Validation**:
   ```python
   if not key.endswith('.txt'):
       return {"error": "Only text files supported"}
   ```

2. **Enhanced Formatting**:
   ```python
   message = f"""
   Word Count Report
   -----------------
   File: {key}
   Word Count: {word_count}
   Processed at: {datetime.now()}
   """
   ```

3. **Multiple Recipients**:
   - Add additional SNS subscriptions
   - Or use SNS topic to fanout to multiple endpoints

4. **Error Handling**:
   ```python
   try:
       # Main logic
   except Exception as e:
       sns.publish(
           TopicArn=os.environ['SNS_TOPIC_ARN'],
           Message=f"Error processing {key}: {str(e)}",
           Subject="Word Count Error"
       )
   ```

## **Submission Requirements**
1. **Email Forwarding**:
   - Forward one of the word count result emails
   - Include the original text file for verification

2. **Screenshot**:
   - Capture your Lambda function configuration page
   - Show the code, triggers, and environment variables

## **Conclusion**
You've successfully built a serverless pipeline that:
- Automatically processes text file uploads
- Performs word count calculations
- Delivers results via multiple channels
- Demonstrates core AWS serverless services

**Key Architecture Benefits**:
- **Event-driven**: Processes files immediately on upload
- **Scalable**: Handles from 1 to 1000s of files automatically
- **Extensible**: Easy to add new features or output channels

**Next Learning Steps**:
1. Add file size validation
2. Implement processing for other file types
3. Create a CloudWatch dashboard for monitoring
4. Explore Step Functions for complex workflows