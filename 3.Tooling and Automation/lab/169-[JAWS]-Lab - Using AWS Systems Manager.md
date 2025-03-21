# Lab: Using AWS Systems Manager

## Lab Overview

**AWS Systems Manager** is a powerful collection of capabilities that allows you to centralize operational data and automate tasks across your AWS resources. In this lab, you will use Systems Manager to:
- Verify configurations and permissions.
- Run tasks on multiple servers.
- Update application settings or configurations.
- Access the command line on an instance.

### Key Concepts:
- **AWS Systems Manager**: A service that helps you manage and automate operational tasks across your AWS resources.
- **Fleet Manager**: A capability of Systems Manager used to collect inventory and manage instances.
- **Run Command**: A capability of Systems Manager used to execute commands on instances.
- **Parameter Store**: A capability of Systems Manager used to store and manage configuration data and secrets.
- **Session Manager**: A capability of Systems Manager used to securely access instances without SSH.

---

## Objectives

After completing this lab, you should be able to:
1. Verify configurations and permissions using Systems Manager.
2. Run tasks on multiple servers using Run Command.
3. Update application settings or configurations using Parameter Store.
4. Access the command line on an instance using Session Manager.

---

## Duration

This lab will take approximately **30 minutes** to complete.

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

## Task 1: Generate Inventory Lists for Managed Instances

### Objective:
Use **Fleet Manager** to collect inventory from an EC2 instance.

### Steps:
1. **Navigate to Systems Manager**:
   - In the AWS Management Console, search for **Systems Manager** in the search bar and select it.

2. **Access Fleet Manager**:
   - In the left navigation pane, under **Node Management**, select **Fleet Manager**.

3. **Set Up Inventory**:
   - Click the **Account management** dropdown list and select **Set up inventory**.

4. **Configure Inventory Details**:
   - In the **Provide inventory details** section, enter the following:
     - **Name**: `Inventory-Association`
   - In the **Targets** section:
     - For **Specify targets by**, select **Manually selecting instances**.
     - Select the row for **Managed Instance**.
   - Leave the other options as default.

5. **Create Inventory Association**:
   - Click **Setup Inventory**.
   - A banner with the message **"Setup inventory request succeeded"** will appear.

6. **View Inventory**:
   - Click the **Node ID** link to go to the **Node overview**.
   - Select the **Inventory** tab to view the installed applications and other details.

---

## Task 2: Install a Custom Application Using Run Command

### Objective:
Use **Run Command** to install a custom web application (Widget Manufacturing Dashboard) on an EC2 instance.

### Steps:
1. **Navigate to Run Command**:
   - In the left navigation pane, under **Node Management**, select **Run Command**.

2. **Run a Command**:
   - Click **Run command**.
   - In the search box, click the search icon and select:
     - **Owner**: `Owned by me`.
   - Select the document with the following details:
     - **Description**: `Install Dashboard App`
     - **Document version**: `1 (Default)`

3. **Select Target Instances**:
   - Under **Target selection**, select **Choose instances manually**.
   - In the **Instances** section, select **Managed Instance**.

4. **Run the Command**:
   - Under **Output options**, clear the **Enable an S3 bucket** checkbox.
   - Click **Run**.
   - A banner with the **Command ID** will indicate that the command was successfully sent.

5. **Validate the Installation**:
   - Wait 1–2 minutes for the **Overall status** to change to **Success**.
   - In the Vocareum console, click the **Details** dropdown list, then click **Show**.
   - Copy the **ServerIP** value (public IP address).
   - Open a new browser tab, paste the IP address, and press **Enter**.
   - The **Widget Manufacturing Dashboard** should appear.

---

## Task 3: Use Parameter Store to Manage Application Settings

### Objective:
Use **Parameter Store** to store a parameter that activates a feature in the application.

### Steps:
1. **Navigate to Parameter Store**:
   - In the left navigation pane, under **Application Management**, select **Parameter Store**.

2. **Create a Parameter**:
   - Click **Create parameter**.
   - Configure the following:
     - **Name**: `/dashboard/show-beta-features`
     - **Description**: `Display beta features`
     - **Tier**: Leave as default.
     - **Type**: Leave as default.
     - **Value**: `True`
   - Click **Create parameter**.
   - A banner with the message **"Create parameter request succeeded"** will appear.

3. **Validate the Parameter**:
   - Return to the browser tab with the **Widget Manufacturing Dashboard** and refresh the page.
   - Notice that three charts are now displayed (the third chart is a beta feature).

4. **Optional: Delete the Parameter**:
   - Delete the parameter and refresh the dashboard to see the third chart disappear.

---

## Task 4: Use Session Manager to Access Instances

### Objective:
Use **Session Manager** to securely access the EC2 instance without SSH.

### Steps:
1. **Navigate to Session Manager**:
   - In the left navigation pane, under **Node Management**, select **Session Manager**.

2. **Start a Session**:
   - Click **Start session**.
   - Select **Managed Instance**.
   - Click **Start session**.
   - A new browser tab will open with a session window.

3. **Run Commands in the Session**:
   - Activate the cursor by clicking anywhere in the session window.
   - Run the following command to list application files:
     ```bash
     ls /var/www/html
     ```
   - Run the following commands to get instance details:
     ```bash
     # Get region
     AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
     export AWS_DEFAULT_REGION=${AZ::-1}

     # List information about EC2 instances
     aws ec2 describe-instances
     ```
   - The output will display the EC2 instance details in JSON format.

---

## Conclusion

Congratulations! You have successfully:
1. Verified configurations and permissions using **Fleet Manager**.
2. Installed a custom application using **Run Command**.
3. Updated application settings using **Parameter Store**.
4. Accessed the command line on an instance using **Session Manager**.

---

### Key Takeaways:
- **AWS Systems Manager** provides a centralized way to manage and automate tasks across AWS resources.
- **Fleet Manager** helps you collect inventory and manage instances.
- **Run Command** allows you to execute commands on instances at scale.
- **Parameter Store** securely stores configuration data and secrets.
- **Session Manager** provides secure access to instances without SSH.