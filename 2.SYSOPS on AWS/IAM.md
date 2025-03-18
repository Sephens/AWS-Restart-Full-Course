
# AWS Identity and Access Management (IAM) Review

## What You Will Learn

### At the Core of This Lesson
You will learn how to:
- Define **AWS Identity and Access Management (IAM)**.
- Recall the types of security credentials and the concepts of IAM users and IAM roles.
- Describe IAM best practices.

---

## IAM Overview

### What is IAM?
- **IAM** is a service that helps securely control access to AWS resources.
- It allows you to manage **authentication** (who can access) and **authorization** (what they can do).

### Key Features of IAM
- **Centralized Management:** Manage access to AWS resources centrally.
- **Users, Groups, and Roles:** Create and manage IAM users, groups, and roles.
- **Policies:** Apply policies to control access to resources.

**Example:**
- Use IAM to control who can terminate EC2 instances or access S3 buckets.

---

## Access to AWS Services

### Programmatic Access
- **Access Key ID and Secret Access Key:** Used for programmatic access via AWS CLI, SDKs, and APIs.
- **AWS CLI Example:**
  ```bash
  $ aws configure
  ```

### Console Access
- **IAM User Name and Password:** Used for accessing the AWS Management Console.
- **Multi-Factor Authentication (MFA):** Adds an extra layer of security.

**Example:**
- Enable MFA for IAM users to secure console access.

---

## Types of Security Credentials

| Type of Credentials | Description |
|----------------------|-------------|
| **Email and Password** | Associated with the AWS account root user. |
| **IAM User Name and Password** | Used for console access. |
| **Access Keys** | Used for programmatic access (AWS CLI, SDKs). |
| **MFA** | Adds an extra layer of security. |
| **Key Pairs** | Used for specific services like EC2. |

**Best Practice:**
- Avoid using the root user for daily tasks. Instead, create IAM users with limited permissions.

---

## Policies and Permissions

### Types of Policies
1. **Identity-Based Policies:** Attached to IAM users, groups, or roles.
2. **Resource-Based Policies:** Attached to resources (e.g., S3 bucket policies).
3. **AWS Organizations SCPs:** Apply permissions boundaries to AWS Organizations.
4. **Access Control Lists (ACLs):** Control access to resources.

**Example IAM Policy:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "MFA-Access",
      "Effect": "Allow",
      "Action": "ec2:*",
      "Resource": "*",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
```

---

## Using IAM Roles

### What are IAM Roles?
- **IAM Roles** allow AWS services or users to temporarily assume permissions.
- **Use Cases:**
  - Cross-account access.
  - Single sign-on (SSO) using SAML 2.0 or OAuth 2.0.

**Example:**
- An EC2 instance can assume a role to access S3 buckets.

---

## IAM Permission Examples

### User-Based Permissions
- **Example:** User Xiulan has Read, Write, and List access to Resource X.

### Resource-Based Permissions
- **Example:** Resource X can be accessed by Carlos, Wang, Efua, and Mateo with varying levels of access.

---

## IAM Best Practices

1. **Avoid Using Root User:** Use IAM users for daily tasks.
2. **Principle of Least Privilege:** Grant only the permissions needed.
3. **Use IAM Roles:** For cross-account access and temporary permissions.
4. **Enable MFA:** For added security.
5. **Rotate Credentials Regularly:** Especially access keys.

**Example:**
- Enable MFA for all IAM users with administrative privileges.

---

## Checkpoint Questions

1. **True or False:** SysOps professionals can use IAM to configure authorization for users.
   - **Answer:** True.

2. **True or False:** As a best practice, AWS recommends using the root account for everyday tasks.
   - **Answer:** False.

3. **Which option does not represent an IAM identity?**
   - **Answer:** Policy.

---

## Key Ideas

- **IAM Identities:** Users, groups, and roles.
- **Access Methods:** Console, AWS CLI, or programmatically.
- **IAM Policies:** JSON documents that define permissions.
- **Roles:** Allow temporary assumption of permissions.
- **Best Practices:** Avoid root user, use least privilege, enable MFA, and use roles for cross-account access.

---

## Thank You

© 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. Correlation, feedback, or other questions? Contact us at [http://anazon.aws.amazon.com/fr/corrector/aws-routing](https://anazon.aws.amazon.com/fr/corrector/aws-routing). All trademarks are the property of their owners.