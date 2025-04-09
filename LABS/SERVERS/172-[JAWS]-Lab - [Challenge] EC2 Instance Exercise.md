# **Challenge Lab Guide: Deploying a Web Server on Amazon EC2**

## **Lab Overview**
In this challenge, you'll create a **web server** on an **Amazon Linux EC2 instance** by:
✅ **Creating a VPC, subnet, and internet gateway**  
✅ **Launching an EC2 instance with user data** (auto-installs Apache)  
✅ **Deploying a custom HTML page**  
✅ **Testing connectivity**  

---

## **Step 1: Create a VPC & Subnet**
1. **Go to VPC Console**:  
   - Search for **VPC** in AWS Console.  
   - Click **Create VPC**.  
   - Configure:  
     - **Name**: `Challenge-VPC`  
     - **IPv4 CIDR**: `10.0.0.0/16`  
     - Click **Create VPC**.  

2. **Create a Public Subnet**:  
   - In **VPC Console** > **Subnets**, click **Create subnet**.  
   - Configure:  
     - **VPC**: `Challenge-VPC`  
     - **Name**: `Public-Subnet`  
     - **Availability Zone**: Pick any (e.g., `us-west-2a`)  
     - **IPv4 CIDR**: `10.0.1.0/24`  
     - Click **Create subnet**.  

3. **Attach an Internet Gateway**:  
   - In **VPC Console** > **Internet Gateways**, click **Create internet gateway**.  
   - Name: `Challenge-IGW` > **Create**.  
   - Select it > **Actions** > **Attach to VPC** > Choose `Challenge-VPC`.  

4. **Configure Route Table**:  
   - Go to **Route Tables** > Find the one for `Challenge-VPC`.  
   - Click **Edit routes** > **Add route**:  
     - **Destination**: `0.0.0.0/0`  
     - **Target**: `Challenge-IGW`  
   - Click **Save changes**.  

---

## **Step 2: Launch the EC2 Instance**
1. **Go to EC2 Console** > **Launch Instance**:  
   - **Name**: `Web-Server`  
   - **AMI**: **Amazon Linux 2023** (or Amazon Linux 2)  
   - **Instance type**: `t3.micro`  
   - **Key pair**: *Create new* (e.g., `web-key`)  

2. **Network Settings**:  
   - **VPC**: `Challenge-VPC`  
   - **Subnet**: `Public-Subnet`  
   - **Auto-assign public IP**: `Enable`  
   - **Security group**:  
     - **Name**: `Web-SG`  
     - **Rules**:  
       - **SSH (Port 22)** – From `My IP`  
       - **HTTP (Port 80)** – From `Anywhere (0.0.0.0/0)`  

3. **Configure Storage**:  
   - **Root volume**: `8 GiB` (gp2)  

4. **User Data (Auto-installs Apache)**:  
   ```bash
   #!/bin/bash
   sudo yum install httpd -y
   sudo systemctl start httpd
   sudo systemctl enable httpd
   sudo chmod 777 /var/www/html
   ```

5. **Launch Instance** > **View Instances**.  

---

## **Step 3: Verify HTTPD Installation**
1. **Check System Log**:  
   - Select instance > **Actions** > **Monitor and troubleshoot** > **Get system log**.  
   - **Screenshot**: Look for `httpd` installation success.  

---

## **Step 4: Deploy the Web Page**
1. **Connect via EC2 Instance Connect**:  
   - Select instance > **Connect** > **EC2 Instance Connect** > **Connect**.  

2. **Create HTML File**:  
   ```bash
   sudo vi /var/www/html/projects.html
   ```
   - Paste:  
     ```html
     <!DOCTYPE html>
     <html>
     <body>
     <h1>YOUR-NAME's re/Start Project Work</h1>
     <p>EC2 Instance Challenge Lab</p>
     </body>
     </html>
     ```
   - Replace `YOUR-NAME` with your name.  
   - Save (`Esc` > `:wq` > `Enter`).  

3. **Fix Permissions**:  
   ```bash
   sudo chmod 644 /var/www/html/projects.html
   ```

---

## **Step 5: Test the Web Server**
1. **Get Public IP**:  
   - In **EC2 Console**, copy the instance’s **Public IPv4 address**.  

2. **Open Browser**:  
   - Navigate to:  
     ```
     http://<PUBLIC_IP>/projects.html
     ```
   - **Screenshot**: Show the displayed page.  

---

## **Submission**
Submit:  
1. **System log screenshot** (showing `httpd` installed).  
2. **Browser screenshot** (showing your HTML page).  

---

## **Troubleshooting**
❌ **Can’t connect via SSH?**  
   - Check **Security Group** allows **Port 22** from your IP.  

❌ **Web page not loading?**  
   - Verify **Security Group** allows **Port 80** (`0.0.0.0/0`).  
   - Check `httpd` is running:  
     ```bash
     sudo systemctl status httpd
     ```

---

## **Key Takeaways**
🔹 **VPC + Internet Gateway = Public Access**  
🔹 **User Data automates setup** (e.g., install Apache).  
🔹 **Security Groups act as firewalls**.  

🚀 **You’ve built a scalable web server on AWS!**  

### **Next Steps**
🔸 **Add a domain** (Route 53 + ACM).  
🔸 **Scale horizontally** with Auto Scaling.  
🔸 **Monitor logs** with CloudWatch.