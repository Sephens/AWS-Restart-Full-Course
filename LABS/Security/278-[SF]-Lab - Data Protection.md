# **Data Protection Using Encryption**  
### **Comprehensive Lab Walkthrough with Detailed Explanations**  

---

## **Lab Overview**  
This lab demonstrates how to use **AWS Key Management Service (KMS)** and the **AWS Encryption CLI** to encrypt and decrypt sensitive data stored on an EC2 instance.  

### **Key Objectives:**  
1. **Create a KMS encryption key** for symmetric encryption.  
2. **Configure an EC2 file server** with AWS Encryption CLI.  
3. **Encrypt plaintext files** into ciphertext.  
4. **Decrypt ciphertext files** back to readable plaintext.  

---

## **Lab Environment**  
- **EC2 Instance:** `File Server` (pre-configured Linux instance).  
- **IAM Role:** `voclabs` (pre-configured with KMS permissions).  

---

## **Task 1: Create an AWS KMS Key**  

### **Step-by-Step Instructions:**  
1. **Open AWS KMS Console**  
   - Search for **KMS** in AWS Console → Select **Key Management Service**.  

2. **Create a Symmetric Key**  
   - Click **Create a key**.  
   - Select **Symmetric** (same key for encryption/decryption).  
   - Click **Next**.  

3. **Configure Key Details**  
   - **Alias:** `MyKMSKey`  
   - **Description:** `Key used to encrypt and decrypt data files`  
   - Click **Next**.  

4. **Set Key Permissions**  
   - **Key Administrators:** Select `voclabs` (IAM role).  
   - **Key Users:** Select `voclabs`.  
   - Click **Next** → **Finish**.  

5. **Copy Key ARN**  
   - Open `MyKMSKey` → Copy the **ARN** (e.g., `arn:aws:kms:us-east-1:123456789012:key/abcd1234-...`).  

### **Explanation:**  
- **Symmetric Encryption:** Uses **one key** for both encryption and decryption (faster than asymmetric).  
- **Key ARN:** Unique identifier for the KMS key (required for CLI operations).  
- **IAM Permissions:**  
  - **Key Administrators:** Can manage key policies.  
  - **Key Users:** Can encrypt/decrypt data.  

---

## **Task 2: Configure the File Server Instance**  

### **Step-by-Step Instructions:**  
1. **Connect to EC2 Instance**  
   - Search for **EC2** → Select **Instances** → Choose `File Server`.  
   - Click **Connect** → **Session Manager** → **Connect**.  

2. **Configure AWS Credentials**  
   - Run:  
     ```bash
     cd ~
     aws configure
     ```  
   - Enter temporary values (press Enter for defaults):  
     ```plaintext
     AWS Access Key ID: 1  
     AWS Secret Access Key: 1  
     Default region: [Paste from Vocareum AWS Details]  
     Default output format: [Leave blank]  
     ```  

3. **Update Credentials File**  
   - From **Vocareum AWS Details**, copy the `[default]` block.  
   - Run:  
     ```bash
     vi ~/.aws/credentials
     ```  
   - Delete existing content (`dd`), paste new credentials, save (`:wq`).  

4. **Install AWS Encryption CLI**  
   - Run:  
     ```bash
     pip3 install aws-encryption-sdk-cli
     export PATH=$PATH:/home/ssm-user/.local/bin
     ```  

### **Explanation:**  
- **AWS Credentials:** Grants the instance permission to use KMS.  
- **Encryption CLI:** Python-based tool for encrypting/decrypting files using KMS.  

---

## **Task 3: Encrypt and Decrypt Data**  

### **Step 1: Create Test Files**  
- Run:  
  ```bash
  touch secret1.txt secret2.txt secret3.txt
  echo 'TOP SECRET 1!!!' > secret1.txt
  cat secret1.txt  # Verify content
  mkdir output
  ```  

### **Step 2: Encrypt a File**  
1. **Set Key ARN Variable**  
   - Run (replace `[KMS ARN]` with your key ARN):  
     ```bash
     keyArn="[KMS ARN]"
     ```  

2. **Encrypt `secret1.txt`**  
   - Run:  
     ```bash
     aws-encryption-cli --encrypt \
                        --input secret1.txt \
                        --wrapping-keys key=$keyArn \
                        --metadata-output ~/metadata \
                        --encryption-context purpose=test \
                        --commitment-policy require-encrypt-require-decrypt \
                        --output ~/output/.
     ```  
   - Verify success:  
     ```bash
     echo $?  # Should return 0
     ls output  # Should show secret1.txt.encrypted
     cat output/secret1.txt.encrypted  # Shows garbled ciphertext
     ```  

### **Step 3: Decrypt the File**  
- Run:  
  ```bash
  cd output
  aws-encryption-cli --decrypt \
                     --input secret1.txt.encrypted \
                     --wrapping-keys key=$keyArn \
                     --commitment-policy require-encrypt-require-decrypt \
                     --encryption-context purpose=test \
                     --metadata-output ~/metadata \
                     --max-encrypted-data-keys 1 \
                     --buffer \
                     --output .
  ```  
- Verify decryption:  
  ```bash
  ls  # Shows secret1.txt.encrypted.decrypted
  cat secret1.txt.encrypted.decrypted  # Shows original plaintext
  ```  

### **Explanation:**  
| **Term**               | **Description**                                                                 |
|-------------------------|-------------------------------------------------------------------------------|
| **Plaintext**           | Original readable data (e.g., `TOP SECRET 1!!!`).                             |
| **Ciphertext**          | Encrypted unreadable data (garbled text).                                     |
| **Encryption Context**  | Key-value pair (`purpose=test`) for audit trails.                             |
| **Commitment Policy**   | Ensures the same key must be used for decryption (`require-encrypt-require-decrypt`). |

---

## **Conclusion**  
### **Key Achievements:**  
✅ **Created a KMS key** for symmetric encryption.  
✅ **Configured AWS Encryption CLI** on an EC2 instance.  
✅ **Encrypted plaintext** into ciphertext.  
✅ **Decrypted ciphertext** back to plaintext.  

### **Best Practices:**  
- **Use KMS Key Policies:** Restrict key usage to specific IAM roles.  
- **Enable Encryption Context:** Adds metadata for auditing.  
- **Rotate Keys Periodically:** Enhances security against breaches.  

This lab demonstrates how AWS KMS and the Encryption CLI provide **end-to-end data protection** for sensitive files. 🔒