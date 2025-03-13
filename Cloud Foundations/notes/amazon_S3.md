# Amazon Simple Storage Service (Amazon S3) - Cloud Foundations

## What You Will Learn

### Core Objectives:
- **Describe the purpose and benefits of Amazon S3.**
- **Explain the basic pricing model of Amazon S3.**

---

## Introduction to Amazon S3

Amazon S3 is a **managed cloud storage solution** that allows you to store and retrieve data as **objects** in **buckets**. It is designed for **durability**, **scalability**, and **security**, making it suitable for a wide range of use cases.

### Key Features:
- **Objects**: Data files (e.g., documents, images, videos) stored in buckets.
- **Buckets**: Logical containers for objects. Bucket names must be unique across all of Amazon S3.
- **Durability**: Designed for **11 nines (99.999999999%)** of durability.
- **Scalability**: Virtually unlimited storage capacity.
- **Access Control**: Granular control over who can access buckets and objects.
- **Redundancy**: Data is stored redundantly across multiple facilities in a region.

---

## Amazon S3 Storage Classes

Amazon S3 offers several **storage classes** designed for different use cases:

### 1. **Amazon S3 Standard**
   - **Use Case**: Frequently accessed data.
   - **Features**: High durability, high availability, low latency, and high throughput.
   - **Examples**: Cloud applications, dynamic websites, content distribution, big data analytics.

### 2. **Amazon S3 Intelligent-Tiering**
   - **Use Case**: Data with unknown or unpredictable access patterns.
   - **Features**: Automatically moves data between **Frequent Access** and **Infrequent Access** tiers based on usage.
   - **Cost**: Small monthly monitoring fee, no retrieval fees.

### 3. **Amazon S3 Standard-Infrequent Access (Standard-IA)**
   - **Use Case**: Data accessed less frequently but requires rapid access when needed.
   - **Features**: Lower storage cost than Standard, with retrieval fees.
   - **Examples**: Long-term storage, backups, disaster recovery.

### 4. **Amazon S3 One Zone-Infrequent Access (One Zone-IA)**
   - **Use Case**: Infrequently accessed data that doesn’t require high availability.
   - **Features**: Data stored in a single Availability Zone, lower cost than Standard-IA.
   - **Examples**: Secondary backups, easily re-creatable data.

### 5. **Amazon S3 Glacier**
   - **Use Case**: Data archiving with retrieval times ranging from minutes to hours.
   - **Features**: Low-cost storage for long-term retention.
   - **Examples**: Regulatory compliance, digital preservation.

### 6. **Amazon S3 Glacier Deep Archive**
   - **Use Case**: Long-term retention of data accessed once or twice a year.
   - **Features**: Lowest-cost storage, retrieval within 12 hours.
   - **Examples**: Financial services, healthcare, public sector compliance.

---

## Accessing Amazon S3

You can access Amazon S3 through:
- **AWS Management Console**
- **AWS CLI (Command Line Interface)**
- **AWS SDKs (Software Development Kits)**
- **REST Endpoints** (HTTP/HTTPS)

### Example: Amazon S3 Bucket and Object URL Structure
- **Bucket URL**: `https://s3.<region>.amazonaws.com/<bucket-name>/`
- **Object URL**: `https://s3.<region>.amazonaws.com/<bucket-name>/<object-key>`

#### Example:
- **Bucket Name**: `my-bucket`
- **Region**: `ap-northeast-1` (Tokyo)
- **Object Key**: `Preview2.mp4`
- **Object URL**: `https://s3.ap-northeast-1.amazonaws.com/my-bucket/Preview2.mp4`

---

## Redundancy in Amazon S3

Amazon S3 stores data redundantly across **multiple facilities** within a region. This ensures high durability, even if two facilities experience concurrent data loss.

### Example:
- **Region**: Tokyo (`ap-northeast-1`)
- **Data**: `helloworld.mp4`
- **Storage**: Data is replicated across multiple facilities in the Tokyo region.

---

## Common Use Cases for Amazon S3

### 1. **Storage for Application Assets**
   - **Example**: Storing user-generated content (e.g., images, videos) for a mobile app.
   - **Benefit**: Centralized storage accessible from anywhere.

### 2. **Static Web Hosting**
   - **Example**: Hosting a website’s static files (HTML, CSS, JavaScript).
   - **Benefit**: Low-latency access and scalability.

### 3. **Backup and Disaster Recovery (DR)**
   - **Example**: Storing backups of critical data with cross-region replication.
   - **Benefit**: High durability and availability.

### 4. **Staging Area for Big Data**
   - **Example**: Storing large datasets for analysis using tools like Amazon EMR or AWS Glue.
   - **Benefit**: Scalable storage for big data processing.

---

## Amazon S3 Pricing

Amazon S3 follows a **pay-as-you-go** pricing model. You pay for:
- **Storage**: GBs per month.
- **Requests**: PUT, COPY, POST, LIST, and GET requests.
- **Data Transfer**: Data transferred out to other regions.

### What You **Don’t Pay For**:
- **Data Transfer In**: Uploading data to Amazon S3 is free.
- **Data Transfer Out to Amazon CloudFront or EC2 in the same region**: No additional charges.

### Example: Cost Estimation
- **Storage Class**: Amazon S3 Standard.
- **Storage Size**: 1 TB of data.
- **Requests**: 10,000 GET requests and 1,000 PUT requests.
- **Data Transfer Out**: 100 GB to another region.

---

## Key Takeaways

- **Amazon S3** is a fully managed cloud storage service.
- **Objects** are stored in **buckets**, with virtually unlimited capacity.
- **Storage Classes** are designed for different use cases (e.g., frequent access, infrequent access, archiving).
- **Pricing** is based on storage, requests, and data transfer out.
- **Access** is available through the AWS Management Console, CLI, SDKs, and REST endpoints.

---

## Additional Notes and Examples

### Example: Uploading an Object to Amazon S3 via AWS CLI
```bash
aws s3 cp myfile.txt s3://my-bucket/myfile.txt
```
- This command uploads `myfile.txt` to the `my-bucket` bucket.

### Example: Setting Up Static Website Hosting
1. **Create a Bucket**: `my-static-website`
2. **Upload Files**: HTML, CSS, JavaScript files.
3. **Enable Static Website Hosting**:
   - Go to the bucket properties in the AWS Management Console.
   - Enable "Static website hosting" and specify the index document (e.g., `index.html`).
4. **Access the Website**:
   - URL: `http://my-static-website.s3-website-<region>.amazonaws.com`

### Example: Cross-Region Replication
- **Source Bucket**: `my-bucket-us-east-1` (US East - N. Virginia)
- **Destination Bucket**: `my-bucket-eu-west-1` (EU - Ireland)
- **Configuration**: Enable cross-region replication in the bucket settings.
- **Benefit**: Data is automatically replicated to the destination bucket for disaster recovery.

### Example: Lifecycle Policy for Archiving
- **Policy**: Move objects to Amazon S3 Glacier after 30 days.
- **Configuration**:
  - Go to the bucket lifecycle settings.
  - Add a rule to transition objects to Glacier after 30 days.
- **Benefit**: Reduce storage costs for infrequently accessed data.

---

## Conclusion

Amazon S3 is a versatile and scalable storage solution that can be used for a wide range of applications, from hosting static websites to storing large datasets for big data processing. By understanding the different storage classes, pricing models, and access methods, you can effectively use Amazon S3 to meet your storage needs.