# **Amazon Route 53 Failover Routing - Comprehensive Lab Guide**

## **Lab Overview**
This lab demonstrates **high-availability DNS failover** using **Amazon Route 53**. You will:
1. **Configure health checks** to monitor a primary web server.
2. **Set up failover routing** to automatically switch traffic to a secondary server if the primary fails.
3. **Test the failover mechanism** by manually stopping the primary instance.

### **Key Concepts**
- **Route 53 Health Checks**: Monitor endpoint availability.
- **Failover Routing Policy**: Automatically redirects traffic if the primary fails.
- **SNS Alerts**: Notifies you via email when a failure occurs.

---

## **Task 1: Confirming the Café Websites**
### **Objective**:  
Verify that two EC2 instances (`CafeInstance1` and `CafeInstance2`) are running in different **Availability Zones (AZs)** with identical café websites.

### **Steps**:
1. **Retrieve Instance Details**  
   - Click **Details** → **Show** at the top of the lab page.  
   - Copy:  
     - `CafeInstance1IPAddress` (Primary)  
     - `CafeInstance2IPAddress` (Secondary)  
     - `PrimaryWebSiteURL`  
     - `SecondaryWebsiteURL`  

2. **Check EC2 Instances**  
   - Open **EC2 Console** → **Instances**.  
   - Verify:  
     - `CafeInstance1` → `Cafe Public Subnet 1 (us-west-2a)`  
     - `CafeInstance2` → `Cafe Public Subnet 2 (us-west-2b)`  

3. **Test Both Websites**  
   - Open `PrimaryWebSiteURL` in a browser.  
     - Note the **Server Information** (AZ: `us-west-2a`).  
   - Open `SecondaryWebsiteURL`.  
     - Confirms same content but different AZ (`us-west-2b`).  

4. **Place a Test Order**  
   - Click **Menu** → **Submit Order**.  
   - Verify the **Order Confirmation** page shows the correct time zone.  

### **Why?**  
- Confirms both instances are **operational** and **identical**.  
- Ensures **high availability** across AZs.  

---

## **Task 2: Configuring a Route 53 Health Check**
### **Objective**:  
Create a **health check** for `CafeInstance1` that:  
- Monitors `/cafe` endpoint every **10 seconds**.  
- Triggers an **email alert** if the site fails.  

### **Steps**:
1. **Open Route 53 Console** → **Health Checks** → **Create Health Check**.  
2. **Configure Health Check**:  
   - **Name**: `Primary-Website-Health`  
   - **Endpoint Monitoring**:  
     - **IP Address**: `CafeInstance1IPAddress`  
     - **Path**: `/cafe`  
   - **Advanced Settings**:  
     - **Request Interval**: `Fast (10 sec)`  
     - **Failure Threshold**: `2` (fails after 2 consecutive checks).  
3. **Set Up Alerts**:  
   - **Create Alarm**: `Yes`  
   - **SNS Topic**: `Primary-Website-Health`  
   - **Email**: Enter your address.  
4. **Create Health Check**.  

5. **Verify Health Status**  
   - Wait ~1 minute → Refresh → Status should show **Healthy**.  
   - Check **Monitoring Tab** for health history.  

6. **Confirm Email Subscription**  
   - AWS sends a **confirmation email**.  
   - Click **Confirm subscription**.  

### **Why?**  
- Ensures **immediate detection** of failures.  
- **Fast (10 sec) checks** minimize downtime.  
- **Email alerts** notify admins of issues.  

---

## **Task 3: Configuring Route 53 Failover Records**
### **Objective**:  
Set up **DNS failover** so that if `CafeInstance1` fails, traffic automatically shifts to `CafeInstance2`.  

### **Task 3.1: Create Primary A Record**
1. **Route 53 Console** → **Hosted Zones** → Select your domain (`XXXXXX.vocareum.training`).  
2. **Create Record**:  
   - **Record Name**: `www`  
   - **Record Type**: `A (IPv4)`  
   - **Value**: `CafeInstance1IPAddress`  
   - **TTL**: `15 sec` (low TTL for faster failover).  
   - **Routing Policy**: `Failover`  
   - **Failover Type**: `Primary`  
   - **Health Check**: `Primary-Website-Health`  
   - **Record ID**: `FailoverPrimary`  
3. **Create Record**.  

### **Task 3.2: Create Secondary A Record**
1. **Create Another Record**:  
   - **Record Name**: `www`  
   - **Record Type**: `A (IPv4)`  
   - **Value**: `CafeInstance2IPAddress`  
   - **TTL**: `15 sec`  
   - **Routing Policy**: `Failover`  
   - **Failover Type**: `Secondary`  
   - **Health Check**: `None` (secondary doesn’t need monitoring).  
   - **Record ID**: `FailoverSecondary`  
2. **Create Record**.  

### **Why?**  
- **Primary Record**: Routes traffic to `CafeInstance1` if healthy.  
- **Secondary Record**: Acts as backup if primary fails.  
- **Low TTL (15 sec)**: Ensures quick DNS updates.  

---

## **Task 4: Verifying DNS Resolution**
### **Objective**:  
Confirm that `www.XXXXXX.vocareum.training/cafe` resolves to the **primary instance**.  

### **Steps**:
1. **Copy Record Name** from Route 53 (e.g., `www.XXXXXX.vocareum.training`).  
2. **Open Browser** → Enter:  
   ```
   http://www.XXXXXX.vocareum.training/cafe/
   ```
3. **Verify**:  
   - Page loads successfully.  
   - **Server Information** shows `us-west-2a` (primary AZ).  

### **Why?**  
- Confirms **DNS is correctly routing** to the primary instance.  

---

## **Task 5: Testing Failover Functionality**
### **Objective**:  
Simulate a failure by **stopping `CafeInstance1`** and verify traffic fails over to `CafeInstance2`.  

### **Steps**:
1. **Stop Primary Instance**:  
   - **EC2 Console** → **Instances** → Select `CafeInstance1`.  
   - **Instance State** → **Stop Instance** → Confirm.  

2. **Monitor Health Check**:  
   - **Route 53** → **Health Checks** → `Primary-Website-Health`.  
   - **Status** changes to **Unhealthy** (~2-5 mins).  

3. **Check Email Alert**:  
   - AWS sends an **SNS notification** (subject: *"ALARM: Primary-Website-Health"*).  

4. **Verify DNS Failover**:  
   - **Refresh** the café website.  
   - **Server Information** now shows `us-west-2b` (secondary AZ).  

### **Why?**  
- **Proves failover works**:  
  - Health check detects failure.  
  - Route 53 updates DNS to secondary IP.  
  - Users automatically redirected with **minimal downtime**.  

---

## **Conclusion**
### **What You Achieved**  
✅ **Configured Route 53 Health Checks** for real-time monitoring.  
✅ **Set Up Failover Routing** for automatic traffic redirection.  
✅ **Tested Failover** by simulating a primary instance failure.  
✅ **Verified Email Alerts** for outage notifications.  

### **Real-World Applications**  
- **Disaster Recovery**: Automatically switch to backup servers.  
- **Zero-Downtime Deployments**: Redirect traffic during maintenance.  
- **Multi-Region HA**: Extend failover across AWS regions.  

### **Best Practices**  
✔ **Use Fast Health Checks** (10 sec) for critical apps.  
✔ **Set Low TTLs** (15-30 sec) for quick DNS updates.  
✔ **Monitor Alerts** to respond to failures quickly.  

This lab demonstrates **enterprise-grade DNS failover**—essential for **high-availability architectures**! 🚀