# AWS Lab: Accessing Amazon Linux AMI via SSH and Using `man` Pages

## Introduction
This lab focuses on using Secure Shell (SSH) to connect to an Amazon Linux AMI instance and exploring the Linux manual (`man`) pages. The environment is pre-configured within Vocareum labs with specific AWS components.

## Lab Components
The following resources are provisioned for you:

1. **Amazon EC2 Command Host** (in public subnet)
   - Pre-configured Linux instance you'll SSH into
   - Located in a public subnet for accessibility

2. **Network Infrastructure**:
   - Public subnet
   - Amazon VPC (Virtual Private Cloud)

## Task 1: Accessing the Amazon Linux AMI via SSH

### Step 1: Locate Your Connection Details
1. In the Vocareum lab environment, find the **SSH connection details** provided
   - Typically includes:
     - Public IP address
     - Username (usually `ec2-user`)
     - Port number (default is 22)
     - SSH private key

### Step 2: Establish SSH Connection
**Using Linux/Mac Terminal**:
```bash
chmod 400 your-private-key.pem
ssh -i your-private-key.pem ec2-user@your-instance-public-ip
```

**Using Windows (PuTTY)**:
1. Convert .pem to .ppk using PuTTYgen
2. Configure PuTTY with:
   - Host Name: ec2-user@your-instance-public-ip
   - Port: 22
   - SSH Auth: Browse to select your .ppk file

**Expected Output**:
```
The authenticity of host '...' can't be established...
Are you sure you want to continue connecting (yes/no)? yes

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

[ec2-user@ip-xxx-xxx-xxx-xxx ~]$
```

### Step 3: Verify Connection
Run basic commands to verify access:
```bash
whoami  # Should return 'ec2-user'
pwd     # Should show your home directory
ls -la  # List directory contents
```

## Task 2: Understanding the `man` Command

### What are Manual Pages?
- **Definition**: Documentation system for Unix/Linux commands
- **Purpose**: Provides detailed information about commands, system calls, and configuration files
- **Organization**: Divided into numbered sections (1=commands, 2=system calls, etc.)

### Basic `man` Command Usage
```bash
man [section] command
```

### Step 1: Accessing a Manual Page
Example: View manual for `ls` command
```bash
man ls
```

**Navigation**:
- `Space`: Page down
- `b`: Page up
- `/pattern`: Search forward
- `n`: Next match
- `q`: Quit

### Step 2: Exploring Manual Sections
Different sections contain different types of documentation:
```bash
man 1 ls     # User commands (default)
man 5 passwd # File formats
man 7 signal # Miscellaneous
```

### Step 3: Searching Manual Pages
1. Search all manual pages for a term:
```bash
man -k "copy file"
```
2. Equivalent to `apropos` command:
```bash
apropos "copy file"
```

### Step 4: Understanding Manual Page Structure
A typical man page contains these sections:
1. NAME - Command name and brief description
2. SYNOPSIS - Command syntax
3. DESCRIPTION - Detailed explanation
4. OPTIONS - Command flags/parameters
5. EXAMPLES - Usage examples
6. SEE ALSO - Related commands

## Task 3: Practical Exercises with `man` Pages

### Exercise 1: Find File Copy Commands
```bash
man -k "copy file"
```
**Expected Output**:
```
cp (1)               - copy files and directories
rsync (1)            - a fast, versatile, remote (and local) file-copying tool
```

### Exercise 2: Examine `cp` Command
```bash
man cp
```
**Key Information to Note**:
- Syntax for recursive copy (`-r` flag)
- Preserve attributes (`-p` flag)
- Interactive mode (`-i` flag)

### Exercise 3: Search Within a Manual Page
While viewing `man ls`:
1. Type `/color` to search for color options
2. Find the `--color` option explanation

## Common Questions and Troubleshooting

**Q: Why can't I connect via SSH?**
A: Common issues include:
- Incorrect key file permissions (should be 400)
- Wrong username (Amazon Linux typically uses 'ec2-user')
- Security group blocking port 22
- Instance not running

**Q: How do I find what section a command is in?**
A: Use `whatis`:
```bash
whatis printf
```
Output shows:
```
printf (1)           - format and print data
printf (3)           - formatted output conversion
```

**Q: The man page I want isn't installed. How to get it?**
A: On Amazon Linux:
```bash
sudo yum install man-pages
```

**Q: How do I print a man page?**
A: Use `man -t command | lpr` or output to PDF:
```bash
man -t ls > ls.ps
ps2pdf ls.ps ls.pdf
```

## Advanced `man` Usage

### Viewing Specific Sections
When a term appears in multiple sections:
```bash
man 2 open   # System call version
man 3 open   # C library function
```

### Creating Custom Manual Pages
You can write your own man pages in groff format:
1. Create file `mytool.1`
2. Write in groff format
3. Install with:
```bash
sudo cp mytool.1 /usr/share/man/man1/
sudo mandb
```

## Best Practices

1. **Always check man pages** before using unfamiliar commands
2. **Use `-k` or `apropos`** when you don't know the exact command name
3. **Bookmark useful commands** you discover in man pages
4. **Combine with `--help`** for quick reference:
```bash
ls --help
```

## Conclusion

This lab taught you:
1. How to securely connect to an Amazon Linux instance via SSH
2. The structure and purpose of Linux manual pages
3. Effective techniques for finding command documentation
4. How to navigate and search within man pages

These skills form the foundation for working with Linux systems and are essential for AWS administration and development work.