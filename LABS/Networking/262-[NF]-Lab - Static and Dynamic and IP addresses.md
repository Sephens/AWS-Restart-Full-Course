# Comprehensive Lab Guide: Static vs. Dynamic IP Addresses in AWS

## Introduction
This lab explores the critical differences between static and dynamic IP addresses in AWS environments, focusing on solving a real-world scenario where an EC2 instance's public IP changes after stop/start cycles.

## Task 1: Investigating the Customer Environment

### Step 1: Understanding the Scenario
**Customer Situation:**
- EC2 instance named "Public Instance"
- Public IP changes after stop/start cycles
- Breaks dependent resources expecting fixed IP
- Instance needs to be stopped to control costs

**Key Concepts:**
- **Dynamic Public IP**: Default AWS behavior - changes after stop/start
- **Static Public IP**: Requires Elastic IP (EIP) assignment
- **Private IP**: Always persists within VPC until termination

### Step 2: Accessing AWS Console
1. Navigate to EC2:
   - Method 1: Search "EC2" in AWS console search bar
   - Method 2: Services → Compute → EC2

**Verification:**
- Confirm you're in the correct region
- Note existing instances (will create new test instance)

### Step 3: Launching Test Instance
Follow these detailed steps:

1. **Choose AMI**:
   - Select "Amazon Linux 2 AMI (HVM)"
   - This provides a standard Linux environment

2. **Instance Type**:
   - Select t3.micro (free tier eligible)
   - Balances cost and performance for testing

3. **Configure Instance**:
   ```yaml
   Network: Lab VPC (vpc-xxxxxxxx)
   Subnet: Public Subnet 1 (subnet-xxxxxx)
   Auto-assign Public IP: Enable
   ```

4. **Add Storage**:
   - Default 8GB gp2 volume (sufficient for testing)

5. **Add Tags**:
   ```yaml
   Key: Name
   Value: test instance
   ```

6. **Security Group**:
   - Select existing "Linux Instance SG"
   - Ensures basic connectivity rules

7. **Key Pair**:
   - Select existing "vockey" RSA key pair
   - Required for SSH access if needed

### Step 4: Observing IP Behavior
1. **Initial State**:
   - Note public and private IPs in Networking tab
   - Example:
     ```
     Public IP: 54.210.167.204
     Private IP: 10.0.1.58
     ```

2. **Stop Instance**:
   - Instance state → Stop instance
   - Observe IPs become blank for public IP

3. **Start Instance**:
   - Instance state → Start instance
   - New public IP assigned (dynamic behavior)
   - Private IP remains the same

**Key Finding**: 
- Public IP is dynamic by default
- Private IP persists (static within VPC lifecycle)

## Implementing Elastic IP Solution

### Step 1: Allocate Elastic IP
1. Navigate to: 
   - EC2 → Network & Security → Elastic IPs
2. Allocate new EIP:
   - Keep all defaults
   - Example allocated: 54.226.172.104

### Step 2: Associate EIP to Instance
1. Select EIP → Actions → Associate Elastic IP
2. Configure association:
   ```yaml
   Resource type: Instance
   Instance: test instance
   Private IP: [auto-populated]
   ```

### Step 3: Verify Solution
1. Check Networking tab:
   - Public IP now shows EIP address
2. Stop/Start test:
   - Public IP persists after stop/start
   - Private IP remains unchanged

**Verification Table**:

| Action       | Public IP Before | Public IP After | Private IP |
|--------------|-------------------|-----------------|------------|
| Initial      | 54.210.167.204    | -               | 10.0.1.58  |
| After Stop   | -                 | -               | -          |
| After Start  | 54.210.178.91     | -               | 10.0.1.58  |
| EIP Assigned | 54.226.172.104    | -               | 10.0.1.58  |
| Post Stop/Start | 54.226.172.104 | 54.226.172.104  | 10.0.1.58  |

## Task 2: Customer Response (Group Activity)

### Recommended Solution Script

**Person 2 (Support Engineer):**
"Bob, we've diagnosed that your 'Public Instance' is using AWS's default dynamic public IP assignment. To maintain a consistent public IP, we recommend:

1. Allocate an Elastic IP in your AWS account
2. Associate it with your EC2 instance
3. Update any DNS records or configurations to use the EIP

This will ensure the public IP remains the same through stop/start cycles. The Elastic IP will remain allocated to your account until you explicitly release it."

**Person 1 (Bob):**
"So if I understand correctly, the changing IP is expected behavior for regular EC2 instances, but Elastic IPs give me that static IP capability I need? And I won't incur charges as long as the EIP is associated with a running instance?"

### Technical Explanation

**Why Default Public IPs Change:**
- AWS uses dynamic public IP pool
- IPs are released when instance stops
- New IP assigned from available pool at start

**Elastic IP Benefits:**
- Persistent public IP address
- Can be remapped between instances
- No charge when properly associated
- Supports DNS record stability

**Important Notes:**
1. EIP charges apply if:
   - Not associated with any instance
   - Associated with stopped instance
   - Associated with unattached network interface

2. Best Practices:
   - Use Route 53 for DNS rather than relying on IPs
   - Document all EIP allocations
   - Monitor for unattached EIPs

## Advanced Considerations

### NAT Gateway Use Case
For private instances needing outbound static IP:
1. Create NAT Gateway in public subnet
2. Assign EIP during creation
3. Update private subnet route tables

### Automation Approach
For infrastructure-as-code users:
```terraform
resource "aws_eip" "web" {
  vpc = true
}

resource "aws_eip_association" "web" {
  instance_id   = aws_instance.web.id
  allocation_id = aws_eip.web.id
}
```

### Troubleshooting Tips

1. If EIP not appearing:
   - Check association status
   - Verify in correct region
   - Refresh console view

2. If connectivity issues:
   - Check security group rules
   - Verify route table has IGW route
   - Test from different networks

This comprehensive solution addresses the customer's immediate need while educating about AWS networking fundamentals and cost optimization strategies.