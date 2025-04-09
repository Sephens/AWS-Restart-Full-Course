# Monitoring Infrastructure Lab Guide

## Lab Overview
This lab demonstrates how to use various AWS monitoring services to monitor your applications and infrastructure. You'll learn to:
- Install and configure the CloudWatch agent
- Monitor application logs with CloudWatch Logs
- Monitor system metrics with CloudWatch Metrics
- Create real-time notifications with CloudWatch Events
- Track infrastructure compliance with AWS Config

## Task 1: Installing the CloudWatch Agent

### Step 1: Access AWS Systems Manager
1. Navigate to AWS Systems Manager from the AWS Management Console
2. Select "Run Command" from the left navigation pane

**Note:** The Run Command feature allows you to remotely execute commands across multiple instances without needing SSH access.

### Step 2: Run the Install Command
1. Click "Run a Command"
2. Select "AWS-ConfigureAWSPackage"
3. Configure parameters:
   - Action: Install
   - Name: AmazonCloudWatchAgent
   - Version: latest
4. Under Targets, select "Choose instances manually" and check the "Web Server" instance
5. Click "Run"

**Example:** This is similar to running a package manager command like `yum install` or `apt-get install`, but done remotely through AWS Systems Manager.

### Step 3: Verify Installation
1. Wait for status to show "Success"
2. View output to confirm successful installation
   - Expected output: "Successfully installed arn:aws:ssm:::package/AmazonCloudWatchAgent"

### Step 4: Create Parameter Store Configuration
1. Navigate to Parameter Store
2. Create a new parameter:
   - Name: Monitor-Web-Server
   - Description: Collect web logs and system metrics
   - Value: Paste the provided JSON configuration

**Key Configuration Elements:**
- Logs collection:
  - HTTP access logs (`/var/log/httpd/access_log`)
  - HTTP error logs (`/var/log/httpd/error_log`)
- Metrics collection:
  - CPU usage (idle, iowait, user, system)
  - Disk usage (percent used, inodes free)
  - Memory usage (percent used)
  - Swap usage (percent used)

### Step 5: Start the CloudWatch Agent
1. Run another command using "AmazonCloudWatch-ManageAgent"
2. Configure parameters:
   - Action: configure
   - Mode: ec2
   - Optional Configuration Source: ssm
   - Optional Configuration Location: Monitor-Web-Server
   - Optional Restart: yes
3. Target the Web Server instance again
4. Run the command and verify success

**Why Parameter Store?** Using Parameter Store allows for centralized configuration management that can be reused across multiple instances.

## Task 2: Monitoring Application Logs with CloudWatch Logs

### Step 1: Generate Log Data
1. Access the web server using the provided IP
2. Attempt to access non-existent pages (e.g., `/start`) to generate 404 errors

### Step 2: View Logs in CloudWatch
1. Navigate to CloudWatch → Log groups
2. View both HttpAccessLog and HttpErrorLog groups
3. Examine log streams containing your test requests

**Note:** The logs are automatically collected from the EC2 instance and centralized in CloudWatch, making them accessible without needing direct server access.

### Step 3: Create Metric Filter
1. Select HttpAccessLog group
2. Create metric filter with pattern:
   ```
   [ip, id, user, timestamp, request, status_code=404, size]
   ```
3. Test the pattern against your instance's log stream
4. Name the filter "404Errors"
5. Configure metric details:
   - Namespace: LogMetrics
   - Metric name: 404Errors
   - Metric value: 1

**How Filter Patterns Work:** The pattern defines how to parse the log fields and only matches entries where status_code=404.

### Step 4: Create Alarm
1. Create alarm from the 404Errors metric
2. Configure:
   - Period: 1 minute
   - Threshold: >= 5 errors
3. Set up SNS notification with your email
4. Confirm subscription via email

### Step 5: Trigger Alarm
1. Generate at least five 404 errors by accessing invalid URLs
2. Wait 1-2 minutes for alarm to trigger
3. Verify alarm state changes to "Alarm" and email notification is received

**Use Case:** This setup helps detect when your application has broken links or missing resources that users are trying to access.

## Task 3: Monitoring Instance Metrics with CloudWatch

### Step 1: View EC2 Metrics
1. Navigate to EC2 → Instances
2. Select Web Server and view Monitoring tab
3. Examine default metrics (CPU, network, disk I/O)

**Limitation:** These are external metrics that don't show internal instance state like memory usage.

### Step 2: View CloudWatch Agent Metrics
1. Navigate to CloudWatch → Metrics
2. View CWAgent metrics:
   - Disk space metrics under "device, fstype, host, path"
   - Memory metrics under "host"

**Advantage:** These metrics provide visibility into internal instance health that isn't available from standard EC2 metrics.

## Task 4: Creating Real-Time Notifications

### Step 1: Create CloudWatch Event Rule
1. Navigate to CloudWatch → Events → Rules
2. Create rule named "Instance_Stopped_Terminated"
3. Configure event pattern:
   - Service: EC2
   - Event Type: Instance State-change Notification
   - States: stopped, terminated
4. Set target to existing SNS topic
5. Create rule

### Step 2: Test Notification
1. Stop the Web Server instance
2. Verify notification email is received with instance state change details

**Alternative Approach:** For better formatted messages, you could trigger a Lambda function to process and format the event data before sending the notification.

## Task 5: Monitoring Infrastructure Compliance

### Step 1: Set Up AWS Config
1. Navigate to AWS Config
2. Complete initial setup if needed (click through defaults)

### Step 2: Add Required Tags Rule
1. Add "required-tags" managed rule
2. Configure to require "project" tag
3. Save rule

### Step 3: Add EBS Volume Check Rule
1. Add "ec2-volume-inuse-check" managed rule
2. Save rule

### Step 4: Review Compliance
1. Wait for rules to evaluate (may take several minutes)
2. View compliance results:
   - required-tags: Web Server should be compliant (has project tag)
   - ec2-volume-inuse-check: Should show one attached (compliant) and one unattached (non-compliant) volume

**Compliance Use Case:** These rules help enforce organizational standards like proper resource tagging and prevent orphaned resources that incur costs.

## Key Takeaways

1. **Centralized Monitoring**: CloudWatch provides a single place to monitor logs and metrics across your infrastructure.

2. **Proactive Alerting**: You can set up alarms to notify you about issues before they impact users.

3. **Compliance Tracking**: AWS Config helps ensure your infrastructure meets organizational standards.

4. **Hybrid Support**: The CloudWatch agent can monitor both AWS and on-premises resources.

5. **Automation**: Systems Manager Run Command allows for remote management at scale.

## Troubleshooting Tips

1. If metrics don't appear immediately, wait a few minutes as there may be a delay in data collection and reporting.

2. For alarms not triggering, verify:
   - The metric filter pattern matches your log format
   - You've generated enough events to exceed the threshold
   - The evaluation period is appropriate for your use case

3. For AWS Config rules showing "No resources in scope", wait longer as the initial evaluation can take time.

## Best Practices

1. **Log Retention**: Configure appropriate retention periods for your CloudWatch Logs based on compliance requirements.

2. **Metric Resolution**: Use 1-minute resolution for critical metrics, standard resolution for less important ones to optimize costs.

3. **Alarm Design**: Avoid overly sensitive alarms that generate noise, but ensure important issues are caught.

4. **Tagging Strategy**: Implement a consistent tagging strategy to make resources easier to manage and monitor.

5. **Documentation**: Document your monitoring strategy and alert response procedures.