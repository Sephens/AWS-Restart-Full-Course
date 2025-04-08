# Lab Guide: Working with Files - Backup and Logging

## Introduction
This lab guide provides detailed instructions for creating file backups, logging backup activities, and transferring backup files in a Linux environment. You'll learn to use the `tar` command for archiving, manage backup logs, and organize backup files efficiently.

## Task 2: Create a Backup

### Step 1: Verify Current Directory
1. Check your current working directory:
   ```bash
   pwd
   ```
   **Expected Output:**
   ```
   /home/ec2-user
   ```

### Step 2: Verify Folder Structure
1. Examine the CompanyA directory structure:
   ```bash
   ls -R CompanyA
   ```
   **Expected Output:**
   ```
   CompanyA/:
   Employees  Finance  HR  IA  Management  SharedFolders

   CompanyA/Employees:
   Schedules.csv

   CompanyA/Finance:
   Salary.csv

   CompanyA/HR:
   Assessments.csv  Managers.csv

   CompanyA/IA:

   CompanyA/Management:
   Promotions.csv  Sections.csv
   ```

### Step 3: Create Tar Archive
1. Create a compressed backup of the CompanyA folder:
   ```bash
   tar -cvpzf backup.CompanyA.tar.gz CompanyA
   ```

**Command Breakdown:**
- `-c`: Create new archive
- `-v`: Verbose output (show progress)
- `-p`: Preserve permissions
- `-z`: Compress with gzip
- `-f`: Specify filename

**Expected Output:**
```
CompanyA/
CompanyA/Management/
CompanyA/Management/Sections.csv
CompanyA/Management/Promotions.csv
CompanyA/Employees/
CompanyA/Employees/Schedules.csv
CompanyA/Finance/
CompanyA/Finance/Salary.csv
CompanyA/HR/
CompanyA/HR/Managers.csv
CompanyA/HR/Assessments.csv
CompanyA/IA/
CompanyA/SharedFolders/
```

### Step 4: Verify Archive Creation
1. Check the created backup file:
   ```bash
   ls
   ```
   **Expected Output:**
   ```
   backup.CompanyA.tar.gz  CompanyA
   ```

**Note:** The `.tar.gz` extension indicates a compressed tar archive, combining both archiving and compression.

## Task 3: Log the Backup

### Step 1: Navigate to CompanyA
1. Change to the CompanyA directory:
   ```bash
   cd /home/ec2-user/CompanyA
   ```

### Step 2: Create Backup Log File
1. Create an empty backups.csv file:
   ```bash
   touch SharedFolders/backups.csv
   ```

### Step 3: Add Backup Entry
1. Record backup details in the log:
   ```bash
   echo "$(date +'%d %b %Y, %H:%M'), backup.CompanyA.tar.gz" | sudo tee SharedFolders/backups.csv
   ```

**Improved Command Explanation:**
- `date +'%d %b %Y, %H:%M'`: Automatically inserts current date/time
- `echo`: Outputs the text
- `|`: Pipes output to next command
- `tee`: Writes to both terminal and file
- `sudo`: Ensures write permissions

**Expected Output:**
```
25 Aug 2021, 16:59, backup.CompanyA.tar.gz
```

### Step 4: Verify Log Entry
1. View the backup log:
   ```bash
   cat SharedFolders/backups.csv
   ```
   **Expected Output:**
   ```
   25 Aug 2021, 16:59, backup.CompanyA.tar.gz
   ```

**Best Practice:** Using the actual date command ensures accurate timestamps rather than hardcoding dates.

## Task 4: Move the Backup File

### Step 1: Verify Location
1. Confirm current directory:
   ```bash
   pwd
   ```
   **Expected Output:**
   ```
   /home/ec2-user/CompanyA
   ```

### Step 2: Transfer Backup File
1. Move the backup to the IA folder:
   ```bash
   mv ../backup.CompanyA.tar.gz IA/
   ```

**Path Explanation:**
- `../`: Goes up one level to /home/ec2-user
- `IA/`: Target directory

### Step 3: Verify Transfer
1. Check both locations:
   ```bash
   ls . IA
   ```
   **Expected Output:**
   ```
   .:
   Employees  Finance  HR  IA  Management  SharedFolders

   IA:
   backup.CompanyA.tar.gz
   ```

## Additional Useful Commands

### View Archive Contents
To inspect a tar archive without extracting:
```bash
tar -tvf IA/backup.CompanyA.tar.gz
```

### Extract Archive
To restore from backup:
```bash
tar -xvpzf IA/backup.CompanyA.tar.gz -C /target/directory
```

### Append to Log File
To add new entries without overwriting:
```bash
echo "$(date +'%d %b %Y, %H:%M'), new_backup.tar.gz" | sudo tee -a SharedFolders/backups.csv
```
Note the `-a` flag for append mode.

## Security Considerations

1. **Permissions**: Ensure only authorized users can access backups
2. **Verification**: Always verify backups after creation
3. **Storage**: Consider storing backups in separate locations
4. **Rotation**: Implement a backup rotation policy to manage disk space

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| "Permission denied" | Use `sudo` or check ownership with `ls -l` |
| Archive too large | Use higher compression (`-j` for bzip2) |
| Missing files in archive | Verify paths and use absolute paths if needed |
| Disk space full | Check with `df -h` before creating large backups |

This lab provides essential skills for file backup management in Linux, crucial for system administration and data protection. The techniques learned can be adapted for automated backup scripts and more complex backup strategies.