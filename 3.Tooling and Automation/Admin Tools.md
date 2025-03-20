# Administration Tools

## What You Will Learn

### At the Core of the Lesson
You will identify various tools to automate administration.

---

## Software Development Kits (SDKs)

### What are SDKs?
- **SDKs** allow you to access AWS services programmatically and write administrative scripts in different programming languages.
- Supported languages include:
  - .NET
  - C++
  - Go
  - Java
  - JavaScript
  - Node.js
  - PHP
  - Python
  - Ruby

### Key Features
- **Infrastructure as Code (IaC)**: SDKs and APIs enable managing AWS resources through code.
- **Extensive Documentation**: Guides, API references, and community forums are available for each SDK.

### Example
- Use the **AWS SDK for Python (Boto3)** to automate the creation of EC2 instances:
  ```python
  import boto3
  ec2 = boto3.client('ec2')
  response = ec2.run_instances(
      ImageId='ami-0abcdef1234567890',
      InstanceType='t2.micro',
      MinCount=1,
      MaxCount=1
  )
  print(response)
  ```

---

## AWS CloudFormation

### What is CloudFormation?
- A tool to create, update, and delete a set of AWS resources as a single unit.
- Resources are defined in a **template** (JSON or YAML format).
- Templates are used to create **stacks**, which are collections of AWS resources.

### Key Features
- **Preview Changes**: See how proposed changes will impact existing resources.
- **Drift Detection**: Detect differences between the stack’s actual and expected configuration.
- **Custom Extensions**: Use AWS Lambda to add custom logic to templates.

### Example
- **Template Example** (YAML):
  ```yaml
  Resources:
    MyEC2Instance:
      Type: AWS::EC2::Instance
      Properties:
        ImageId: ami-0abcdef1234567890
        InstanceType: t2.micro
  ```

### How CloudFormation Works
1. **Define Resources**: Create a template or use a prebuilt one.
2. **Upload Template**: Upload to CloudFormation or store in Amazon S3.
3. **Create Stack**: CloudFormation provisions the resources.
4. **Manage Stack**: Update, detect drift, or delete the stack.

### Benefits of CloudFormation
- **Reusability**: Use the same template to create multiple stacks.
- **Repeatability**: Deploy the same environment repeatedly.
- **Maintainability**: Ensure configuration consistency across environments.

---

## AWS OpsWorks

### What is OpsWorks?
- A configuration management service that automates server configuration, deployment, and management.
- Based on **Chef** and **Puppet**, popular open-source automation platforms.

### OpsWorks Versions
1. **AWS OpsWorks for Chef Automate**:
   - Fully managed Chef Automate server.
   - Automates tasks like software and OS configurations, continuous compliance, and database setups.

2. **AWS OpsWorks for Puppet Enterprise**:
   - Managed Puppet Enterprise server.
   - Provides workflow automation for orchestration, provisioning, and traceability.

3. **AWS OpsWorks Stacks**:
   - Configuration management service using Chef.
   - Helps configure and operate applications of all sizes.

### Example
- Use OpsWorks to automate the deployment of a web application across multiple EC2 instances.

---

## Checkpoint Questions

1. **Which AWS tool can a developer use to write an automated script in Python to access an AWS service?**
   - **AWS SDK for Python**

2. **In which CloudFormation component would an administrator define the AWS infrastructure resources that they want to provision?**
   - **Template**

3. **Which AWS service provides managed instances of Chef and Puppet?**
   - **OpsWorks**

---

## Key Ideas

- **AWS SDKs**: Provide access to AWS services using APIs in various programming languages.
- **CloudFormation**: Helps create, update, and delete AWS infrastructure predictably and repeatedly.
- **OpsWorks**: Automates configuration management tasks using Chef and Puppet.

---

## Thank You

© 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. Correlation, feedback, or other questions? Contact us at [http://anazon.aws.amazon.com/products/aws-raising](https://anazon.aws.amazon.com/products/aws-raising). All trademarks are the property of their owners.

---

## Additional Notes and Examples

### Example of AWS SDK for Python (Boto3)
- **Use Case**: Automate the creation of an S3 bucket.
  ```python
  import boto3
  s3 = boto3.client('s3')
  s3.create_bucket(Bucket='my-unique-bucket-name')
  ```

### Example of CloudFormation Template
- **Use Case**: Create an S3 bucket using CloudFormation.
  ```yaml
  Resources:
    MyS3Bucket:
      Type: AWS::S3::Bucket
      Properties:
        BucketName: my-unique-bucket-name
  ```

### Example of OpsWorks
- **Use Case**: Automate the deployment of a web application using Chef.
  - Define the application configuration in a Chef recipe.
  - Use OpsWorks to deploy the recipe across multiple EC2 instances.

By leveraging these tools, you can automate and manage your AWS infrastructure efficiently.