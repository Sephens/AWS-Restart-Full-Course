# Comprehensive Lab Guide: Creating Bash Shell Scripts for Automated Backups

## Introduction
This lab provides hands-on experience with creating a Bash shell script to automate folder backups. You'll learn essential scripting concepts including shebang lines, variables, command substitution, and archiving with tar.

## Task 2: Creating a Backup Shell Script

### Step 1: Verify Working Directory
1. Check current directory:
   ```bash
   pwd
   ```
   **Expected Output:**
   ```
   /home/ec2-user/
   ```

### Step 2: Create Script File
1. Create empty script file:
   ```bash
   touch backup.sh
   ```

### Step 3: Set Execute Permissions
1. Make script executable:
   ```bash
   sudo chmod 755 backup.sh
   ```

**Permission Breakdown:**
- `7` (owner): read+write+execute (4+2+1)
- `5` (group): read+execute (4+0+1)
- `5` (others): read+execute (4+0+1)

### Step 4: Edit Script Content
1. Open in text editor:
   ```bash
   vi backup.sh
   ```
2. Press `i` to enter insert mode

### Step 5: Add Shebang Line
1. First line of script:
   ```bash
   #!/bin/bash
   ```

**Shebang Explanation:**
- Tells system which interpreter to use
- Must be first line in script
- Common alternatives: `#!/bin/sh`, `#!/usr/bin/env bash`

### Step 6: Create Date Variable
1. Add date variable:
   ```bash
   DAY="$(date +%Y_%m_%d_%T_%H_%M)"
   ```

**Date Format Breakdown:**
- `%Y`: 4-digit year (2023)
- `%m`: 2-digit month (08)
- `%d`: 2-digit day (24)
- `%T`: Time (HH:MM:SS)
- `%H`: Hour (24-hour format)
- `%M`: Minute

**Alternative Formats:**
- Simple date: `$(date +%F)` → "2023-08-24"
- Timestamp: `$(date +%s)` → Unix epoch time

### Step 7: Create Backup Path Variable
1. Add backup path:
   ```bash
   BACKUP="/home/$USER/backups/$DAY-backup-CompanyA.tar.gz"
   ```

**Variable Notes:**
- `$USER`: Automatic variable containing current username
- Creates path like: `/home/ec2-user/backups/2023_08_24_14:30:00_14_30-backup-CompanyA.tar.gz`
- Ensures unique filename for each backup

### Step 8: Add Tar Command
1. Include archive command:
   ```bash
   tar -csvpzf $BACKUP /home/$USER/CompanyA
   ```

**Tar Flags Explained:**
- `-c`: Create new archive
- `-s`: Preserve order
- `-v`: Verbose output
- `-p`: Preserve permissions
- `-z`: Compress with gzip
- `-f`: Specify filename

### Step 9: Save and Exit
1. Press `ESC` to exit insert mode
2. Type `:wq` and press Enter to write and quit

### Final Script Contents:
```bash
#!/bin/bash
DAY="$(date +%Y_%m_%d_%T_%H_%M)"
BACKUP="/home/$USER/backups/$DAY-backup-CompanyA.tar.gz"
tar -csvpzf $BACKUP /home/$USER/CompanyA
```

## Executing the Backup Script

### Step 1: Run the Script
1. Execute backup:
   ```bash
   ./backup.sh
   ```

**Expected Output:**
```
tar: Removing leading `/' from member names
/home/ec2-user/CompanyA/
/home/ec2-user/CompanyA/Management/
/home/ec2-user/CompanyA/Management/Sections.csv
...
```

**Note About Warning:**
- "Removing leading `/' from member names" appears because we used absolute paths
- This is normal and prevents extraction to root directory

### Step 2: Verify Backup Creation
1. Check backups directory:
   ```bash
   ls backups/
   ```

**Expected Output:**
```
2023_08_24_14:30:00_14_30-backup-CompanyA.tar.gz
```

## Enhancing the Script

### 1. Add Directory Creation
Modify script to create backups directory if missing:
```bash
#!/bin/bash
mkdir -p "/home/$USER/backups"
DAY="$(date +%Y_%m_%d_%T_%H_%M)"
BACKUP="/home/$USER/backups/$DAY-backup-CompanyA.tar.gz"
tar -csvpzf $BACKUP /home/$USER/CompanyA
```

### 2. Add Error Handling
Improved version with error checking:
```bash
#!/bin/bash

# Create backups directory if it doesn't exist
BACKUP_DIR="/home/$USER/backups"
mkdir -p "$BACKUP_DIR" || { echo "Failed to create backup directory"; exit 1; }

# Generate timestamp
DAY=$(date +%Y_%m_%d_%T_%H_%M) || { echo "Failed to get date"; exit 1; }

# Set backup path
BACKUP_FILE="$BACKUP_DIR/$DAY-backup-CompanyA.tar.gz"

# Create backup
if tar -csvpzf "$BACKUP_FILE" "/home/$USER/CompanyA"; then
    echo "Backup created successfully: $BACKUP_FILE"
else
    echo "Backup failed!" >&2
    exit 1
fi
```

### 3. Add Logging
Version with logging:
```bash
#!/bin/bash

LOG_FILE="/home/$USER/backups/backup.log"
BACKUP_DIR="/home/$USER/backups"

# Log function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

mkdir -p "$BACKUP_DIR" || { log "Failed to create backup directory"; exit 1; }

DAY=$(date +%Y_%m_%d_%T_%H_%M) || { log "Failed to get date"; exit 1; }
BACKUP_FILE="$BACKUP_DIR/$DAY-backup-CompanyA.tar.gz"

log "Starting backup of CompanyA"
if tar -csvpzf "$BACKUP_FILE" "/home/$USER/CompanyA"; then
    log "Backup completed successfully: $BACKUP_FILE"
else
    log "Backup failed!"
    exit 1
fi
```

## Scheduling with Cron

### Daily Backup Job
1. Edit crontab:
   ```bash
   crontab -e
   ```
2. Add line for daily 2AM backup:
   ```bash
   0 2 * * * /home/ec2-user/backup.sh
   ```

### Weekly Backup with Rotation
Enhanced script with rotation:
```bash
#!/bin/bash

# Keep last 7 backups
BACKUP_DIR="/home/$USER/backups"
mkdir -p "$BACKUP_DIR"

# Create new backup
DAY=$(date +%Y_%m_%d)
BACKUP_FILE="$BACKUP_DIR/$DAY-backup-CompanyA.tar.gz"
tar -csvpzf "$BACKUP_FILE" "/home/$USER/CompanyA"

# Remove backups older than 7 days
find "$BACKUP_DIR" -name "*-backup-CompanyA.tar.gz" -mtime +7 -delete
```

## Security Considerations

1. **Permissions**: Ensure only authorized users can access backups
2. **Storage**: Consider separate storage device for backups
3. **Encryption**: Add encryption for sensitive data
4. **Verification**: Implement backup verification steps
5. **Rotation**: Automate old backup deletion

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| Permission denied | Use `sudo` or check script permissions |
| Backup directory missing | Add `mkdir -p` command |
| Script not found | Ensure PATH includes script location |
| No space left | Check disk space with `df -h` |
| Backup too large | Exclude unnecessary files with `--exclude` |

This lab provides essential skills for automating system administration tasks with Bash scripting. The backup script created can be adapted for various real-world scenarios including database backups, configuration backups, and deployment automation.