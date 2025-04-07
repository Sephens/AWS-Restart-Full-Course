# Introduction to Linux - Comprehensive Guide

## Table of Contents
1. [What is Linux?](#what-is-linux)
2. [Linux Components](#linux-components)
3. [Linux User Interfaces](#linux-user-interfaces)
4. [Linux Documentation](#linux-documentation)
5. [Linux Distributions](#linux-distributions)
6. [Connecting to Linux Servers](#connecting-to-linux-servers)
7. [Key Takeaways](#key-takeaways)

---

## What is Linux?

### Definition
Linux is an **open-source** operating system (OS) based on Unix, created by **Linus Torvalds** in 1991. It is modular, stable, and widely used for both servers and desktops.

### Key Features
| Feature | Description | Example |
|---------|------------|---------|
| **Open Source** | Code is publicly modifiable | Custom kernels for specific needs |
| **Multi-User** | Supports multiple simultaneous users | Shared server environments |
| **Multi-Tasking** | Runs multiple applications concurrently | Running a web server + database |
| **Networking** | Built-in support for networks | SSH, HTTP, FTP services |

**Example**:  
Amazon Linux 2 is optimized for AWS EC2 instances, offering automatic security updates.

---

## Linux Components

### 1. Kernel
- **Core Function**: Manages hardware resources (CPU, memory, devices).  
- **Example**:  
  ```bash
  uname -r  # Check kernel version
  ```
  Output: `5.10.0-1062.aws.x86_64`

### 2. Daemons
- Background services (names end with `d`).  
- **Examples**:  
  - `sshd`: Handles SSH connections.  
  - `syslogd`: Manages system logs.  

### 3. Applications
- User programs like web browsers (`Firefox`) or text editors (`Vim`).  

### 4. Files & Directories
- **Structure**:  
  ```plaintext
  /home/user/file.txt  # Path format
  ```
- **Config Files**:  
  - Location: `/etc/` (e.g., `/etc/ssh/sshd_config`).  
  - Extensions: `.conf`, `.cfg`.

---

## Linux User Interfaces

### CLI vs. GUI
| Interface | Pros | Cons | Use Case |
|-----------|------|------|----------|
| **CLI** | Lightweight, scriptable | Steeper learning curve | Servers, automation |
| **GUI** | User-friendly | Resource-intensive | Desktops, beginners |

### Shell Types
| Shell | Description | Default in |
|-------|-------------|------------|
| `bash` | Bourne-Again Shell (default) | Most Linux distros |
| `sh` | Original Unix shell | Legacy systems |
| `zsh` | Extended features | macOS (recent) |

**Example**:  
To check your shell:  
```bash
echo $SHELL
```
Output: `/bin/bash`

---

## Linux Documentation

### `man` Command
- **Purpose**: Displays manual pages for commands.  
- **Usage**:  
  ```bash
  man ls  # Show manual for 'ls'
  ```
- **Navigation**:  
  - `Space`: Next page  
  - `/keyword`: Search  
  - `q`: Quit  

**Example Output**:  
```
LS(1)  
NAME  
       ls - list directory contents  
SYNOPSIS  
       ls [OPTION]... [FILE]...
```

### Other Help Tools
- `--help` flag: Quick summary (e.g., `ls --help`).  
- `info`: Detailed docs (e.g., `info coreutils`).

---

## Linux Distributions

### Major Families
| Distribution | Derived From | Example OS |
|--------------|--------------|------------|
| **Red Hat** | Fedora | RHEL, CentOS, Amazon Linux 2 |
| **Debian** | Debian | Ubuntu, Kali Linux |
| **SUSE** | OpenSUSE | SUSE Enterprise |

### Popular Distros
1. **Amazon Linux 2**: Optimized for AWS.  
2. **Ubuntu**: User-friendly, great for beginners.  
3. **CentOS Stream**: Rolling-release RHEL derivative.  

**Installation Example**:  
```bash
sudo yum update  # Amazon Linux/CentOS
sudo apt update  # Debian/Ubuntu
```

---

## Connecting to Linux Servers

### SSH Access
- **Command**:  
  ```bash
  ssh -i key.pem ec2-user@<IP>  # Linux/macOS
  ```
- **Windows**: Use **PuTTY** with `.ppk` keys.  

### Key Steps:
1. **Download Key**: `.pem` (Linux) or `.ppk` (PuTTY).  
2. **Set Permissions**:  
   ```bash
   chmod 400 key.pem  # Secure the key
   ```
3. **Connect**:  
   ```bash
   ssh -i key.pem ec2-user@1.2.3.4
   ```

**Lab Environment**:  
- AWS EC2 instances use `ec2-user` as the default account.  
- Security groups must allow **port 22** (SSH).  

---

## Key Takeaways

1. **Linux is Open Source**: Free to use, modify, and distribute.  
2. **Distributions**: Packages like Amazon Linux 2 bundle the kernel with tools.  
3. **CLI is Powerful**: Essential for servers and automation.  
4. **Bash is Default**: Learn `bash` for most Linux systems.  
5. **Documentation**: Use `man` and `--help` for command references.  

**Best Practices**:  
- Always secure SSH keys (`chmod 400`).  
- Prefer CLI for server management.  
- Regularly update your system (`yum/apt update`).  

---

## Checkpoint Answers

**Q: What is a Linux distribution?**  
A: A packaged OS combining the Linux kernel with software (e.g., Ubuntu, Amazon Linux 2).  

**Q: Is bash the default shell?**  
A: **True** – Most distros use `bash` as the default.  

**Q: How to get command help?**  
A: Use `man <command>` (e.g., `man ls`).  

---
