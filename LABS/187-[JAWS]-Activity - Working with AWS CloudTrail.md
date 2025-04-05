# AWS CloudTrail Investigation Lab Guide

## Lab Overview
This lab demonstrates how to use AWS CloudTrail to investigate security incidents in your AWS environment. You'll play the role of a security analyst investigating a hack of the Café website, using various tools to analyze CloudTrail logs and identify the attacker.

## Activity Objectives
After completing this activity, you will be able to:
- Configure a CloudTrail trail
- Analyze CloudTrail logs using multiple methods
- Import CloudTrail data into Athena for SQL queries
- Identify security vulnerabilities and remediate them
- Secure an EC2 instance after a compromise

## Business Context
The Café leadership team discovered their website was hacked. As the security analyst, you need to:
1. Discover who made unauthorized changes
2. Determine how they gained access
3. Remediate the security issues
4. Prevent future incidents

## Detailed Step-by-Step Guide

### Task 1: Initial Setup and Website Observation

#### Step 1.1: Modify Security Group
1. Navigate to EC2 → Instances
2. Select "Café Web Server (WebSecurityGroup)"
3. In Security tab, click the security group link
4. Edit inbound rules:
   - Add SSH (port 22) access restricted to your IP (CIDR with /32)
   - **Important:** Verify it's not open to 0.0.0.0/0

#### Step 1.2: Verify Website
1. Copy the instance's public IP
2. Access `http://<WebServerIP>/cafe/`
3. Confirm the website appears normal

**Note:** This establishes a baseline before the hack occurs.

### Task 2: Create CloudTrail and Detect Hack

#### Step 2.1: Create CloudTrail Trail
1. Navigate to CloudTrail
2. Create trail named exactly "monitor"
3. Configuration:
   - Create new S3 bucket (name starts with "monitoring")
   - AWS KMS alias: Your initials + "-KMS" (e.g., "kc-KMS")
4. Complete creation wizard with defaults

**Why exact name?** Some AWS services reference trails by name, so consistency is important.

#### Step 2.2: Observe the Hack
1. Refresh the café website (may need Shift+Refresh)
2. Notice the hacked content (inappropriate image)
3. Investigate EC2 security group:
   - Unauthorized SSH rule added (0.0.0.0/0)
   
**Analysis:** The security group change allowed the attacker SSH access, which they used to modify the website.

### Task 3: Analyze CloudTrail Logs

#### Step 3.1: Connect to EC2 Instance
**Windows Users:**
1. Download PPK file
2. Use PuTTY to SSH into instance
3. Authenticate with the PPK key

**Mac/Linux Users:**
1. Download PEM file
2. Set permissions: `chmod 400 labsuser.pem`
3. SSH: `ssh -i labsuser.pem ec2-user@<public-ip>`

#### Step 3.2: Download CloudTrail Logs
1. Create directory: `mkdir ctraillogs && cd ctraillogs`
2. List S3 buckets: `aws s3 ls`
3. Download logs: `aws s3 cp s3://monitoring####/ . --recursive`
4. Extract: `gunzip *.gz`

**Note:** If no logs appear, wait 5 minutes as CloudTrail delivers logs periodically.

#### Step 3.3: Analyze with grep
1. View log structure: `cat <file> | python -m json.tool`
2. Search for web server IP activity:
   ```bash
   ip=<WebServerIP>
   for i in $(ls); do echo $i && cat $i | python -m json.tool | grep sourceIPAddress; done
   ```
3. Search for event names:
   ```bash
   for i in $(ls); do echo $i && cat $i | python -m json.tool | grep eventName; done
   ```

**Example Finding:** Look for `AuthorizeSecurityGroupIngress` events which modify security groups.

#### Step 3.4: Analyze with AWS CLI
1. Find console logins:
   ```bash
   aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin
   ```
2. Find security group modifications:
   ```bash
   aws cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::EC2::SecurityGroup --output text
   ```
3. Narrow to web server's security group:
   ```bash
   region=$(curl http://169.254.169.254/latest/dynamic/instance-identity/document|grep region | cut -d '"' -f4)
   sgId=$(aws ec2 describe-instances --filters "Name=tag:Name,Values='Café Web Server'" --query 'Reservations[*].Instances[*].SecurityGroups[*].[GroupId]' --region $region --output text)
   aws cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::EC2::SecurityGroup --region $region --output text | grep $sgId
   ```

**Analysis:** The CLI provides more targeted queries than grep alone.

### Task 4: Advanced Analysis with Athena

#### Step 4.1: Create Athena Table
1. In CloudTrail, go to Event History → Create Athena Table
2. Use the monitoring bucket for storage location
3. Analyze the auto-generated CREATE TABLE statement
4. Create the table

**Note:** This table structure maps to CloudTrail's JSON schema for SQL querying.

#### Step 4.2: Query Logs in Athena
1. Set query results location: `s3://monitoring####/results/`
2. Run initial query:
   ```sql
   SELECT * FROM cloudtrail_logs_monitoring#### LIMIT 5
   ```
3. Refine query to key columns:
   ```sql
   SELECT useridentity.userName, eventtime, eventsource, eventname, requestparameters 
   FROM cloudtrail_logs_monitoring#### 
   LIMIT 30
   ```

#### Challenge: Identify the Hacker
Use SQL queries to find:
1. Who modified the security group
2. When they did it
3. Their IP address
4. Access method (console/API)

**Solution Query:**
```sql
SELECT useridentity.userName, eventtime, eventsource, eventname, sourceipaddress, requestparameters
FROM cloudtrail_logs_monitoring####
WHERE eventsource = 'ec2.amazonaws.com'
AND eventname LIKE '%SecurityGroup%'
ORDER BY eventtime DESC
```

**Expected Findings:**
- User: "chaos"
- Action: "AuthorizeSecurityGroupIngress"
- Time: [timestamp of attack]
- IP: [attacker's IP]
- Method: Likely API call via AWS CLI

### Task 5: Remediation and Security Hardening

#### Step 5.1: Remove Attacker Access
1. Check logged in users: `who`
2. Find attacker sessions: `sudo aureport --auth`
3. Kill attacker process: `sudo kill -9 [PID]`
4. Delete attacker user: `sudo userdel -r chaos-user`

#### Step 5.2: Secure SSH
1. Edit SSH config: `sudo vi /etc/ssh/sshd_config`
   - Disable password authentication
   - Enable only key-based auth
2. Restart SSH: `sudo service sshd restart`
3. Remove insecure security group rule

**Security Best Practice:** Always disable password authentication for SSH in cloud environments.

#### Step 5.3: Restore Website
1. Navigate to web directory: `cd /var/www/html/cafe/images/`
2. Restore backup: `sudo mv Coffee-and-Pastries.backup Coffee-and-Pastries.jpg`
3. Verify website displays correctly

#### Step 5.4: Delete IAM User
1. Navigate to IAM → Users
2. Delete the "chaos" user
3. Confirm deletion

**Least Privilege Principle:** Regularly review IAM users and remove unnecessary accounts.

## Key Findings and Remediation

### Attack Timeline
1. Attacker ("chaos" user) used AWS credentials to:
   - Modify security group (open SSH to 0.0.0.0/0)
2. Accessed instance via SSH:
   - Created "chaos-user" OS account
   - Modified SSH config to allow password auth
   - Defaced website
   - Created backup of original image

### Security Improvements Implemented
1. **Detection:**
   - Enabled CloudTrail logging
   - Established monitoring for critical changes
2. **Remediation:**
   - Removed unauthorized access
   - Restored original configuration
3. **Prevention:**
   - Hardened SSH configuration
   - Removed compromised IAM user
   - Implemented security group best practices

## Best Practices for Cloud Security

1. **Monitoring:**
   - Enable CloudTrail in all regions
   - Store logs in separate, secure S3 bucket
   - Enable log file validation

2. **Access Control:**
   - Follow principle of least privilege
   - Regularly review IAM users and permissions
   - Require MFA for privileged users

3. **Instance Security:**
   - Restrict SSH access to known IPs
   - Disable password authentication
   - Regularly patch and update systems

4. **Incident Response:**
   - Establish investigation procedures
   - Document remediation steps
   - Conduct post-mortem analysis

## Conclusion

This lab demonstrated a complete security investigation using AWS tools:
1. **Detection:** CloudTrail provided audit logs of all API activity
2. **Investigation:** Multiple analysis methods (grep, AWS CLI, Athena) uncovered the attack
3. **Remediation:** Removed attacker access and restored systems
4. **Prevention:** Implemented security hardening measures

By implementing these practices, organizations can better detect, investigate, and prevent security incidents in their AWS environments.