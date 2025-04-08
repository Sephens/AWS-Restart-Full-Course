# Managing Users and Groups in Linux - Complete Lab Guide

## Introduction
This lab provides hands-on experience with Linux user and group management, covering creation, organization, and permission validation. We'll create a corporate user structure with appropriate group assignments.

## Task 1: Preparation
### Verify Current Directory
```bash
pwd
```
**Expected Output**: `/home/ec2-user`  
**Purpose**: Confirms we're in the default user's home directory before creating new users.

## Task 2: Creating Users

### Step 1: Create First User (Alejandro Rosalez)
1. **Add user account**:
   ```bash
   sudo useradd arosalez
   ```
   - Creates user `arosalez` with default settings
   - `sudo` grants temporary root privileges

2. **Set password**:
   ```bash
   sudo passwd arosalez
   ```
   **Interaction**:
   ```
   New password: P@ssword1234!
   Retype new password: P@ssword1234!
   ```
   - Password won't display as you type
   - Uses corporate standard password

### Step 2: Verify User Creation
```bash
sudo cat /etc/passwd | cut -d: -f1
```
**Sample Output**:
```
root
bin
...
ec2-user
arosalez
```
**Breakdown**:
- `/etc/passwd` stores all user accounts
- `cut -d: -f1` extracts just usernames (first field)
- Pipe (`|`) sends output of `cat` to `cut`

### Step 3: Create Remaining Users
Repeat for all users in the table:
```bash
sudo useradd eowusu && sudo passwd eowusu
sudo useradd jdoe && sudo passwd jdoe
...
sudo useradd ssarkar && sudo passwd ssarkar
```

**Pro Tip**: Use tab completion for usernames after typing `sudo passwd `

### Step 4: Final Verification
```bash
sudo cat /etc/passwd | cut -d: -f1 | tail -12
```
**Purpose**: Shows last 12 users (including new ones)

## Task 3: Creating and Populating Groups

### Step 1: Create Groups
1. **Sales group**:
   ```bash
   sudo groupadd Sales
   ```

2. **Verify creation**:
   ```bash
   cat /etc/group | grep Sales
   ```
   **Output**: `Sales:x:1014:`

3. **Create remaining groups**:
   ```bash
   sudo groupadd HR
   sudo groupadd Finance
   sudo groupadd Shipping
   sudo groupadd Managers
   sudo groupadd CEO
   ```

### Step 2: Add Users to Groups
1. **Add to Sales group**:
   ```bash
   sudo usermod -a -G Sales arosalez
   sudo usermod -a -G Sales nwolf
   ```

   **Options Explained**:
   - `-a`: Append to existing groups (don't replace)
   - `-G`: Specify group(s) to add

2. **Add to multiple groups**:
   ```bash
   sudo usermod -a -G HR,Managers ljuan
   sudo usermod -a -G Finance,Managers mmajor
   ```

3. **Special cases**:
   ```bash
   # CEO group
   sudo usermod -a -G CEO mjackson
   
   # Add ec2-user to all groups
   sudo usermod -a -G Sales,HR,Finance,Shipping,Managers,CEO ec2-user
   ```

### Step 3: Verify Group Memberships
```bash
sudo cat /etc/group | egrep "Sales|HR|Finance|Shipping|Managers|CEO"
```
**Expected Output**:
```
Sales:x:1014:arosalez,nwolf,ec2-user
HR:x:1015:ljuan,smartinez,ec2-user
Finance:x:1016:mmajor,ssarkar,ec2-user
Shipping:x:1017:eowusu,jdoe,psantos,ec2-user
Managers:x:1018:arosalez,ljuan,mmajor,ec2-user
CEO:x:1019:mjackson,ec2-user
```

## Task 4: Testing User Access

### Step 1: Switch to New User
```bash
su arosalez
```
**Authentication**:
```
Password: P@ssword1234!
```
**Prompt Change**: `[arosalez@ip-xxx-xxx-xxx-xxx ec2-user]$`

### Step 2: Test File Creation
1. **Attempt in ec2-user's home**:
   ```bash
   touch myFile.txt
   ```
   **Error**: `Permission denied`  
   **Why**: Users can't write in others' home directories by default

2. **Try with sudo**:
   ```bash
   sudo touch myFile.txt
   ```
   **Error**: `arosalez is not in sudoers file`  
   **Security**: Only authorized users can use `sudo`

### Step 3: Inspect Security Logs
1. **Return to ec2-user**:
   ```bash
   exit
   ```

2. **View security logs**:
   ```bash
   sudo cat /var/log/secure | tail -5
   ```
   **Sample Entry**:
   ```
   Aug 9 14:45:55 ip-10-0-10-217 sudo: arosalez : user NOT in sudoers ; TTY=pts/1 ; PWD=/home/ec2-user ; USER=root ; COMMAND=/bin/touch myFile.txt
   ```

## Advanced Topics & Troubleshooting

### Q: How to grant sudo privileges?
```bash
sudo visudo
```
Add line:
```
arosalez ALL=(ALL) ALL
```

### Q: How to set password expiration?
```bash
sudo chage -M 90 -W 7 arosalez
```
- `-M 90`: Password expires after 90 days
- `-W 7`: Warn 7 days before expiration

### Q: How to delete users?
```bash
sudo userdel -r jdoe  # -r removes home directory
```

### Q: How to see a user's groups?
```bash
groups arosalez
```
Output: `arosalez : arosalez Sales Managers`

## Best Practices

1. **Password Policies**:
   - Use `pwquality` to enforce complexity
   - Set expiration with `chage`

2. **Group Management**:
   - Create functional groups before users
   - Use secondary groups for permissions

3. **Security**:
   - Limit `sudo` access
   - Regularly review `/etc/passwd` and `/etc/group`
   - Monitor `/var/log/secure`

4. **Documentation**:
   - Maintain a user-group matrix
   - Document special permissions

## Conclusion

This lab covered:
1. User creation with `useradd` and `passwd`
2. Group management with `groupadd` and `usermod`
3. Permission testing and security logging
4. Enterprise-scale user/group structure implementation

These skills are essential for system administrators managing multi-user Linux environments, particularly in corporate or organizational settings with complex permission requirements.