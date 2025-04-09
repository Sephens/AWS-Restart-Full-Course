# **Lab Guide: Using AWS Systems Manager**  

## **Lab Overview**  
This lab demonstrates how to use **AWS Systems Manager (SSM)** to:  
✅ **Inventory EC2 instances** (track software & configurations)  
✅ **Install apps using Run Command** (no SSH required)  
✅ **Manage app settings with Parameter Store** (secure configuration storage)  
✅ **Securely access instances with Session Manager** (no SSH keys needed)  

---

## **Task 1: Set Up Inventory for an EC2 Instance**  

### **Objective**  
Use **Systems Manager Inventory** to track installed software on an EC2 instance.  

### **Step-by-Step Instructions**  

1. **Go to AWS Systems Manager:**  
   - Navigate to **AWS Console** > **Systems Manager**.  

2. **Configure Inventory:**  
   - Under **Node Management**, select **Fleet Manager**.  
   - Choose your **Managed Instance** (EC2 instance with SSM Agent).  
   - Click **Setup Inventory**.  
   - Leave defaults and click **Setup Inventory**.  

3. **View Inventory Data:**  
   - Click the **Node ID** link.  
   - Go to the **Inventory** tab.  
   - Review installed applications (e.g., `Amazon SSM Agent`, `AWS CLI`).  

### **Key Notes**  
🔹 **No SSH needed** – Inventory collects data automatically.  
🔹 **Useful for audits** – Track software versions across instances.  

---

## **Task 2: Install a Web App Using Run Command**  

### **Objective**  
Deploy a **Widget Manufacturing Dashboard** app using **Run Command**.  

### **Step-by-Step Instructions**  

1. **Run Command:**  
   - Go to **Node Management** > **Run Command**.  
   - Search for **"Install Dashboard App"** (Owned by AWS).  
   - Select the document.  

2. **Target the Instance:**  
   - Under **Target selection**, choose **"Choose instances manually"**.  
   - Select your **Managed Instance**.  

3. **Execute the Command:**  
   - Click **Run**.  
   - Wait 1-2 mins for status to change to **Success**.  

4. **Verify the App:**  
   - Copy the instance’s **Public IP** from **AWS Details**.  
   - Open a browser and paste the IP.  
   - The **Widget Manufacturing Dashboard** should appear.  

### **Why This Matters**  
🔹 **Automates deployments** – No manual SSH or scripts.  
🔹 **Scales to multiple instances** – Run commands fleet-wide.  

---

## **Task 3: Manage App Settings with Parameter Store**  

### **Objective**  
Use **Parameter Store** to toggle a **beta feature** in the dashboard.  

### **Step-by-Step Instructions**  

1. **Create a Parameter:**  
   - Go to **Application Management** > **Parameter Store**.  
   - Click **Create parameter**.  
   - Configure:  
     - **Name:** `/dashboard/show-beta-features`  
     - **Description:** `Display beta features`  
     - **Value:** `True`  
   - Click **Create parameter**.  

2. **Verify the Change:**  
   - Refresh the **Widget Dashboard** browser tab.  
   - A **third chart** (beta feature) now appears.  

3. **(Optional) Disable the Feature:**  
   - Delete the parameter.  
   - Refresh the dashboard – the beta chart disappears.  

### **Key Notes**  
🔹 **Secure storage** – Encrypt sensitive data (e.g., passwords).  
🔹 **Hierarchical structure** – Organize parameters (e.g., `/app/dev/db-url`).  

---

## **Task 4: Access Instances Securely with Session Manager**  

### **Objective**  
Connect to the EC2 instance **without SSH** using **Session Manager**.  

### **Step-by-Step Instructions**  

1. **Start a Session:**  
   - Go to **Node Management** > **Session Manager**.  
   - Click **Start session**.  
   - Select your **Managed Instance**.  
   - Click **Start session**.  

2. **Run Commands in the Browser Shell:**  
   - List web app files:  
     ```bash
     ls /var/www/html
     ```  
   - Fetch EC2 metadata:  
     ```bash
     AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
     export AWS_DEFAULT_REGION=${AZ::-1}
     aws ec2 describe-instances
     ```  

### **Why This Matters**  
🔹 **No SSH keys or open ports** – Reduces attack surface.  
🔹 **Audit logs** – All sessions are logged in **CloudTrail**.  

---

## **Conclusion**  
✅ **Tracked software with Inventory**  
✅ **Deployed an app using Run Command**  
✅ **Toggled features via Parameter Store**  
✅ **Accessed instances securely with Session Manager**  

### **Key Takeaways**  
🔹 **Systems Manager automates ops tasks** (no manual SSH).  
🔹 **Parameter Store centralizes configurations** (e.g., feature flags).  
🔹 **Session Manager improves security** (no bastion hosts needed).  

🚀 **You’re now ready to manage AWS resources at scale with Systems Manager!**  

### **Next Steps**  
🔸 **Automate patching** with **Maintenance Windows**.  
🔸 **Create custom SSM Documents** for repeatable tasks.  
🔸 **Restrict Session Manager access** using IAM policies.