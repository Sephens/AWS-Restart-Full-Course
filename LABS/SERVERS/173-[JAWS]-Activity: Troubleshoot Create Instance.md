# **Lab Guide: Troubleshooting EC2 Instance Creation with AWS CLI**

## **Lab Overview**
This lab teaches you to:
✅ **Launch an EC2 LAMP stack instance** using AWS CLI  
✅ **Troubleshoot common EC2 launch issues**  
✅ **Verify web server and database functionality**  

---

## **Task 1: Connect to CLI Host**
1. **Go to EC2 Console** > **Instances**.
2. Select **CLI Host** instance > **Connect** > **EC2 Instance Connect** > **Connect**.

---

## **Task 2: Configure AWS CLI**
```bash
aws configure
```
Enter:  
- **AWS Access Key ID**: *(From **Details** > **Show**)*  
- **AWS Secret Access Key**: *(From **Details**)*  
- **Default region**: *(From **LabRegion** in Details)*  
- **Output format**: `json`  

---

## **Task 3: Troubleshoot EC2 Launch**

### **Step 1: Backup & Review Script**
```bash
cd ~/sysops-activity-files/starters
cp create-lamp-instance-v2.sh create-lamp-instance.backup
view create-lamp-instance-v2.sh  # Read-only mode
```
**Key Sections to Check**:
- **Lines 16-29**: VPC lookup logic  
- **Lines 31-55**: Subnet, key pair, and AMI ID collection  
- **Lines 124-152**: Security group creation  
- **Lines 154-168**: EC2 instance launch  

### **Step 2: First Run (Expected Failure)**
```bash
./create-lamp-instance-v2.sh
```
**Issue #1**: `InvalidAMIID.NotFound`  
**Cause**: AMI ID is Region-specific. The script uses a hardcoded AMI ID that doesn’t exist in your Region.  

**Fix**:
1. Replace the hardcoded AMI ID (e.g., `ami-xxxxxxxxxx`) with:  
   ```bash
   AMI=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --query 'Parameters[0].[Value]' --output text)
   ```
2. Save and rerun the script.  

---

### **Step 3: Web Server Troubleshooting**
**Issue #2**: Website not loading (`http://<public-ip>`)  
**Diagnosis**:
1. **Check Security Group**:  
   - Ensure **Port 80 (HTTP)** is open to `0.0.0.0/0`.  
   - Update via CLI:  
     ```bash
     aws ec2 authorize-security-group-ingress \
       --group-id <SG-ID> \
       --protocol tcp \
       --port 80 \
       --cidr 0.0.0.0/0
     ```
2. **Verify HTTPD Service**:  
   - Connect to the LAMP instance via **EC2 Instance Connect**:  
     ```bash
     sudo systemctl status httpd  # Should show "active (running)"
     ```
3. **Port Scan with Nmap**:  
   ```bash
   sudo yum install -y nmap
   nmap -Pn <public-ip>
   ```
   - If **Port 80 is closed**, revisit security group rules.  

---

### **Step 4: Verify User Data Execution**
```bash
sudo tail -f /var/log/cloud-init-output.log
```
**Expected Output**:  
- "Hello From Your Web Server!"  
- MariaDB/PHP installation success messages.  
- "Create Database script completed".  

---

## **Task 4: Test Café Website**
1. **Homepage**:  
   ```http
   http://<public-ip>/cafe
   ```
2. **Place Orders**:  
   - Navigate to **Menu** > Select items > **Submit Order**.  
3. **Order History**:  
   - Verify orders persist (stored in MariaDB).  

---

## **Key Fixes Summary**
| **Issue**               | **Solution**                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Invalid AMI ID           | Use `aws ssm get-parameters` to fetch the latest AMI dynamically.           |
| Port 80 Not Accessible   | Update security group to allow HTTP traffic (`0.0.0.0/0`).                  |
| HTTPD Not Running        | Check `sudo systemctl status httpd` and restart if needed.                  |

---

## **Conclusion**
✅ **Launched LAMP stack instance** via AWS CLI  
✅ **Resolved AMI and security group issues**  
✅ **Verified web app and database functionality**  

### **Key Takeaways**
🔹 **AMI IDs are Region-specific** – Always fetch dynamically.  
🔹 **Security Groups act as firewalls** – Double-check inbound rules.  
🔹 **User Data logs** are in `/var/log/cloud-init-output.log`.  

🚀 **Now you can deploy and troubleshoot EC2 instances programmatically!**  

### **Next Steps**
🔸 **Automate deployments** with CloudFormation/Terraform.  
🔸 **Set up monitoring** with CloudWatch.  
🔸 **Secure the database** with IAM roles.