# Managing Services in Linux - Comprehensive Guide

## Table of Contents
- [Managing Services in Linux - Comprehensive Guide](#managing-services-in-linux---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction to Service Management](#introduction-to-service-management)
  - [Systemctl Command](#systemctl-command)
    - [Basic Usage](#basic-usage)
    - [Service Lifecycle](#service-lifecycle)
    - [Demonstration](#demonstration)
  - [Monitoring Commands](#monitoring-commands)
    - [System Performance](#system-performance)
    - [Resource Monitoring](#resource-monitoring)
  - [AWS Integration](#aws-integration)
  - [Checkpoint Questions and Answers](#checkpoint-questions-and-answers)
  - [Key Takeaways](#key-takeaways)

## Introduction to Service Management

Services in Linux are background processes (daemons) that provide key functionality like networking, security, and remote administration. Unlike regular processes, services:

- Start automatically at boot
- Run in the background
- Can be managed collectively
- Often have configuration files

**Key concepts:**
- Modern Linux uses `systemd` as the init system
- Services are managed primarily with `systemctl`
- Services can depend on other services

## Systemctl Command

### Basic Usage

The `systemctl` command is the primary tool for managing services in systemd-based Linux distributions.

**Basic syntax:**
```bash
systemctl <subcommand> <service_name>
```

**Common subcommands:**
```bash
start      # Start a service
stop       # Stop a service
restart    # Restart a service
reload     # Reload configuration without interruption
enable     # Enable at boot
disable    # Disable at boot
status     # Check service status
is-active  # Check if service is running
is-enabled # Check if service starts at boot
```

### Service Lifecycle

**Example managing Apache (httpd):**
```bash
# Check status
sudo systemctl status httpd

# Start service
sudo systemctl start httpd

# Enable at boot
sudo systemctl enable httpd

# Verify
sudo systemctl is-enabled httpd  # Output: enabled
sudo systemctl is-active httpd   # Output: active
```

**Troubleshooting tips:**
1. After config changes, always restart the service:
   ```bash
   sudo systemctl restart httpd
   ```
2. For configuration changes that don't require full restart:
   ```bash
   sudo systemctl reload httpd
   ```
3. Check logs for service issues:
   ```bash
   journalctl -u httpd -xe
   ```

### Demonstration

1. **Show running services:**
   ```bash
   systemctl
   ```

2. **List all services (active/inactive):**
   ```bash
   systemctl list-units --type=service
   ```

3. **List active services only:**
   ```bash
   systemctl list-units --type=service --state=active
   ```

4. **View service dependencies:**
   ```bash
   systemctl list-dependencies httpd
   ```

## Monitoring Commands

### System Performance

| Command | Description | Example |
|---------|-------------|---------|
| `lscpu` | CPU information | `lscpu \| grep "Model name"` |
| `lshw` | Hardware details | `sudo lshw -short` |
| `vmstat` | Virtual memory stats | `vmstat 1` (refresh every 1s) |
| `free` | Memory usage | `free -h` (human-readable) |
| `uptime` | System load | `uptime` shows 1/5/15 min loads |

### Resource Monitoring

**Disk space:**
```bash
df -h  # Human-readable disk free space
du -sh /var/log  # Size of /var/log directory
```

**Process monitoring:**
```bash
top       # Interactive process viewer
htop      # Enhanced version of top (install with yum install htop)
iotop     # Monitor disk I/O
iftop     # Monitor network traffic
```

**Example workflow for troubleshooting:**
1. Check system load with `uptime`
2. Identify resource hogs with `top`
3. Verify disk space with `df -h`
4. Check service status with `systemctl status <service>`

## AWS Integration

**Amazon CloudWatch** provides enhanced monitoring for EC2 instances:

- Monitors CPU, disk, network, memory
- Sets alarms for thresholds (e.g., CPU > 90%)
- Integrates with SNS for notifications

**Key metrics to monitor:**
- `CPUUtilization`
- `DiskReadOps`/`DiskWriteOps`
- `NetworkIn`/`NetworkOut`
- `MemoryUtilization`

**Example alarm setup:**
1. Create CloudWatch alarm when CPU > 80% for 5 minutes
2. Configure SNS topic to email admin
3. Set up Auto Scaling based on alarms

## Checkpoint Questions and Answers

1. **How might you use the top command when troubleshooting?**
   - Identify processes consuming high CPU (`shift+p`)
   - Sort by memory usage (`shift+m`)
   - Check load averages at top of display
   - Example: If system is slow, `top` might reveal a runaway process using 99% CPU

2. **Why restart a service instead of the entire computer?**
   - Minimizes downtime (only affects one service)
   - Other services continue running uninterrupted
   - Faster resolution than full reboot
   - Example: Restarting `sshd` when connection issues occur, rather than rebooting the entire web server

## Key Takeaways

1. **Service Management**
   - Use `systemctl` for complete service control
   - Remember to `enable` critical services for boot
   - `restart` vs `reload` - know when to use each

2. **Monitoring Essentials**
   - `top/htop` for real-time process monitoring
   - `df/du` for disk space management
   - `lscpu/free` for hardware resource checks

3. **Best Practices**
   - Monitor services before they cause issues
   - Set up alerts for critical services
   - Document service dependencies
   - Test restart procedures during maintenance windows

**Example Maintenance Procedure:**
1. Check service status: `systemctl status nginx`
2. Backup config: `cp /etc/nginx/nginx.conf /backup/`
3. Test config: `nginx -t`
4. Apply changes: `systemctl reload nginx`
5. Verify: `curl -I localhost`