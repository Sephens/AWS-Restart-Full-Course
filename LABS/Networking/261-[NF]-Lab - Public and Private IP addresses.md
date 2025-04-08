# Comprehensive Lab Guide: Public vs. Private IP Addresses in AWS

## Introduction
This lab explores the critical differences between public and private IP addresses in AWS environments, using a real-world troubleshooting scenario to reinforce networking concepts.

## Task 1: Investigating the Customer Environment

### Step 1: Understanding the Scenario
**Customer Situation:**
- Two EC2 instances (A and B) in same VPC (10.0.0.0/16)
- Instance A cannot reach internet
- Instance B can reach internet
- Identical VPC configurations
- Customer question about using public IP ranges for VPC

**Troubleshooting Approach:**
Using OSI model layers to systematically diagnose:
1. **Physical/Link Layer**: AZ placement, network interfaces
2. **Network Layer**: IP addressing, routing tables
3. **Transport Layer**: Security groups, NACLs
4. **Session/Application**: Instance configurations

### Step 2: Accessing AWS Console
1. Navigate to EC2:
   - Method 1: Search "EC2" in AWS console search bar
   - Method 2: Services → Compute → EC2

**Verification:**
- Confirm you see two instances (A and B)
- Ensure you're in the correct region (shown in top right)

### Step 3: Documenting Instance Details
1. For **Instance A**:
   - Select checkbox
   - Navigate to "Networking" tab
   - Record:
     - Instance name
     - Private IPv4 address
     - Public IPv4 address
     - Subnet ID
     - Security groups

2. Repeat for **Instance B**

**Expected Findings Table:**

| Instance | Private IP | Public IP | Subnet | Security Groups |
|----------|------------|-----------|--------|-----------------|
| A        | 10.0.1.5   | 52.1.2.3  | Sub1   | sg-12345        |
| B        | 10.0.1.6   | 52.1.2.4  | Sub1   | sg-12345        |

**Key Observations:**
- Both instances show public IPs (suggests internet access possible)
- Same subnet and security groups (rules out these as causes)

## Task 2: Analyzing IP Address Differences

### Public vs Private IP Fundamentals

**Private IP Ranges (RFC 1918):**
- 10.0.0.0/8 (10.0.0.0 - 10.255.255.255)
- 172.16.0.0/12 (172.16.0.0 - 172.31.255.255)
- 192.168.0.0/16 (192.168.0.0 - 192.168.255.255)

**Public IP Ranges:**
- All other IPv4 addresses not in private ranges
- Globally routable on the internet
- Must be unique worldwide

### AWS-Specific Behavior

**EC2 Networking Facts:**
1. Private IP:
   - Assigned from VPC CIDR range
   - Persistent until instance termination
   - Used for internal communication

2. Public IP:
   - Assigned from AWS pool
   - Non-persistent (changes after stop/start)
   - Requires Internet Gateway (IGW) in route table

**Why Instance A Fails:**
After deeper inspection, we'd find:
- Instance A's **route table** lacks default route to IGW
- Or its **elastic network interface** has no public IP
- Or **NACL** is blocking outbound traffic

## Task 3: Customer Response (Group Activity)

### Recommended Solution

**For Jess's Immediate Issue:**
1. Verify Instance A's:
   - Route table associations
   - Network interface configuration
   - NACL outbound rules

2. Suggested commands to run on Instance A:
   ```bash
   # Check network routes
   ip route show

   # Test internet connectivity
   ping 8.8.8.8
   curl -v http://example.com
   ```

**For the Public IP Range Question:**
*Never use public IP ranges for VPC because:*
1. **Routing Conflicts**: May overlap with real internet hosts
2. **Connectivity Issues**: Impossible to reach those actual public hosts
3. **AWS Restrictions**: Many public ranges are blocked in VPCs
4. **Security Risks**: Potential exposure to unintended internet traffic

### Group Activity Script

**Person 1 (Support Engineer):**
"Jess, we've diagnosed that Instance A lacks proper routing to the internet despite having a public IP. The root cause appears to be [specific finding]. For your VPC design question, we strongly recommend against using public IP ranges because..."

**Person 2 (Jess):** 
"Thanks for explaining. So if I understand correctly, even though both instances show public IPs, Instance A can't reach the internet because [repeat explanation]? And for future VPCs, I should always stick to RFC 1918 ranges because..."

## Additional Troubleshooting Steps

### Advanced Verification

1. Check route tables:
   ```bash
   aws ec2 describe-route-tables --filters "Name=vpc-id,Values=vpc-12345"
   ```

2. Examine network interfaces:
   ```bash
   aws ec2 describe-network-interfaces --filters "Name=attachment.instance-id,Values=i-12345"
   ```

3. Review NACLs:
   ```bash
   aws ec2 describe-network-acls --filters "Name=vpc-id,Values=vpc-12345"
   ```

## Real-World Best Practices

1. **VPC Design**:
   - Use /16 to /20 CIDR blocks from RFC 1918
   - Leave room for expansion
   - Avoid overlapping ranges with on-prem networks

2. **Troubleshooting Flow**:
   ```mermaid
   graph TD
     A[Connectivity Issue] --> B[Check Instance Status]
     B --> C[Verify Security Groups]
     C --> D[Check NACLs]
     D --> E[Review Route Tables]
     E --> F[Inspect IGW/NAT]
   ```

3. **Documentation**:
   - Maintain network topology diagrams
   - Document all CIDR allocations
   - Track route table purposes

This comprehensive approach ensures thorough understanding of AWS networking while providing actionable solutions to the customer's specific issues.