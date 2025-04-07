# Linux Users, Groups, and Permissions - Comprehensive Guide

## Table of Contents
- [Linux Users, Groups, and Permissions - Comprehensive Guide](#linux-users-groups-and-permissions---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [User Management](#user-management)
    - [Understanding /etc/passwd](#understanding-etcpasswd)
    - [User Account Commands](#user-account-commands)
  - [Group Management](#group-management)
    - [Understanding /etc/group](#understanding-etcgroup)
    - [Group Commands](#group-commands)
  - [Permission Elevation](#permission-elevation)
    - [su Command](#su-command)
    - [sudo Command](#sudo-command)
  - [AWS IAM Integration](#aws-iam-integration)
  - [Checkpoint Questions \& Answers](#checkpoint-questions--answers)
  - [Key Takeaways](#key-takeaways)

## User Management

### Understanding /etc/passwd

The `/etc/passwd` file contains all user account information in a colon-separated format:

```
username:password:UID:GID:GECOS:home_directory:shell
```

**Example entry:**
```
mmajor:x:1002:1002:Mary Major:/home/mmajor:/bin/bash
```

**Key fields:**
- **Username**: Login name (mmajor)
- **Password**: 'x' indicates password is in /etc/shadow
- **UID**: User ID (1002)
- **GID**: Primary group ID (1002)
- **GECOS**: Comment/description (Mary Major)
- **Home directory**: (/home/mmajor)
- **Shell**: Default shell (/bin/bash)

**View commands:**
```bash
tail /etc/passwd       # Last 10 users
head -n 5 /etc/passwd  # First 5 users
grep mmajor /etc/passwd # Find specific user
```

### User Account Commands

| Command | Description | Example |
|---------|-------------|---------|
| `useradd` | Create user | `useradd -c "John Doe" -d /home/jdoe jdoe` |
| `usermod` | Modify user | `usermod -s /bin/zsh jdoe` |
| `userdel` | Delete user | `userdel -r jdoe` (with home dir) |
| `passwd` | Set password | `passwd jdoe` |

**Detailed examples:**
```bash
# Create user with custom home and shell
sudo useradd -m -d /home/dev_jdoe -s /bin/zsh -c "Developer John Doe" jdoe

# Modify user to expire on specific date
sudo usermod -e 2025-12-31 jdoe

# Lock/unlock account
sudo passwd -l jdoe  # Lock
sudo passwd -u jdoe  # Unlock
```

## Group Management

### Understanding /etc/group

Group information is stored in `/etc/group` with format:
```
group_name:password:GID:user_list
```

**Example:**
```
devs:x:1004:mmajor,jdoe
```

**View commands:**
```bash
tail /etc/group
getent group devs  # Alternative to grep
```

### Group Commands

| Command | Description | Example |
|---------|-------------|---------|
| `groupadd` | Create group | `groupadd devs` |
| `groupmod` | Modify group | `groupmod -n developers devs` |
| `groupdel` | Delete group | `groupdel devs` |
| `gpasswd` | Manage members | `gpasswd -a jdoe devs` |

**Managing group membership:**
```bash
# Add user to group (append)
sudo usermod -aG devs jdoe

# Set exact group membership
sudo usermod -G devs,hr jdoe

# Remove user from group
sudo gpasswd -d jdoe devs

# Set group administrators
sudo gpasswd -A jdoe devs
```

## Permission Elevation

### su Command

**Substitute User** - switches to another user account:

```bash
su - jdoe       # Login as jdoe with their environment
su -            # Login as root (requires root password)
su -c "whoami"  # Run single command as another user
```

**Key differences:**
- `su` - keeps current environment
- `su -` - loads target user's environment

### sudo Command

**Superuser Do** - executes commands with elevated privileges:

```bash
sudo yum update          # Run as root
sudo -u jdoe whoami     # Run as specific user
sudo -l                 # List allowed commands
```

**Configuring sudo access:**
1. Edit sudoers file safely:
   ```bash
   sudo visudo
   ```
2. Example entries:
   ```
   # Allow user full access
   jdoe ALL=(ALL) ALL
   
   # Allow group passwordless access to specific commands
   %devs ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart httpd
   ```

**Best Practices:**
- Prefer sudo over su for auditing
- Grant minimal required permissions
- Use groups for sudo access management
- Regularly review `/var/log/secure` for sudo usage

## AWS IAM Integration

**AWS Identity and Access Management (IAM) provides:**

1. **Centralized access control** for AWS resources
2. **Three access methods**:
   - AWS Management Console (Web UI)
   - AWS CLI (Command Line)
   - AWS SDKs (Programmatic)

3. **Key components**:
   - **Users**: Individual accounts (like Linux users)
   - **Groups**: Collections of users (like Linux groups)
   - **Roles**: Temporary permissions for services
   - **Policies**: JSON documents defining permissions

**Example IAM policy (similar to sudoers):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:Describe*",
      "Resource": "*"
    }
  ]
}
```

## Checkpoint Questions & Answers

1. **Which command adds a user account?**  
   - `useradd` - Creates new user accounts  
   Example: `sudo useradd -m -s /bin/bash jdoe`

2. **Which command resets a user password?**  
   - `passwd` - Sets or changes passwords  
   Example: `sudo passwd jdoe`

3. **How are groups useful to administrators?**  
   - Enables bulk permission management  
   - Simplifies access control (e.g., `chown :devs file`)  
   - Allows sudo access delegation to groups  
   Example: `sudo chmod 770 /projects -R -P devs`

4. **Which command grants full admin permissions in the user's environment?**  
   - `su root` - Switches to root while keeping current environment variables  
   Contrast with `su - root` which loads root's environment

## Key Takeaways

1. **User Security Principles**
   - Always use `sudo` instead of direct root login
   - Follow principle of least privilege
   - Regularly audit user accounts and permissions

2. **Effective Group Management**
   - Organize users by function (devs, admins, etc.)
   - Set group permissions on shared directories:
     ```bash
     sudo chown :devs /shared
     sudo chmod 2775 /shared  # Set group sticky bit
     ```

3. **Sudo Best Practices**
   - Use `visudo` for safe editing
   - Grant specific commands rather than ALL
   - Implement passwordless sudo cautiously

4. **AWS IAM Parallels**
   - IAM users ≈ Linux users
   - IAM groups ≈ Linux groups
   - IAM policies ≈ sudoers entries

**Example Workflow for New Developer:**
```bash
# Create account
sudo useradd -m -c "Dev User" -s /bin/bash -G devs dev_user

# Set password
sudo passwd dev_user

# Configure sudo access
sudo visudo
# Add: %devs ALL=(ALL) /usr/bin/git, /usr/bin/docker

# Set file permissions
sudo chown :devs /projects
sudo chmod 2775 /projects
```

**Audit Checklist:**
1. Review `/etc/passwd` for unused accounts
2. Check `/etc/group` for proper membership
3. Verify sudoers file with `sudo -l -U username`
4. Monitor `/var/log/secure` for privilege escalations