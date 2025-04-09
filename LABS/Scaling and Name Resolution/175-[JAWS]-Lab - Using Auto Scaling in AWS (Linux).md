# **Lab Guide: Using Auto Scaling in AWS (Linux)**

## **Lab Overview**
This lab teaches you to:
✅ **Create an EC2 instance** using AWS CLI  
✅ **Generate a custom AMI** for consistent deployments  
✅ **Set up an Application Load Balancer (ALB)**  
✅ **Configure Auto Scaling** with dynamic scaling policies  
✅ **Test scaling under load**  

---

## **Task 1: Create an AMI for Auto Scaling**

### **1.1 Connect to Command Host**
1. **Go to EC2 Console** > **Instances** > Select **Command Host**.
2. Click **Connect** > **EC2 Instance Connect**.

### **1.2 Configure AWS CLI**
```bash
aws configure
```
- Leave **Access Key ID/Secret** blank (preconfigured).
- Set **Default Region**: `us-west-2` (or your lab region).
- **Output Format**: `json`.

### **1.3 Launch EC2 Instance**
```bash
cd /home/ec2-user/
more UserData.txt  # Review web server setup script
```
**Replace placeholders** in this command (use values from **Details** > **Show**):
```bash
aws ec2 run-instances \
  --key-name KEYNAME \
  --instance-type t3.micro \
  --image-id AMIID \
  --user-data file:///home/ec2-user/UserData.txt \
  --security-group-ids HTTPACCESS \
  --subnet-id SUBNETID \
  --associate-public-ip-address \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]' \
  --output text --query 'Instances[*].InstanceId'
```
**Note the Instance ID** (`NEW-INSTANCE-ID`).

### **1.4 Create AMI**
```bash
aws ec2 create-image \
  --instance-id NEW-INSTANCE-ID \
  --name "WebServerAMI" \
  --description "AMI for Auto Scaling"
```
**Key Notes**:  
🔹 AMI captures the **exact state** of the instance (OS + apps).  
🔹 Used later for **Auto Scaling launches**.

---

## **Task 2: Set Up Auto Scaling**

### **2.1 Create Application Load Balancer (ALB)**
1. **Go to EC2 Console** > **Load Balancers** > **Create ALB**.
   - **Name**: `WebServerELB`  
   - **VPC**: `Lab VPC`  
   - **Subnets**: `Public Subnet 1` & `Public Subnet 2`  
   - **Security Group**: `HTTPAccess` (allow HTTP)  
2. **Target Group**:  
   - **Name**: `webserver-app`  
   - **Health Check Path**: `/index.php`  
3. **Listener**: Forward to `webserver-app` (HTTP:80).  
4. Note the **ALB DNS name**.

### **2.2 Create Launch Template**
1. **Go to EC2 Console** > **Launch Templates** > **Create**.
   - **Name**: `web-app-launch-template`  
   - **AMI**: `WebServerAMI` (from Task 1.4)  
   - **Instance Type**: `t3.micro`  
   - **Security Group**: `HTTPAccess`  

### **2.3 Configure Auto Scaling Group**
1. From the launch template, select **Create Auto Scaling Group**.
   - **Name**: `Web App Auto Scaling Group`  
   - **VPC**: `Lab VPC`  
   - **Subnets**: `Private Subnet 1` & `Private Subnet 2`  
2. **Attach to ALB**:  
   - Target Group: `webserver-app`  
   - Health Check Type: `ELB`  
3. **Scaling Policies**:  
   - **Desired**: `2` | **Min**: `2` | **Max**: `4`  
   - **Metric**: `Average CPU utilization` (Target: `50%`)  
4. **Tags**: `Name=WebApp`  
5. Click **Create**.

**Why This Matters**:  
🔹 Auto Scaling **maintains instance health** and adjusts capacity based on CPU load.  

---

## **Task 3: Verify Auto Scaling**

### **3.1 Check Instances**
1. **Go to EC2 Console** > **Instances**.
   - Wait for 2 `WebApp` instances to show **2/2 checks passed**.  
2. **Verify Target Group**:  
   - Go to **Target Groups** > `webserver-app`.  
   - Ensure instances are **Healthy**.

### **3.2 Test ALB**
- Open the **ALB DNS name** in a browser.  
- The **Load Test app** should appear.  

---

## **Task 4: Test Scaling Under Load**

### **4.1 Trigger High CPU**
1. In the Load Test app, click **Start Stress**.  
   - This spikes CPU to **100%**.  
2. **Monitor Scaling**:  
   - Go to **Auto Scaling Groups** > **Activity Tab**.  
   - New instances launch when CPU > 50% (takes ~5 mins).  

### **4.2 Verify New Instances**
- Check **EC2 Console** for additional `WebApp` instances (up to 4).  

---

## **Key Troubleshooting Tips**
| **Issue**                | **Solution**                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Instances not healthy    | Check **Target Group Health Checks** (`/index.php` path).                   |
| No scaling triggered     | Verify **CloudWatch Alarms** for CPU metrics.                               |
| ALB not routing traffic  | Confirm **Security Group** allows HTTP (Port 80) from `0.0.0.0/0`.          |

---

## **Conclusion**
✅ **Created AMI** for consistent deployments  
✅ **Deployed ALB** for fault-tolerant traffic distribution  
✅ **Configured Auto Scaling** with dynamic policies  
✅ **Verified scaling** under CPU load  

### **Key Takeaways**
🔹 **ALB + Auto Scaling = High Availability**  
🔹 **Target Tracking Policies** automate scaling decisions.  
🔹 **Private Subnets** enhance security for backend instances.  

🚀 **You’ve built a self-healing, scalable web architecture!**  

### **Next Steps**
🔸 **Enable HTTPS** with ACM certificates.  
🔸 **Set up CloudWatch Dashboards** for monitoring.  
🔸 **Implement Lifecycle Hooks** for graceful scaling.