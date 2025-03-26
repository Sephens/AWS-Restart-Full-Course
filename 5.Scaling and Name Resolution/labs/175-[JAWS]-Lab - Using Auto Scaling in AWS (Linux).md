# **Comprehensive Step-by-Step Explanation of the AWS Auto Scaling Lab**

This lab walks you through creating an **Auto Scaling group** with a **load balancer** using the **AWS CLI** and **AWS Management Console**. Below is a detailed breakdown of each step.

---

## **Task 1: Creating a New AMI for Auto Scaling**
### **Objective**:  
- Launch an EC2 instance via AWS CLI.  
- Create an Amazon Machine Image (AMI) from it for Auto Scaling.

---

### **Task 1.1: Connecting to the Command Host Instance**
1. **Access the EC2 Console**  
   - Open AWS Management Console → Search for **EC2** → Select **Instances**.  
   - Locate the **Command Host** instance (pre-provisioned).  

2. **Connect via EC2 Instance Connect**  
   - Select **Command Host** → Click **Connect** → Choose **EC2 Instance Connect** → **Connect**.  
   - A terminal session opens, allowing CLI access.  

**Why?**  
- The **Command Host** is a dedicated EC2 instance where you run AWS CLI commands.  
- It’s preconfigured with necessary permissions.

---

### **Task 1.2: Configuring the AWS CLI**
1. **Check the Current AWS Region**  
   ```bash
   curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region
   ```
   - Output: `"region": "us-west-2"` (or your lab’s region).  

2. **Configure AWS CLI Credentials**  
   ```bash
   aws configure
   ```
   - Press **Enter** for **Access Key** and **Secret Key** (pre-configured in the lab).  
   - Enter the **Region** (e.g., `us-west-2`).  
   - Set output format: `json`.  

3. **Navigate to the Script Directory**  
   ```bash
   cd /home/ec2-user/
   ```
   - Contains `UserData.txt`, which installs a web server on new instances.

**Why?**  
- Ensures AWS CLI commands execute in the correct region.  
- No manual key entry needed (lab handles credentials).

---

### **Task 1.3: Creating a New EC2 Instance**
1. **Review the User Data Script**  
   ```bash
   more UserData.txt
   ```
   - This script:  
     - Updates packages (`yum update`).  
     - Installs **Apache (httpd)** and **PHP**.  
     - Deploys a **CPU stress-test app** (`index.php`).  
     - Cleans up SSH keys and logs for security.  

2. **Get Lab Parameters**  
   - Click **"Details"** → **"Show"** at the top of the lab page.  
   - Note:  
     - `KEYNAME` (SSH key pair, unused here).  
     - `AMIID` (Amazon Linux 2 AMI).  
     - `HTTPACCESS` (Security Group allowing HTTP).  
     - `SUBNETID` (Public subnet for initial instance).  

3. **Launch the Web Server Instance**  
   ```bash
   aws ec2 run-instances --key-name KEYNAME --instance-type t3.micro \
   --image-id AMIID --user-data file:///home/ec2-user/UserData.txt \
   --security-group-ids HTTPACCESS --subnet-id SUBNETID \
   --associate-public-ip-address \
   --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]' \
   --output text --query 'Instances[*].InstanceId'
   ```
   - **Output**: Returns the new instance ID (e.g., `i-0123456789abcdef0`).  

4. **Wait Until Instance is Running**  
   ```bash
   aws ec2 wait instance-running --instance-ids NEW-INSTANCE-ID
   ```

5. **Get the Public DNS Name**  
   ```bash
   aws ec2 describe-instances --instance-id NEW-INSTANCE-ID \
   --query 'Reservations[0].Instances[0].NetworkInterfaces[0].Association.PublicDnsName'
   ```
   - **Output**: `ec2-1-2-3-4.us-west-2.compute.amazonaws.com`.  

6. **Verify the Web Server**  
   - Open a browser and visit:  
     ```
     http://PUBLIC-DNS-ADDRESS/index.php
     ```
   - **Expected**: A webpage with **"Start Stress"** button appears.  
   - **Do not click "Start Stress" yet** (used later for scaling tests).  

**Why?**  
- The instance runs a web server with a CPU stress-test tool.  
- This will be the **baseline AMI** for Auto Scaling.

---

### **Task 1.4: Creating a Custom AMI**
1. **Create an AMI from the Instance**  
   ```bash
   aws ec2 create-image --name WebServerAMI --instance-id NEW-INSTANCE-ID
   ```
   - **Output**: Returns an `ImageId` (e.g., `ami-0123456789abcdef0`).  

2. **AMI Creation Process**  
   - The instance **reboots** temporarily.  
   - AWS takes a **snapshot** of the root volume.  
   - The AMI appears in **EC2 → AMIs** (status: `pending` → `available`).  

**Why?**  
- The AMI contains the **pre-configured web server**.  
- Auto Scaling will use this to launch identical instances.

---

## **Task 2: Creating an Auto Scaling Environment**
### **Objective**:  
- Create a **Load Balancer** to distribute traffic.  
- Define a **Launch Template** (instance blueprint).  
- Set up **Auto Scaling** with dynamic scaling policies.  

---

### **Task 2.1: Creating an Application Load Balancer (Console)**
1. **EC2 → Load Balancers → Create Load Balancer**  
   - Type: **Application Load Balancer (ALB)**.  
   - Name: `WebServerELB`.  
   - Scheme: **Internet-facing**.  

2. **Network Mapping**  
   - VPC: **Lab VPC**.  
   - Availability Zones: **Select both** (e.g., `us-west-2a`, `us-west-2b`).  
   - Subnets: **Public Subnet 1 & 2**.  

3. **Security Group**  
   - Remove default, select **HTTPAccess** (allows HTTP traffic).  

4. **Listener & Routing**  
   - Protocol: **HTTP:80**.  
   - **Create Target Group**:  
     - Name: `webserver-app`.  
     - Health check path: `/index.php`.  
   - Associate target group with ALB.  

5. **Create Load Balancer**  
   - Note the **DNS name** (e.g., `WebServerELB-123456.us-west-2.elb.amazonaws.com`).  

**Why?**  
- ALB distributes traffic across instances in **multiple AZs**.  
- Health checks ensure only healthy instances receive traffic.

---

### **Task 2.2: Creating a Launch Template (Console)**
1. **EC2 → Launch Templates → Create Launch Template**  
   - Name: `web-app-launch-template`.  
   - AMI: **WebServerAMI** (from Task 1.4).  
   - Instance type: **t3.micro**.  
   - Security group: **HTTPAccess**.  
   - No key pair (no SSH access needed).  

2. **Create Template**  
   - This defines the **instance configuration** for Auto Scaling.  

**Why?**  
- Ensures all Auto Scaling instances use the same setup.  
- Avoids manual configuration for each new instance.

---

### **Task 2.3: Creating an Auto Scaling Group (Console)**
1. **From Launch Template → Create Auto Scaling Group**  
   - Name: `Web App Auto Scaling Group`.  

2. **Network Settings**  
   - VPC: **Lab VPC**.  
   - Subnets: **Private Subnet 1 & 2** (for high availability).  

3. **Load Balancing**  
   - Attach to **webserver-app** target group.  
   - Enable **ELB health checks**.  

4. **Group Size & Scaling Policy**  
   - Desired capacity: **2**.  
   - Minimum: **2**.  
   - Maximum: **4**.  
   - Scaling policy:  
     - **Target tracking**: `Average CPU utilization`.  
     - Target value: **50%**.  

5. **Tags**  
   - Key: `Name`, Value: `WebApp` (applies to all instances).  

6. **Create Auto Scaling Group**  
   - Two instances launch automatically in private subnets.  

**Why?**  
- Auto Scaling **maintains 2–4 instances**.  
- If CPU > 50%, it adds instances.  
- If CPU < 50%, it removes instances (but keeps at least 2).

---

## **Task 3: Verifying Auto Scaling**
1. **Check EC2 Instances**  
   - Two instances named **WebApp** appear.  
   - Wait for **Status Checks** to pass (`2/2 checks`).  

2. **Verify Target Group Health**  
   - EC2 → Target Groups → `webserver-app`.  
   - Both instances should show **healthy**.  

3. **Test Load Balancer**  
   - Open the ALB’s **DNS name** in a browser.  
   - The **stress-test webpage** should load.  

**Why?**  
- Confirms load balancer routes traffic correctly.  
- Ensures Auto Scaling instances are operational.

---

## **Task 4: Testing Auto Scaling**
1. **Trigger CPU Load**  
   - On the webpage, click **"Start Stress"**.  
   - This runs a CPU-intensive script (`stress --cpu 1`).  

2. **Monitor Auto Scaling**  
   - EC2 → Auto Scaling Groups → **Activity tab**.  
   - After ~5 minutes:  
     - **New instances launch** (CPU > 50%).  
     - EC2 console shows **3–4 instances**.  

3. **Scaling Down (Optional)**  
   - If you stop the stress test, Auto Scaling **removes extra instances** (but keeps 2).  

**Why?**  
- Proves Auto Scaling **responds to load changes**.  
- Ensures high availability during traffic spikes.

---

## **Conclusion**
### **What You Achieved**  
✅ Created an **EC2 instance** via CLI.  
✅ Built an **AMI** for consistent deployments.  
✅ Set up a **Load Balancer** for traffic distribution.  
✅ Configured **Auto Scaling** to handle variable loads.  
✅ Tested **dynamic scaling** under CPU stress.  

### **Real-World Use Cases**  
- **Web Applications**: Handle traffic spikes.  
- **Microservices**: Scale services independently.  
- **Batch Processing**: Adjust capacity based on workload.  

### **Best Practices**  
✔ Use **multiple Availability Zones** for high availability.  
✔ Set **meaningful scaling policies** (CPU, memory, custom metrics).  
✔ Monitor with **CloudWatch alarms**.  

This lab provides hands-on experience with **scalable AWS architectures**—essential for cloud engineers! 🚀