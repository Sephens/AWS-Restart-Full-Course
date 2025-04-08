# Comprehensive Lab Guide: Creating VPCs and Subnets in AWS

## Introduction
This lab provides a complete walkthrough for creating an Amazon Virtual Private Cloud (VPC) with properly sized subnets to meet specific IP addressing requirements. We'll help a startup owner configure their first VPC with appropriate CIDR ranges.

## Task 1: Understanding Customer Requirements

### Customer Needs Analysis
**Paulo's Requirements:**
1. New VPC with ~15,000 private IP addresses
2. Use 192.x.x.x private range
3. Public subnet with at least 50 IP addresses
4. Guidance on AWS networking fundamentals

**Key Concepts:**
- **VPC**: Isolated virtual network in AWS cloud
- **Subnet**: Segment of VPC IP range in an Availability Zone
- **CIDR**: Classless Inter-Domain Routing notation (e.g., 192.168.0.0/16)
- **RFC 1918**: Defines private IP address ranges

### Step 1: Calculating CIDR Ranges

**Private IP Ranges (RFC 1918):**
1. 10.0.0.0/8 (16,777,216 addresses)
2. 172.16.0.0/12 (1,048,576 addresses)
3. 192.168.0.0/16 (65,536 addresses)

**For 15,000 IPs:**
- Next available size is /18 (16,382 usable addresses)
- Example: 192.168.0.0/18

**Public Subnet Sizing:**
- Minimum 50 addresses → /26 (64 addresses)
- Example: 192.168.1.0/26

## Task 2: Creating the VPC

### Step 1: Accessing VPC Console
1. Navigate to AWS Management Console
2. Search for "VPC" or find under Networking services
3. Select "Your VPCs" in left navigation

### Step 2: Launching VPC Wizard
1. Click "Launch VPC Wizard"
2. Select "VPC with a Single Public Subnet"
3. Click "Select"

### Step 3: Configuring VPC Parameters

**VPC Configuration:**
```yaml
IPv4 CIDR block: 192.168.0.0/18
VPC name: First VPC
Public subnet IPv4 CIDR: 192.168.1.0/26
Availability Zone: No Preference
Subnet name: Public subnet
```

**Verification:**
- /18 provides 16,382 usable addresses (meets 15k requirement)
- /26 provides 64 addresses (meets 50+ requirement)
- All addresses within RFC 1918 private range

### Step 4: Creating the VPC
1. Review all parameters
2. Click "Create VPC"
3. Wait for "VPC Successfully Created" confirmation

## Task 3: Verifying the Setup

### Checking VPC Details
1. Navigate to "Your VPCs"
2. Select "First VPC"
3. Verify:
   - CIDR block (192.168.0.0/18)
   - State (available)
   - Tenancy (default)

### Examining Subnets
1. Navigate to "Subnets"
2. Verify Public subnet:
   - CIDR (192.168.1.0/26)
   - Route table association
   - Available IP count (~64)

## Task 4: Creating Customer Documentation

### Step-by-Step Guide for Paulo

**1. Planning Your Network:**
- Use CIDR calculator to determine needed ranges
- Remember AWS reserves 5 IPs per subnet
- Formula: Usable IPs = 2^(32 - netmask) - 5

**2. Creating the VPC:**
```markdown
1. Go to AWS VPC Console
2. Launch VPC Wizard
3. Select "VPC with Single Public Subnet"
4. Configure:
   - VPC CIDR: 192.168.0.0/18
   - Subnet CIDR: 192.168.1.0/26
5. Click "Create"
```

**3. Next Steps:**
- Create security groups
- Launch EC2 instances
- Configure Internet Gateway (auto-created in wizard)
- Set up route tables

## Task 5: Group Activity - Customer Walkthrough

### Role Play Script

**Person 2 (Support Engineer):**
"Paulo, for your VPC with ~15,000 IPs, we recommend:
1. Using 192.168.0.0/18 which gives you 16,382 addresses
2. Creating a /26 public subnet (64 addresses) at 192.168.1.0/26
3. This leaves room for 255 additional /26 subnets if needed"

**Person 1 (Paulo):**
"I see - so the /18 gives me my 15k+ private IPs in the 192.168 range, and the /26 public subnet meets my 50 IP requirement while leaving room to grow. How would I add more subnets later?"

### Advanced Considerations

**Subnet Design Best Practices:**
1. Leave room for expansion between subnets
2. Use consistent numbering scheme (e.g., 192.168.1.x, 192.168.2.x)
3. Document all allocations
4. Consider multi-AZ deployments for production

**Example Modular Design:**
```yaml
VPC: 192.168.0.0/16 (65,536 IPs)
Public Subnets:
  - AZ1: 192.168.1.0/24
  - AZ2: 192.168.2.0/24
Private Subnets:
  - AZ1: 192.168.3.0/20
  - AZ2: 192.168.19.0/20
```

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| CIDR overlaps with existing network | Choose different RFC 1918 range |
| Not enough IPs in subnet | Increase CIDR size (e.g., /24 → /23) |
| Can't connect to internet | Verify route table has IGW route |
| "Invalid CIDR" error | Check for typing errors in format |

## Real-World Applications

1. **Multi-Tier Applications**: Web (public), App (private), DB (isolated)
2. **Hybrid Cloud**: Connect to on-prem networks via VPN/Direct Connect
3. **Microservices**: Isolate services in different subnets
4. **Security Zones**: Separate dev/test/prod environments

This comprehensive solution addresses all of Paulo's requirements while providing expandability for future growth and clear documentation for his reference. The VPC design follows AWS best practices for subnet sizing and IP allocation.