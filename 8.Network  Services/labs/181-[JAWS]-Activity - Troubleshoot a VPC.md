# **Lab: Troubleshooting a VPC**  
**Objective:** Troubleshoot VPC configurations and analyze VPC Flow Logs.  

---

## **Lab Overview**  
This lab involves troubleshooting networking issues in a VPC environment with:  
- **Two VPCs (VPC1 and VPC2)**  
- **EC2 instances (Cafe Web Server & CLI Host)**  
- **Flow Logs for traffic analysis**  

### **Tasks Breakdown**  
1. **Create an S3 bucket** to store VPC Flow Logs.  
2. **Configure VPC Flow Logs** to capture traffic data.  
3. **Troubleshoot VPC issues** preventing web access and SSH connectivity.  
4. **Analyze Flow Logs** to identify rejected connections.  

---

## **Step-by-Step Walkthrough**  

### **Task 1: Connect to the CLI Host Instance**  
**Objective:** Use EC2 Instance Connect to access the CLI Host instance for AWS CLI operations.  

#### **Steps:**  
1. **Open AWS Console** → **EC2 Dashboard**.  
2. **Locate the "CLI Host" instance** → **Click "Connect"**.  
3. **Choose "EC2 Instance Connect"** → **Click "Connect"**.  
   - A terminal session opens in a new tab.  
4. **Configure AWS CLI:**  
   ```bash
   aws configure
   ```
   - Enter the provided `AccessKey`, `SecretKey`, and set `us-west-2` as the default region.  
   - Output format: `json`.  

✅ **Verification:**  
- Run `aws sts get-caller-identity` to confirm CLI access.  

---

### **Task 2: Create VPC Flow Logs**  
**Objective:** Log all VPC traffic to an S3 bucket for analysis.  

#### **Steps:**  
1. **Create an S3 bucket:**  
   ```bash
   aws s3api create-bucket --bucket flowlog123456 --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
   ```
   - Replace `123456` with random digits.  

2. **Get VPC1 ID:**  
   ```bash
   aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,Tags[?Key==`Name`].Value,CidrBlock]' --filters "Name=tag:Name,Values='VPC1'"
   ```
   - Note the `VpcId` (e.g., `vpc-0a1b2c3d4e5f6g7h8`).  

3. **Enable Flow Logs:**  
   ```bash
   aws ec2 create-flow-logs --resource-type VPC --resource-ids <VPC-ID> --traffic-type ALL --log-destination-type s3 --log-destination arn:aws:s3:::flowlog123456
   ```
   - Replace `<VPC-ID>` with the ID from Step 2.  

4. **Verify Flow Logs:**  
   ```bash
   aws ec2 describe-flow-logs
   ```
   - Check for `"FlowLogStatus": "ACTIVE"`.  

✅ **Verification:**  
- Check S3 bucket (`flowlog123456`) for logs.  

---

### **Task 3: Troubleshoot VPC Issues**  
**Objective:** Fix connectivity issues preventing web access and SSH.  

#### **Issue 1: Web Server Unreachable**  
1. **Check Web Server Status:**  
   ```bash
   aws ec2 describe-instances --filter "Name=ip-address,Values=<WebServerIP>" --query 'Reservations[*].Instances[*].[State,PrivateIpAddress,InstanceId,SecurityGroups,SubnetId,KeyName]'
   ```
   - If `State` is `running`, proceed.  

2. **Test Port Access:**  
   ```bash
   sudo yum install -y nmap
   nmap <WebServerIP>
   ```
   - If no ports are open, check **Security Groups (SG)** and **Route Tables**.  

3. **Check Security Group Rules:**  
   ```bash
   aws ec2 describe-security-groups --group-ids <WebServerSgId>
   ```
   - Ensure inbound rules allow HTTP (port `80`) and SSH (port `22`).  

4. **Fix Route Table:**  
   ```bash
   aws ec2 describe-route-tables --filter "Name=association.subnet-id,Values=<VPC1PubSubnetID>"
   ```
   - If missing `0.0.0.0/0` → **Internet Gateway (IGW)**, add it:  
     ```bash
     aws ec2 create-route --route-table-id <RouteTableID> --destination-cidr-block 0.0.0.0/0 --gateway-id <IGW-ID>
     ```

✅ **Verification:**  
- Refresh the browser tab with `http://<WebServerIP>`. Should display:  
  > **"Hello From Your Web Server!"**  

#### **Issue 2: SSH Connection Fails**  
1. **Check Network ACLs:**  
   ```bash
   aws ec2 describe-network-acls --filter "Name=association.subnet-id,Values=<VPC1PublicSubnetID>" --query 'NetworkAcls[*].[NetworkAclId,Entries]'
   ```
   - Look for **DENY rules** on port `22`.  

2. **Fix ACL Rules:**  
   - Delete problematic rules:  
     ```bash
     aws ec2 delete-network-acl-entry --network-acl-id <ACL-ID> --rule-number <RuleNumber> --egress false
     ```

✅ **Verification:**  
- Retry SSH via EC2 Instance Connect → **Should succeed**.  

---

### **Task 4: Analyze Flow Logs**  
**Objective:** Examine logs to identify rejected connections.  

#### **Steps:**  
1. **Download Logs:**  
   ```bash
   mkdir flowlogs && cd flowlogs
   aws s3 cp s3://flowlog123456/ . --recursive
   cd AWSLogs/<AccountID>/vpcflowlogs/us-west-2/YYYY/MM/DD/
   gunzip *.gz
   ```

2. **Search for Rejected SSH Attempts:**  
   ```bash
   grep -rn REJECT . | grep 22 | grep <Your-IP>
   ```
   - Example output:  
     ```
     <filename>:<line>:2 <timestamp> eni-12345678 <Your-IP> <WebServerIP> 22 6 20 REJECT OK
     ```

3. **Convert Timestamps:**  
   ```bash
   date -d @1554496931
   ```
   - Matches your failed SSH attempts.  

✅ **Verification:**  
- Logs confirm **REJECT** entries for SSH (port `22`).  

---

## **Conclusion**  
### **Key Takeaways**  
✔ **Flow Logs** help monitor and troubleshoot VPC traffic.  
✔ **Security Groups & NACLs** control inbound/outbound access.  
✔ **Route Tables** must include an IGW for public subnets.  

### **Next Steps**  
- Use **Amazon Athena** for advanced log queries.  
- Automate **VPC troubleshooting** with AWS Lambda.  

---

## **Troubleshooting Tips**  
❌ **Flow Logs Not Appearing?**  
- Verify **S3 bucket permissions** (Bucket Policy must allow `vpc-flow-logs.amazonaws.com`).  
- Check **IAM role permissions** for VPC Flow Logs.  

❌ **Still Can’t SSH?**  
- Ensure **Key Pair** is correctly assigned.  
- Verify **NACLs** are not blocking ephemeral ports (`1024-65535`).  

---

## **Final Notes**  
This lab reinforces:  
🔹 **VPC Networking Fundamentals**  
🔹 **Security Best Practices**  
🔹 **Log Analysis Techniques**  

**End of Lab.** 🚀