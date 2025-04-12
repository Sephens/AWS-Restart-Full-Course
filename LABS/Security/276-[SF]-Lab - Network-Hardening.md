# Network Hardening Using Amazon Inspector and AWS Systems Manager - Detailed Lab Walkthrough

## Lab Overview
This lab focuses on identifying and remediating network security vulnerabilities in an AWS environment using Amazon Inspector and AWS Systems Manager. The scenario involves securing a company's infrastructure by analyzing network configurations, updating security controls, and implementing more secure access methods.

### Key Concepts:
- **Amazon Inspector**: An automated security assessment service that helps identify vulnerabilities in your AWS resources
- **Network Reachability Analysis**: Examines how resources can communicate within your VPC and with external networks
- **Security Groups**: Virtual firewalls that control inbound and outbound traffic for EC2 instances
- **AWS Systems Manager Session Manager**: Provides secure, auditable instance management without needing open inbound ports

## Lab Environment
The environment consists of:
- **BastionServer**: EC2 instance in a public subnet (acts as jump host)
- **AppServer**: EC2 instance in a private subnet (application server)
- Pre-configured IAM roles and AWS services

## Task 1: View EC2 Instances and Add Tags

### Step-by-Step Instructions:

1. **Access EC2 Console**:
   - Navigate to AWS Management Console
   - Select "Services" > "EC2"
   - Ensure "New EC2 Experience" is enabled (top-left corner)

2. **View Instances**:
   - In the left navigation pane, select "Instances"
   - Observe both running instances: BastionServer and AppServer

3. **Tag BastionServer**:
   - Select the "BastionServer" instance
   - Click the "Tags" tab
   - Click "Manage tags"
   - Add a new tag:
     - Key: `SecurityScan`
     - Value: `true`
   - Click "Save"

### Explanation:
- Tags are key-value pairs that help organize and identify AWS resources
- Amazon Inspector uses tags to determine which instances to scan
- The tag `SecurityScan: true` will be used to include this instance in our security assessment

### Example:
This is similar to labeling a server in a data center with "For Security Audit" to indicate it should be included in security checks.

## Task 2: Configure and Run Amazon Inspector

### Step-by-Step Instructions:

1. **Access Amazon Inspector**:
   - Navigate to "Services" > "Security, Identity, & Compliance" > "Inspector"
   - If presented with options, choose "Switch to Inspector Classic"

2. **Initial Setup**:
   - Click "Get started"
   - Select "Advanced setup"

3. **Create Assessment Target**:
   - Name: `Network-Audit`
   - Uncheck "All Instances"
   - For tags:
     - Key: `SecurityScan`
     - Value: `true`
   - Uncheck "Install Agents"
   - Click "Next"

4. **Create Assessment Template**:
   - Name: `Assessment-Template-Network`
   - Under "Rules packages", keep only "Network Reachability-1.1"
   - Duration: "15 Minutes"
   - Uncheck "Assessment Schedule"
   - Click "Next"
   - Click "Create"

5. **Monitor Scan Progress**:
   - In left navigation, select "Assessment runs"
   - Expand your run to view status
   - Wait for status to show "Analysis complete" (3-5 minutes)

### Explanation:
- **Assessment Target**: Defines which resources to scan (in this case, instances with our specific tag)
- **Assessment Template**: Configures what to scan for (network reachability in this case)
- **Agentless Scanning**: Doesn't require software installation on instances
- **Network Reachability Rules**: Analyzes security groups, NACLs, route tables to determine potential vulnerabilities

### Common Questions:
**Q: Why use agentless scanning?**
A: Some operating systems may not support agents, or you may not have permission to install software on instances.

**Q: How long does scanning take?**
A: Typically 3-5 minutes for a small environment, but depends on the number of resources.

## Task 3: Analyze Amazon Inspector Findings

### Step-by-Step Instructions:

1. **View Findings**:
   - After scan completes, select "Findings" in left navigation
   - Findings are categorized by severity (High, Medium, Low)

2. **Examine High-Severity Finding**:
   - Expand the high-severity finding
   - Note:
     - Affected instance (BastionServer)
     - Description: TCP port 23 (Telnet) is reachable from internet
     - Recommended actions

3. **Examine Medium-Severity Finding**:
   - Expand medium-severity findings
   - Note:
     - TCP port 22 (SSH) is reachable from internet
     - Differences between Telnet and SSH security

### Explanation:
- **Port 23 (Telnet)**: Unencrypted protocol, considered insecure
- **Port 22 (SSH)**: Encrypted but still a potential vulnerability if open to the internet
- Findings provide specific details about vulnerabilities and remediation suggestions

### Security Implications:
- Telnet sends credentials in plain text - easily intercepted
- SSH is encrypted but still provides shell access - should be restricted
- Both services exposed to entire internet (0.0.0.0/0) is dangerous

## Task 4: Update Security Groups

### Step-by-Step Instructions:

1. **Access Security Group**:
   - From high-severity finding, click the security group link
   - This opens the security group attached to BastionServer

2. **Modify Inbound Rules**:
   - Select "Inbound rules" tab
   - Click "Edit inbound rules"
   - Delete the rule for port 23 (Telnet)
   - For SSH (port 22) rule:
     - Remove "0.0.0.0/0"
     - Change source to "My IP"
   - Click "Save rules"

3. **Rescan Environment**:
   - Return to Amazon Inspector
   - Select "Assessment templates"
   - Check "Assessment-Template-Network" and click "Run"
   - Wait for new scan to complete (30-60 seconds)
   - Verify in "Findings" that high-severity issue is resolved

### Explanation:
- **0.0.0.0/0**: Represents the entire internet - dangerous for management ports
- **My IP**: Automatically uses your current public IP address
- **Defense in Depth**: Removing unnecessary services reduces attack surface

### Best Practices:
- Always restrict management ports to specific IPs
- Remove unused rules entirely rather than just disabling
- Regularly review security group rules as part of security audits

## Task 5: Replace BastionServer with Systems Manager

### Step-by-Step Instructions:

1. **Remove SSH Access**:
   - Navigate to EC2 > Security Groups
   - Select "BastionServerSG"
   - Edit inbound rules
   - Delete SSH rule entirely
   - Save rules

2. **Stop BastionServer**:
   - Go to EC2 > Instances
   - Select "BastionServer"
   - Choose "Instance state" > "Stop instance"
   - Confirm stop action

3. **Connect to AppServer via Session Manager**:
   - Select "AppServer"
   - Click "Connect"
   - Choose "Session Manager" tab
   - Click "Connect"
   - In terminal:
     - Run `cd ~`
     - Run `pwd` (should show `/home/ssm-user`)

4. **Final Scan**:
   - Return to Amazon Inspector
   - Run assessment again
   - Verify no findings remain

### Explanation:
- **Session Manager Benefits**:
  - No need for open inbound ports
  - No SSH keys to manage
  - All sessions logged for auditing
  - Uses IAM for access control
- **Bastion Server Elimination**:
  - Removes potential attack vector
  - Reduces management overhead
  - More secure access method

### Architectural Improvement:
Traditional approach:
```
Internet -> Bastion (SSH) -> AppServer
```
New approach:
```
Internet -> Systems Manager -> AppServer
```
The new approach eliminates the need for a publicly accessible jump host entirely.

## Conclusion

### Key Achievements:
1. **Configured Amazon Inspector** to scan EC2 instances using tags
2. **Ran agentless network audit** identifying vulnerable ports
3. **Analyzed findings** to understand security risks
4. **Updated security groups** to restrict access
5. **Implemented Session Manager** for more secure instance access

### Security Best Practices Reinforced:
- Principle of least privilege
- Regular vulnerability scanning
- Elimination of unnecessary services
- Secure remote access methods
- Defense in depth strategy

### Next Steps:
- Schedule regular Inspector scans
- Implement findings notification (Amazon SNS)
- Expand scanning to include other rule packages
- Consider implementing just-in-time access for additional security