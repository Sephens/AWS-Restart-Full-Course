# Lab Guide: Working with the File System

## Introduction
This lab guide provides comprehensive instructions for creating, organizing, and modifying a folder structure in Linux. You'll learn essential file system operations including creating directories and files, copying, moving, and deleting items, and reorganizing directory structures.

## Task 2: Create a Folder Structure

### Step 1: Verify Current Directory
1. Check your current directory:
   ```bash
   pwd
   ```
   **Expected Output:**
   ```
   /home/ec2-user
   ```

2. If not in your home directory, navigate there:
   ```bash
   cd /home/ec2-user
   ```

### Step 2: Create Main Directory
1. Create the CompanyA directory:
   ```bash
   mkdir CompanyA
   ```

### Step 3: Create Subdirectories
1. Navigate into CompanyA:
   ```bash
   cd CompanyA
   ```

2. Create three subdirectories at once:
   ```bash
   mkdir Finance HR Management
   ```

3. Verify creation:
   ```bash
   ls
   ```
   **Expected Output:**
   ```
   Finance  HR  Management
   ```

### Step 4: Create Files in HR Directory
1. Navigate to HR:
   ```bash
   cd HR
   ```

2. Create two empty CSV files:
   ```bash
   touch Assessments.csv TrialPeriod.csv
   ```

3. Verify files:
   ```bash
   ls
   ```
   **Expected Output:**
   ```
   Assessments.csv  TrialPeriod.csv
   ```

### Step 5: Create Files in Finance Directory
1. Move back to CompanyA and into Finance:
   ```bash
   cd ../Finance
   ```

2. Create two financial files:
   ```bash
   touch Salary.csv ProfitAndLossStatements.csv
   ```

3. Verify files:
   ```bash
   ls
   ```
   **Expected Output:**
   ```
   ProfitAndLossStatements.csv  Salary.csv
   ```

### Step 6: Create Files in Management Directory
1. Return to CompanyA:
   ```bash
   cd ..
   ```

2. Create management files without changing directories:
   ```bash
   touch Management/Managers.csv Management/Schedule.csv
   ```

3. Verify files:
   ```bash
   ls Management
   ```
   **Expected Output:**
   ```
   Managers.csv  Schedule.csv
   ```

### Step 7: Verify Complete Structure
1. Check the entire structure recursively:
   ```bash
   ls -laR
   ```

**Explanation of Commands:**
- `mkdir`: Creates directories
- `touch`: Creates empty files
- `ls -laR`: Lists all files recursively with details
- Relative paths (`../`) help navigate without full paths

## Task 3: Delete and Reorganize Folders

### Step 1: Verify Starting Position
1. Ensure you're in CompanyA:
   ```bash
   pwd
   ```
   **Expected Output:**
   ```
   /home/ec2-user/CompanyA
   ```

### Step 2: Copy Finance to HR
1. Copy the Finance directory into HR:
   ```bash
   cp -r Finance HR
   ```

2. Verify the copy:
   ```bash
   ls HR/Finance
   ```
   **Expected Output:**
   ```
   ProfitAndLossStatements.csv  Salary.csv
   ```

### Step 3: Remove Original Finance
1. First attempt (will fail):
   ```bash
   rmdir Finance
   ```
   **Error Message:**
   ```
   rmdir: failed to remove 'Finance/': Directory not empty
   ```

2. Empty the directory first:
   ```bash
   rm Finance/ProfitAndLossStatements.csv Finance/Salary.csv
   ```

3. Then remove the empty directory:
   ```bash
   rmdir Finance
   ```

4. Verify removal:
   ```bash
   ls
   ```
   **Expected Output:**
   ```
   HR  Management
   ```

### Step 4: Move Management to HR
1. Move the Management directory:
   ```bash
   mv Management HR
   ```

2. Verify the move:
   ```bash
   ls . HR/Management
   ```
   **Expected Output:**
   ```
   .:
   HR

   HR/Management:
   Managers.csv  Schedule.csv
   ```

### Step 5: Create and Populate Employees Directory
1. Navigate to HR:
   ```bash
   cd HR
   ```

2. Create Employees directory:
   ```bash
   mkdir Employees
   ```

3. Move HR files to Employees:
   ```bash
   mv Assessments.csv TrialPeriod.csv Employees
   ```

4. Verify the new structure:
   ```bash
   ls . Employees
   ```
   **Expected Output:**
   ```
   .:
   Employees  Finance  Management

   Employees:
   Assessments.csv  TrialPeriod.csv
   ```

## Final Structure Verification
The final structure should match:
```
/home/ec2-user/CompanyA/
/home/ec2-user/CompanyA/HR/
/home/ec2-user/CompanyA/HR/Finance/
/home/ec2-user/CompanyA/HR/Finance/ProfitAndLossStatements.csv
/home/ec2-user/CompanyA/HR/Finance/Salary.csv
/home/ec2-user/CompanyA/HR/Employees/
/home/ec2-user/CompanyA/HR/Employees/Assessments.csv
/home/ec2-user/CompanyA/HR/Employees/TrialPeriod.csv
/home/ec2-user/CompanyA/HR/Management/
/home/ec2-user/CompanyA/HR/Management/Managers.csv
/home/ec2-user/CompanyA/HR/Management/Schedule.csv
```

## Key Command Summary
| Command | Description | Example |
|---------|-------------|---------|
| `mkdir` | Create directory | `mkdir CompanyA` |
| `touch` | Create empty file | `touch file.txt` |
| `cp -r` | Copy recursively | `cp -r dir1 dir2` |
| `rm` | Remove files | `rm file.txt` |
| `rmdir` | Remove empty directory | `rmdir emptydir` |
| `mv` | Move/rename | `mv oldname newname` |
| `ls -laR` | List all recursively | `ls -laR` |

## Common Pitfalls and Solutions
1. **"Directory not empty" error**: Use `rm -r` instead of `rmdir` for non-empty directories
2. **Permission denied**: Use `sudo` if needed, or check ownership with `ls -l`
3. **Wrong directory**: Frequently verify with `pwd` and `ls`
4. **Accidental deletions**: Consider using `-i` flag with `rm` for confirmation prompts

This lab provides essential skills for managing files and directories in Linux, forming the foundation for more advanced system administration tasks.