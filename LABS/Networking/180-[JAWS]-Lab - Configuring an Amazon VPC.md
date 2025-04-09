# Configuring a VPC - Detailed Lab Walkthrough

## Lab Overview
This lab guides you through creating a complete Amazon Virtual Private Cloud (VPC) environment including public and private subnets, internet connectivity, and bastion host configuration.

## Objectives
- Create a VPC with public and private subnets
- Configure internet connectivity via Internet Gateway and NAT Gateway
- Set up a bastion server for secure access
- Establish proper routing between network components

## Task 1: Creating a VPC

### Purpose
Create the foundational VPC network that will contain all other components.

### Steps:
1. **Access VPC Console**:
   - Search for "VPC" in AWS Console
   - Navigate to "Your VPCs"

2. **Create New VPC**:
   - Click "Create VPC"
   - Select "VPC only" option
   - Configure:
     - Name tag: `Lab VPC`
     - IPv4 CIDR: `10.0.0.0/16`
     - No IPv6 CIDR
     - Tenancy: Default
   - Click "Create VPC"

3. **Enable DNS Hostnames**:
   - Select the new VPC
   - Choose "Actions" → "Edit VPC settings"
   - Check "Enable DNS hostnames"
   - Click "Save"

### Notes:
- The 10.0.0.0/16 CIDR provides 65,536 IP addresses
- DNS hostnames allow instances to get public DNS names
- Default tenancy means instances share hardware with others

## Task 2: Creating Subnets

### Purpose
Divide the VPC into logical segments with different access characteristics.

### Task 2.1: Creating a Public Subnet

1. **Navigate to Subnets**:
   - In VPC console, go to "Subnets"
   - Click "Create subnet"

2. **Configure Public Subnet**:
   - VPC: Select "Lab VPC"
   - Subnet name: `Public Subnet`
   - Availability Zone: Choose first AZ (e.g., us-east-1a)
   - IPv4 CIDR: `10.0.0.0/24` (256 addresses)
   - Click "Create subnet"

3. **Enable Auto-Assign Public IP**:
   - Select the new subnet
   - Choose "Actions" → "Edit subnet settings"
   - Check "Enable auto-assign public IPv4 address"
   - Click "Save"

### Task 2.2: Creating a Private Subnet

1. **Create Private Subnet**:
   - Click "Create subnet"
   - Configure:
     - VPC: "Lab VPC"
     - Subnet name: `Private Subnet`
     - Same AZ as public subnet
     - IPv4 CIDR: `10.0.2.0/23` (512 addresses)
   - Click "Create subnet"

### Notes:
- Public subnet will host internet-facing resources
- Private subnet will host protected resources
- Larger CIDR for private subnet anticipates more internal resources
- Subnets are still isolated until we add routing

## Task 3: Creating an Internet Gateway

### Purpose
Provide internet access for resources in the public subnet.

### Steps:
1. **Navigate to Internet Gateways**:
   - In VPC console, go to "Internet Gateways"
   - Click "Create internet gateway"

2. **Create IGW**:
   - Name tag: `Lab IGW`
   - Click "Create internet gateway"

3. **Attach to VPC**:
   - Select the new IGW
   - Choose "Actions" → "Attach to VPC"
   - Select "Lab VPC"
   - Click "Attach internet gateway"

### Notes:
- IGW provides two-way internet access
- Must be attached to a VPC to function
- Only one IGW needed per VPC

## Task 4: Configuring Route Tables

### Purpose
Control how traffic flows between subnets and to/from the internet.

### Steps:
1. **Navigate to Route Tables**:
   - In VPC console, go to "Route Tables"
   - Find the main route table for Lab VPC

2. **Rename Main Route Table**:
   - Select the route table
   - Click the name to edit
   - Change to `Private Route Table`
   - Click "Save"

3. **Create Public Route Table**:
   - Click "Create route table"
   - Name: `Public Route Table`
   - VPC: "Lab VPC"
   - Click "Create"

4. **Add Internet Route**:
   - Select the new route table
   - Go to "Routes" tab
   - Click "Edit routes"
   - Add route:
     - Destination: `0.0.0.0/0`
     - Target: Select "Lab IGW"
   - Click "Save changes"

5. **Associate Public Subnet**:
   - Go to "Subnet associations" tab
   - Click "Edit subnet associations"
   - Select "Public Subnet"
   - Click "Save associations"

### Notes:
- Main route table becomes our private route table
- Public route table gets internet-bound traffic rule
- Association makes the public subnet truly "public"

## Task 5: Launching a Bastion Server

### Purpose
Create a secure entry point to access private resources.

### Steps:
1. **Navigate to EC2 Console**:
   - Search for "EC2" in AWS Console
   - Go to "Instances"

2. **Launch Instance**:
   - Click "Launch instances"
   - Configure:
     - Name: `Bastion Server`
     - AMI: Amazon Linux 2023
     - Instance type: t3.micro
     - Key pair: Proceed without key pair
     - Network settings:
       - VPC: "Lab VPC"
       - Subnet: "Public Subnet"
       - Auto-assign public IP: Enable
       - Security group:
         - Name: `Bastion Security Group`
         - Description: `Allow SSH`
         - Rule: SSH from Anywhere (0.0.0.0/0)
   - Click "Launch instance"

### Notes:
- Bastion acts as a secure jump host
- SSH access open to internet (in lab only - restrict in production)
- No key pair needed because we'll use EC2 Instance Connect

## Task 6: Creating a NAT Gateway

### Purpose
Allow private subnet resources to access the internet without exposing them.

### Steps:
1. **Navigate to NAT Gateways**:
   - Search for "NAT gateways" in AWS Console
   - Click "Create NAT gateway"

2. **Configure NAT Gateway**:
   - Name: `Lab NAT gateway`
   - Subnet: "Public Subnet"
   - Click "Allocate Elastic IP"
   - Click "Create NAT gateway"

3. **Update Private Route Table**:
   - Go back to VPC console → "Route Tables"
   - Select "Private Route Table"
   - Go to "Routes" tab
   - Click "Edit routes"
   - Add route:
     - Destination: `0.0.0.0/0`
     - Target: Select the new NAT gateway
   - Click "Save changes"

### Notes:
- NAT Gateway needs Elastic IP
- Placed in public subnet to access internet
- Private subnet traffic to internet routes through NAT
- NAT Gateway is highly available (unlike NAT instances)

## Optional Challenge: Testing the Private Subnet

### Purpose
Validate the complete network configuration.

### Steps:

1. **Launch Private Instance**:
   - In EC2 console, launch new instance:
     - Name: `Private Instance`
     - AMI: Amazon Linux 2023
     - Instance type: t3.micro
     - Key pair: Proceed without key pair
     - Network settings:
       - VPC: "Lab VPC"
       - Subnet: "Private Subnet"
       - Security group:
         - Name: `Private Instance SG`
         - Description: `Allow SSH from Bastion`
         - Rule: SSH from 10.0.0.0/16
     - Advanced details:
       - User data:
         ```bash
         #!/bin/bash
         echo 'lab-password' | passwd ec2-user --stdin
         sed -i 's|[#]*PasswordAuthentication no|PasswordAuthentication yes|g' /etc/ssh/sshd_config
         systemctl restart sshd.service
         ```

2. **Connect to Bastion**:
   - Select "Bastion Server"
   - Click "Connect" → "EC2 Instance Connect"
   - Click "Connect"

3. **SSH to Private Instance**:
   - In EC2 console, note private IP of "Private Instance"
   - From bastion terminal:
     ```bash
     ssh <private-ip>
     ```
   - When prompted:
     - "Are you sure...": yes
     - Password: `lab-password`

4. **Test Internet Access**:
   - From private instance:
     ```bash
     ping -c 3 amazon.com
     ```
   - Should see successful ping responses

### Notes:
- Private instance has no public IP
- Can only be accessed via bastion
- Internet access verified via NAT Gateway
- User data script enables password auth for lab purposes only

## Conclusion

### Key Accomplishments:
1. Created complete VPC with public/private subnets
2. Established internet connectivity patterns
3. Implemented bastion host architecture
4. Verified proper network functionality

### Architecture Components:
- **VPC**: 10.0.0.0/16
- **Public Subnet**: 10.0.0.0/24 with IGW access
- **Private Subnet**: 10.0.2.0/23 with NAT access
- **Bastion Host**: Secure entry point in public subnet
- **NAT Gateway**: Outbound internet for private resources

### Security Considerations:
- Production environments should:
  - Restrict bastion SSH access to specific IPs
  - Use SSH keys instead of passwords
  - Consider AWS Systems Manager instead of bastion
  - Implement network ACLs for additional security