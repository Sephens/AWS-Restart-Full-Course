# Comprehensive Lab Guide: Managing Log Files in Linux

## Introduction
This lab provides hands-on experience with reviewing and analyzing Linux log files, focusing on authentication logs and user login history. You'll learn essential commands for security monitoring and system administration.

## Task 2: Reviewing Secure Log Files

### Step 1: Verify Working Directory
1. Check current directory:
   ```bash
   pwd
   ```
   **Expected Output:**
   ```
   /home/ec2-user/companyA
   ```

2. Navigate if needed:
   ```bash
   cd /home/ec2-user/companyA
   ```

### Step 2: Examine Secure Logs
1. View authentication logs:
   ```bash
   sudo less /tmp/log/secure
   ```

**Key Information in Secure Logs:**
- Failed login attempts
- Successful authentications
- User session openings/closings
- sudo command usage
- SSH access attempts

**Common Log Entries:**
```
Aug 24 14:30:01 ip-10-0-10-81 sshd[1234]: Failed password for invalid user admin from 192.168.1.100 port 54321 ssh2
Aug 24 14:31:05 ip-10-0-10-81 sudo:   ec2-user : TTY=pts/0 ; PWD=/home/ec2-user ; USER=root ; COMMAND=/bin/yum update
```

**Alternative Log Viewing Methods:**
1. Tail last 10 lines:
   ```bash
   sudo tail /var/log/secure
   ```
2. Follow in real-time:
   ```bash
   sudo tail -f /var/log/secure
   ```
3. Filter for failed attempts:
   ```bash
   sudo grep "Failed password" /var/log/secure
   ```

### Step 3: Exit Log Viewer
1. Press `q` to quit less

## Reviewing User Login History

### Step 1: Check Last Logins
1. View user login history:
   ```bash
   sudo lastlog
   ```

**Output Interpretation:**
```
Username         Port     From             Latest
root             pts/1    192.168.1.100    Tue Aug 24 14:30:01 +0000 2023
bin                                        **Never logged in**
daemon                                     **Never logged in**
ec2-user          pts/0    :0              Mon Aug 23 09:15:22 +0000 2023
```

**Key Columns:**
- **Username**: System account name
- **Port**: Terminal/connection type
- **From**: Source IP address
- **Latest**: Timestamp of last login

### Step 2: Alternative Login History Commands
1. Recent logins:
   ```bash
   last
   ```
   **Shows:** Reboot events, login/logout times, durations

2. Current logged-in users:
   ```bash
   who
   ```

3. Failed login attempts:
   ```bash
   lastb
   ```

## Advanced Log Analysis Techniques

### 1. Filtering by Date/Time
```bash
sudo awk '/Aug 24 14:/' /var/log/secure
```

### 2. Counting Failed Attempts
```bash
sudo grep "Failed password" /var/log/secure | wc -l
```

### 3. Identifying Suspicious IPs
```bash
sudo grep "Failed password" /var/log/secure | awk '{print $11}' | sort | uniq -c | sort -nr
```

### 4. Creating Daily Reports
```bash
sudo grep "$(date +'%b %d')" /var/log/secure > daily_auth_report.txt
```

## Log Rotation and Maintenance

### 1. View Rotation Configuration
```bash
cat /etc/logrotate.conf
```

### 2. Check Secure Log Rotation
```bash
cat /etc/logrotate.d/syslog
```

### 3. Manual Rotation (for testing)
```bash
sudo logrotate -vf /etc/logrotate.d/syslog
```

## Security Best Practices

1. **Regular Monitoring**: Set up daily log reviews
2. **Centralized Logging**: Configure rsyslog to forward logs
3. **Alerting**: Create scripts to notify of suspicious activity
4. **Retention**: Maintain logs per compliance requirements
5. **Integrity**: Use log signing to prevent tampering

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| Missing log files | Check alternate locations (/var/log, /tmp/log) |
| Permission denied | Use sudo or check group memberships |
| Empty logs | Verify service is running and logging |
| Large log files | Implement rotation or archiving |
| No lastlog data | System may not track all user types |

## Real-World Applications

1. **Security Auditing**: Detect brute force attacks
2. **Compliance**: Demonstrate access controls
3. **Troubleshooting**: Diagnose authentication issues
4. **Forensics**: Investigate security incidents
5. **User Management**: Identify inactive accounts

This lab provides fundamental skills for working with Linux authentication logs, essential for system administrators, security professionals, and DevOps engineers. The techniques learned form the basis for more advanced security monitoring and incident response workflows.