# Lab: Creating a Website on S3

## Lab Overview

In this lab, you will use the **AWS Command Line Interface (AWS CLI)** to:
- Create an **Amazon S3 bucket**.
- Create a new **IAM user** with full access to Amazon S3.
- Upload files to Amazon S3 to host a static website for the **Café & Bakery**.
- Create a batch file to update the website when changes are made locally.

### Key Concepts:
- **Amazon S3**: A scalable object storage service for hosting static websites.
- **IAM**: A service for managing access to AWS resources.
- **AWS CLI**: A command-line tool for interacting with AWS services.
- **Static Website**: A website that serves fixed content (HTML, CSS, images) without server-side processing.

---

## Objectives

After completing this lab, you should be able to:
1. Run AWS CLI commands to interact with IAM and Amazon S3.
2. Deploy a static website to an S3 bucket.
3. Create a script to copy files from a local directory to Amazon S3.

---

## Duration

This lab will take approximately **45 minutes** to complete.

---

## Accessing the AWS Management Console

1. **Start the Lab**:
   - At the top of these instructions, click **Start Lab**.
   - Wait until the message **"Lab status: ready"** appears, then close the **Start Lab** panel by clicking **X**.

2. **Open the AWS Management Console**:
   - Next to **Start Lab**, click **AWS**. This will open the AWS Management Console in a new browser tab.
   - If a new tab does not open, check your browser for a pop-up blocker notification and allow pop-ups for this site.

3. **Arrange Your Workspace**:
   - Position the AWS Management Console alongside these instructions for easy reference.

---

## Task 1: Connect to an Amazon Linux EC2 Instance Using SSM

### Objective:
Use **AWS Systems Manager Session Manager** to connect to an EC2 instance.

### Steps:
1. **Copy the Session URL**:
   - Click the **Details** button at the top, then click **Show**.
   - Copy the **InstanceSessionUrl** value.

2. **Open the Session**:
   - Paste the URL into a new browser tab to open a terminal session.

3. **Switch to the `ec2-user`**:
   - Run the following commands to switch to the `ec2-user` and confirm the home directory:
     ```bash
     sudo su -l ec2-user
     pwd
     ```

---

## Task 2: Configure the AWS CLI

### Objective:
Configure the AWS CLI with credentials.

### Steps:
1. **Run the `aws configure` Command**:
   - In the terminal, run:
     ```bash
     aws configure
     ```

2. **Enter Configuration Details**:
   - **AWS Access Key ID**: Copy and paste the `AccessKey` value from the **Details** pane.
   - **AWS Secret Access Key**: Copy and paste the `SecretKey` value from the **Details** pane.
   - **Default region name**: Enter `us-west-2`.
   - **Default output format**: Enter `json`.

---

## Task 3: Create an S3 Bucket Using the AWS CLI

### Objective:
Create an S3 bucket to host the website.

### Steps:
1. **Run the `create-bucket` Command**:
   - Replace `<bucket-name>` with a unique name (e.g., `twhitlock256`):
     ```bash
     aws s3api create-bucket --bucket <bucket-name> --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
     ```
   - Example:
     ```bash
     aws s3api create-bucket --bucket twhitlock256 --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
     ```

2. **Verify the Bucket Creation**:
   - A JSON response with a `Location` field confirms the bucket was created.

---

## Task 4: Create a New IAM User with Full Access to Amazon S3

### Objective:
Create an IAM user and grant it full access to Amazon S3.

### Steps:
1. **Create the IAM User**:
   - Run the following command:
     ```bash
     aws iam create-user --user-name awsS3user
     ```

2. **Create a Login Profile**:
   - Run the following command:
     ```bash
     aws iam create-login-profile --user-name awsS3user --password Training123!
     ```

3. **Copy the AWS Account Number**:
   - In the AWS Management Console, click the account dropdown (top right) and copy the **12-digit Account ID**.

4. **Log in as the New User**:
   - Sign out of the AWS Management Console.
   - Log back in as the IAM user:
     - **Account ID**: Paste the 12-digit number.
     - **IAM user name**: `awsS3user`.
     - **Password**: `Training123!`.

5. **Attach the S3 Full Access Policy**:
   - Find the S3 full access policy:
     ```bash
     aws iam list-policies --query "Policies[?contains(PolicyName,'S3')]"
     ```
   - Attach the policy to the user:
     ```bash
     aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name awsS3user
     ```

---

## Task 5: Adjust S3 Bucket Permissions

### Objective:
Make the S3 bucket publicly accessible.

### Steps:
1. **Disable Block Public Access**:
   - In the AWS Management Console, navigate to the S3 bucket.
   - Go to **Permissions** > **Block public access** > **Edit**.
   - Uncheck **Block all public access** and save.

2. **Enable ACLs**:
   - Go to **Permissions** > **Object Ownership** > **Edit**.
   - Select **ACLs enabled** and save.

---

## Task 6: Extract the Website Files

### Objective:
Extract the static website files.

### Steps:
1. **Extract the Files**:
   - Run the following commands:
     ```bash
     cd ~/sysops-activity-files
     tar xvzf static-website-v2.tar.gz
     cd static-website
     ```

2. **Verify the Files**:
   - Run `ls` to confirm the presence of `index.html`, `css`, and `images`.

---

## Task 7: Upload Files to Amazon S3

### Objective:
Upload the website files to the S3 bucket.

### Steps:
1. **Enable Static Website Hosting**:
   - Replace `<my-bucket>` with your bucket name:
     ```bash
     aws s3 website s3://<my-bucket>/ --index-document index.html
     ```

2. **Upload the Files**:
   - Run the following command:
     ```bash
     aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://<my-bucket>/ --recursive --acl public-read
     ```

3. **Verify the Upload**:
   - Run the following command:
     ```bash
     aws s3 ls <my-bucket>
     ```

4. **Access the Website**:
   - In the AWS Management Console, go to the S3 bucket.
   - Under **Properties**, copy the **Bucket website endpoint URL** and open it in a browser.

---

## Task 8: Create a Batch File to Update the Website

### Objective:
Create a script to automate website updates.

### Steps:
1. **Create the Script**:
   - Run the following commands:
     ```bash
     cd ~
     touch update-website.sh
     vi update-website.sh
     ```
   - Add the following content (replace `<my-bucket>` with your bucket name):
     ```bash
     #!/bin/bash
     aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://<my-bucket>/ --recursive --acl public-read
     ```
   - Save and exit (`Esc` > `:wq` > `Enter`).

2. **Make the Script Executable**:
   - Run the following command:
     ```bash
     chmod +x update-website.sh
     ```

3. **Modify the Website**:
   - Edit `index.html`:
     ```bash
     vi sysops-activity-files/static-website/index.html
     ```
   - Change colors (e.g., `bgcolor="aquamarine"` to `bgcolor="gainsboro"`).

4. **Run the Script**:
   - Run the following command:
     ```bash
     ./update-website.sh
     ```

5. **View the Changes**:
   - Refresh the website in your browser.

---

## Optional Challenge

### Objective:
Use the `aws s3 sync` command to make updates more efficient.

### Steps:
1. **Modify the Script**:
   - Replace the `aws s3 cp` command with:
     ```bash
     aws s3 sync /home/ec2-user/sysops-activity-files/static-website/ s3://<my-bucket>/ --acl public-read
     ```

2. **Test the Script**:
   - Make a small change to `index.html` and run the script.
   - Observe that only the modified file is uploaded.

---

## Conclusion

Congratulations! You have successfully:
1. Run AWS CLI commands to interact with IAM and Amazon S3.
2. Deployed a static website to an S3 bucket.
3. Created a script to copy files from a local directory to Amazon S3.

---

### Key Takeaways:
- **Amazon S3** is a cost-effective solution for hosting static websites.
- **AWS CLI** provides a powerful way to automate AWS tasks.
- **IAM** ensures secure access to AWS resources.
- **Batch files** can streamline repetitive tasks like website updates.

---

## End Lab

1. **End the Lab**:
   - At the top of the page, click **End Lab** > **Yes**.
2. **Close the Panel**:
   - Click the **X** to close the **End Lab** panel.