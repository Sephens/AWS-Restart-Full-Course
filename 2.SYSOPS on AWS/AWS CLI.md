# AWS Command Line Interface (AWS CLI)

## What You Will Learn

### At the Core of the Lesson
You will learn how to:
- Define the **AWS Command Line Interface (AWS CLI)**.
- Explain the steps for installing the AWS CLI on Linux.
- Describe details about the AWS CLI.

---

## AWS CLI Overview

### Three Ways to Use AWS
1. **AWS Management Console:** Provides an intuitive graphical interface for AWS services.
2. **SDKs:** Call AWS services APIs from most major programming languages (e.g., Python, Ruby, .NET, Java).
3. **AWS CLI:** Provides access to AWS services through a command-line interface on Linux, macOS, or Windows.

### AWS CLI Features
- **Flexibility:** Create custom tools and scripts for AWS services.
- **Automation:** Automate tasks like launching EC2 instances or managing S3 buckets.
- **Cross-Platform:** Available for Linux, macOS, and Windows.

**Example:**
- Use the AWS CLI to create a script that launches EC2 instances with specific tags or AMIs.

---

## Introduction to the AWS CLI

### AWS CLI Configuration
After installing the AWS CLI, you can configure it using the `aws configure` command:
```bash
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```

### AWS CLI Output Formats
- **Table:** Human-readable tabular format.
- **JSON:** Default format, useful for programmatic usage.
- **Text:** Tab-delimited lines, useful for scripting.

**Example:**
- To set the output format to table:
  ```bash
  $ export AWS_DEFAULT_OUTPUT="table"
  ```

---

## Install the AWS CLI on Linux

### Steps to Install AWS CLI on Linux
1. **Download the AWS CLI package:**
   ```bash
   $ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   ```
2. **Extract the package:**
   ```bash
   $ unzip awscliv2.zip
   ```
3. **Run the install program:**
   ```bash
   $ sudo ./aws/install
   ```
4. **Verify the installation:**
   ```bash
   $ aws --version
   ```
   Expected output:
   ```
   aws-cli/2.4.5 Python/3.8.8 Linux/4.14.133-113.105.amzn2.x86_64 botocore/2.4.5
   ```

---

## Using the AWS CLI

### Command-Line Format
The AWS CLI command structure is as follows:
```bash
aws <serviceName> <operation> [options and parameters]
```

**Example:**
- Stop an EC2 instance:
  ```bash
  $ aws ec2 stop-instances --instance-ids i-1234567890abcdef0 --output json
  ```
- Launch an EC2 instance using a JSON file:
  ```bash
  $ aws ec2 run-instances --cli-input-json file://webserver.json
  ```

### AWS CLI Help
Use the `help` command to explore available commands and their syntax:
```bash
$ aws help
$ aws ec2 help
$ aws ec2 describe-instances help
```

**Example:**
- List available EC2 commands:
  ```bash
  $ aws ec2 help
  ```

---

## AWS CLI Output (in JSON Format)

### Example: Describe EC2 Instances
```bash
$ aws ec2 describe-instances
{
    "Reservations": [
        {
            "Groups": [],
            "Instances": [
                {
                    "ImageId": "ami-023bec20",
                    "InstanceId": "i-068035fce1e9abcc9",
                    "InstanceType": "m5.large",
                    "KeyName": "mykeypair",
                    "LaunchTime": "2019-06-15T11:55:16.000Z",
                    "Placement": {
                        "AvailabilityZone": "us-west-2a"
                    },
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "PublicIpAddress": "54.252.186.255",
                    "PublicDnsName": "ec2-54-252-186-255.us-west-2.compute.amazonaws.com",
                    "PrivateIpAddress": "10.0.50.14"
                }
            ]
        }
    ]
}
```

---

## Query Option

### Use the `--query` Option to Filter Output
- Show only the first EC2 instance:
  ```bash
  $ aws ec2 describe-instances --query 'Reservations[0].Instances[0]'
  ```
- Show the state of the first instance:
  ```bash
  $ aws ec2 describe-instances --query 'Reservations[0].Instances[0].State.Name'
  ```
- Show the state of all instances:
  ```bash
  $ aws ec2 describe-instances --query 'Reservations[*].Instances[*].State.Name'
  ```

---

## Filter Option

### Use the `--filter` Option to Restrict Results
- Show only Windows instances:
  ```bash
  $ aws ec2 describe-instances --filter "Name=platform,Values=windows"
  ```
- Show only `t2.micro` and `t2.small` instances:
  ```bash
  $ aws ec2 describe-instances --query "Reservations[*].Instances[*].InstanceId" --filter "Name=instance-type,Values=t2.micro,t2.small"
  ```

---

## Dry-Run Option

### Use the `--dry-run` Option to Test Permissions
- Check if you have permissions to launch an EC2 instance:
  ```bash
  $ aws ec2 run-instances --image-id ami-la2b3c4d --count 1 --instance-type c5.large --key-name MyKeyPair --security-groups MySecurityGroup --dry-run
  ```

**Output:**
- If authorized:
  ```
  An error occurred (DryRunOperation) when calling the RunInstances operation: Request would have succeeded, but DryRun flag is set.
  ```
- If unauthorized:
  ```
  An error occurred (UnauthorizedOperation) when calling the RunInstances operation: You are not authorized to perform this operation.
  ```

---

## Common AWS CLI Commands

### Amazon EC2 Commands
- **Launch an EC2 instance:**
  ```bash
  $ aws ec2 run-instances
  ```
- **Describe EC2 instances:**
  ```bash
  $ aws ec2 describe-instances
  ```
- **Create an EBS volume:**
  ```bash
  $ aws ec2 create-volume
  ```
- **Create a VPC:**
  ```bash
  $ aws ec2 create-vpc
  ```

### Amazon S3 Commands
- **List S3 buckets:**
  ```bash
  $ aws s3 ls
  ```
- **Copy files to/from S3:**
  ```bash
  $ aws s3 cp
  ```
- **Move files in S3:**
  ```bash
  $ aws s3 mv
  ```
- **Delete files in S3:**
  ```bash
  $ aws s3 rm
  ```

---

## Checkpoint Questions

1. **Which operating systems can the AWS CLI be installed on?**
   - Linux, macOS, and Windows.

2. **How do system operators check which version of the AWS CLI they are using in Linux?**
   - Use the command:
     ```bash
     $ aws --version
     ```

3. **What is the purpose of the `--dry-run` option in an AWS CLI command?**
   - It checks whether you have the required permissions to run a command without actually executing it.

---

## Key Ideas

- The AWS CLI allows you to interact with AWS services using commands entered in a command-line tool.
- The structure of an AWS CLI command is:
  ```bash
  aws <serviceName> <operation> [options and parameters]
  ```
- The `--filter` option runs on the server side and returns results that match a filter condition.
- The `--query` option runs on the client side and limits how much of the returned data is displayed.
- The `--dry-run` option checks permissions without executing the command.

---

## Thank You

© 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. Correlation, feedback, or other questions? Contact us at [http://anazon.aws.amazon.com/products/aws-raising](https://anazon.aws.amazon.com/products/aws-raising). All trademarks are the property of their owners.

---
