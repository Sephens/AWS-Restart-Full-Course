# AWS Systems Manager

## What You Will Learn

### At the Core of the Lesson
You will learn how to identify the capabilities of **AWS Systems Manager**.

---

## Systems Manager Overview

### What is AWS Systems Manager?
- A collection of capabilities that help you manage applications and infrastructure running in the AWS Cloud.
- Automates configuration and management of systems on-premises and in the cloud.

### Key Features
- **Software Inventory**: Collects software inventory.
- **OS Management and Configuration**: Configures Microsoft Windows and Linux operating systems.
- **OS Patches**: Applies operating system patches.
- **System Images**: Creates system images.

---

## Capabilities Overview

### Core Capabilities of AWS Systems Manager
1. **Documents**: Define actions performed on managed instances.
2. **Automation**: Automates common IT tasks.
3. **Run Command**: Runs predefined commands on EC2 instances.
4. **Session Manager**: Securely connects to instances without opening inbound ports.
5. **Patch Manager**: Automates OS and software patching.
6. **Maintenance Windows**: Schedules maintenance tasks.
7. **State Manager**: Maintains consistent configurations.
8. **Parameter Store**: Centralized store for configuration data and secrets.
9. **Inventory**: Collects information about instances and installed software.

---

## Documents

### What are Documents?
- Define the actions Systems Manager performs on managed instances.
- Types:
  - **Owned by Amazon**: Predefined documents.
  - **Owned by You**: Custom documents.
  - **Shared with You**: Shared from another account.

### Example
- **Command Documents**: Used by State Manager and Run Command.
- **Automation Runbooks**: Used by Systems Manager Automation.

---

## Automation

### What is Automation?
- Safely automates common and repetitive IT tasks across AWS resources.

### Steps to Use Automation
1. **Create an Automation Document**: Define steps and parameters.
2. **Run the Automation Document**: Automatically performs steps.
3. **Monitor and Verify Results**: Confirm expected outcomes.

### Example
- Remediate unreachable instances.
- Create golden Amazon Machine Images (AMIs).
- Patch instances.

---

## Run Command

### What is Run Command?
- Automates common administrative tasks and configuration changes at scale.

### Key Features
- Use predefined commands or create custom ones.
- Choose instances manually or by tags.
- Run commands immediately or on a schedule.

### Example Commands
- **AWS-InstallWindowsUpdates**: Installs updates on Windows instances.
- **AWS-RunPowerShellScript**: Runs PowerShell scripts.
- **AWS-RunShellScript**: Runs shell scripts on Linux/macOS.

---

## Session Manager

### What is Session Manager?
- Securely connects to instances without opening inbound ports or using bastion hosts.

### Key Features
- Interactive browser-based shell.
- Tracks user sessions and logs commands.
- Integrates with AWS CloudTrail, Amazon S3, and Amazon CloudWatch Logs.

### Example
- Audit user access to instances.
- Log commands for compliance.

---

## Patch Manager

### What is Patch Manager?
- Automates OS and software patching across EC2 instances or on-premises machines.

### Steps to Use Patch Manager
1. **Create a Patch Baseline**: Define rules for patches.
2. **Define a Maintenance Window**: Schedule patching.
3. **Apply Patches**: Automatically patch and reboot instances.
4. **Audit Results**: Review patch compliance.

### Example
- Patch a group of EC2 instances during a maintenance window.

---

## Maintenance Windows

### What are Maintenance Windows?
- Schedule windows for administrative and maintenance tasks.

### Steps to Use Maintenance Windows
1. **Create a Maintenance Window**: Define name, schedule, and duration.
2. **Assign Targets**: Specify resources to update.
3. **Assign Tasks**: Define tasks to run (e.g., Run Command, Automation workflows).
4. **Review Task Status**: Monitor task completion.

### Example
- Patch operating systems or install software during a maintenance window.

---

## State Manager

### What is State Manager?
- Maintains consistent configurations for EC2 or on-premises instances.

### Steps to Use State Manager
1. **Choose or Create a Document**: Define the desired state.
2. **Associate Instances**: Target instances for the configuration.
3. **Specify a Schedule**: Define how often to apply the state.
4. **Output Data (Optional)**: Write command output to Amazon S3.

### Example
- Ensure all instances have the same security settings.

---

## Parameter Store

### What is Parameter Store?
- Centralized store for configuration data and secrets.

### Key Features
- Stores data as name-value pairs.
- Supports plain text or encrypted data.
- Integrates with AWS Key Management Service (KMS).

### Example
- Store database passwords securely and retrieve them using the AWS CLI.

---

## Inventory

### What is Inventory?
- Collects information about instances and installed software.

### Key Features
- Tracks application data, files, network configurations, and more.
- Supports managing application assets and tracking licenses.

### Example
- Monitor installed software across multiple instances.

---

## Checkpoint Questions

1. **What are some ways that Systems Manager helps users?**
   - Collect software inventory, configure operating systems, apply OS patches, and create system images.

2. **Which Systems Manager capability defines the actions that Systems Manager performs on your managed instances?**
   - **Documents**

3. **Which Systems Manager capability can you use to manage your EC2 instances through an interactive browser-based shell in the AWS Management Console?**
   - **Session Manager**

---

## Key Ideas

- **Automation**: Safely automate common IT tasks across AWS resources.
- **Patch Manager and Maintenance Windows**: Apply OS patches based on a predefined schedule.
- **Suite of Capabilities**: Automate operational tasks across AWS and on-premises resources.

---

## Thank You

© 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. Correlation, feedback, or other questions? Contact us at [http://anazon.aws.amazon.com/fr/corrector/aws-routing](https://anazon.aws.amazon.com/fr/corrector/aws-routing). All trademarks are the property of their owners.