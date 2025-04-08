# Comprehensive Lab Guide: Managing File Permissions in Linux

## Introduction
This lab provides hands-on experience with Linux file permissions and ownership, crucial for system security and proper access control. You'll learn to modify file ownership, set permissions using both symbolic and numeric modes, and apply these concepts to a business directory structure.

## Task 2: Change File and Folder Ownership

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

### Step 2: Change CompanyA Ownership
1. Recursively change owner to CEO (mjackson) and group to Personnel:
   ```bash
   sudo chown -R mjackson:Personnel /home/ec2-user/companyA
   ```

**Command Breakdown:**
- `sudo`: Execute with superuser privileges
- `chown`: Change ownership command
- `-R`: Recursive (apply to all contents)
- `mjackson:Personnel`: New owner and group
- Path: `/home/ec2-user/companyA`

**Example Output:** (No output means success)

### Step 3: Change HR Department Ownership
1. Change HR folder to HR manager (ljuang) and HR group:
   ```bash
   sudo chown -R ljuang:HR HR
   ```

**Note:** Unlike the first command, this uses relative path (HR) since we're already in companyA

### Step 4: Change Finance Department Ownership
1. Change Finance folder to finance manager (mmajor) and Finance group:
   ```bash
   sudo chown -R mmajor:Finance HR/Finance
   ```

**Path Explanation:** 
- Uses `HR/Finance` because Finance is within HR in this structure

### Step 5: Verify Changes
1. Check all ownership changes:
   ```bash
   ls -laR
   ```

**Expected Output Structure:**
```
.:
total 12
drwxr-xr-x 8 mjackson Personnel 4096 Aug 25 14:30 .
drwx------ 4 ec2-user ec2-user  4096 Aug 25 14:30 ..
drwxr-xr-x 2 ljuang   HR        4096 Aug 25 14:30 HR

./HR:
total 8
drwxr-xr-x 2 ljuang HR     4096 Aug 25 14:30 .
drwxr-xr-x 8 mjackson Personnel 4096 Aug 25 14:30 ..
drwxr-xr-x 2 mmajor Finance 4096 Aug 25 14:30 Finance

./HR/Finance:
total 8
drwxr-xr-x 2 mmajor Finance 4096 Aug 25 14:30 .
drwxr-xr-x 2 ljuang HR     4096 Aug 25 14:30 ..
```

**Common Questions:**
Q: Why use `-R` flag?
A: It applies changes recursively to all subdirectories and files. Without it, only the top-level folder's ownership changes.

Q: What if I get "operation not permitted"?
A: Ensure you're using `sudo` for ownership changes of system files or files you don't own.

## Task 3: Change Permission Modes

### Step 1: Verify Location
1. Confirm you're in companyA:
   ```bash
   pwd
   ```

### Step 2: Create Test File (Symbolic Mode)
1. Create symbolic_mode_file with vim:
   ```bash
   sudo vim symbolic_mode_file
   ```
2. Press `i` to insert, type some text, then:
   - `ESC` to exit insert mode
   - `:wq` to write and quit

### Step 3: Modify Permissions (Symbolic Mode)
1. Add group write permission:
   ```bash
   sudo chmod g+w symbolic_mode_file
   ```

**Symbolic Mode Explanation:**
- `g`: Group owner
- `+`: Add permission
- `w`: Write permission
- Other symbols: `u` (user), `o` (others), `-` (remove), `=` (set exact)

### Step 4: Create Test File (Absolute Mode)
1. Create absolute_mode_file:
   ```bash
   sudo vim absolute_mode_file
   ```
2. Add content and save as before

### Step 5: Modify Permissions (Absolute Mode)
1. Set permissions to 764:
   ```bash
   sudo chmod 764 absolute_mode_file
   ```

**Numeric Mode Breakdown:**
- Each digit represents permissions for:
  - First digit (7): User (owner) permissions
  - Second digit (6): Group permissions
  - Third digit (4): Others permissions
- Permission values:
  - 4: Read (r)
  - 2: Write (w)
  - 1: Execute (x)
- 7 = 4+2+1 (rwx)
- 6 = 4+2 (rw-)
- 4 = 4 (r--)

### Step 6: Verify Permissions
1. View permission details:
   ```bash
   ls -l
   ```

**Expected Output:**
```
-rw-rw-r-- 1 mjackson Personnel 0 Aug 25 15:00 symbolic_mode_file
-rwxrw-r-- 1 mjackson Personnel 0 Aug 25 15:01 absolute_mode_file
```

**Permission Interpretation:**
- `-rw-rw-r--` (symbolic_mode_file):
  - User: rw-
  - Group: rw-
  - Others: r--
- `-rwxrw-r--` (absolute_mode_file):
  - User: rwx
  - Group: rw-
  - Others: r--

## Task 4: Assign Department Permissions

### Step 1: Verify Location
1. Confirm you're in companyA:
   ```bash
   pwd
   ```

### Step 2: Set Shipping Department Permissions
1. Change Shipping folder ownership:
   ```bash
   sudo chown -R eowusu:Shipping Shipping
   ```

### Step 3: Set Sales Department Permissions
1. Change Sales folder ownership:
   ```bash
   sudo chown -R nwolf:Sales Sales
   ```

### Step 4: Verify Changes
1. Check Shipping permissions:
   ```bash
   ls -laR Shipping
   ```

2. Check Sales permissions:
   ```bash
   ls -laR Sales
   ```

**Expected Verification Output:**
```
Shipping:
total 8
drwxr-xr-x 2 eowusu Shipping 4096 Aug 25 15:10 .
drwxr-xr-x 9 mjackson Personnel 4096 Aug 25 15:10 ..

Sales:
total 8
drwxr-xr-x 2 nwolf Sales   4096 Aug 25 15:10 .
drwxr-xr-x 9 mjackson Personnel 4096 Aug 25 15:10 ..
```

## Advanced Permission Concepts

### Special Permissions
1. **SetUID (4)**: Executes as file owner
   ```bash
   chmod 4755 executable_file
   ```
2. **SetGID (2)**: Executes with group privileges
   ```bash
   chmod 2755 executable_file
   ```
3. **Sticky Bit (1)**: Only owner can delete in shared dir
   ```bash
   chmod 1777 shared_directory
   ```

### Default Permissions (umask)
1. View current umask:
   ```bash
   umask
   ```
2. Set default permissions (e.g., 0022):
   ```bash
   umask 0022
   ```

## Permission Troubleshooting

| Symptom | Solution |
|---------|----------|
| "Permission denied" | Check current permissions with `ls -l` |
| Can't change ownership | Use `sudo` or verify you're the owner |
| Changes don't apply to subfolders | Forgot `-R` flag for recursive changes |
| Script won't execute | Add execute permission: `chmod +x script.sh` |

## Best Practices
1. **Least Privilege**: Grant minimum necessary permissions
2. **Regular Audits**: Periodically review permissions
3. **Group Management**: Use groups for department access
4. **Documentation**: Maintain records of permission schemes
5. **Backup**: Backup ACLs with `getfacl` before major changes

This comprehensive permission management lab provides the foundation for secure file system administration in Linux environments. The skills learned are essential for maintaining proper access controls in both personal and enterprise systems.