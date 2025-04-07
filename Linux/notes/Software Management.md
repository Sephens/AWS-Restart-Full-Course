# Linux Software Management - Comprehensive Guide

## Table of Contents
- [Linux Software Management - Comprehensive Guide](#linux-software-management---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Package Management Systems](#package-management-systems)
    - [RPM/YUM (Red Hat-based)](#rpmyum-red-hat-based)
    - [DPKG/APT (Debian-based)](#dpkgapt-debian-based)
  - [Working with Repositories](#working-with-repositories)
  - [YUM Package Manager](#yum-package-manager)
    - [Basic Operations](#basic-operations)
    - [Advanced Usage](#advanced-usage)
  - [Installing from Source Code](#installing-from-source-code)
  - [File Retrieval Utilities](#file-retrieval-utilities)
    - [wget](#wget)
    - [curl](#curl)
  - [Practical Examples](#practical-examples)
  - [Checkpoint Questions \& Answers](#checkpoint-questions--answers)
  - [Key Takeaways](#key-takeaways)

## Package Management Systems

### RPM/YUM (Red Hat-based)

**Used by:** Amazon Linux 2, RHEL, CentOS, Fedora  
**File extension:** `.rpm`  
**Configuration files:**
- `/etc/yum.conf` (main configuration)
- `/etc/yum.repos.d/` (repository definitions)

**Key tools:**
- `rpm`: Low-level package manager
- `yum`/`dnf`: High-level package manager (handles dependencies)

**Example workflow:**
```bash
# Search for a package
yum search nginx

# Install with dependencies
sudo yum install -y nginx

# Verify installation
rpm -qi nginx
```

### DPKG/APT (Debian-based)

**Used by:** Ubuntu, Debian  
**File extension:** `.deb`  
**Configuration files:**
- `/etc/apt/sources.list`
- `/etc/apt/sources.list.d/`

**Key tools:**
- `dpkg`: Low-level package manager
- `apt`/`apt-get`: High-level package manager

**Example workflow:**
```bash
# Update package lists
sudo apt update

# Install package
sudo apt install nginx

# Verify installation
dpkg -l nginx
```

## Working with Repositories

Repositories are collections of software packages maintained on servers. AWS provides several for Amazon Linux 2:

- `amzn2-core`: Core OS packages
- `amzn2extra-docker`: Docker-related packages
- `amzn2extra-nginx`: Nginx packages

**Managing repositories:**
```bash
# List enabled repos
yum repolist

# Enable extra repo
sudo amazon-linux-extras enable nginx1

# Add custom repo
sudo yum-config-manager --add-repo http://example.com/repo
```

## YUM Package Manager

### Basic Operations

| Command | Description | Example |
|---------|-------------|---------|
| `install` | Install package | `yum install httpd` |
| `update` | Update package | `yum update httpd` |
| `remove` | Remove package | `yum remove httpd` |
| `search` | Search packages | `yum search python` |
| `list` | List packages | `yum list installed` |

### Advanced Usage

**Common options:**
- `-y`: Assume yes to prompts
- `--nogpgcheck`: Skip GPG verification (not recommended)
- `--enablerepo`: Temporarily enable repo

**Useful commands:**
```bash
# View package info
yum info nginx

# Check available updates
yum check-update

# Clean cache
yum clean all

# View history
yum history
```

## Installing from Source Code

**Typical workflow:**
1. **Install development tools:**
   ```bash
   sudo yum groupinstall "Development Tools"
   ```

2. **Download source:**
   ```bash
   wget https://example.com/software-1.0.tar.gz
   ```

3. **Extract:**
   ```bash
   tar xzvf software-1.0.tar.gz
   cd software-1.0
   ```

4. **Configure, compile, install:**
   ```bash
   ./configure
   make
   sudo make install
   ```

**Pros:**
- Get latest versions not in repos
- Custom compilation options
- Access to development versions

**Cons:**
- No automatic dependency resolution
- No automatic updates
- More complex troubleshooting

## File Retrieval Utilities

### wget

**Features:**
- Recursive downloads
- Automatic resume
- Simple syntax

**Examples:**
```bash
# Basic download
wget https://example.com/file.zip

# Continue interrupted download
wget -c https://example.com/large-file.iso

# Mirror website
wget -mk https://example.com
```

### curl

**Features:**
- Supports more protocols (including SCP, SFTP)
- Better for API interactions
- Output control

**Examples:**
```bash
# Download file
curl -o localname.zip https://example.com/file.zip

# Test API endpoint
curl -X GET https://api.example.com/data

# Upload file
curl -F "file=@localfile" https://example.com/upload
```

## Practical Examples

**1. Installing AWS CLI:**
```bash
# For Amazon Linux 2:
sudo yum install -y awscli

# Alternative method:
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

**2. Setting up LAMP stack:**
```bash
sudo yum install -y httpd mariadb-server php php-mysqlnd
sudo systemctl start httpd
sudo systemctl start mariadb
sudo systemctl enable httpd
sudo systemctl enable mariadb
```

**3. Finding package files:**
```bash
# For installed RPM:
rpm -ql httpd

# For installed DEB:
dpkg -L apache2
```

## Checkpoint Questions & Answers

1. **How is the software installed by a package manager provided?**  
   - Software is provided in pre-compiled packages (`.rpm` or `.deb`) containing:
     - Binary executables
     - Configuration files
     - Documentation
     - Dependency information
     - Installation scripts

2. **What is another way to install software on Linux besides package managers?**  
   - Compiling from source code:
     - Download source tarball
     - Extract and run `./configure`, `make`, `make install`
   - Example compiling Nginx:
     ```bash
     wget https://nginx.org/download/nginx-1.19.10.tar.gz
     tar xzvf nginx-1.19.10.tar.gz
     cd nginx-1.19.10
     ./configure
     make
     sudo make install
     ```

3. **Which utility (wget or curl) resumes interrupted downloads?**  
   - `wget` automatically resumes interrupted downloads with `-c` option
   - `curl` requires manual resume with `-C -` option

## Key Takeaways

1. **Package Management Essentials**
   - Know your distro's package system (RPM/YUM vs DPKG/APT)
   - Always prefer package managers over source when possible
   - Keep repositories updated (`yum update` or `apt update`)

2. **Repository Knowledge**
   - Official repos provide verified, secure packages
   - Be cautious with third-party repositories
   - AWS maintains optimized repos for Amazon Linux

3. **Best Practices**
   - Use `-y` carefully in scripts
   - Regularly clean package cache (`yum clean all`)
   - Review package contents before installation (`rpm -qlp`)
   - Document manual installations for future reference

4. **Troubleshooting Tips**
   - Check `/var/log/yum.log` for installation issues
   - Verify package integrity with `rpm -V`
   - Resolve dependencies with `yum deplist`

**Example Maintenance Checklist:**
1. Update package lists: `sudo yum makecache`
2. Apply security updates: `sudo yum update --security`
3. Clean old packages: `sudo package-cleanup --oldkernels`
4. Verify system integrity: `rpm -Va`