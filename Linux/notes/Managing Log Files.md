# Managing Log Files in Linux - Comprehensive Guide

## Table of Contents
1. [Introduction to Log Files](#introduction-to-log-files)
2. [Viewing Log Files](#viewing-log-files)
3. [Logging Levels](#logging-levels)
4. [Key Log Files](#key-log-files)
5. [Log Rotation](#log-rotation)
6. [Key Takeaways](#key-takeaways)

---

## Introduction to Log Files

### What Are Log Files?
Log files are records of events that occur within a Linux system, including:
- **System events** (startup/shutdown times)
- **User activities** (logins/logouts)
- **Application operations** (errors, transactions)
- **Service status** (running/stopped services)

**Example**:  
```bash
sudo cat /var/log/yum.log  # Shows package installation history
```

### Importance of Logging
- **Security Audits**: Track unauthorized access attempts.
- **Troubleshooting**: Identify root causes of system issues.
- **Compliance**: Meet industry regulations (e.g., SLAs).

---

## Viewing Log Files

### Essential Commands
| Command | Purpose | Example |
|---------|---------|---------|
| `cat` | Display entire file | `cat /var/log/syslog` |
| `tail` | Show last lines | `tail -n 20 /var/log/auth.log` |
| `head` | Show first lines | `head /var/log/boot.log` |
| `less` | Interactive viewing | `less /var/log/nginx/access.log` |
| `grep` | Search for patterns | `grep "ERROR" /var/log/syslog` |

**Example**:  
```bash
sudo tail -f /var/log/httpd/error_log  # Real-time monitoring of Apache errors
```

### Filtering Logs with `grep`
- Search for specific errors:  
  ```bash
  grep "Failed password" /var/log/auth.log  # Find failed login attempts
  ```
- Combine with `tail`:  
  ```bash
  tail -f /var/log/secure | grep "invalid user"  # Monitor suspicious logins
  ```

---

## Logging Levels

### Severity Levels
| Level | Keyword | Description |
|-------|---------|-------------|
| 0 | EMERG | System is unusable |
| 1 | ALERT | Immediate action required |
| 2 | CRIT | Critical failures |
| 3 | ERROR | Non-critical errors |
| 4 | WARN | Warnings (default level) |
| 5 | NOTICE | Normal but significant events |
| 6 | INFO | Informational messages |
| 7 | DEBUG | Detailed debugging info |

**Note**: Higher levels include lower ones (e.g., `WARN` shows `ERROR` and `CRIT` messages).

---

## Key Log Files

### Common Log Locations
| File | Purpose |
|------|---------|
| `/var/log/syslog` | General system messages |
| `/var/log/auth.log` | Authentication logs (Debian) |
| `/var/log/secure` | Authentication logs (RHEL) |
| `/var/log/kern.log` | Kernel messages |
| `/var/log/httpd/` | Apache web server logs |
| `/var/log/mysql/` | MySQL database logs |

**Example**:  
```bash
sudo less /var/log/syslog  # View system-wide events
```

### Specialized Commands
- `lastlog`: View recent user logins.  
  ```bash
  lastlog -u ec2-user  # Check login history for a user
  ```
- `dmesg`: Kernel ring buffer messages.  
  ```bash
  dmesg | grep "USB"  # Find USB device events
  ```

---

## Log Rotation

### Why Rotate Logs?
- Prevents logs from consuming excessive disk space.
- Archives old logs for historical analysis.

### `logrotate` Utility
- **Compress**: Old logs are gzipped (e.g., `auth.log.2.gz`).
- **Rotate**: Files are renamed (e.g., `auth.log.1` → `auth.log.2`).
- **Delete**: Old logs are purged based on retention rules.

**Example Configuration**:  
```plaintext
/var/log/nginx/*.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
}
```

**Manual Rotation**:  
```bash
sudo logrotate -f /etc/logrotate.conf  # Force rotation
```

---

## Key Takeaways

1. **Log Files**: Essential for security, debugging, and compliance.
2. **Viewing Tools**: Use `tail`, `grep`, and `less` for efficient log analysis.
3. **Rotation**: Configure `logrotate` to manage log file size and retention.
4. **Critical Logs**: Monitor `/var/log/auth.log` (logins) and `/var/log/syslog` (system events).

**Best Practices**:  
- Regularly archive and compress logs.  
- Set appropriate logging levels (`WARN` for production).  
- Use `grep` to filter relevant entries quickly.  

---

## Checkpoint Answers

**Q: Which log files troubleshoot login issues?**  
A:  
- Debian: `/var/log/auth.log`  
- RHEL: `/var/log/secure`  

**Q: Why are logs important?**  
A: They provide a record of system events, helping with security, debugging, and compliance.  

---