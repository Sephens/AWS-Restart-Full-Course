# Comprehensive Lab Guide: Managing and Monitoring Services in Linux

## Introduction
This lab provides hands-on experience with service management and system monitoring in Linux environments, covering both local system tools and AWS CloudWatch. You'll learn to control web services, monitor system resources, and utilize cloud-based monitoring solutions.

## Task 2: Managing the httpd Service

### Step 1: Check httpd Service Status
1. Verify Apache web server status:
   ```bash
   sudo systemctl status httpd.service
   ```

**Expected Output Analysis:**
```
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
```
- **Loaded**: Service definition exists in systemd
- **Active**: Current running state (inactive/dead means not running)
- **Disabled**: Won't start automatically at boot

### Step 2: Start the httpd Service
1. Start Apache service:
   ```bash
   sudo systemctl start httpd.service
   ```

2. Verify service is running:
   ```bash
   sudo systemctl status httpd.service
   ```

**Active Service Output:**
```
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Thu 2023-08-24 14:30:45 UTC; 5s ago
```

**Key Status Indicators:**
- `active (running)`: Service is operational
- Process ID and uptime shown
- Recent log entries displayed

### Step 3: Test Web Server Access
1. Open browser and navigate to:
   ```
   http://<your-instance-public-ip>
   ```

**Expected Result:**
- Apache HTTP Server Test Page appears
- Confirms web server is properly serving content

### Step 4: Stop the httpd Service
1. Halt the web service:
   ```bash
   sudo systemctl stop httpd.service
   ```

**Additional Service Commands:**
- Restart: `sudo systemctl restart httpd.service`
- Enable at boot: `sudo systemctl enable httpd.service`
- Disable at boot: `sudo systemctl disable httpd.service`

## Task 3: Monitoring System Resources

### Step 1: Basic System Monitoring with top
1. Launch process monitor:
   ```bash
   top
   ```

**Key top Interface Sections:**
1. **System Summary**:
   - Uptime, users, load averages (1/5/15 minutes)
2. **Task States**:
   - Total processes and breakdown by state
3. **CPU Usage**:
   - User vs system usage, idle percentage
4. **Memory Usage**:
   - Physical RAM and swap space utilization
5. **Process List**:
   - Sorted by CPU usage by default

**Navigation Commands:**
- Sort by memory: `M`
- Show full commands: `c`
- Filter by user: `u` then username
- Change update delay: `d` then seconds
- Quit: `q`

### Step 2: Simulate High Load Scenario
1. Run stress test script:
   ```bash
   ./stress.sh & top
   ```

**Expected Observations:**
- CPU usage spikes in top display
- stress process appears at top of process list
- Possible increase in system temperature readings

### Step 3: AWS CloudWatch Monitoring

#### Accessing CloudWatch
1. Open AWS Management Console
2. Search for "CloudWatch"
3. Navigate to Dashboards > Automatic dashboards > EC2

**CloudWatch Dashboard Features:**
- **CPU Utilization**: Percentage of EC2 compute units used
- **Disk Metrics**: Read/write operations and bytes
- **Network**: In/out traffic volume
- **Customization**: Add/remove widgets, adjust time ranges

#### Monitoring the Stress Test
1. Observe CPU utilization graph:
   - Initial baseline values
   - Spike when stress script started
   - Gradual return to baseline after script completion

**Advanced CloudWatch Features:**
- **Metrics**: Granular resource tracking
- **Alarms**: Notifications for thresholds
- **Logs**: Centralized log collection
- **Events**: Automated responses to changes

## Comprehensive Monitoring Techniques

### Local Monitoring Tools
| Tool | Purpose | Example Command |
|------|---------|-----------------|
| `htop` | Enhanced process viewer | `sudo htop` |
| `vmstat` | System resource overview | `vmstat 1` |
| `iostat` | Disk I/O statistics | `iostat -xz 1` |
| `netstat` | Network connections | `netstat -tulnp` |
| `dmesg` | Kernel ring buffer | `dmesg | tail` |

### CloudWatch Best Practices
1. **Custom Dashboards**: Create focused views for specific applications
2. **Detailed Monitoring**: Enable 1-minute granularity (default is 5)
3. **Alarms**: Set thresholds for critical metrics
4. **Log Integration**: Stream system logs to CloudWatch
5. **Cost Awareness**: Monitor your monitoring costs

## Troubleshooting Guide

### Common httpd Issues
| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Failed to start | Port 80 in use | `sudo netstat -tulnp \| grep :80` |
| Connection refused | Firewall blocking | `sudo systemctl status firewalld` |
| No test page | Missing index.html | Check `/var/www/html` content |

### Monitoring Pitfalls
1. **False Positives**: Set appropriate alarm thresholds
2. **Metric Gaps**: Ensure all critical services are monitored
3. **Data Overload**: Focus on key performance indicators
4. **Notification Fatigue**: Consolidate alerts meaningfully

## Real-World Applications

1. **Web Service Management**: Deploy and maintain Apache/Nginx
2. **Performance Tuning**: Identify and resolve bottlenecks
3. **Capacity Planning**: Track usage trends over time
4. **Incident Response**: Detect and diagnose issues quickly
5. **Compliance Reporting**: Demonstrate system health

This lab provides essential skills for maintaining and monitoring Linux-based web services in both traditional and cloud environments, forming the foundation for professional system administration and DevOps practices.