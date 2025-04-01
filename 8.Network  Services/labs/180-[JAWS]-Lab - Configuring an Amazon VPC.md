# AWS VPC Configuration Lab - Comprehensive Guide

## Lab Overview
This lab guides you through creating a secure AWS Virtual Private Cloud (VPC) with public and private subnets, including all necessary networking components. You'll configure routing, launch instances, and test connectivity.

## Lab Architecture
The final architecture will include:
- 1 VPC (10.0.0.0/16)
- 1 Public Subnet (10.0.0.0/24) with:
  - Bastion server (EC2 instance)
  - NAT Gateway
- 1 Private Subnet (10.0.2.0/23) with:
  - Private EC2 instance (optional)
- Internet Gateway for public access
- Properly configured route tables

## Detailed Step-by-Step Instructions

### Task 1: Creating a VPC

1. **Navigate to VPC Console**
   - Search for "VPC" in AWS Console
   - Select "Your VPCs" in left navigation

2. **Create New VPC**
   - Click "Create VPC"
   - Configuration:
     - Resources: VPC only
     - Name tag: Lab VPC
     - IPv4 CIDR: 10.0.0.0/16
     - IPv6: No IPv6 CIDR block
     - Tenancy: Default
   - Click "Create VPC"

3. **Enable DNS Hostnames**
   - Select your new VPC
   - Actions → Edit VPC settings
   - Enable DNS hostnames
   - Save

**Why this matters**: DNS hostnames allow instances to get public DNS names, making them easier to access.

### Task 2: Creating Subnets

#### Task 2.1: Public Subnet
1. Navigate to "Subnets"
2. Click "Create subnet"
   - VPC: Lab VPC
   - Name: Public Subnet
   - AZ: Select first available zone
   - IPv4 CIDR: 10.0.0.0/24
3. Enable auto-assign public IP:
   - Select subnet → Actions → Edit subnet settings
   - Enable auto-assign public IPv4 address

#### Task 2.2: Private Subnet
1. Create another subnet:
   - VPC: Lab VPC
   - Name: Private Subnet
   - Same AZ as public subnet
   - IPv4 CIDR: 10.0.2.0/23
   - (This gives twice the IP space of public subnet)

**Note**: The private subnet doesn't get auto-assigned public IPs since it shouldn't be directly accessible from internet.

### Task 3: Creating an Internet Gateway

1. Navigate to "Internet Gateways"
2. Create new IGW:
   - Name: Lab IGW
3. Attach to VPC:
   - Select IGW → Actions → Attach to VPC
   - Choose "Lab VPC"

**Key Concept**: IGW enables communication between your VPC and the internet.

### Task 4: Configuring Route Tables

#### Private Route Table
1. Navigate to "Route Tables"
2. Find the main route table (associated with Lab VPC)
3. Rename to "Private Route Table"
   - Default route: 10.0.0.0/16 → local

#### Public Route Table
1. Create new route table:
   - Name: Public Route Table
   - VPC: Lab VPC
2. Add route:
   - Destination: 0.0.0.0/0
   - Target: Lab IGW
3. Associate with Public Subnet:
   - Subnet associations → Edit
   - Select Public Subnet

**Routing Logic**:
- Public subnet traffic to internet (0.0.0.0/0) goes through IGW
- All local VPC traffic stays within VPC

### Task 5: Launching Bastion Server

1. Navigate to EC2 Console
2. Launch instance:
   - Name: Bastion Server
   - AMI: Amazon Linux 2023
   - Instance type: t3.micro
   - Key pair: None (using EC2 Instance Connect)
   - Network:
     - VPC: Lab VPC
     - Subnet: Public Subnet
     - Auto-assign public IP: Enable
   - Security group:
     - Name: Bastion Security Group
     - Description: Allow SSH
     - Inbound rule: SSH from 0.0.0.0/0
3. Launch instance

**Security Note**: In production, restrict SSH access to specific IPs, not 0.0.0.0/0.

### Task 6: Creating NAT Gateway

1. Navigate to "NAT Gateways"
2. Create NAT Gateway:
   - Name: Lab NAT gateway
   - Subnet: Public Subnet
   - Allocate Elastic IP
3. Update Private Route Table:
   - Add route: 0.0.0.0/0 → NAT Gateway

**Why NAT Gateway?** Allows private subnet instances to initiate outbound internet connections while remaining inaccessible from internet.

## Optional Challenge: Testing Private Subnet

### Launch Private Instance
1. Launch EC2 instance:
   - Name: Private Instance
   - AMI: Amazon Linux 2023
   - Instance type: t3.micro
   - Network:
     - VPC: Lab VPC
     - Subnet: Private Subnet
   - Security group:
     - Name: Private Instance SG
     - Description: Allow SSH from Bastion
     - Inbound rule: SSH from 10.0.0.0/16
   - Advanced Details → User data:
     ```bash
     #!/bin/bash
     echo 'lab-password' | passwd ec2-user --stdin
     sed -i 's|[#]*PasswordAuthentication no|PasswordAuthentication yes|g' /etc/ssh/sshd_config
     systemctl restart sshd.service
     ```

### Connect to Private Instance
1. Connect to Bastion Server via EC2 Instance Connect
2. From bastion, SSH to private instance:
   ```bash
   ssh <private-ip>
   ```
   Password: lab-password

3. Test internet connectivity:
   ```bash
   ping -c 3 amazon.com
   ```

**Verification**: Successful ping confirms NAT Gateway is working properly.

## Troubleshooting Tips

1. **Instance not accessible?**
   - Check security group rules
   - Verify route tables
   - Confirm NAT Gateway is in "Available" state

2. **No internet access from private subnet?**
   - Verify NAT Gateway route exists in private route table
   - Check NAT Gateway is in public subnet

3. **DNS not resolving?**
   - Confirm DNS hostnames are enabled in VPC settings

## Security Best Practices

1. **Bastion Host Security**
   - Use SSH key pairs instead of passwords
   - Implement multi-factor authentication
   - Restrict inbound SSH to specific IPs

2. **Network Hardening**
   - Use network ACLs for additional subnet-level protection
   - Implement VPC Flow Logs for traffic monitoring
   - Consider using AWS Systems Manager instead of bastion hosts

## Cost Optimization

1. **NAT Gateway Costs**
   - NAT Gateways incur hourly charges + data processing fees
   - For development, consider NAT Instances as cheaper alternative
   - Delete resources when not in use

2. **Instance Sizing**
   - Use t3.micro or t3.small for lab environments
   - Right-size instances based on actual workload needs

## Conclusion

This lab demonstrated how to:
1. Create a secure VPC with public/private subnets
2. Configure proper routing with IGW and NAT Gateway
3. Implement bastion host architecture
4. Test connectivity between subnets

The architecture follows AWS best practices for security and network isolation while providing necessary internet access.