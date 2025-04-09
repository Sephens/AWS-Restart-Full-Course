# Troubleshooting a VPC - Detailed Lab Walkthrough

## Lab Overview
This lab guides you through troubleshooting VPC networking issues and analyzing VPC Flow Logs to diagnose connectivity problems.

## Objectives
- Create and configure VPC Flow Logs
- Troubleshoot common VPC configuration issues
- Analyze flow log data to diagnose network problems

## Task 1: Connecting to the CLI Host Instance

### Purpose
Establish a working environment for running AWS CLI commands to troubleshoot the VPC.

### Steps:
1. **Access EC2 Console**:
   - Search for "EC2" in AWS Console
   - Navigate to "Instances"

2. **Connect to CLI Host**:
   - Select the "CLI Host" instance
   - Click "Connect"
   - Choose "EC2 Instance Connect" tab
   - Click "Connect"

3. **Configure AWS CLI**:
   ```bash
   aws configure
   ```
   - Enter provided credentials:
     - AWS Access Key ID: [AccessKey]
     - AWS Secret Access Key: [SecretKey]
     - Default region: `us-west-2`
     - Output format: `json`

## Task 2: Creating VPC Flow Logs

### Purpose
Capture network traffic data for troubleshooting.

### Steps:
1. **Create S3 Bucket**:
   ```bash
   aws s3api create-bucket --bucket flowlog###### --region 'us-west-2' \
   --create-bucket-configuration LocationConstraint='us-west-2'
   ```
   - Replace `######` with random numbers
   - Note the bucket name for later use

2. **Get VPC1 ID**:
   ```bash
   aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,Tags[?Key==`Name`].Value,CidrBlock]' \
   --filters "Name=tag:Name,Values='VPC1'"
   ```

3. **Create Flow Log**:
   ```bash
   aws ec2 create-flow-logs --resource-type VPC --resource-ids <vpc-id> \
   --traffic-type ALL --log-destination-type s3 \
   --log-destination arn:aws:s3:::<flowlog######>
   ```
   - Replace `<vpc-id>` and `<flowlog######>` with your values

4. **Verify Flow Log**:
   ```bash
   aws ec2 describe-flow-logs
   ```
   - Confirm status is "ACTIVE"

## Task 3: Troubleshooting VPC Configuration Issues

### Purpose
Diagnose and fix connectivity problems with the web server.

### Initial Symptoms:
- Cannot access web server via browser (HTTP)
- Cannot SSH to web server instance

### Troubleshooting Challenge #1: Web Access Issue

1. **Check Instance Status**:
   ```bash
   aws ec2 describe-instances --filter "Name=ip-address,Values='<WebServerIP>'" \
   --query 'Reservations[*].Instances[*].[State,PrivateIpAddress,InstanceId,SecurityGroups,SubnetId,KeyName]'
   ```

2. **Install nmap**:
   ```bash
   sudo yum install -y nmap
   ```

3. **Scan Web Server Ports**:
   ```bash
   nmap <WebServerIP>
   ```
   - If no ports open, check security groups

4. **Check Security Group**:
   ```bash
   aws ec2 describe-security-groups --group-ids <WebServerSgId>
   ```
   - Verify inbound rules allow HTTP (port 80)

5. **Check Route Table**:
   ```bash
   aws ec2 describe-route-tables --filter "Name=association.subnet-id,Values='<VPC1PubSubnetID>'"
   ```
   - Should have route to internet gateway (0.0.0.0/0 -> igw-...)

6. **Add Missing Route**:
   ```bash
   aws ec2 create-route --route-table-id <rtb-id> \
   --destination-cidr-block 0.0.0.0/0 --gateway-id <igw-id>
   ```
   - After fixing, web page should load

### Troubleshooting Challenge #2: SSH Access Issue

1. **Check Network ACL**:
   ```bash
   aws ec2 describe-network-acls --filter "Name=association.subnet-id,Values='<VPC1PublicSubnetID>'" \
   --query 'NetworkAcls[*].[NetworkAclId,Entries]'
   ```
   - Look for rules blocking SSH (port 22)

2. **Delete Problematic ACL Entry**:
   ```bash
   aws ec2 delete-network-acl-entry --network-acl-id <acl-id> \
   --rule-number 100 --egress
   ```
   - After fixing, should be able to SSH via EC2 Instance Connect

## Task 4: Analyzing Flow Logs

### Purpose
Examine captured network traffic to understand connectivity issues.

### Steps:

1. **Create Directory**:
   ```bash
   mkdir flowlogs
   cd flowlogs
   ```

2. **Download Flow Logs**:
   ```bash
   aws s3 cp s3://<flowlog######>/ . --recursive
   ```

3. **Navigate to Log Directory**:
   ```bash
   cd AWSLogs/<AccountID>/vpcflowlogs/us-west-2/yyyy/mm/dd/
   ```

4. **Extract Logs**:
   ```bash
   gunzip *.gz
   ```

5. **Analyze Log Structure**:
   ```bash
   head <filename>
   ```
   - Shows column headers

6. **Find Rejected Connections**:
   ```bash
   grep -rn REJECT .
   ```

7. **Find SSH Rejects**:
   ```bash
   grep -rn 22 . | grep REJECT
   ```

8. **Find Your SSH Attempts**:
   - Get your public IP from Security Group console
   ```bash
   grep -rn 22 . | grep REJECT | grep <your-ip>
   ```

9. **Verify Network Interface**:
   ```bash
   aws ec2 describe-network-interfaces \
   --filters "Name=association.public-ip,Values='<WebServerIP>'" \
   --query 'NetworkInterfaces[*].[NetworkInterfaceId,Association.PublicIp]'
   ```

10. **Convert Timestamps**:
    ```bash
    date -d @<timestamp>
    ```

## Conclusion

### Key Accomplishments:
1. Successfully configured VPC Flow Logs to S3
2. Diagnosed and fixed web access issues:
   - Missing internet gateway route
3. Diagnosed and fixed SSH access issues:
   - Restrictive network ACL rules
4. Analyzed flow logs to verify troubleshooting

### Troubleshooting Methodology:
1. Verify instance state
2. Check security group rules
3. Verify route tables
4. Check network ACLs
5. Use flow logs to confirm traffic patterns

### Best Practices:
- Enable flow logs before troubleshooting
- Use least-privilege security groups
- Document network ACL rules
- Monitor flow logs regularly
- Consider using Amazon Athena for advanced log analysis