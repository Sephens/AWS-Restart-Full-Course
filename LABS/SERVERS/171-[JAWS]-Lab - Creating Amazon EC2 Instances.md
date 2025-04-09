# **Lab Guide: Creating Amazon EC2 Instances**

## **Lab Overview**
This lab teaches you how to:
✅ **Launch an EC2 instance** (Bastion Host) via AWS Console  
✅ **Connect to the instance** using EC2 Instance Connect  
✅ **Launch a web server instance** using AWS CLI  
✅ **Troubleshoot connectivity issues** (Optional Challenges)  

---

## **Task 1: Launch a Bastion Host via AWS Console**

### **Step-by-Step Instructions**
1. **Navigate to EC2 Console**:  
   - Search for **EC2** in AWS Console.  
   - Click **Launch instance** > **Launch instance**.

2. **Configure Instance**:  
   - **Name**: `Bastion host`  
   - **AMI**: **Amazon Linux 2** (Default)  
   - **Instance type**: `t3.micro`  
   - **Key pair**: *Proceed without key pair* (We'll use EC2 Instance Connect)  

3. **Network Settings**:  
   - **VPC**: `Lab VPC`  
   - **Subnet**: `Public Subnet` (Auto-selected)  
   - **Auto-assign public IP**: `Enable`  
   - **Security group**:  
     - **Name**: `Bastion security group`  
     - **Description**: `Permit SSH connections`  

4. **Advanced Details**:  
   - **IAM instance profile**: `Bastion-Role` *(Allows CLI access)*  

5. **Launch Instance**:  
   - Click **Launch instance** > **View all instances**.  

---

## **Task 2: Connect to the Bastion Host**

### **Step-by-Step Instructions**
1. **Select the Bastion Host**:  
   - In **EC2 Console** > **Instances**, check the `Bastion host`.  
   - Click **Connect**.  

2. **Use EC2 Instance Connect**:  
   - Select **EC2 Instance Connect** tab.  
   - Click **Connect** to open a browser-based terminal.  

---

## **Task 3: Launch a Web Server via AWS CLI**

### **Step 1: Retrieve the Latest AMI**
```bash
# Set Region
AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
export AWS_DEFAULT_REGION=${AZ::-1}

# Get Latest Amazon Linux 2 AMI
AMI=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --query 'Parameters[0].[Value]' --output text)
echo $AMI
```

### **Step 2: Get Subnet ID**
```bash
SUBNET=$(aws ec2 describe-subnets --filters 'Name=tag:Name,Values=Public Subnet' --query Subnets[].SubnetId --output text)
echo $SUBNET
```

### **Step 3: Get Security Group ID**
```bash
SG=$(aws ec2 describe-security-groups --filters Name=group-name,Values=WebSecurityGroup --query SecurityGroups[].GroupId --output text)
echo $SG
```

### **Step 4: Download User Data Script**
```bash
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-1-23732/171-lab-JAWS-create-ec2/s3/UserData.txt
cat UserData.txt  # Verify script installs Apache + web app
```

### **Step 5: Launch Web Server**
```bash
INSTANCE=$(\
aws ec2 run-instances \
--image-id $AMI \
--subnet-id $SUBNET \
--security-group-ids $SG \
--user-data file:///home/ec2-user/UserData.txt \
--instance-type t3.micro \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Web Server}]' \
--query 'Instances[*].InstanceId' \
--output text \
)
echo $INSTANCE
```

### **Step 6: Verify Instance Status**
```bash
aws ec2 describe-instances --instance-ids $INSTANCE --query 'Reservations[].Instances[].State.Name' --output text
```
- Wait until status changes to `running`.

### **Step 7: Test the Web Server**
```bash
aws ec2 describe-instances --instance-ids $INSTANCE --query Reservations[].Instances[].PublicDnsName --output text
```
- Copy the **Public DNS** and paste into a browser.  
- You should see the web app!  

---

## **Optional Challenges**

### **Challenge 1: Fix Misconfigured Web Server**
**Problem**: Cannot connect via EC2 Instance Connect.  
**Solution**:  
1. Check if **Security Group** allows **SSH (Port 22)**.  
2. Verify **IAM role** has proper permissions.  

### **Challenge 2: Fix Web Server Installation**
**Problem**: Website doesn’t load.  
**Solution**:  
1. Check **Security Group** allows **HTTP (Port 80)**.  
2. Verify **User Data script** executed correctly:  
   ```bash
   sudo tail -f /var/log/cloud-init-output.log
   ```

---

## **Conclusion**
✅ **Launched Bastion Host** via AWS Console  
✅ **Connected via EC2 Instance Connect** (No SSH keys)  
✅ **Deployed Web Server** using AWS CLI  
✅ **Automated setup** with User Data scripts  

### **Key Takeaways**
🔹 **EC2 Instance Connect** is secure (no key management).  
🔹 **User Data scripts** automate post-launch configurations.  
🔹 **AWS CLI enables infrastructure-as-code** (repeatable deployments).  

🚀 **Now you can launch and manage EC2 instances programmatically!**  

### **Next Steps**
🔸 **Explore Auto Scaling Groups** for high availability.  
🔸 **Use CloudFormation** for templated deployments.  
🔸 **Set up ALB** to distribute traffic across instances.