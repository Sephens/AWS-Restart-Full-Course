# **Lab Guide: Install and Configure the AWS CLI**  

## **Lab Overview**  
This lab teaches you how to:  
✅ **Install the AWS CLI** on a **Red Hat Linux** instance  
✅ **Configure AWS CLI credentials** to connect to an AWS account  
✅ **Interact with AWS IAM** using the CLI  
✅ **Complete a challenge** to retrieve an IAM policy in JSON format  

---

## **Task 1: Connect to the Red Hat Linux Instance**  

### **Step-by-Step Instructions**  
1. **SSH into the Instance:**  
   - Use the provided **SSH key** (`.pem` or `.ppk`).  
   - Example (Linux/macOS):  
     ```bash
     chmod 400 your-key.pem  
     ssh -i your-key.pem ec2-user@<Instance-IP>
     ```
   - *(For Windows, use **PuTTY** with the `.ppk` key.)*  

---

## **Task 2: Install the AWS CLI**  

### **Step-by-Step Instructions**  
1. **Download AWS CLI:**  
   ```bash
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   ```

2. **Unzip the Installer:**  
   ```bash
   unzip -u awscliv2.zip
   ```

3. **Run the Installer:**  
   ```bash
   sudo ./aws/install
   ```

4. **Verify Installation:**  
   ```bash
   aws --version
   ```
   - Expected output:  
     ```plain
     aws-cli/2.7.24 Python/3.8.8 Linux/4.14.133-113.105.amzn2.x86_64 botocore/2.4.5
     ```

5. **Test AWS CLI Help:**  
   ```bash
   aws help
   ```
   - Press `q` to exit.  

---

## **Task 3: Observe IAM in AWS Console**  

### **Step-by-Step Instructions**  
1. **Go to IAM Console:**  
   - In AWS Console, search for **IAM**.  

2. **View `awsstudent` User:**  
   - Navigate to **Users** > **awsstudent**.  
   - Under **Permissions**, click **lab_policy** > **{} JSON** to see the policy.  

3. **Note Access Keys:**  
   - Go to **Security credentials** tab.  
   - Find the **Access key ID** (needed for CLI setup).  

---

## **Task 4: Configure AWS CLI Credentials**  

### **Step-by-Step Instructions**  
1. **Run `aws configure`:**  
   ```bash
   aws configure
   ```
2. **Enter Credentials:**  
   - **AWS Access Key ID:** *(From **Details** dropdown)*  
   - **AWS Secret Access Key:** *(From **Details** dropdown)*  
   - **Default region name:** `us-west-2`  
   - **Default output format:** `json`  

---

## **Task 5: Test IAM Access via CLI**  

### **Step-by-Step Instructions**  
1. **List IAM Users:**  
   ```bash
   aws iam list-users
   ```
   - Expected: JSON list of IAM users.  

---

## **Challenge Activity: Retrieve IAM Policy in JSON**  

### **Objective**  
Use the **AWS CLI** to:  
1. **List all IAM policies** (filter for `lab_policy`).  
2. **Download the policy in JSON format**.  

### **Solution**  

1. **List All Local Policies:**  
   ```bash
   aws iam list-policies --scope Local
   ```
   - Find `lab_policy` ARN (e.g., `arn:aws:iam::123456789012:policy/lab_policy`).  

2. **Get Policy Version (JSON):**  
   ```bash
   aws iam get-policy-version \
     --policy-arn arn:aws:iam::123456789012:policy/lab_policy \
     --version-id v1 > lab_policy.json
   ```
   - *(Replace `arn` and `version-id` with your values.)*  

3. **Verify File:**  
   ```bash
   cat lab_policy.json
   ```

---

## **Conclusion**  
✅ **Installed AWS CLI** on Red Hat Linux  
✅ **Configured AWS credentials**  
✅ **Accessed IAM via CLI**  
✅ **Retrieved IAM policy in JSON**  

### **Key Takeaways**  
🔹 **AWS CLI allows programmatic AWS control** (alternative to Console).  
🔹 **IAM policies define permissions** (JSON format).  
🔹 **Access keys authenticate CLI sessions**.  

🚀 **You’re now ready to automate AWS tasks using the CLI!**