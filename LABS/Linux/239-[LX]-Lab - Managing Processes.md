# Comprehensive Lab Guide: Managing Processes in Linux

## Introduction
This lab provides hands-on experience with process management in Linux, covering process monitoring, logging, and automation using cron jobs. You'll learn essential system administration skills for tracking and managing system resources.

## Task 2: Create Process Log File

### Step 1: Verify Working Directory
1. Check current directory:
   ```bash
   pwd
   ```
   **Expected Output:**
   ```
   /home/ec2-user/companyA
   ```

2. If not in companyA, navigate there:
   ```bash
   cd /home/ec2-user/companyA
   ```

### Step 2: Create Filtered Process Log
1. Generate process list excluding root processes and kernel threads:
   ```bash
   sudo ps -aux | grep -v root | grep -v '\[.*\]' | sudo tee SharedFolders/processes.csv
   ```

**Command Breakdown:**
- `sudo ps -aux`: List all processes with detailed information
- `grep -v root`: Exclude lines containing "root"
- `grep -v '\[.*\]'`: Exclude kernel threads (enclosed in brackets)
- `sudo tee SharedFolders/processes.csv`: Save output to file while displaying it

**Example Output:**
```
ec2-user   1234  0.0  0.1 123456 7890 ?        S    14:30   0:00 /usr/bin/python
ec2-user   5678  0.1  0.2 234567 8901 ?        Sl   14:31   0:01 /usr/lib/firefox
```

### Step 3: Verify Process Log
1. Check created file contents:
   ```bash
   cat SharedFolders/processes.csv
   ```

**Common Questions:**
Q: Why exclude root processes and kernel threads?
A: For security auditing, we often want to focus on user processes. Root processes and kernel threads are system-level and typically numerous.

Q: What if I need to include column headers?
A: Use:
```bash
(ps -aux --headers | head -n 1; ps -aux | grep -v root | grep -v '\[.*\]') | sudo tee SharedFolders/processes.csv
```

## Task 3: Monitor Processes with top

### Step 1: Launch top
1. Start process monitor:
   ```bash
   top
   ```

**Key top Interface Elements:**
1. **System Summary**: Uptime, users, load averages
2. **Task States**: Total, running, sleeping, stopped, zombie
3. **CPU Usage**: User vs system, idle percentage
4. **Memory Usage**: Physical and swap
5. **Process List**: Sorted by CPU usage by default

### Step 2: Analyze Process States
1. Observe the "Tasks" line (second line):
   ```
   Tasks: 120 total, 2 running, 118 sleeping, 0 stopped, 0 zombie
   ```

**Process State Meanings:**
- **Running**: Actively using CPU
- **Sleeping**: Waiting for resources (normal)
- **Stopped**: Suspended (e.g., with Ctrl+Z)
- **Zombie**: Terminated but not reaped by parent

### Step 3: Customize top Display
1. Sort by memory usage:
   - Press `M` while in top
2. Show full command paths:
   - Press `c`
3. Filter by user:
   - Press `u` then enter username
4. Quit:
   - Press `q`

### Step 4: View top Version Info
1. Check version and help:
   ```bash
   top -hv
   ```

**Advanced top Usage:**
- Batch mode for scripting:
  ```bash
  top -b -n 1 > process_snapshot.txt
  ```
- Custom interval (2 seconds):
  ```bash
  top -d 2
  ```

## Task 4: Create Automated Audit with Cron

### Step 1: Edit Crontab
1. Open root's crontab:
   ```bash
   sudo crontab -e
   ```

### Step 2: Configure Cron Environment
1. Add these lines at the top:
   ```bash
   SHELL=/bin/bash
   PATH=/usr/bin:/bin:/usr/local/bin
   MAILTO=root
   ```

**Configuration Explanation:**
- `SHELL`: Specifies which shell to use
- `PATH`: Sets search path for commands
- `MAILTO`: Where to send job output

### Step 3: Add Cron Job
1. Add this job entry (runs hourly at :00):
   ```bash
   0 * * * * ls -la $(find . -name "*.csv") | sed -e 's/\.csv/#####.csv/g' > /home/ec2-user/companyA/SharedFolders/filteredAudit.csv
   ```

**Job Breakdown:**
- `0 * * * *`: Runs at minute 0 of every hour
- `find . -name "*.csv"`: Locates all CSV files
- `ls -la`: Gets detailed file info
- `sed`: Replaces ".csv" with "#####.csv"
- `>`: Redirects output to audit file

### Step 4: Verify Crontab
1. List installed cron jobs:
   ```bash
   sudo crontab -l
   ```

**Expected Output:**
```
SHELL=/bin/bash
PATH=/usr/bin:/bin:/usr/local/bin
MAILTO=root
0 * * * * ls -la $(find . -name "*.csv") | sed -e 's/\.csv/#####.csv/g' > /home/ec2-user/companyA/SharedFolders/filteredAudit.csv
```

## Cron Management Tips

### Common Time Specifications
| Example | Meaning |
|---------|---------|
| `0 * * * *` | Hourly at :00 |
| `0 0 * * *` | Daily at midnight |
| `0 0 * * 0` | Weekly (Sunday midnight) |
| `*/15 * * * *` | Every 15 minutes |
| `0 0 1 * *` | Monthly on 1st |

### Debugging Cron Jobs
1. Check mail for errors (configured via MAILTO)
2. Log output to file:
   ```bash
   0 * * * * /path/to/command >> /var/log/cron.log 2>&1
   ```
3. Verify environment variables:
   ```bash
   * * * * * env > /tmp/cron_env.txt
   ```

## Security Considerations

1. **Process Monitoring**: Regularly check for unexpected processes
2. **Cron Security**:
   - Restrict crontab access via `/etc/cron.allow`
   - Validate all cron job commands
3. **Log Rotation**: Implement log rotation for process logs
4. **Audit Trails**: Maintain records of all automated jobs

## Real-World Applications

1. **Security Auditing**: Track non-root processes for anomalies
2. **Performance Tuning**: Use top to identify resource hogs
3. **Automated Maintenance**: Schedule regular system checks
4. **Compliance Reporting**: Generate periodic access logs

This lab provides fundamental skills for enterprise Linux system administration, particularly in process monitoring and automation - critical for maintaining secure and efficient systems.