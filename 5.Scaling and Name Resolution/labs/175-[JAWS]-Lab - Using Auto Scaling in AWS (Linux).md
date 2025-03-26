# Scaling and Load Balancing Your Architecture - AWS CLI Lab Guide

## Lab Overview
This lab demonstrates how to use AWS CLI to create an Auto Scaling environment with Elastic Load Balancing. You'll create a web server instance, build an AMI from it, and configure auto scaling to maintain optimal performance under variable loads.

### Key Differences from Console Lab
- **AWS CLI Focus**: All initial setup performed via command line
- **Command Host**: Uses a dedicated EC2 instance for CLI operations
- **Scripted Deployment**: Web server setup automated through user data

## Detailed Lab Steps

### Task 1: Creating a New AMI for Auto Scaling

#### Task 1.1: Connecting to Command Host
1. **Access EC2 Console**:
   - Search for "EC2" in AWS Console
   - Select "Instances" from left navigation
   - Select "Command Host" instance
   - Click "Connect" → "EC2 Instance Connect" → "Connect"

2. **Verify Connection**:
   - Terminal session opens to Command Host
   - All subsequent commands run here unless specified

#### Task 1.2: Configuring AWS CLI
1. **Check Region**:
   ```bash
   curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region
   ```
   - Note the Region (e.g., us-west-2)

2. **Configure CLI**:
   ```bash
   aws configure
   ```
   - Press Enter for Access Key and Secret Key
   - Enter Region from above
   - Output format: `json`

3. **Navigate to Scripts**:
   ```bash
   cd /home/ec2-user/
   ```

#### Task 1.3: Creating New EC2 Instance
1. **Review User Data**:
   ```bash
   more UserData.txt
   ```
   - Script installs Apache, PHP, and load test application
   - Cleans security artifacts

2. **Get Lab Parameters**:
   - Click "Details" → "Show" at top of lab page
   - Note: KEYNAME, AMIID, HTTPACCESS, SUBNETID

3. **Launch Instance**:
   ```bash
   aws ec2 run-instances --key-name KEYNAME --instance-type t3.micro \
   --image-id AMIID --user-data file:///home/ec2-user/UserData.txt \
   --security-group-ids HTTPACCESS --subnet-id SUBNETID \
   --associate-public-ip-address \
   --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]' \
   --output text --query 'Instances[*].InstanceId'
   ```
   - Copy the returned InstanceId (NEW-INSTANCE-ID)

4. **Wait for Running**:
   ```bash
   aws ec2 wait instance-running --instance-ids NEW-INSTANCE-ID
   ```

5. **Get Public DNS**:
   ```bash
   aws ec2 describe-instances --instance-id NEW-INSTANCE-ID \
   --query 'Reservations[0].Instances[0].NetworkInterfaces[0].Association.PublicDnsName'
   ```
   - Copy output (PUBLIC-DNS-ADDRESS)

6. **Verify Web Server**:
   - Open browser to: `http://PUBLIC-DNS-ADDRESS/index.php`
   - Wait 5 minutes for setup to complete
   - Don't click "Start Stress" yet

#### Task 1.4: Creating Custom AMI
1. **Create AMI**:
   ```bash
   aws ec2 create-image --name WebServerAMI --instance-id NEW-INSTANCE-ID
   ```
   - Note the returned ImageId
   - AMI creation continues in background

### Task 2: Creating Auto Scaling Environment

#### Task 2.1: Creating Application Load Balancer (Console)
1. **Navigate to EC2** → "Load Balancers"
2. **Create Application Load Balancer**:
   - Name: `WebServerELB`
   - Scheme: Internet-facing
   - VPC: Lab VPC
   - Mappings: Both AZs → Public Subnet 1 & 2
   - Security Group: HTTPAccess (remove default)
3. **Create Target Group**:
   - Name: `webserver-app`
   - Protocol: HTTP:80
   - Health check path: `/index.php`
4. **Complete Setup**:
   - Associate target group
   - Create load balancer
   - Note DNS name

#### Task 2.2: Creating Launch Template (Console)
1. **EC2** → "Launch Templates"
2. **Create Template**:
   - Name: `web-app-launch-template`
   - AMI: WebServerAMI (My AMIs tab)
   - Instance type: t3.micro
   - Security group: HTTPAccess
   - No key pair
3. **Create Template**

#### Task 2.3: Creating Auto Scaling Group (Console)
1. **From Launch Template** → "Create Auto Scaling Group"
2. **Basic Configuration**:
   - Name: `Web App Auto Scaling Group`
3. **Network**:
   - VPC: Lab VPC
   - Subnets: Private Subnet 1 & 2 (10.0.2.0/24, 10.0.4.0/24)
4. **Load Balancing**:
   - Attach to `webserver-app` target group
   - Enable ELB health checks
5. **Group Size**:
   - Desired: 2
   - Minimum: 2
   - Maximum: 4
6. **Scaling Policies**:
   - Target tracking: Average CPU 50%
7. **Tags**:
   - Key: Name, Value: WebApp
8. **Create Group**

### Task 3: Verifying Auto Scaling Configuration
1. **Check Instances**:
   - EC2 → Instances
   - Verify two "WebApp" instances initializing
   - Wait for "2/2 checks passed"

2. **Verify Target Group**:
   - EC2 → Target Groups → webserver-app
   - Confirm both instances show "healthy"

### Task 4: Testing Auto Scaling
1. **Access Load Balancer**:
   - Open browser to load balancer DNS
   - Click "Start Stress"

2. **Monitor Scaling**:
   - EC2 → Auto Scaling Groups → Activity tab
   - Within 5-15 minutes, new instances launch
   - EC2 console shows additional "WebApp" instances

## Key CLI Commands Reference
| Purpose | Command |
|---------|---------|
| Check Region | `curl http://169.254.169.254/latest/dynamic/instance-identity/document \| grep region` |
| Launch Instance | `aws ec2 run-instances [parameters]` |
| Create AMI | `aws ec2 create-image --name NAME --instance-id ID` |
| Describe Instances | `aws ec2 describe-instances --instance-id ID` |
| Wait for Running | `aws ec2 wait instance-running --instance-ids ID` |

## Architecture Notes
1. **Security Design**:
   - Web servers in private subnets
   - Only load balancer in public subnets
   - HTTPAccess security group restricts traffic

2. **High Availability**:
   - Instances spread across two AZs
   - Load balancer distributes traffic evenly

3. **Scaling Behavior**:
   - Maintains 50% CPU utilization
   - Scales between 2-4 instances
   - Health checks ensure only healthy instances receive traffic

## Troubleshooting
- **Instance Not Healthy**:
  - Verify `/index.php` returns 200
  - Check security group rules
  - Review user data script execution

- **Scaling Not Triggering**:
  - Confirm CloudWatch alarms in "Alarm" state
  - Verify sufficient cooldown time passed
  - Check CPU metrics in CloudWatch

- **AMI Creation Delays**:
  - Can take 5-10 minutes
  - Check EC2 → AMIs for status
  - Original instance reboots during process

## Cleanup
The lab automatically terminates resources when completed. For manual cleanup:
1. Delete Auto Scaling Group
2. Delete Launch Template
3. Delete Load Balancer and Target Group
4. Terminate all EC2 instances
5. Deregister AMI and delete snapshot

## Real-World Applications
This pattern is ideal for:
- Web applications with variable traffic
- Microservices architectures
- Batch processing workloads
- CI/CD build environments

Best practice would add:
- HTTPS listeners
- Detailed CloudWatch dashboards
- Instance lifecycle hooks
- Custom scaling metrics