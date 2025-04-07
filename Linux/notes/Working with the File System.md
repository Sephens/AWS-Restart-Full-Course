# Working with the Linux File System - Comprehensive Guide

## Table of Contents
- [Working with the Linux File System - Comprehensive Guide](#working-with-the-linux-file-system---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Linux File System Fundamentals](#linux-file-system-fundamentals)
    - [Everything is a File](#everything-is-a-file)
    - [File Naming Conventions](#file-naming-conventions)
  - [File System Hierarchy Standard (FHS)](#file-system-hierarchy-standard-fhs)
  - [Essential File Commands](#essential-file-commands)
    - [Navigation Commands](#navigation-commands)
    - [File Inspection Commands](#file-inspection-commands)
    - [File Operations Commands](#file-operations-commands)
  - [Directory Management](#directory-management)
  - [Path Navigation](#path-navigation)
    - [Absolute vs Relative Paths](#absolute-vs-relative-paths)
  - [Checkpoint Questions \& Answers](#checkpoint-questions--answers)
  - [Key Takeaways](#key-takeaways)

## Linux File System Fundamentals

### Everything is a File

**Core Concept:** In Linux, everything is represented as a file:
- Regular files (documents, scripts)
- Directories (special files that contain other files)
- Devices (/dev/sda1)
- Processes (/proc/[PID])
- Sockets and pipes

**Examples:**
```bash
ls /dev    # List device files
ls /proc   # View process information
cat /proc/cpuinfo  # CPU information as a file
```

### File Naming Conventions

**Rules:**
- Case sensitive (File.txt ≠ file.txt)
- Can contain most characters except `/`
- Spaces allowed but require quoting/escaping
- Extensions are conventional but not enforced

**Best Practices:**
```bash
# Good naming
report_2023.pdf
backup_script.sh

# Problematic naming (avoid)
My Document.txt  # Space requires quoting
file/name.txt    # Contains illegal /
```

## File System Hierarchy Standard (FHS)

**Key Directories:**

| Directory | Purpose | Example Contents |
|-----------|---------|------------------|
| `/`       | Root    | Top-level directory |
| `/bin`    | Essential binaries | ls, cp, bash |
| `/etc`    | Configuration files | sshd_config |
| `/home`   | User directories | /home/ec2-user |
| `/var`    | Variable data | logs, databases |
| `/tmp`    | Temporary files | - |
| `/usr`    | User programs | Applications |
| `/dev`    | Device files | sda, tty |
| `/proc`   | Process info | Virtual filesystem |

**View Structure:**
```bash
tree -L 1 /  # View top-level directories
ls -l /etc   # Examine config files
```

## Essential File Commands

### Navigation Commands

| Command | Description | Example |
|---------|-------------|---------|
| `pwd`   | Print working directory | `pwd` → `/home/user` |
| `cd`    | Change directory | `cd /var/log` |
| `ls`    | List directory contents | `ls -lah` |

**Advanced `ls` Options:**
```bash
ls -l   # Long listing
ls -a   # Show hidden files
ls -t   # Sort by modification time
ls -S   # Sort by size
ls -R   # Recursive listing
```

### File Inspection Commands

| Command | Description | Example |
|---------|-------------|---------|
| `cat`   | Display entire file | `cat config.txt` |
| `less`  | Interactive file viewer | `less logfile.log` |
| `more`  | Basic pager | `more longfile.txt` |
| `head`  | Show first lines | `head -n 5 file.txt` |
| `tail`  | Show last lines | `tail -f app.log` |

**Comparison:**
```bash
# For large files:
less bigfile.log  # Recommended (can scroll both ways)
more bigfile.log  # Older, limited functionality

# Monitoring logs:
tail -f /var/log/syslog  # Follow new entries
```

### File Operations Commands

| Command | Description | Example |
|---------|-------------|---------|
| `cp`    | Copy files | `cp file.txt backup/` |
| `mv`    | Move/rename | `mv old.txt new.txt` |
| `rm`    | Remove files | `rm -i oldfile.txt` |
| `touch` | Create empty file | `touch newfile.txt` |

**Important Options:**
```bash
cp -rv source_dir/ dest_dir/  # Recursive verbose copy
mv -i file.txt ~/backups/     # Interactive move
rm -I *.tmp                   # Interactive bulk delete
```

## Directory Management

| Command | Description | Example |
|---------|-------------|---------|
| `mkdir` | Create directory | `mkdir -p project/{src,test}` |
| `rmdir` | Remove empty dir | `rmdir emptydir` |
| `rm -r` | Remove recursively | `rm -rf tempdir/` |

**Advanced Usage:**
```bash
# Create complex structure
mkdir -p project/{src/{main,test},docs,config}

# Set permissions on creation
mkdir -m 750 secure_dir
```

## Path Navigation

### Absolute vs Relative Paths

**Absolute Path:**
- Starts from root (`/`)
- Always points to same location
- Example: `/home/user/Documents/report.txt`

**Relative Path:**
- Starts from current directory
- Changes based on working directory
- Example: `../config/settings.ini` (from `/home/user`)

**Navigation Examples:**
```bash
cd /var/log          # Absolute
cd ../../etc         # Relative (go up two levels)
cd ~/Documents       # Home directory reference
cd -                 # Previous directory
```

**Special Path References:**
- `.` - Current directory
- `..` - Parent directory
- `~` - Home directory
- `-` - Previous directory

## Checkpoint Questions & Answers

1. **Difference between absolute and relative paths?**  
   - Absolute: Full path from root (`/etc/ssh/config`)  
   - Relative: Path from current location (`../config/file.txt`)  

2. **When to use `less` vs `more`?**  
   - Use `less` for:  
     - Bidirectional scrolling  
     - Faster loading of large files  
     - Advanced search (`/pattern`)  
   - `more` is simpler but only scrolls forward  

3. **How to verify file integrity after transfer?**  
   ```bash
   # Sender:
   sha256sum important.dat > checksum.txt
   
   # Receiver:
   sha256sum -c checksum.txt
   ```

## Key Takeaways

1. **File System Basics**
   - Everything in Linux is a file
   - Case-sensitive naming
   - FHS provides standardized directory structure

2. **Essential Commands**
   - Navigation: `pwd`, `cd`, `ls`
   - Inspection: `cat`, `less`, `head`, `tail`
   - Operations: `cp`, `mv`, `rm`, `touch`

3. **Path Navigation**
   - Absolute paths for scripting/reliability
   - Relative paths for quick navigation
   - Special references (`.`, `..`, `~`, `-`)

4. **Best Practices**
   - Use `less` instead of `more`
   - Prefer `-i` flag for destructive operations
   - Combine commands with pipes:  
     `grep "error" /var/log/syslog | less`

**Example Workflow:**
```bash
# 1. Navigate to project directory
cd ~/projects/webapp

# 2. Create directory structure
mkdir -p {src,assets/{images,styles},config}

# 3. Copy template files
cp -r ../templates/* src/

# 4. Check disk usage
du -sh .  # Human-readable size

# 5. Find largest files
find . -type f -exec du -h {} + | sort -rh | head -n 5
```