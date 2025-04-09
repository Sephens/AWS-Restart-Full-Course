# **Lab Guide: Amazon Route 53 Failover Routing**

## **Lab Overview**
This lab teaches you to configure **failover routing** for high availability:
✅ **Set up Route 53 health checks** with email alerts  
✅ **Configure primary/secondary DNS records**  
✅ **Test automatic failover** when the primary server fails  

---

## **Task 1: Verify Café Websites**
1. **Copy Instance Details**:  
   - From **AWS Details**, note:  
     - `CafeInstance1IPAddress` (Primary)  
     - `CafeInstance2IPAddress` (Secondary)  
     - `PrimaryWebSiteURL` & `SecondaryWebsiteURL`  

2. **Test Both Instances**:  
   - Open both URLs in browser tabs.  
   - Confirm **Server Information** shows different AZs (e.g., `us-west-2a` vs `us-west-2b`).  
   - Place test orders to verify functionality.  

**Key Notes**:  
🔹 Both instances run identical LAMP stacks in **different AZs** for redundancy.  

---

## **Task 2: Configure Health Check**
1. **Go to Route 53 Console** > **Health Checks** > **Create**.  
2. **Configure**:  
   - **Name**: `Primary-Website-Health`  
   - **Endpoint**: IP address (`CafeInstance1IPAddress`)  
   - **Path**: `/cafe`  
   - **Advanced**:  
     - **Request Interval**: `Fast (10 seconds)`  
     - **Failure Threshold**: `2`  
3. **Set Up Alerts**:  
   - **Create SNS Topic**: `Primary-Website-Health`  
   - **Email**: Your address (check inbox to **confirm subscription**).  
4. **Verify**:  
   - Status changes to **Healthy** (~1 minute).  
   - Monitor under **Monitoring tab**.  

**Why This Matters**:  
🔹 Health checks **trigger failover** when primary fails.  

---

## **Task 3: Configure Failover Records**
### **3.1 Primary A Record**
1. **Go to Hosted Zones** > Select your domain.  
2. **Create Record**:  
   - **Name**: `www`  
   - **Type**: `A` (IPv4)  
   - **Value**: `CafeInstance1IPAddress`  
   - **TTL**: `15`  
   - **Routing Policy**: `Failover` (Primary)  
   - **Health Check**: `Primary-Website-Health`  
   - **Record ID**: `FailoverPrimary`  

### **3.2 Secondary A Record**
1. **Create Record**:  
   - **Name**: `www`  
   - **Type**: `A`  
   - **Value**: `CafeInstance2IPAddress`  
   - **TTL**: `15`  
   - **Routing Policy**: `Failover` (Secondary)  
   - **Record ID**: `FailoverSecondary`  

**Key Notes**:  
📌 **Primary record** links to health check.  
📌 **Secondary record** activates automatically if primary fails.  

---

## **Task 4: Verify DNS Resolution**
1. **Copy Record Name**: From hosted zone (e.g., `www.XXXXXX.vocareum.training`).  
2. **Open in Browser**:  
   ```http
   http://www.XXXXXX.vocareum.training/cafe/
   ```
   - Verify **Server Information** shows primary AZ (e.g., `us-west-2a`).  

---

## **Task 5: Test Failover**
1. **Simulate Failure**:  
   - Go to **EC2 Console** > **Instances** > Select `CafeInstance1` > **Stop Instance**.  
2. **Monitor Health Check**:  
   - In Route 53, refresh **Health Checks** until status changes to **Unhealthy** (~2-5 mins).  
3. **Check Email**: AWS SNS alert arrives.  
4. **Verify Failover**:  
   - Refresh browser tab with your domain.  
   - **Server Information** now shows secondary AZ (e.g., `us-west-2b`).  

**Troubleshooting**:  
❌ **No Failover?**  
   - Wait 5+ mins for DNS propagation.  
   - Confirm health check is **Unhealthy**.  

---

## **Conclusion**
✅ **Configured health checks** with email alerts  
✅ **Set up failover routing** between AZs  
✅ **Verified automatic failover**  

### **Key Takeaways**
🔹 **Route 53 health checks** monitor endpoint availability.  
🔹 **Failover routing** ensures high availability.  
🔹 **SNS alerts** notify of failures.  

🚀 **Your web app now survives AZ outages automatically!**  

### **Next Steps**
🔸 **Set up weighted routing** for A/B testing.  
🔸 **Enable HTTPS** with ACM certificates.  
🔸 **Monitor DNS latency** with Route 53 latency records.