# Amazon EC2 Lab: Launching, Resizing, and Managing Instances

## Introduction
Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. This lab walks through the complete process of launching, monitoring, resizing, and terminating an EC2 instance with a web server.

## Task 1: Launching Your EC2 Instance

### Step 1: Naming Your EC2 Instance
- **Action**: In the Name and tags pane, enter "Web Server" in the Name text box
- **Explanation**: 
  - This creates a Name tag for your instance
  - Tags help identify and organize AWS resources
  - Example: You could add additional tags like "Environment: Production" or "Owner: DevOps"

### Step 2: Choosing an Amazon Machine Image (AMI)
- **Action**: Keep the default Amazon Linux 2 AMI selected
- **Explanation**:
  - AMIs are templates containing the software configuration (OS, application server, applications)
  - Amazon Linux 2 is a supported and maintained Linux image optimized for AWS
  - Alternative options include Ubuntu, Windows Server, or custom AMIs

### Step 3: Choosing an Instance Type
- **Action**: Select t3.micro from the dropdown
- **Explanation**:
  - t3.micro is part of the burstable performance instance family
  - Specs: 2 vCPUs, 1 GiB memory
  - Good for low-traffic websites or development environments
  - Cost-effective option eligible for AWS Free Tier

### Step 4: Configuring a Key Pair
- **Action**: Select "Proceed without a key pair"
- **Explanation**:
  - Normally you would create/download a key pair for SSH access
  - Since we won't SSH into this instance, we can skip this
  - In production, always use key pairs for secure access

### Step 5: Configuring Network Settings
- **Action**: 
  1. Select "Lab VPC" for the VPC
  2. Configure security group:
     - Name: "Web Server security group"
     - Description: "Security group for my web server"
  3. Remove the default SSH rule
- **Explanation**:
  - VPCs provide isolated network environments
  - Security groups act as virtual firewalls
  - We remove SSH access since we won't need it, improving security
  - Initially no inbound access is allowed (will add HTTP later)

### Step 6: Adding Storage
- **Action**: Keep default 8 GiB gp2 EBS volume
- **Explanation**:
  - EBS volumes are network-attached storage
  - 8 GiB is sufficient for our web server
  - gp2 is general purpose SSD (good balance of price/performance)

### Step 7: Configuring Advanced Details
- **Action**:
  1. Enable termination protection
  2. Paste User Data script:
     ```bash
     #!/bin/bash
     yum -y install httpd
     systemctl enable httpd
     systemctl start httpd
     echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
     ```
- **Explanation**:
  - Termination protection prevents accidental instance termination
  - User Data scripts run on first launch
  - This script:
    - Installs Apache web server (httpd)
    - Configures it to start on boot
    - Creates a simple HTML page

### Step 8: Launching the EC2 Instance
- **Action**: Click "Launch instance" then "View all instances"
- **What Happens**:
  - Instance starts in "pending" state
  - Progresses to "running" once launched
  - Takes 1-2 minutes to fully initialize
  - User Data script executes during initialization

## Task 2: Monitor Your Instance

### Checking Instance Status
- **Action**: View the Status checks tab
- **Explanation**:
  - System reachability: Checks if instance is running on host
  - Instance reachability: Checks if OS is responding
  - Both must pass for instance to be fully operational

### Viewing CloudWatch Metrics
- **Action**: Check the Monitoring tab
- **Explanation**:
  - Shows CPU utilization, network traffic, disk metrics
  - Basic monitoring (5-minute intervals) is free
  - Detailed monitoring (1-minute intervals) costs extra

### Getting Instance Screenshot
- **Action**: Use "Get Instance Screenshot" option
- **Explanation**:
  - Helpful for troubleshooting when you can't access instance
  - Shows console output as if a screen were attached
  - Useful for diagnosing boot issues

## Task 3: Update Security Group and Access Web Server

### Testing Initial Web Access
- **Action**: Try accessing public IP in browser
- **Result**: Connection fails
- **Why?**: Security group doesn't allow HTTP (port 80) traffic

### Updating Security Group
- **Action**:
  1. Navigate to Security Groups
  2. Select "Web Server security group"
  3. Add inbound rule:
     - Type: HTTP
     - Source: Anywhere-IPv4 (0.0.0.0/0)
- **Explanation**:
  - HTTP rule allows web traffic on port 80
  - "Anywhere" means any IP can access (not recommended for production)
  - Better practice would be to restrict to specific IPs

### Verifying Web Access
- **Action**: Refresh browser with instance IP
- **Expected Result**: "Hello From Your Web Server!" message appears

## Task 4: Resize Your Instance

### Stopping the Instance
- **Action**: Stop the instance before resizing
- **Important Notes**:
  - Must stop instance before changing type
  - No charges for stopped instances (except EBS storage)
  - Instance retains its private IP when stopped

### Changing Instance Type
- **Action**: Change from t3.micro to t3.small
- **Impact**:
  - t3.small has 2 vCPUs and 2 GiB memory (double the memory)
  - Cost increases from ~$0.0104/hr to ~$0.0208/hr (us-east-1)

### Resizing EBS Volume
- **Action**: Increase root volume from 8 GiB to 10 GiB
- **Notes**:
  - Can increase size while instance is stopped
  - Can't decrease size (must create new volume)
  - After starting instance, need to extend filesystem to use new space

### Starting the Resized Instance
- **Action**: Start the instance
- **Post-Start Checks**:
  - Verify instance comes up properly
  - Check web server is still accessible
  - Monitor performance with additional resources

## Task 5: Test Termination Protection

### Attempting to Terminate
- **Action**: Try to terminate instance with protection enabled
- **Result**: Error message appears
- **Why?**: Termination protection prevents accidental deletion

### Disabling Protection
- **Action**: Disable termination protection
- **Considerations**:
  - Only disable when you're sure you want to terminate
  - Can re-enable protection at any time

### Terminating the Instance
- **Action**: Terminate the instance
- **Important Notes**:
  - Default behavior is to delete root EBS volume
  - Data on instance store volumes is lost
  - Termination is permanent - cannot be undone
  - Consider taking a snapshot first if you might need the data later

## Key Takeaways

1. **EC2 Basics**: Learned how to launch, configure, and terminate instances
2. **Security**: Implemented security groups and termination protection
3. **Scalability**: Changed instance type and EBS volume size
4. **Automation**: Used User Data for automated configuration
5. **Monitoring**: Explored various monitoring options

## Common Questions

**Q: Why can't I SSH into my instance?**
A: We intentionally removed SSH access by deleting the inbound SSH rule in the security group for security purposes. To add SSH access, you would need to add an inbound rule for port 22 from your IP address.

**Q: How do I access my instance if I don't have SSH?**
A: For management without SSH:
1. Use EC2 Instance Connect (browser-based SSH)
2. Use Systems Manager Session Manager
3. View system logs in the EC2 console

**Q: Is the web server data persistent?**
A: The simple HTML page we created is stored on the root EBS volume. If we terminate the instance and choose to delete the volume, this data would be lost. For persistent storage, you could:
1. Store content on a separate EBS volume and not delete it on termination
2. Use S3 for static content
3. Backup important data regularly

**Q: How would I make this production-ready?**
1. Use HTTPS instead of HTTP
2. Restrict security group to specific IPs
3. Implement Auto Scaling for high availability
4. Use a proper CI/CD pipeline for deployments
5. Monitor with CloudWatch alarms
6. Route traffic through a load balancer