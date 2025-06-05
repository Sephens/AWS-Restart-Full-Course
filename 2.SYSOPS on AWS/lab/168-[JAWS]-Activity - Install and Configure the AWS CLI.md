# Lab: Install and Configure the AWS CLI

## Lab Overview

The **AWS Command Line Interface (AWS CLI)** is a powerful tool that allows you to interact with AWS services directly from your command line. This lab will guide you through the process of installing and configuring the AWS CLI on a **Red Hat Linux** instance. You will also learn how to connect the AWS CLI to an AWS account and use it to interact with **AWS Identity and Access Management (IAM)**.

### Key Concepts:
- **AWS CLI**: A unified tool to manage AWS services from the command line.
- **IAM**: A service that helps you securely control access to AWS resources.
- **EC2 Instance**: A virtual server in AWS's cloud.
- **SSH**: A protocol used to securely connect to remote servers.

### Lab Diagram:
- A **Virtual Private Cloud (VPC)** contains a **Red Hat EC2 instance**.
- The **AWS CLI** is installed and configured on the instance.
- You access the instance via an **SSH connection**.
- The AWS CLI is configured to interact with **IAM**.

---

## Objectives

After completing this lab, you should be able to:
1. Install and configure the AWS CLI.
2. Connect the AWS CLI to an AWS account.
3. Access IAM by using the AWS CLI.

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

## Task 1: Connect to the Red Hat EC2 Instance Using SSH

### For Windows Users:
1. **Download the PPK File**:
   - Click the **Details** dropdown menu above these instructions, then click **Show**.
   - Click **Download PPK** and save the `labsuser.ppk` file (usually in the **Downloads** directory).
   - Note the **Public IP** address of the instance.

2. **Download and Configure PuTTY**:
   - If you don’t have PuTTY installed, download it from [here](https://www.putty.org/).
   - Open `putty.exe` and configure your session using the **Public IP** and the `labsuser.ppk` file.
   - Follow the instructions in [Connect to your Linux instance using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html).

3. **Connect to the Instance**:
   - Once configured, click **Open** to establish the SSH connection.

### For macOS and Linux Users:
1. **Download the PEM File**:
   - Click the **Details** dropdown menu, then click **Show**.
   - Click **Download PEM** and save the `labsuser.pem` file.
   - Copy the **Public IP** address for later use.

2. **Change Permissions on the PEM File**:
   - Open a terminal window and navigate to the directory where the `labsuser.pem` file is saved (e.g., `cd ~/Downloads`).
   - Run the following command to change the file permissions:
     ```bash
     chmod 400 labsuser.pem
     ```

3. **Connect to the Instance**:
   - Run the following command, replacing `<ip-address>` with the Public IP address:
     ```bash
     ssh -i labsuser.pem ec2-user@<ip-address>
     ```
   - When prompted, type `yes` to connect to the remote server.

---

## Task 2: Install the AWS CLI on a Red Hat Linux Instance

1. **Download the AWS CLI Installer**:
   - Run the following command to download the AWS CLI installer:
     ```bash
     curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
     ```

2. **Unzip the Installer**:
   - Run the following command to unzip the installer:
     ```bash
     unzip -u awscliv2.zip
     ```

3. **Install the AWS CLI**:
   - Run the following command to install the AWS CLI:
     ```bash
     sudo ./aws/install
     ```

4. **Verify the Installation**:
   - Run the following command to confirm the installation:
     ```bash
     aws --version
     ```
   - Example output:
     ```plaintext
     aws-cli/2.7.24 Python/3.8.8 Linux/4.14.133-113.105.amzn2.x86_64 botocore/2.4.5
     ```

5. **Test the AWS CLI**:
   - Run the following command to display the AWS CLI help menu:
     ```bash
     aws help
     ```
   - Press `q` to exit the help menu.

---

## Task 3: Observe IAM Configuration Details in the AWS Management Console

1. **Navigate to IAM**:
   - In the AWS Management Console, search for **IAM** in the search bar and select it.

2. **View your account user name for example, the `awsstudent` User**:
   - In the left navigation pane, click **Users**, then select **awsstudent**.
   - Under the **Permissions** tab, click the arrow next to **lab_policy**, then click the `{} JSON` button to view the policy document.

3. **View Security Credentials**:
   - Click the **Security credentials** tab.
   - Locate the **Access keys** section and note the **Access key ID**.

---

## Task 4: Configure the AWS CLI to Connect to Your AWS Account

1. **Run the `aws configure` Command**:
   - In the SSH terminal, run the following command:
     ```bash
     aws configure
     ```

2. **Enter Configuration Details**:
   - **AWS Access Key ID**: Copy and paste the `AccessKey` value from the **Details** dropdown.
   - **AWS Secret Access Key**: Copy and paste the `SecretKey` value from the **Details** dropdown.
   - **Default region name**: Enter `us-west-2`.
   - **Default output format**: Enter `json`.

---

## Task 5: Observe IAM Configuration Details Using the AWS CLI

1. **Test the IAM Configuration**:
   - Run the following command to list IAM users:
     ```bash
     aws iam list-users
     ```
   - A successful response will display a JSON object containing a list of IAM users.

---

## Activity 1 Challenge

### Objective:
Use the AWS CLI to download the `lab_policy` document in JSON format.

### Steps:
1. **List IAM Policies**:
   - Run the following command to list customer-managed policies:
     ```bash
     aws iam list-policies --scope Local
     ```

2. **Retrieve the Policy Version**:
   - Use the `Arn` and `DefaultVersionId` from the `lab_policy` document to retrieve the JSON policy:
     ```bash
     aws iam get-policy-version --policy-arn <policy-arn> --version-id <version-id> > lab_policy.json
     ```
   - Example:
     ```bash
     aws iam get-policy-version --policy-arn arn:aws:iam::038946776283:policy/lab_policy --version-id v1 > lab_policy.json
     ```

---

## Activity Summary

### Key Takeaways:
- The AWS CLI allows you to manage AWS services from the command line.
- You need an **Access Key ID** and **Secret Access Key** to connect the AWS CLI to an AWS account.
- The AWS CLI can be used to interact with IAM and other AWS services.

---

## Conclusion

Congratulations! You have successfully:
1. Installed and configured the AWS CLI.
2. Connected the AWS CLI to an AWS account.
3. Accessed IAM using the AWS CLI.

---

### Additional Notes:
- Always secure your access keys and avoid sharing them.
- Use the AWS CLI documentation for advanced commands and troubleshooting: [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html).