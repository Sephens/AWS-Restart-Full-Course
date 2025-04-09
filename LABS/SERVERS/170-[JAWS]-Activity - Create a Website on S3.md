# **Lab Guide: Creating a Website on Amazon S3**

## **Lab Overview**
This lab teaches you how to:
✅ **Create an S3 bucket** and configure it for static website hosting  
✅ **Create an IAM user** with S3 permissions  
✅ **Upload website files** using AWS CLI  
✅ **Automate updates** with a bash script  

---

## **Task 1: Connect to EC2 via Session Manager**
1. **Copy the Session URL** from **AWS Details** > **Show**  
2. Open the URL in a new browser tab (SSM connects automatically)  
3. Switch to `ec2-user`:  
   ```bash
   sudo su -l ec2-user
   pwd  # Verify: /home/ec2-user
   ```

---

## **Task 2: Configure AWS CLI**
```bash
aws configure
```
Enter:  
- **AWS Access Key ID**: *(From **Details**)*  
- **AWS Secret Access Key**: *(From **Details**)*  
- **Default region**: `us-west-2`  
- **Output format**: `json`  

---

## **Task 3: Create an S3 Bucket**
```bash
aws s3api create-bucket \
  --bucket <your-unique-name> \  # e.g., `jsmith123`
  --region us-west-2 \
  --create-bucket-configuration LocationConstraint=us-west-2
```
✅ **Success Output**:  
```json
{"Location": "http://<your-bucket>.s3.amazonaws.com/"}
```

---

## **Task 4: Create an IAM User for S3**
1. **Create User**:  
   ```bash
   aws iam create-user --user-name awsS3user
   ```
2. **Set Password**:  
   ```bash
   aws iam create-login-profile \
     --user-name awsS3user \
     --password Training123!
   ```
3. **Attach S3 Full Access Policy**:  
   ```bash
   aws iam attach-user-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess \
     --user-name awsS3user
   ```

---

## **Task 5: Configure Bucket Permissions**
1. **Disable "Block Public Access"**:  
   - Go to **S3 Console** > **Bucket** > **Permissions**  
   - Edit **Block public access** > **Uncheck all** > **Save**  
2. **Enable ACLs**:  
   - Under **Permissions** > **Object Ownership** > **Edit**  
   - Select **ACLs enabled** > **Save**  

---

## **Task 6: Extract Website Files**
```bash
cd ~/sysops-activity-files
tar xvzf static-website-v2.tar.gz
cd static-website
ls  # Verify: `index.html`, `css/`, `images/`
```

---

## **Task 7: Upload Files & Enable Website Hosting**
1. **Enable Static Website Hosting**:  
   ```bash
   aws s3 website s3://<your-bucket>/ --index-document index.html
   ```
2. **Upload Files**:  
   ```bash
   aws s3 cp ./ s3://<your-bucket>/ --recursive --acl public-read
   ```
3. **Verify Upload**:  
   ```bash
   aws s3 ls s3://<your-bucket>/
   ```
4. **Access Website**:  
   - In **S3 Console** > **Bucket** > **Properties**  
   - Copy **Bucket website endpoint** URL and open in browser  

---

## **Task 8: Create an Update Script**
1. **Create Script**:  
   ```bash
   vi ~/update-website.sh
   ```
   Press `i` and paste:  
   ```bash
   #!/bin/bash
   aws s3 sync /home/ec2-user/sysops-activity-files/static-website/ s3://<your-bucket>/ --acl public-read
   ```
   Save (`Esc` > `:wq` > `Enter`)  

2. **Make Executable**:  
   ```bash
   chmod +x ~/update-website.sh
   ```

3. **Test the Script**:  
   - Edit `index.html` (e.g., change colors)  
   - Run:  
     ```bash
     ./update-website.sh
     ```
   - Refresh the website to see changes  

---

## **Optional Challenge: Optimize with `sync`**
- **`aws s3 sync`** only uploads **changed files** (faster than `cp`).  
- Test by modifying one file and running:  
  ```bash
  aws s3 sync ./ s3://<your-bucket>/ --acl public-read
  ```

---

## **Conclusion**
✅ **Deployed a static website on S3**  
✅ **Automated updates with a script**  
✅ **Learned IAM & S3 CLI commands**  

### **Key Takeaways**
🔹 **S3 hosts static websites** (HTML, CSS, JS)  
🔹 **IAM policies control access**  
🔹 **`sync` > `cp`** for efficient updates  

🚀 **Now you can deploy and manage websites on AWS!**  

### **Next Steps**
🔸 **Add a custom domain** (Route 53 + CloudFront)  
🔸 **Enable versioning** for backup/rollback  
🔸 **Secure with HTTPS** (AWS Certificate Manager)