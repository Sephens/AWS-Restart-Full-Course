# AWS Services and Service Categories - Cloud Foundations

## What You Will Learn

### Core Objectives:
- **Identify AWS services and service categories.**

---

## Introduction to AWS Service Categories

AWS offers a **broad set of cloud-based services** organized into various **service categories**. Each category consists of multiple services designed to meet different cloud computing needs. This module focuses on the most widely used services, particularly those relevant to the **AWS Certified Cloud Practitioner exam**.

### Key Service Categories:
- **Compute**
- **Storage**
- **Containers**
- **Database**
- **Networking and Content Delivery**
- **Security, Identity, and Compliance**
- **Management and Governance**
- **Cost Management**

---

## Storage Service Category

### Key Services:
1. **Amazon Simple Storage Service (Amazon S3)**
   - **Purpose**: Object storage for scalable, secure, and durable data storage.
   - **Use Cases**: Websites, mobile apps, backup, archive, IoT, big data analytics.
   - **Example**: Storing user-generated content (e.g., images, videos) for a mobile app.

2. **Amazon Elastic Block Store (Amazon EBS)**
   - **Purpose**: High-performance block storage for EC2 instances.
   - **Use Cases**: Databases, enterprise applications, big data analytics.
   - **Example**: Running a MySQL database on an EC2 instance with EBS for persistent storage.

3. **Amazon Elastic File System (Amazon EFS)**
   - **Purpose**: Scalable, managed NFS file system for cloud and on-premises resources.
   - **Use Cases**: Shared file storage for applications, big data processing.
   - **Example**: Hosting shared files for a multi-instance web application.

4. **Amazon S3 Glacier**
   - **Purpose**: Low-cost storage for data archiving and long-term backup.
   - **Use Cases**: Regulatory compliance, digital preservation.
   - **Example**: Archiving financial records for 7-10 years to meet compliance requirements.

---

## Compute Service Category

### Key Services:
1. **Amazon Elastic Compute Cloud (Amazon EC2)**
   - **Purpose**: Resizable virtual machines in the cloud.
   - **Use Cases**: Web servers, application servers, game servers.
   - **Example**: Hosting a web application on an EC2 instance.

2. **Amazon EC2 Auto Scaling**
   - **Purpose**: Automatically adjust the number of EC2 instances based on demand.
   - **Use Cases**: Handling traffic spikes, cost optimization.
   - **Example**: Scaling a web application during a flash sale.

3. **AWS Elastic Beanstalk**
   - **Purpose**: Deploy and scale web applications without managing infrastructure.
   - **Use Cases**: Web applications, APIs.
   - **Example**: Deploying a Node.js application with automatic scaling.

4. **AWS Lambda**
   - **Purpose**: Run code without provisioning servers (serverless computing).
   - **Use Cases**: Event-driven applications, data processing.
   - **Example**: Processing uploaded files in S3 automatically.

---

## Containers Service Category

### Key Services:
1. **Amazon Elastic Container Service (Amazon ECS)**
   - **Purpose**: Orchestrate Docker containers.
   - **Use Cases**: Microservices, containerized applications.
   - **Example**: Running a microservices-based e-commerce platform.

2. **Amazon Elastic Container Registry (Amazon ECR)**
   - **Purpose**: Store and manage Docker container images.
   - **Use Cases**: Container image storage for ECS or EKS.
   - **Example**: Storing Docker images for a CI/CD pipeline.

3. **Amazon Elastic Kubernetes Service (Amazon EKS)**
   - **Purpose**: Run Kubernetes on AWS.
   - **Use Cases**: Kubernetes-based applications.
   - **Example**: Managing a Kubernetes cluster for a multi-tenant SaaS application.

4. **AWS Fargate**
   - **Purpose**: Run containers without managing servers.
   - **Use Cases**: Serverless container deployments.
   - **Example**: Running a batch processing job in containers without managing EC2 instances.

---

## Database Service Category

### Key Services:
1. **Amazon Relational Database Service (Amazon RDS)**
   - **Purpose**: Managed relational databases (MySQL, PostgreSQL, etc.).
   - **Use Cases**: Web applications, enterprise applications.
   - **Example**: Hosting a PostgreSQL database for a web application.

2. **Amazon Aurora**
   - **Purpose**: High-performance relational database compatible with MySQL and PostgreSQL.
   - **Use Cases**: High-performance applications, enterprise databases.
   - **Example**: Running a high-traffic e-commerce database.

3. **Amazon Redshift**
   - **Purpose**: Data warehousing and analytics.
   - **Use Cases**: Big data analytics, business intelligence.
   - **Example**: Analyzing sales data from multiple regions.

4. **Amazon DynamoDB**
   - **Purpose**: NoSQL database with single-digit millisecond performance.
   - **Use Cases**: Real-time applications, gaming, IoT.
   - **Example**: Storing user session data for a gaming application.

---

## Networking and Content Delivery Service Category

### Key Services:
1. **Amazon Virtual Private Cloud (Amazon VPC)**
   - **Purpose**: Isolated network environment in the cloud.
   - **Use Cases**: Private cloud environments, hybrid cloud.
   - **Example**: Creating a private network for a multi-tier web application.

2. **Elastic Load Balancing (ELB)**
   - **Purpose**: Distribute incoming traffic across multiple targets.
   - **Use Cases**: High-availability applications, load balancing.
   - **Example**: Distributing traffic across multiple EC2 instances.

3. **Amazon CloudFront**
   - **Purpose**: Content delivery network (CDN) for low-latency content delivery.
   - **Use Cases**: Media streaming, static website hosting.
   - **Example**: Delivering video content to global users with low latency.

4. **Amazon Route 53**
   - **Purpose**: Scalable DNS service.
   - **Use Cases**: Domain name management, traffic routing.
   - **Example**: Routing traffic to the nearest AWS region for a global application.

---

## Security, Identity, and Compliance Service Category

### Key Services:
1. **AWS Identity and Access Management (IAM)**
   - **Purpose**: Manage access to AWS resources.
   - **Use Cases**: User and group permissions, role-based access.
   - **Example**: Granting an application access to an S3 bucket.

2. **AWS Organizations**
   - **Purpose**: Manage multiple AWS accounts.
   - **Use Cases**: Centralized billing, security policies.
   - **Example**: Enforcing security policies across multiple AWS accounts.

3. **AWS Key Management Service (AWS KMS)**
   - **Purpose**: Manage encryption keys.
   - **Use Cases**: Data encryption, compliance.
   - **Example**: Encrypting sensitive data stored in S3.

4. **AWS Shield**
   - **Purpose**: DDoS protection.
   - **Use Cases**: Protecting web applications from DDoS attacks.
   - **Example**: Securing a high-traffic e-commerce website.

---

## Cost Management Service Category

### Key Services:
1. **AWS Cost and Usage Report**
   - **Purpose**: Detailed cost and usage data.
   - **Use Cases**: Cost analysis, budgeting.
   - **Example**: Analyzing monthly AWS costs.

2. **AWS Budgets**
   - **Purpose**: Set custom budgets and alerts.
   - **Use Cases**: Cost control, budget tracking.
   - **Example**: Setting a monthly budget for EC2 usage.

3. **AWS Cost Explorer**
   - **Purpose**: Visualize and manage AWS costs.
   - **Use Cases**: Cost optimization, forecasting.
   - **Example**: Identifying cost-saving opportunities.

---

## Management and Governance Service Category

### Key Services:
1. **AWS Management Console**
   - **Purpose**: Web-based interface for managing AWS resources.
   - **Use Cases**: Resource management, monitoring.
   - **Example**: Launching an EC2 instance via the console.

2. **AWS Config**
   - **Purpose**: Track resource inventory and changes.
   - **Use Cases**: Compliance, auditing.
   - **Example**: Monitoring changes to S3 bucket policies.

3. **Amazon CloudWatch**
   - **Purpose**: Monitor resources and applications.
   - **Use Cases**: Performance monitoring, alerting.
   - **Example**: Setting up alerts for high CPU usage on EC2 instances.

4. **AWS CloudTrail**
   - **Purpose**: Track user activity and API usage.
   - **Use Cases**: Security auditing, compliance.
   - **Example**: Auditing who accessed an S3 bucket.

---

## Activity: AWS Management Console Clickthrough

### Scenario:
- **Task**: Explore the AWS Management Console and answer questions about service categories and resource levels.

### Questions:
1. **Which service category is IAM in?**
   - **Answer**: Security, Identity, and Compliance.

2. **Which service category is Amazon VPC in?**
   - **Answer**: Networking and Content Delivery.

3. **Does a subnet exist at the Region or Availability Zone level?**
   - **Answer**: Availability Zone.

4. **Does a VPC exist at the Region or Availability Zone level?**
   - **Answer**: Region.

5. **Which services are global (IAM, Route 53) vs. regional (EC2, Lambda)?**
   - **Answer**: IAM and Route 53 are global; EC2 and Lambda are regional.

---

## Key Takeaways

- **AWS offers a broad set of cloud-based services** across multiple categories, including Compute, Storage, Networking, and Security.
- **The AWS Management Console** provides a web-based interface for managing AWS resources.
- **Understanding service categories** helps in selecting the right AWS services for your needs.

---

## Additional Notes and Examples

### Example: Using Amazon S3 for Static Website Hosting
1. **Create a Bucket**: `my-static-website`.
2. **Upload Files**: HTML, CSS, JavaScript files.
3. **Enable Static Website Hosting**:
   - Go to the bucket properties in the AWS Management Console.
   - Enable "Static website hosting" and specify the index document (e.g., `index.html`).
4. **Access the Website**:
   - URL: `http://my-static-website.s3-website-<region>.amazonaws.com`.

### Example: Using AWS Lambda for Event-Driven Processing
1. **Create a Lambda Function**: Triggered by S3 uploads.
2. **Configure Trigger**: Set up an S3 event to trigger the Lambda function when a file is uploaded.
3. **Process Files**: The Lambda function processes the uploaded file (e.g., resizing images).

### Example: Using Amazon RDS for a Web Application
1. **Create an RDS Instance**: Choose MySQL or PostgreSQL.
2. **Connect to the Database**: Use the database endpoint to connect your web application.
3. **Automate Backups**: Enable automated backups for disaster recovery.

---

## Conclusion

AWS provides a wide range of services across various categories to meet different cloud computing needs. By understanding these categories and the services within them, you can effectively design, deploy, and manage cloud-based solutions. The AWS Management Console is a powerful tool for managing these resources, and understanding the global vs. regional nature of services is crucial for effective cloud management.