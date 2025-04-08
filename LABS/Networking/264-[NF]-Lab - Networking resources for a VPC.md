# Comprehensive Lab Guide: Creating Networking Resources in Amazon VPC

## Introduction
This lab provides a complete walkthrough for building a fully functional Amazon Virtual Private Cloud (VPC) with all necessary networking components to enable internet connectivity. We'll help a startup owner configure their VPC to allow EC2 instances to communicate with the internet.

## Task 1: Building the VPC Infrastructure

### Step 1: Creating the VPC
1. Navigate to VPC service in AWS Console
2. Select "Your VPCs" → "Create VPC"
3. Configure:
   - Name tag: Test VPC
   - IPv4 CIDR: 192.168.0.0/18
   - Leave all other defaults

**Key Points:**
- CIDR /18 provides 16,382 usable IP addresses
- 192.168.0.0/16 is RFC 1918 private range
- VPC acts as virtual data center in AWS cloud

### Step 2: Creating Subnets
1. Navigate to "Subnets" → "Create subnet"
2. Configure public subnet:
   - VPC: Test VPC
   - Subnet name: Public subnet
   - Availability Zone: No preference
   - IPv4 CIDR: 192.168.1.0/26

**Subnet Sizing:**
- /26 provides 64 IP addresses (meets 50+ requirement)
- Public subnet will host internet-facing resources

### Step 3: Creating Route Table
1. Navigate to "Route Tables" → "Create route table"
2. Configure:
   - Name: Public route table
   - VPC: Test VPC

**Route Table Purpose:**
- Controls traffic routing within VPC
- Will be associated with public subnet
- Will contain route to internet gateway

### Step 4: Creating Internet Gateway
1. Navigate to "Internet Gateways" → "Create internet gateway"
2. Configure:
   - Name: IGW test VPC
3. After creation, attach to Test VPC

**Internet Gateway Function:**
- Provides VPC with internet connectivity
- Performs NAT for instances with public IPs
- Required for outbound internet access

### Step 5: Configuring Route Table
1. Edit routes in Public route table:
   - Add route: 0.0.0.0/0 → Target: IGW test VPC
2. Associate route table with Public subnet

**Route Explanation:**
- 0.0.0.0/0 = all internet traffic
- IGW as target enables internet access
- Association applies to public subnet

### Step 6: Creating Network ACL
1. Navigate to "Network ACLs" → "Create network ACL"
2. Configure:
   - Name: Public Subnet NACL
   - VPC: Test VPC
3. Add rules:
   - Inbound: Rule 100, All traffic, 0.0.0.0/0, Allow
   - Outbound: Rule 100, All traffic, 0.0.0.0/0, Allow

**NACL Characteristics:**
- Stateless firewall at subnet level
- Processes rules in order (lowest number first)
- Explicit allow/deny rules required

### Step 7: Creating Security Group
1. Navigate to "Security Groups" → "Create security group"
2. Configure:
   - Name: public security group
   - Description: allows public access
   - VPC: Test VPC
3. Add rules:
   - Inbound: SSH (22), HTTP (80), HTTPS (443) from 0.0.0.0/0
   - Outbound: All traffic to 0.0.0.0/0

**Security Group Notes:**
- Stateful firewall at instance level
- Default deny all inbound, allow all outbound
- Supports allow rules only

## Task 2: Launching and Connecting to EC2 Instance

### Step 1: Launching Instance
1. Navigate to EC2 → "Launch instances"
2. Configure:
   - AMI: Amazon Linux 2023
   - Instance type: t3.micro
   - Key pair: vockey
   - Network: Test VPC
   - Subnet: Public subnet
   - Auto-assign public IP: Enable
   - Security group: public security group

**Instance Configuration:**
- Placed in public subnet for internet access
- Public IP assigned automatically
- Security group allows SSH access

### Step 2: Connecting to Instance
**Windows Users:**
1. Download PPK key file
2. Use PuTTY to SSH to instance public IP
3. Login as "ec2-user"

**Mac/Linux Users:**
1. Download PEM key file
2. Set permissions: `chmod 400 labsuser.pem`
3. Connect: `ssh -i labsuser.pem ec2-user@<public-ip>`

**Connection Notes:**
- Key pair provides secure authentication
- ec2-user is default admin account
- Verify public IP in EC2 console

## Task 3: Testing Internet Connectivity

### Step 1: Ping Test
1. In SSH session, run:
   ```bash
   ping google.com
   ```
2. Observe successful replies
3. Press Ctrl+C to stop

**Expected Output:**
```
PING google.com (142.250.190.46) 56(84) bytes of data.
64 bytes from lga34s31-in-f14.1e100.net (142.250.190.46): icmp_seq=1 ttl=117 time=1.24 ms
```

**Troubleshooting:**
- If ping fails:
  - Verify route table has IGW route
  - Check security group outbound rules
  - Confirm NACL allows all traffic
  - Ensure instance has public IP

## Architecture Validation

### Complete Resource Map
| Resource | Configuration | Purpose |
|----------|--------------|---------|
| VPC | 192.168.0.0/18 | Logical isolation |
| Public Subnet | 192.168.1.0/26 | Internet-facing resources |
| Internet Gateway | Attached to VPC | Internet access |
| Route Table | 0.0.0.0/0 → IGW | Internet routing |
| Security Group | Allow SSH/HTTP/HTTPS | Instance firewall |
| NACL | Allow all traffic | Subnet firewall |

## Best Practices

1. **Naming Conventions**:
   - Use consistent, descriptive names
   - Include environment (prod, test, dev)
   - Example: "prod-web-sg" for production web security group

2. **Security Recommendations**:
   - Restrict SSH access to known IPs
   - Use separate security groups per tier
   - Implement least privilege access

3. **Scalability Considerations**:
   - Leave room for subnet expansion
   - Use multiple AZs for production
   - Consider NAT gateways for private subnets

## Common Questions

**Q: Why can't I ping my instance?**
A: Check:
1. Security group inbound rules (ICMP)
2. NACL inbound/outbound rules
3. Instance operating system firewall
4. Route table associations

**Q: How do I make my IP persistent?**
A: Use Elastic IP address instead of auto-assigned public IP

**Q: Why use both NACL and security groups?**
A: Defense in depth - NACL protects at subnet level, security groups at instance level

This comprehensive solution provides a fully functional VPC with internet connectivity, following AWS best practices for network architecture and security. The step-by-step approach ensures all components are properly configured and validated through connectivity testing.