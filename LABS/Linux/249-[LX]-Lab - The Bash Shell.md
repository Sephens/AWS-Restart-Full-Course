# Comprehensive Lab Guide: Working with the Bash Shell

## Introduction
This lab provides hands-on experience with two fundamental Bash shell concepts: creating command aliases and managing the PATH environment variable. These skills are essential for efficient Linux system administration and workflow optimization.

## Task 2: Creating a Backup Alias

### Step 1: Verify Current Directory
1. Check working directory:
   ```bash
   pwd
   ```
   **Expected Output:**
   ```
   /home/ec2-user
   ```

### Step 2: Create Backup Alias
1. Define the alias:
   ```bash
   alias backup='tar -cvzf '
   ```

**Alias Breakdown:**
- `alias backup`: Creates shortcut command "backup"
- `tar -cvzf`: The actual command being aliased
  - `-c`: Create new archive
  - `-v`: Verbose output
  - `-z`: Compress with gzip
  - `-f`: Specify filename

**Example Usage:**
```bash
backup archive_name.tar.gz directory_to_backup
```

### Step 3: Execute Backup Command
1. Backup CompanyA folder:
   ```bash
   backup backup_companyA.tar.gz CompanyA
   ```

**Expected Output:**
```
CompanyA/
CompanyA/Management/
CompanyA/Management/Sections.csv
CompanyA/Management/Promotions.csv
...
```

### Step 4: Verify Archive Creation
1. List directory contents:
   ```bash
   ls
   ```
   **Expected Output:**
   ```
   backup_companyA.tar.gz  CompanyA
   ```

**Making Alias Permanent:**
To persist the alias across sessions:
1. Edit `~/.bashrc`:
   ```bash
   nano ~/.bashrc
   ```
2. Add the alias definition
3. Reload configuration:
   ```bash
   source ~/.bashrc
   ```

## Task 3: Managing the PATH Variable

### Step 1: Navigate to Script Directory
1. Change to bin directory:
   ```bash
   cd /home/ec2-user/CompanyA/bin
   ```

### Step 2: Execute Script Directly
1. Run hello.sh:
   ```bash
   ./hello.sh
   ```
   **Expected Output:**
   ```
   hello ec2-user
   ```

### Step 3: Execute from Parent Directory
1. Move up one level:
   ```bash
   cd ..
   ```
2. Run with full relative path:
   ```bash
   ./bin/hello.sh
   ```

### Step 4: Attempt Direct Execution (Fails)
1. Try running directly:
   ```bash
   hello.sh
   ```
   **Expected Error:**
   ```
   bash: hello.sh: command not found
   ```

### Step 5: Examine PATH Variable
1. View current PATH:
   ```bash
   echo $PATH
   ```
   **Sample Output:**
   ```
   /usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/ec2-user/.local/bin:/home/ec2-user/bin
   ```

### Step 6: Update PATH Variable
1. Add CompanyA/bin to PATH:
   ```bash
   PATH=$PATH:/home/ec2-user/CompanyA/bin
   ```

### Step 7: Verify Successful Update
1. Run script directly:
   ```bash
   hello.sh
   ```
   **Expected Output:**
   ```
   hello ec2-user
   ```

## Making PATH Changes Permanent

### Method 1: ~/.bashrc
1. Edit configuration file:
   ```bash
   nano ~/.bashrc
   ```
2. Add line:
   ```bash
   export PATH=$PATH:/home/ec2-user/CompanyA/bin
   ```
3. Reload:
   ```bash
   source ~/.bashrc
   ```

### Method 2: ~/.profile
For system-wide changes:
1. Edit:
   ```bash
   sudo nano /etc/profile
   ```
2. Add PATH modification
3. Log out and back in

## Advanced Concepts

### Alias with Parameters
For more complex aliases requiring parameters:
```bash
alias backup='function _backup(){ tar -cvzf $1 $2; };_backup'
```

### PATH Management Best Practices
1. Order matters - first match in PATH is executed
2. Security risk - avoid adding current directory (.) to PATH
3. Organization - keep custom scripts in ~/bin
4. Verification - check with `which command`

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| Alias not working | Check for typos, reload shell |
| Command still not found | Verify script has execute permissions (`chmod +x`) |
| PATH reset after logout | Add to appropriate config file |
| Permission denied | Use `sudo` or check file ownership |

## Real-World Applications

1. **Automation**: Create aliases for frequent complex commands
2. **Productivity**: Shorten lengthy commands
3. **Script Management**: Organize personal scripts in custom PATH
4. **System Administration**: Standardize commands across teams
5. **Troubleshooting**: Create diagnostic command shortcuts

This lab provides foundational skills for working efficiently in the Bash shell, essential for both personal productivity and professional system administration tasks. The concepts learned form the basis for more advanced shell scripting and system configuration.