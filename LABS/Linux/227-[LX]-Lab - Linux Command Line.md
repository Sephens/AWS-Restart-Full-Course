# Linux Command Line Lab: System Exploration and Command History

## Introduction
This lab guides you through connecting to an Amazon Linux EC2 instance and exploring fundamental Linux commands to understand system information and improve command-line workflow efficiency.

## Task 1: Connect to Amazon Linux EC2 Instance via SSH

### For Windows Users:

#### Step 1: Download Credentials
1. Select the **Details** drop-down menu above the instructions
2. Select **Show** to view the Credentials window
3. Click **Download PPK** to save `labsuser.ppk` (typically to Downloads folder)
4. Note the **PublicIP** address displayed
5. Close the Details panel by clicking **X**

#### Step 2: Configure PuTTY
1. Download and install PuTTY if not already installed
2. Open `putty.exe`
3. Configure the session with:
   - Host Name: `ec2-user@<PublicIP>`
   - Connection type: SSH
   - Port: 22
4. Under SSH > Auth, browse and select the downloaded `labsuser.ppk` file
5. Click **Open** to initiate the connection

**Note**: First connection will display a security alert - click **Yes** to continue.

### For macOS/Linux Users:

#### Step 1: Download Credentials
1. Select the **Details** drop-down menu
2. Select **Show** to view Credentials
3. Click **Download PEM** to save `labsuser.pem`
4. Note the **PublicIP** address
5. Close the Details panel

#### Step 2: Configure SSH Connection
1. Open terminal
2. Navigate to download directory:
   ```bash
   cd ~/Downloads
   ```
3. Set proper permissions:
   ```bash
   chmod 400 labsuser.pem
   ```
4. Connect using:
   ```bash
   ssh -i labsuser.pem ec2-user@<PublicIP>
   ```
5. Type `yes` when prompted about first connection

**Expected Connection Output**:
```
       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

[ec2-user@ip-xxx-xxx-xxx-xxx ~]$
```

## Task 2: System Exploration Commands

### Step 1: Basic System Information
1. **User Identification**:
   ```bash
   whoami
   ```
   - Output: `ec2-user`
   - Shows current logged-in user

2. **Hostname Information**:
   ```bash
   hostname -s
   ```
   - Output: Shortened hostname (e.g., `ip-10-0-0-1`)
   - `-s` flag shows only the first component before first dot

3. **System Uptime**:
   ```bash
   uptime -p
   ```
   - Output: Human-readable uptime (e.g., "up 2 hours 30 minutes")
   - Shows how long system has been running

### Step 2: User Session Information
```bash
who -H -a
```
**Output Columns**:
- **NAME**: Username
- **LINE**: Terminal line
- **TIME**: Login time
- **IDLE**: Idle time
- **PID**: Process ID
- **COMMENT**: Additional info
- **EXIT**: Exit status if logged out

**Example Output**:
```
NAME       LINE         TIME             IDLE          PID COMMENT
ec2-user   pts/0        Sep 1 18:25       .         12345 (10.0.0.1)
```

### Step 3: Time Zone Exploration
1. **New York Time**:
   ```bash
   TZ=America/New_York date
   ```
   Output: `Wed Sep 1 21:27:35 EDT 2021`

2. **Los Angeles Time**:
   ```bash
   TZ=America/Los_Angeles date
   ```
   Output: `Wed Sep 1 18:27:35 PDT 2021`

**Note**: If system time is incorrect, these will display wrong times.

### Step 4: Calendar Views
1. **Julian Calendar**:
   ```bash
   cal -j
   ```
   - Shows dates consecutively (Feb 32 follows Jan 31)
   - Helpful for certain business applications

2. **Week Start Options**:
   ```bash
   cal -s  # Sunday start (default)
   cal -m  # Monday start
   ```

### Step 5: User Identity Information
```bash
id ec2-user
```
**Sample Output**:
```
uid=1000(ec2-user) gid=1000(ec2-user) groups=1000(ec2-user),4(adm),10(wheel)
```
- Shows user ID (uid), group ID (gid), and supplementary groups

## Task 3: Command History Workflow Optimization

### Step 1: View Command History
```bash
history
```
**Features**:
- Displays numbered list of recent commands
- Default stores last 500 commands
- History is maintained between sessions in `~/.bash_history`

### Step 2: Reverse History Search
1. Press `Ctrl+R`
2. Type `TZ` to search for previous time zone commands
3. Press `Tab` to select and edit the command
4. Use arrow keys to modify before execution

**Example Workflow**:
```
(reverse-i-search)`TZ': TZ=America/New_York date
```
After `Tab`, you can edit the timezone before running.

### Step 3: Repeat Last Command
```bash
!!
```
- Re-executes the most recent command
- Equivalent to pressing `Up Arrow` then `Enter`

**Example**:
```bash
date
!!  # Runs 'date' again
```

## Additional Command Line Tips

### Searching Manual Pages
```bash
man -k "time zone"  # Find relevant commands
man 5 timezone      # View timezone file format
```

### Command Aliases
Create shortcuts for common commands:
```bash
alias ny='TZ=America/New_York date'
alias la='TZ=America/Los_Angeles date'
```

### Persistent History Configuration
To enhance history retention:
```bash
echo 'HISTSIZE=10000' >> ~/.bashrc
echo 'HISTFILESIZE=20000' >> ~/.bashrc
source ~/.bashrc
```

## Common Questions

**Q: Why can't I see all my previous commands in history?**
A: By default, bash only maintains a limited history. To increase:
```bash
export HISTSIZE=10000
export HISTFILESIZE=20000
```

**Q: How do I clear my command history?**
A: Use:
```bash
history -c  # Clear current session
history -w  # Write empty history to file
```

**Q: What if my timezone commands don't work?**
A: The timezone database might be incomplete. Install full package:
```bash
sudo yum install tzdata
```

**Q: How can I find a command I ran yesterday?**
A: View full history file:
```bash
less ~/.bash_history
```
Or search with:
```bash
grep "searchterm" ~/.bash_history
```

## Conclusion

This lab covered:
1. Secure SSH connection to EC2 instances
2. Fundamental system exploration commands
3. Timezone and calendar operations
4. Efficient command history usage

These skills form the foundation for effective Linux system administration and AWS management. Regular practice with these commands will significantly improve your terminal productivity.