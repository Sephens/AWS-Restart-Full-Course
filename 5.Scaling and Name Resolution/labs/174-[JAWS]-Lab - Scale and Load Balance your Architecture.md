# Scaling and Load Balancing Your Architecture - Lab Guide

## Lab Overview
This lab demonstrates how to use Elastic Load Balancing (ELB) and Amazon EC2 Auto Scaling to create a scalable and highly available infrastructure. You'll learn how to distribute traffic across multiple instances and automatically adjust capacity based on demand.

### Key Concepts
- **Elastic Load Balancing (ELB)**: Automatically distributes incoming traffic across multiple EC2 instances
- **Auto Scaling**: Maintains application availability by automatically adjusting EC2 capacity
- **Launch Templates**: Configuration templates for EC2 instances used by Auto Scaling
- **Target Groups**: Logical groupings of instances that receive traffic from a load balancer
- **CloudWatch Alarms**: Monitor metrics and trigger scaling actions

## Lab Architecture
### Starting Architecture
![Starting Architecture](starting-arch.png)
- Single web server (Web Server 1) in a public subnet

### Final Architecture
![Final Architecture](final-arch.png)
- Application Load Balancer in public subnets
- Auto Scaling group with EC2 instances in private subnets across two Availability Zones
- CloudWatch monitoring for scaling policies

## Detailed Lab Steps

### Task 1: Creating an AMI for Auto Scaling
**Purpose**: Create a standardized image that Auto Scaling will use to launch new instances.

1. **Navigate to EC2 Console**:
   - Search for "EC2" in AWS Console
   - Select "Instances" from left navigation

2. **Create AMI from Web Server 1**:
   - Select "Web Server 1" instance
   - Actions → Image and templates → Create image
   - Configure:
     - Image name: `Web Server AMI`
     - Description: `Lab AMI for Web Server`
   - Click "Create image"

**Notes**:
- AMI creation takes several minutes (you can proceed with next tasks while it completes)
- The AMI includes:
  - The root volume snapshot
  - All instance configuration
  - Installed applications (like the Load Test app in this case)

**Example Use Case**: 
Creating consistent deployment images for your web application ensures every new instance has identical software configurations.

### Task 2: Creating a Load Balancer
**Purpose**: Distribute traffic across multiple instances in different Availability Zones.

1. **Navigate to Load Balancers**:
   - EC2 Console → Load Balancing → Load Balancers
   - Click "Create Load Balancer"
   - Select "Application Load Balancer"

2. **Configure Basic Settings**:
   - Name: `LabELB`
   - Scheme: Internet-facing (default)
   - IP address type: IPv4 (default)

3. **Network Mapping**:
   - VPC: `Lab VPC`
   - Mappings: Select both AZs
     - AZ1: Public Subnet 1
     - AZ2: Public Subnet 2

4. **Security Groups**:
   - Remove default security group
   - Add `Web Security Group` (allows HTTP traffic)

5. **Listeners and Routing**:
   - Default listener: HTTP on port 80
   - Click "Create target group" link (opens new tab)

6. **Create Target Group**:
   - Target type: Instances
   - Name: `lab-target-group`
   - Protocol: HTTP
   - Port: 80
   - Health checks: Default settings
   - Click "Create target group"

7. **Complete Load Balancer Setup**:
   - Return to Load Balancer tab
   - Refresh target group list
   - Select `lab-target-group` for default action
   - Click "Create load balancer"

8. **Record DNS Name**:
   - View load balancer
   - Copy DNS name (e.g., `LabELB-123456789.us-west-2.elb.amazonaws.com`)
   - Save for later testing

**Key Points**:
- Application Load Balancer (ALB) operates at Layer 7 (HTTP/HTTPS)
- Cross-AZ load balancing improves fault tolerance
- Target groups decouple load balancer from instance management

**Troubleshooting**:
- If target group creation fails, verify VPC and subnet selections
- Ensure security group allows HTTP (port 80) traffic

### Task 3: Creating a Launch Template
**Purpose**: Define the configuration for instances launched by Auto Scaling.

1. **Navigate to Launch Templates**:
   - EC2 Console → Instances → Launch Templates
   - Click "Create launch template"

2. **Basic Configuration**:
   - Name: `lab-app-launch-template`
   - Description: `A web server for the load test app`
   - Auto Scaling guidance: Enabled

3. **AMI Selection**:
   - My AMIs tab
   - Select "Web Server AMI" created earlier

4. **Instance Type**:
   - Select `t3.micro` (free tier eligible)
   - Note: If unavailable, use `t2.micro`

5. **Key Pair**:
   - Select "Don't include in launch template" (no SSH access needed)

6. **Security Groups**:
   - Select `Web Security Group`

7. **Create Template**:
   - Click "Create launch template"
   - View created template

**Important Considerations**:
- Launch templates replace launch configurations (newer/better approach)
- Can specify multiple instance types for flexibility
- Can include user data for instance initialization

### Task 4: Creating an Auto Scaling Group
**Purpose**: Automatically maintain desired number of instances and scale based on demand.

1. **From Launch Template**:
   - Select `lab-app-launch-template`
   - Actions → Create Auto Scaling group

2. **Basic Configuration**:
   - Name: `Lab Auto Scaling Group`

3. **Network Settings**:
   - VPC: `Lab VPC`
   - Subnets: Private Subnet 1 and Private Subnet 2
     - Provides cross-AZ redundancy

4. **Load Balancing**:
   - Attach to existing load balancer
   - Target group: `lab-target-group`
   - Health check type: ELB (in addition to EC2)

5. **Group Size**:
   - Desired capacity: 2
   - Minimum: 2
   - Maximum: 4

6. **Scaling Policies**:
   - Target tracking policy
   - Metric: Average CPU utilization
   - Target value: 50%
   - Instances will scale to maintain ~50% CPU

7. **Tags**:
   - Key: `Name`
   - Value: `Lab Instance`
   - Tags propagate to all launched instances

8. **Create Group**:
   - Review settings
   - Click "Create Auto Scaling group"

**Scaling Behavior**:
- If average CPU > 50% for sustained period → add instances
- If average CPU < 50% for sustained period → remove instances
- Always maintains between 2-4 instances

**Architecture Benefits**:
- Instances in private subnets are more secure
- Automatic replacement of failed instances
- Cost optimization through scaling

### Task 5: Verifying Load Balancing
**Purpose**: Confirm load balancer properly distributes traffic to instances.

1. **Check Instance Status**:
   - EC2 Console → Instances
   - Verify two new "Lab Instance" instances running
   - May take 2-3 minutes to initialize

2. **Check Target Group Health**:
   - EC2 Console → Target Groups
   - Select `lab-target-group`
   - Verify both instances show "healthy" status

3. **Test Load Balancer**:
   - Open browser tab
   - Paste load balancer DNS name
   - Verify "Load Test" application appears
   - Refresh page multiple times to see requests distributed

**Verification Tips**:
- Unhealthy instances won't receive traffic
- Health checks verify HTTP 200 response
- Cross-AZ load balancing ensures zone failures don't impact availability

### Task 6: Testing Auto Scaling
**Purpose**: Validate scaling policies respond to increased load.

1. **Monitor CloudWatch Alarms**:
   - CloudWatch Console → All Alarms
   - Observe two Auto Scaling-created alarms
   - Initially both in "OK" state

2. **Generate Load**:
   - In Load Test application tab
   - Click "Load Test" button
   - This simulates CPU-intensive workload

3. **Observe Scaling**:
   - Refresh CloudWatch alarms periodically
   - Within 5 minutes:
     - AlarmHigh should trigger (CPU > 50%)
     - Auto Scaling will launch new instances
   - EC2 Console → Instances shows new instances

**Scaling Timeline**:
1. CPU load increases
2. CloudWatch metrics reflect increased utilization
3. Alarm transitions to "In alarm" state
4. Auto Scaling adds capacity (may take several minutes)
5. CPU utilization decreases as load spreads

**Important Note**:
- Scaling out is faster than scaling in (protects against flapping)
- Cooldown periods prevent rapid scaling actions

### Task 7: Terminating Web Server 1
**Purpose**: Clean up original instance no longer needed.

1. **Select Instance**:
   - EC2 Console → Instances
   - Select "Web Server 1"

2. **Terminate**:
   - Instance state → Terminate instance
   - Confirm termination

**Cleanup Rationale**:
- All traffic now goes through load balancer
- Auto Scaling manages instance lifecycle
- Reduces unnecessary costs

## Optional Challenge: Creating AMI via AWS CLI
For advanced users with remaining time:

1. **Connect to Instance**:
   - Use EC2 Instance Connect
   - Or SSH with proper credentials

2. **Configure AWS CLI**:
   ```bash
   aws configure
   ```
   - Enter access keys from lab credentials

3. **Create AMI**:
   ```bash
   aws ec2 create-image \
     --instance-id i-1234567890abcdef0 \
     --name "CLI-Created-AMI" \
     --description "AMI created via AWS CLI"
   ```

4. **Verify**:
   ```bash
   aws ec2 describe-images --owners self
   ```

## Conclusion
### Key Takeaways
1. **AMI Creation**: Standardized images ensure consistent deployments
2. **Load Balancing**: Distributes traffic and improves availability
3. **Auto Scaling**: Automatically adjusts capacity based on demand
4. **Monitoring**: CloudWatch enables data-driven scaling decisions

### Real-World Applications
- E-commerce sites handling traffic spikes
- SaaS applications with variable workloads
- Microservices architectures requiring elasticity

### Best Practices
- Always use multiple Availability Zones
- Set appropriate health check thresholds
- Monitor scaling activities
- Test failure scenarios

## Q&A
**Q: Why use private subnets for Auto Scaling instances?**
A: Private subnets provide additional security by preventing direct internet access. All traffic flows through the load balancer, which can implement security controls.

**Q: How quickly does Auto Scaling respond to load changes?**
A: Typically within 5-15 minutes, depending on metric collection intervals and cooldown periods.

**Q: Can I use different instance types in an Auto Scaling group?**
A: Yes, launch templates support multiple instance types and sizes for flexibility.

**Q: What happens if an instance fails health checks?**
A: Auto Scaling terminates the unhealthy instance and launches a replacement.

**Q: How do I choose the right scaling metrics?**
A: CPU utilization is common for compute-bound workloads. For web apps, consider request count or latency metrics.