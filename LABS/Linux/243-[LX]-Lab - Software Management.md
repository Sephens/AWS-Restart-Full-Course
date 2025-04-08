# Comprehensive Lab Guide: Software Management in Linux

## Introduction
This lab provides hands-on experience with essential Linux package management tasks, including system updates, package rollbacks, and AWS CLI installation. You'll learn to use the yum package manager and configure AWS command-line tools for cloud management.

## Task 2: Updating the Linux Machine

### Step 1: Verify Working Directory
1. Check current directory:
   ```bash
   pwd
   ```
   **Expected Output:**
   ```
   /home/ec2-user/companyA
   ```

### Step 2: Check for Available Updates
1. List available updates:
   ```bash
   sudo yum -y check-update
   ```

**Command Breakdown:**
- `sudo`: Execute with root privileges
- `yum`: Yellowdog Updater Modified (package manager)
- `-y`: Assume "yes" to all prompts
- `check-update`: List available updates without installing

### Step 3: Apply Security Updates
1. Install security patches:
   ```bash
   sudo yum update --security
   ```

**Security Update Notes:**
- Only updates packages with security fixes
- Critical for maintaining system security
- Should be performed regularly (weekly/monthly)

### Step 4: Perform Full System Upgrade
1. Update all packages:
   ```bash
   sudo yum -y upgrade
   ```

**Upgrade vs Update:**
- `update`: Checks for and installs newer versions
- `upgrade`: Same as update but also removes obsolete packages

### Step 5: Install Apache HTTP Server
1. Install httpd package:
   ```bash
   sudo yum install httpd -y
   ```

**Verification:**
1. Check installed version:
   ```bash
   httpd -v
   ```
2. Verify service status:
   ```bash
   sudo systemctl status httpd
   ```

## Task 3: Rolling Back a Package

### Step 1: View Update History
1. List yum transactions:
   ```bash
   sudo yum history list
   ```

**Output Interpretation:**
```
ID  | Login user            | Date and time     | Action(s) | Altered
------------------------------------------------------------
2   | EC2 ... <ec2-user>    | <date>            | Install   | 9
1   | System <unset>        | <date>            | I, O, U   | 18
```
- **ID**: Transaction reference number
- **Action(s)**: I (Install), U (Update), E (Erase), O (Downgrade)

### Step 2: Inspect Specific Transaction
1. View transaction details:
   ```bash
   sudo yum history info <ID>
   ```

**Example:**
```bash
sudo yum history info 2
```

**Key Details:**
- Transaction timestamp
- User who performed it
- Exact command used
- Packages affected

### Step 3: Perform Rollback
1. Undo specific transaction:
   ```bash
   sudo yum -y history undo <ID>
   ```

**Rollback Options:**
- `undo`: Revert single transaction
- `rollback`: Revert all transactions after specified ID
- `redo`: Reapply a transaction

**Verification:**
1. Check package version after rollback:
   ```bash
   yum list installed httpd
   ```

## Task 4: Installing AWS CLI

### Step 1: Verify Python Installation
1. Check Python version:
   ```bash
   python3 --version
   ```
   **Requirement:** Python 3.3+ or Python 2.6.5+

### Step 2: Check for pip
1. Verify pip availability:
   ```bash
   pip3 --version
   ```

**If Missing:**
1. Install pip:
   ```bash
   sudo yum install python3-pip
   ```

### Step 3: Download AWS CLI
1. Get installer package:
   ```bash
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   ```

**Alternative Methods:**
- Using pip: `pip3 install awscli --upgrade`
- Using yum: `sudo yum install awscli`

### Step 4: Install AWS CLI
1. Unzip package:
   ```bash
   unzip awscliv2.zip
   ```
2. Run installer:
   ```bash
   sudo ./aws/install
   ```

**Installation Locations:**
- Binary: `/usr/local/bin/aws`
- Files: `/usr/local/aws-cli`

### Step 5: Verify Installation
1. Check AWS CLI version:
   ```bash
   aws --version
   ```
2. View help:
   ```bash
   aws help
   ```

## Task 5: Configuring AWS CLI

### Step 1: Run Configuration
1. Start interactive setup:
   ```bash
   aws configure
   ```

**Configuration Prompts:**
```
AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: us-west-2
Default output format [None]: json
```

### Step 2: Add Credentials
1. Edit credentials file:
   ```bash
   sudo nano ~/.aws/credentials
   ```
2. Add lab credentials:
   ```ini
   [default]
   aws_access_key_id=<your access key ID>
   aws_secret_access_key=<your access key>
   aws_session_token=<your session token>
   ```

**File Locations:**
- Credentials: `~/.aws/credentials`
- Config: `~/.aws/config`

### Step 3: Test AWS CLI
1. Describe EC2 instance:
   ```bash
   aws ec2 describe-instance-attribute --instance-id i-1234567890abcdefg --attribute instanceType
   ```

**Expected Output:**
```json
{
    "InstanceId": "i-1234567890abcdefg",
    "InstanceType": {
        "Value": "t3.micro"
    }
}
```

## Best Practices

### Package Management
1. **Regular Updates**: Schedule weekly security updates
2. **Change Control**: Document all manual package changes
3. **Testing**: Test updates in staging before production
4. **Backups**: Create system snapshots before major updates

### AWS CLI Security
1. **IAM Roles**: Prefer roles over long-term credentials
2. **Permissions**: Follow principle of least privilege
3. **Rotation**: Regularly rotate access keys
4. **MFA**: Enable Multi-Factor Authentication

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| Yum lock error | Remove lock: `sudo rm -f /var/run/yum.pid` |
| Broken dependencies | Clean cache: `sudo yum clean all` |
| AWS CLI not found | Verify PATH: `echo $PATH` |
| Permission denied | Use sudo or check file permissions |
| Invalid credentials | Verify keys and region |

This lab provides essential skills for maintaining Linux systems and integrating with AWS cloud services. The techniques learned form the foundation for professional system administration and cloud operations.