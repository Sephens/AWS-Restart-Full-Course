# **Systems Hardening with Patch Manager via AWS Systems Manager**  
### **Comprehensive Lab Walkthrough with Detailed Explanations**  

---

## **Lab Overview**  
This lab demonstrates how to automate **patch management** for EC2 instances (both Linux and Windows) using **AWS Systems Manager Patch Manager**.  

### **Key Objectives:**  
1. **Patch Linux instances** using default baselines.  
2. **Create a custom patch baseline** for Windows instances.  
3. **Tag and patch Windows instances** using patch groups.  
4. **Verify patch compliance** across all instances.  

---

## **Lab Environment**  
The lab includes:  
- **3 Linux EC2 instances** (Amazon Linux 2)  
- **3 Windows EC2 instances** (Windows Server 2019)  
- **Pre-configured IAM roles** allowing Systems Manager to manage instances.  

---

## **Task 1: Patch Linux Instances Using Default Baselines**  

### **Step-by-Step Instructions:**  
1. **Access AWS Systems Manager**  
   - Open the **AWS Management Console**.  
   - Search for **Systems Manager** and select it.  

2. **View Managed Instances in Fleet Manager**  
   - Under **Node Management**, select **Fleet Manager**.  
   - Observe the **3 Linux** and **3 Windows** instances.  
   - Select **Linux-1** → **Node actions** → **View details** to verify its configuration.  

3. **Initiate Patching for Linux Instances**  
   - Navigate to **Patch Manager** under **Node Management**.  
   - Click **Patch now**.  
   - Configure patching settings:  
     - **Patching operation:** `Scan and install`  
     - **Reboot option:** `Reboot if needed`  
     - **Target selection:** `Specify instance tags`  
       - **Tag key:** `Patch Group`  
       - **Tag value:** `LinuxProd`  
   - Click **Patch now**.  

4. **Monitor Patch Status**  
   - A new page shows the patching progress.  
   - Wait until all **3 Linux instances** show **successful completion**.  

### **Explanation:**  
- **Default Patch Baselines:** AWS provides predefined baselines for supported OS types.  
- **Scan & Install:** First scans for missing patches, then installs them.  
- **Reboot Handling:** Ensures patches requiring a reboot are applied correctly.  
- **Tag-Based Targeting:** Uses tags (`Patch Group: LinuxProd`) to select instances.  

---

## **Task 2: Create a Custom Patch Baseline for Windows Instances**  

### **Step-by-Step Instructions:**  
1. **Navigate to Patch Manager**  
   - In **Systems Manager**, go to **Patch Manager** → **Patch baselines**.  

2. **Create a New Patch Baseline**  
   - Click **Create patch baseline**.  
   - Configure:  
     - **Name:** `WindowsServerSecurityUpdates`  
     - **Description:** `Windows security baseline patch`  
     - **Operating system:** `Windows`  
     - **Uncheck** `Default patch baseline`.  

3. **Define Approval Rules**  
   - **Rule 1 (Critical Security Updates):**  
     - **Products:** `WindowsServer2019`  
     - **Classification:** `SecurityUpdates`  
     - **Severity:** `Critical`  
     - **Auto-approval delay:** `3 days`  
     - **Compliance reporting:** `Critical`  
   - **Rule 2 (Important Security Updates):**  
     - Same as above, but set **Severity:** `Important` and **Compliance reporting:** `High`.  
   - Click **Create patch baseline**.  

4. **Associate Patch Group**  
   - Select the new baseline → **Actions** → **Modify patch groups**.  
   - Add patch group: **`WindowsProd`** → **Add** → **Close**.  

### **Explanation:**  
- **Custom Baselines:** Allow granular control over which patches are approved.  
- **Auto-Approval Rules:** Automatically approve patches after a delay (e.g., 3 days for testing).  
- **Patch Groups:** Logical groupings to apply different baselines (e.g., `WindowsProd` for production servers).  

---

## **Task 3: Patch Windows Instances Using Patch Groups**  

### **Step 3.1: Tag Windows Instances**  
1. **Open EC2 Console**  
   - Search for **EC2** → **Instances**.  
2. **Tag Each Windows Instance**  
   - Select **Windows-1** → **Tags** → **Manage tags**.  
   - Add tag:  
     - **Key:** `Patch Group`  
     - **Value:** `WindowsProd`  
   - Repeat for **Windows-2** and **Windows-3**.  

### **Step 3.2: Initiate Patching**  
1. **Return to Patch Manager**  
   - Click **Patch now**.  
2. **Configure Patching Settings**  
   - **Patching operation:** `Scan and install`  
   - **Reboot option:** `Reboot if needed`  
   - **Target selection:** `Specify instance tags`  
     - **Tag key:** `Patch Group`  
     - **Tag value:** `WindowsProd`  
   - Click **Patch now**.  

3. **Monitor Patch Execution**  
   - Click the **Execution ID** to view progress.  
   - Under **Run Command**, check **Output** for details.  

### **Explanation:**  
- **Tag-Based Patching:** Ensures only instances with `Patch Group: WindowsProd` are patched.  
- **Patch Manager Uses Run Command:** Executes `AWS-RunPatchBaseline` document to apply patches.  

---

## **Task 4: Verify Patch Compliance**  

### **Step-by-Step Instructions:**  
1. **Check Compliance Summary**  
   - In **Patch Manager**, go to **Dashboard**.  
   - Verify **Compliant: 6** (all instances patched).  

2. **Review Compliance Details**  
   - Navigate to **Compliance reporting**.  
   - Confirm all instances show **Compliant**.  
   - Check:  
     - **Critical noncompliant count** (should be `0`).  
     - **Security noncompliant count** (should be `0`).  

3. **Inspect Individual Nodes**  
   - Click a **Windows instance ID** → **Patch tab**.  
   - View installed patches and timestamps.  

### **Explanation:**  
- **Compliance Reporting:** Shows which instances meet the patch baseline.  
- **Noncompliant Counts:** Indicates missing critical/security patches.  

---

## **Conclusion**  
### **Key Achievements:**  
✅ **Patched Linux instances** using default baselines.  
✅ **Created a custom baseline** for Windows security updates.  
✅ **Tagged and patched Windows instances** using patch groups.  
✅ **Verified compliance** across all instances.  

### **Best Practices:**  
- **Regular Patching:** Schedule maintenance windows for automated patching.  
- **Test Patches:** Use staging environments before production deployment.  
- **Monitor Compliance:** Set up AWS Config rules for continuous compliance checks.  

This lab demonstrates how **AWS Systems Manager Patch Manager** simplifies OS and application patching at scale while maintaining security compliance. 🚀