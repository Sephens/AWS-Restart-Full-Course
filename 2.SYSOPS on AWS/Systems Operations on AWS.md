# Systems Operations on AWS

## What You Will Learn

### At the Core of This Lesson
You will learn how to describe **systems operations (SysOps)** and **automation** in the cloud.

This lesson provides an introduction to systems operations (SysOps). It describes the overall responsibilities of a SysOps professional and highlights the importance of automation in the cloud.

---

## What is Systems Operations (SysOps)?

### Definition
**Systems operations (SysOps)** is concerned with the deployment, administration, and monitoring of systems and network resources in an **automatable and reusable manner**.

### Key Responsibilities
SysOps supports technical systems by monitoring them and ensuring that their performance meets expectations and is trouble-free. SysOps professionals typically need to understand the entire system environment.

### Benefits of SysOps
- **Scalability:** Ability to configure and manage thousands of servers and devices in a repeatable way.
- **Error Reduction:** Replace manual processes with automated ones to reduce errors.
- **Real-Time Visibility:** Gain real-time insights into the state of the infrastructure through monitoring.

---

## Systems Operations: Responsibilities

### Overview
SysOps professionals are involved in many—and often all—facets of delivering IT solutions. Their responsibilities include:

1. **Build:** Create separate environments for development, test, and production.
2. **Test:** Test backup and disaster recovery procedures.
3. **Deploy:** Deploy applications and workloads into their runtime environment.
4. **Monitor:** Monitor the health and performance of infrastructure resources.
5. **Maintain:** Apply patches and upgrades in a consistent and regular manner.
6. **Safeguard:** Apply and enforce security measures across all infrastructure layers.

### Automation in SysOps
SysOps professionals typically use automation due to the large size of the infrastructure. Automation helps in:
- **Repeatable Deployment:** Deploy infrastructure and applications on demand.
- **Self-Describing Systems:** Create systems that can describe their own state and configuration.
- **Secure Systems:** Build well-tested, secure systems.

---

## Systems Operations in the Cloud

### Cloud Computing and Automation
Cloud computing provides organizations the ability to automate the development, testing, and deployment of complex IT operations. Automation in the cloud offers:
- **Repeatable Deployment:** Deploy infrastructure and applications on demand.
- **Self-Describing Systems:** Systems that can describe their own state and configuration.
- **Secure Systems:** Build well-tested, secure systems.

### Automation Tools
Automation can be achieved through:
- **Scripts:** Linux shell scripts, Python, Ruby, or C# applications.
- **Templates:** AWS CloudFormation templates for infrastructure as code.

**Example:**
- In the cloud, you can provision computing resources in minutes using automated scripts.
- In an on-premises environment, the same process could take days and require manual intervention.

For more information, see [Getting started with AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html).

---

## Checkpoint Questions

1. **True or False:** SysOps supports technical systems by monitoring systems and helping ensure that system performance is accurate and trouble-free.
   - **Answer:** True.

2. **True or False:** SysOps involves the responsibilities and tasks required to build (create), test, deploy, monitor, maintain, and safeguard complex computing systems.
   - **Answer:** True.

3. **True or False:** SysOps professionals can create reusable infrastructure templates by using the AWS Identity and Access Management (IAM) service.
   - **Answer:** False. SysOps professionals use **AWS CloudFormation** to create reusable infrastructure templates.

---

## Key Ideas

- **SysOps supports technical systems** by monitoring them and ensuring their performance meets expectations.
- **SysOps professionals** are responsible for the administration of large, multiuser systems.
- **Automation** provides the ability to create deployable, reusable infrastructure in the cloud.
- **SysOps includes** the development of reusable infrastructure templates.

---

## Troubleshooting Knowledge Base Project

### Project Introduction
- **Objective:** Build a **Troubleshooting Knowledge Base**.
- **Purpose:** Document common technical challenges and solutions encountered during AWS Cloud deployments.

### Project Goals
- **Describe** common technical challenges in deploying, upgrading, and maintaining AWS Cloud deployments.
- **Explain** how to overcome specific technical challenges by adjusting deployment configurations.
- **Present** troubleshooting techniques to stakeholders.

### Activity Steps
1. **Open the Troubleshooting Knowledge Base Template** for editing.
2. **Create New Entries** as you encounter troubleshooting situations.

### Categories of Focus
- **Security and Compliance**
- **Foundational IT**

### Example Entries
| Issue # | Category | Issue Description | Symptoms | Root Cause Analysis |
|---------|----------|-------------------|----------|---------------------|
| **Example One** | Networking | Application on Amazon EC2 instance; connectivity issue | Could not connect to an existing website. | The instance was no longer running. |
| **Example Two** | Networking | SSH to EC2 instance issue | Could not SSH to a running EC2 instance. | Incorrect permissions on the private key and security group settings. |
| **Example Three** | Foundational IT | Out of disk space on an EC2 instance | Application stopped running. | The instance ran out of disk space. |
| **Example Four** | Foundational IT | Linux service stopped running | Web page hosted on an instance was not loading. | The web server wasn’t running. |

---

## Thank You

© 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. Correlation, feedback, or other questions? Contact us at [http://anazon.aws.amazon.com/fr/corrector/aws-routing](https://anazon.aws.amazon.com/fr/corrector/aws-routing). All trademarks are the property of their owners.

Thank you for completing this lesson.

---

## Additional Notes and Examples

### Example of Automation in SysOps
- **Scenario:** A company needs to deploy a web application across multiple environments (development, test, production).
- **Traditional Approach:** Manually set up servers, install software, and configure each environment.
- **Cloud Approach:** Use **AWS CloudFormation** to define the infrastructure as code. Deploy the same template across all environments with minimal manual intervention.

### Example of Troubleshooting Knowledge Base Entry
- **Issue:** EC2 instance running out of disk space.
- **Symptoms:** Application stops running, disk usage at 100%.
- **Root Cause:** Log files were not rotated, leading to excessive disk usage.
- **Solution:** Implement log rotation and increase disk size using Amazon EBS.

### Example of SysOps Automation with AWS CLI
- **Scenario:** Automate the deployment of an EC2 instance with specific configurations.
- **Steps:**
  1. Use the **AWS CLI** to create an EC2 instance.
  2. Automate the installation of required software using a shell script.
  3. Use **AWS CloudFormation** to manage the entire infrastructure as code.

By leveraging automation and documenting troubleshooting steps, SysOps professionals can ensure efficient and reliable system operations in the cloud.