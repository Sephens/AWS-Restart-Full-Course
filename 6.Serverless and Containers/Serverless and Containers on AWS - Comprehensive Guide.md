# Serverless and Containers on AWS - Comprehensive Guide

## Table of Contents
- [Serverless and Containers on AWS - Comprehensive Guide](#serverless-and-containers-on-aws---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [AWS Lambda](#aws-lambda)
  - [Working with AWS Lambda](#working-with-aws-lambda)
  - [APIs and REST](#apis-and-rest)
  - [Amazon API Gateway](#amazon-api-gateway)
  - [AWS Step Functions](#aws-step-functions)
  - [Containers on AWS](#containers-on-aws)
  - [Knowledge Check](#knowledge-check)
  - [Key Takeaways](#key-takeaways)

---

## Overview

**Serverless and Containers**  
This unit introduces serverless computing and container technologies on AWS, focusing on key services like AWS Lambda, API Gateway, Step Functions, and container services (ECR, ECS, EKS, Fargate).  

**Learning Objectives**:  
- Understand serverless computing and AWS Lambda.  
- Learn about APIs (REST) and Amazon API Gateway.  
- Explore AWS Step Functions for workflow orchestration.  
- Identify container services on AWS and their use cases.  

**Duration**:  
- Total estimated time: ~5 hours (including labs).  

**Example**:  
A startup uses AWS Lambda for backend processing and API Gateway to expose REST APIs, reducing infrastructure costs by 70%.  

---

## AWS Lambda

**What is AWS Lambda?**  
A serverless compute service that runs code in response to events (e.g., S3 uploads, HTTP requests) without managing servers.  

**Key Features**:  
- **Event-Driven**: Triggers include S3, DynamoDB, CloudWatch Events.  
- **Scaling**: Automatically scales with request volume.  
- **Pay-per-Use**: Billed per execution (100ms increments).  

**Example**:  
```python
# Lambda function (Python) to process S3 uploads
import boto3
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(f"File {key} uploaded to {bucket}")
```

**Traditional vs. Serverless**:  
| **Aspect**       | **Traditional**               | **Serverless (Lambda)**       |
|------------------|-------------------------------|-------------------------------|
| **Provisioning** | Manual (EC2 instances)        | Automatic (AWS-managed)       |
| **Scaling**      | Manual/ASG                   | Auto-scaling                  |
| **Cost**         | Pay for idle resources        | Pay only for executions       |

**Lab Tasks**:  
1. Create a Lambda function triggered by a CloudWatch schedule.  
2. Debug using CloudWatch Logs.  

---

## Working with AWS Lambda

**Key Labs**:  
1. **Basic Lambda Lab**:  
   - Create a function with IAM permissions.  
   - Add a Lambda layer (e.g., for external libraries like `requests`).  
   - Test with a mock S3 event.  

2. **Challenge Lab**:  
   - Build a Lambda function triggered by S3 uploads that sends an SNS notification.  

**Example IAM Policy**:  
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": "arn:aws:s3:::my-bucket/*"
  }]
}
```

**Troubleshooting Tips**:  
- Check CloudWatch Logs for errors.  
- Verify IAM roles have correct permissions.  

---

## APIs and REST

**What is a REST API?**  
An architectural style for web services using HTTP methods (GET, POST, PUT, DELETE) to interact with resources.  

**HTTP Methods**:  
- **GET**: Retrieve data (e.g., fetch user details).  
- **POST**: Create data (e.g., submit a form).  
- **PUT**: Update data (e.g., edit a profile).  
- **DELETE**: Remove data (e.g., delete a record).  

**Example Request/Response**:  
```http
GET /users/1 HTTP/1.1
Host: api.example.com

HTTP/1.1 200 OK
{"id": 1, "name": "John Doe"}
```

**Status Codes**:  
- `200 OK`: Success.  
- `404 Not Found`: Resource not found.  
- `500 Server Error`: Backend failure.  

---

## Amazon API Gateway

**Purpose**:  
Fully managed service to create, publish, and secure APIs at scale.  

**Key Benefits**:  
- **Integration**: Connects to Lambda, EC2, or external endpoints.  
- **Security**: Supports IAM, Cognito, and API keys.  
- **Traffic Management**: Throttling and caching.  

**Example Architecture**:  
1. Client → API Gateway → Lambda → DynamoDB.  
2. Response routed back through API Gateway.  

**Use Case**:  
A mobile app uses API Gateway to expose Lambda functions for user authentication and data retrieval.  

---

## AWS Step Functions

**Purpose**:  
Orchestrates serverless workflows using state machines (e.g., order processing).  

**Key Features**:  
- **Visual Workflows**: Define steps as JSON (e.g., `"Type": "Task"`).  
- **Retry Logic**: Handles failures automatically.  
- **Integrations**: Works with Lambda, ECS, SNS.  

**Example Workflow**:  
1. Start → Validate input (Lambda) → Process payment (Lambda) → Send confirmation (SNS) → End.  

**Use Case**:  
An e-commerce site uses Step Functions to manage order fulfillment across multiple services.  

---

## Containers on AWS

**Key Services**:  
1. **Amazon ECR**: Docker image registry (stores/tracks images).  
2. **Amazon ECS**: Orchestrates containers (Docker compatible).  
3. **Amazon EKS**: Managed Kubernetes.  
4. **AWS Fargate**: Serverless containers (no EC2 management).  

**Example Deployment**:  
```bash
# Push image to ECR
aws ecr get-login-password | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
```

**Fargate vs. EC2**:  
| **Feature**       | **Fargate**                     | **EC2**                     |
|------------------|---------------------------------|-----------------------------|
| **Management**   | No servers (AWS-managed)        | Self-managed instances      |
| **Scaling**      | Automatic                       | Manual/ASG                 |
| **Cost**         | Pay per vCPU/memory             | Pay for EC2 instances      |

---

## Knowledge Check

**Questions & Answers**:  
1. **Q**: Which service runs containers without managing servers?  
   **A**: AWS Fargate.  
2. **Q**: What stores Docker images on AWS?  
   **A**: Amazon ECR.  
3. **Q**: Which REST method creates a resource?  
   **A**: POST.  

**Scenario**:  
A developer needs to deploy a microservice. They should:  
1. Build a Docker image.  
2. Push to ECR.  
3. Deploy using ECS Fargate.  

---

## Key Takeaways

- **Serverless**: Lambda + API Gateway for event-driven apps.  
- **Containers**: Use ECS/EKS for orchestration; Fargate for serverless.  
- **Workflows**: Step Functions for multi-step processes.  

**Example Project**:  
A weather app uses Lambda to fetch data, API Gateway for REST endpoints, and Fargate to run a containerized dashboard.  

**Feedback**: Contact [AWS Training](https://support.aws.amazon.com/#/contacts/aws-training).  

© 2023, Amazon Web Services, Inc. or its affiliates. All rights reserved.