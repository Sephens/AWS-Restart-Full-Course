# **Lab Guide: Scaling and Load Balancing Your Architecture**

## **Lab Overview**
This lab teaches you to:
✅ **Create an AMI** from an existing EC2 instance  
✅ **Set up an Application Load Balancer (ALB)**  
✅ **Configure Auto Scaling** with dynamic scaling policies  
✅ **Monitor performance** with CloudWatch alarms  

---

## **Task 1: Create an AMI for Auto Scaling**
### **Step-by-Step Instructions**
1. **Go to EC2 Console** > **Instances**.
2. Select **Web Server 1** > **Actions** > **Image and templates** > **Create image**.
   - **Name**: `Web Server AMI`  
   - **Description**: `Lab AMI for Web Server`  
3. Click **Create image**.  
   - Note the AMI ID for later use.  

**Why This Matters**:  
🔹 AMIs allow **consistent deployments** of preconfigured instances.  

---

## **Task 2: Create an Application Load Balancer (ALB)**
### **Step-by-Step Instructions**
1. **Go to EC2 Console** > **Load Balancers** > **Create Load Balancer** > **Application Load Balancer**.  
2. **Configure ALB**:  
   - **Name**: `LabELB`  
   - **VPC**: `Lab VPC`  
   - **Mappings**: Select both AZs + **Public Subnet 1/2**.  
   - **Security Group**: `Web Security Group` (remove default).  
3. **Target Group**:  
   - **Name**: `lab-target-group`  
   - **Target Type**: `Instances`  
4. **Listener**: Forward to `lab-target-group` (HTTP:80).  
5. Click **Create** > Note the **DNS name**.  

**Key Notes**:  
📌 ALB distributes traffic across **multiple AZs** for high availability.  

---

## **Task 3: Create a Launch Template**
### **Step-by-Step Instructions**
1. **Go to EC2 Console** > **Launch Templates** > **Create launch template**.  
2. **Configure**:  
   - **Name**: `lab-app-launch-template`  
   - **AMI**: `Web Server AMI` (My AMIs tab)  
   - **Instance Type**: `t3.micro`  
   - **Security Group**: `Web Security Group`  
3. Click **Create launch template**.  

**Why This Matters**:  
🔹 Launch templates **standardize instance configurations** for Auto Scaling.  

---

## **Task 4: Create an Auto Scaling Group**
### **Step-by-Step Instructions**
1. From the launch template, select **Actions** > **Create Auto Scaling group**.  
2. **Configure**:  
   - **Name**: `Lab Auto Scaling Group`  
   - **VPC**: `Lab VPC`  
   - **Subnets**: `Private Subnet 1` & `Private Subnet 2`  
3. **Attach to ALB**:  
   - Select `lab-target-group`  
   - **Health Check Type**: `ELB`  
4. **Scaling Policies**:  
   - **Desired**: `2` | **Min**: `2` | **Max**: `4`  
   - **Scaling Policy**: `Target tracking` (CPU @ 50%).  
5. **Tags**: Add `Name: Lab Instance`.  
6. Click **Create Auto Scaling group**.  

**Key Notes**:  
📌 Auto Scaling **maintains instance health** and adjusts capacity based on CPU.  

---

## **Task 5: Verify Load Balancing**
### **Step-by-Step Instructions**
1. **Go to EC2 Console** > **Instances**:  
   - Verify 2 new `Lab Instance` instances are running.  
2. **Check Target Group**:  
   - Go to **Target Groups** > `lab-target-group`.  
   - Wait for instances to show **Healthy**.  
3. **Test ALB**:  
   - Paste the ALB **DNS name** into a browser.  
   - The **Load Test app** should appear.  

**Why This Matters**:  
🔹 ALB ensures **traffic is evenly distributed** across healthy instances.  

---

## **Task 6: Test Auto Scaling**
### **Step-by-Step Instructions**
1. **Generate Load**:  
   - In the Load Test app, click **Load Test**.  
2. **Monitor CloudWatch**:  
   - Go to **CloudWatch** > **Alarms**.  
   - Wait for `AlarmHigh` to trigger (CPU > 50%).  
3. **Verify Scaling**:  
   - Return to **EC2 Console** > **Instances**.  
   - New instances should launch (up to 4).  

**Key Notes**:  
📌 Auto Scaling **responds to demand** while staying within limits.  

---

## **Task 7: Clean Up**
1. **Terminate Web Server 1**:  
   - Select **Web Server 1** > **Instance State** > **Terminate**.  

---

## **Optional Challenge: Create AMI via CLI**
```bash
aws ec2 create-image \
  --instance-id <INSTANCE_ID> \
  --name "CLI-AMI" \
  --description "AMI created via CLI"
```

---

## **Conclusion**
✅ **Created AMI** for consistent deployments  
✅ **Deployed ALB** for fault-tolerant traffic distribution  
✅ **Configured Auto Scaling** with dynamic policies  
✅ **Verified scaling** under load  

### **Key Takeaways**
🔹 **ALB + Auto Scaling = High Availability**  
🔹 **CloudWatch Alarms** automate scaling decisions.  
🔹 **Private Subnets** enhance security for backend instances.  

🚀 **You’ve built a scalable, self-healing architecture!**  

### **Next Steps**
🔸 **Set up HTTPS** with ACM certificates.  
🔸 **Enable logging** for ALB access logs.  
🔸 **Implement lifecycle hooks** for graceful scaling.