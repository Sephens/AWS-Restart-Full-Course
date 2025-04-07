# Working with Files in Linux - Comprehensive Guide

## Table of Contents
- [Working with Files in Linux - Comprehensive Guide](#working-with-files-in-linux---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [File Inspection Commands](#file-inspection-commands)
    - [hash Command](#hash-command)
    - [cksum Command](#cksum-command)
  - [File Search Commands](#file-search-commands)
    - [find Command](#find-command)
    - [grep Command](#grep-command)
    - [diff Command](#diff-command)
  - [File Linking](#file-linking)
    - [Hard Links](#hard-links)
    - [Symbolic Links](#symbolic-links)
  - [File Compression](#file-compression)
    - [tar Command](#tar-command)
    - [gzip Command](#gzip-command)
    - [zip and unzip Commands](#zip-and-unzip-commands)
  - [Checkpoint Questions \& Answers](#checkpoint-questions--answers)
  - [Key Takeaways](#key-takeaways)

## File Inspection Commands

### hash Command

**Purpose:** Tracks and displays recently executed commands  
**Key features:**
- Maintains a hash table of command locations
- Shows hit count (number of executions)
- Can manipulate command path resolution

**Examples:**
```bash
hash                 # Show all hashed commands
hash -l              # Display in reusable format
hash -t ls           # Show full path of 'ls'
hash -d vim          # Remove vim from hash table
hash -p /usr/bin/vim myvim  # Create alias 'myvim' for vim
```

**Use case:** Troubleshooting command not found errors by verifying path resolution

### cksum Command

**Purpose:** Verify file integrity through checksums  
**How it works:**
- Generates CRC (Cyclic Redundancy Check) value
- Outputs checksum + byte count
- Identical files produce identical checksums

**Examples:**
```bash
cksum document.txt
# 3292389273 1048576 document.txt
# Checksum^  Size^    Filename^

# Verify transfer integrity:
cksum original.txt > checksum.txt
# After transfer:
cksum received.txt | diff - checksum.txt
```

**Advanced alternatives:**
```bash
md5sum file.txt    # 128-bit MD5 hash
sha256sum file.txt # 256-bit SHA hash (more secure)
```

## File Search Commands

### find Command

**Purpose:** Locate files based on various criteria

**Basic syntax:**
```bash
find [path] [options] [action]
```

**Common options:**
| Option | Description | Example |
|--------|-------------|---------|
| `-name` | Search by name | `find / -name "*.conf"` |
| `-iname` | Case-insensitive name | `find . -iname "README*"` |
| `-user` | Search by owner | `find ~ -user ec2-user` |
| `-size` | Search by size | `find /var/log -size +10M` |
| `-mtime` | Modified time | `find /etc -mtime -7` (last 7 days) |

**Advanced examples:**
```bash
# Find and delete old temp files
find /tmp -type f -mtime +30 -delete

# Find PHP files containing "mysql_connect"
find . -name "*.php" -exec grep -l "mysql_connect" {} \;

# Find large files and sort by size
find / -type f -size +100M -exec ls -lh {} + | sort -k5 -rh
```

### grep Command

**Purpose:** Search file contents for patterns

**Common options:**
| Option | Description | Example |
|--------|-------------|---------|
| `-i` | Case insensitive | `grep -i "error" log.txt` |
| `-r` | Recursive search | `grep -r "function" /src` |
| `-n` | Show line numbers | `grep -n "TODO" script.py` |
| `-v` | Invert match | `grep -v "#" config.cfg` |
| `-A/B/C` | Context lines | `grep -A3 -B2 "exception" log.txt` |

**Advanced usage:**
```bash
# Count occurrences per file
grep -rc "pattern" /path/to/files

# Search multiple patterns
grep -e "error" -e "warning" system.log

# Use regex patterns
grep -E "^[A-Za-z].*[0-9]$" data.txt
```

### diff Command

**Purpose:** Compare files line by line

**Output formats:**
- Normal (default)
- Unified (`-u`) - more readable
- Context (`-c`) - shows surrounding lines

**Examples:**
```bash
diff file1.txt file2.txt
diff -u old.conf new.conf > changes.patch
diff -rq dir1/ dir2/  # Compare directories
```

**Colorized output:**
```bash
diff --color=always file1 file2 | less -R
```

## File Linking

### Hard Links

**Characteristics:**
- Points directly to file's inode
- Shares same storage as original
- Cannot cross filesystems
- All links equal (no "original")
- Persists after original deletion

**Creation:**
```bash
ln original.txt hardlink.txt
```

**Verification:**
```bash
ls -i  # Show inode numbers
stat file.txt  # Show link count
```

### Symbolic Links

**Characteristics:**
- Points to filename (not inode)
- Can cross filesystems
- Can point to directories
- Becomes broken if target deleted
- Shows as `lrwxrwxrwx` in `ls -l`

**Creation:**
```bash
ln -s /path/to/original symlink_name
```

**Best practices:**
- Use absolute paths for system-wide links
- Relative paths work for local links
- Verify with `readlink symlink_name`

## File Compression

### tar Command

**Purpose:** Archive files without compression (tarball)

**Common operations:**
```bash
# Create archive
tar -cvf archive.tar file1 file2 dir/

# Extract archive
tar -xvf archive.tar

# List contents
tar -tvf archive.tar
```

**Compressed archives:**
```bash
# Create gzipped tar
tar -czvf archive.tar.gz /path/to/files

# Extract gzipped tar
tar -xzvf archive.tar.gz

# For bzip2 use -j instead of -z
tar -cjvf archive.tar.bz2 files/
```

### gzip Command

**Purpose:** Compress individual files

**Examples:**
```bash
gzip largefile.log       # Compress to largefile.log.gz
gzip -9 data.csv        # Maximum compression
gzip -d archive.gz      # Decompress
zcat file.gz            # View without decompressing
```

**Combining with tar:**
```bash
# Create and compress in one step
tar -czvf backup.tar.gz /important/data

# Alternative separate steps
tar -cvf backup.tar /important/data
gzip backup.tar
```

### zip and unzip Commands

**Purpose:** Create/extract ZIP archives (compatible with Windows)

**Examples:**
```bash
# Create ZIP
zip -r archive.zip folder/

# Extract ZIP
unzip archive.zip

# Exclude files
zip -r backup.zip /data -x "*.tmp"

# Split into volumes
zip -r -s 100m backup.zip large_folder/
```

**Password protection:**
```bash
zip -e secure.zip sensitive.doc
```

## Checkpoint Questions & Answers

1. **Can find locate files by owner?**  
   Yes: `find /path -user username` locates all files owned by specified user.

2. **Which command bundles files?**  
   `tar` bundles files into a single archive (tarball). Example:  
   ```bash
   tar -cvf bundle.tar file1 file2 dir/
   ```

3. **How to verify file integrity after transfer?**  
   Use checksum comparison:  
   ```bash
   # Sender:
   cksum important.dat > checksum.txt
   
   # Receiver:
   cksum received.dat | diff - checksum.txt
   # No output means identical files
   ```

## Key Takeaways

1. **File Inspection**
   - `hash`: Track command usage and paths
   - `cksum`: Basic file integrity verification
   - Prefer `sha256sum` for security-critical checks

2. **Search Techniques**
   - `find`: Powerful file location tool
   - `grep`: Content searching with regex support
   - Combine them: `find . -name "*.log" -exec grep -l "error" {} +`

3. **Linking Strategies**
   - Hard links: Same filesystem, persistent
   - Soft links: Flexible, can break

4. **Compression Methods**
   - `tar + gzip`: Standard Linux compression
   - `zip`: Cross-platform compatibility
   - Consider compression level vs speed tradeoffs

**Example Workflow:**
```bash
# 1. Find all modified config files
find /etc -name "*.conf" -mtime -1

# 2. Search for deprecated setting
grep -r "UseDNS yes" /etc/ssh/

# 3. Create backup of modified files
tar -czvf ssh_backup_$(date +%F).tar.gz /etc/ssh/

# 4. Verify backup integrity
sha256sum ssh_backup_*.tar.gz > backup_checksums.txt

# 5. Create symlink to latest backup
ln -s ssh_backup_*.tar.gz latest_backup.tar.gz
```