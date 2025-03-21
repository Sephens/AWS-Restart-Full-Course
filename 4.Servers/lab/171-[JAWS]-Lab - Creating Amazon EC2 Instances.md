# **Lab: Creating Amazon EC2 Instances**

## **Lab Overview**

In this lab, you will learn how to launch **Amazon Elastic Compute Cloud (EC2)** instances using both the **AWS Management Console** and the **AWS Command Line Interface (AWS CLI)**. You will create a **bastion host** (a secure gateway to your private instances) and use it to launch a **web server instance**. By the end of this lab, you will have a fully functional architecture consisting of a bastion host and a web server instance in a **Virtual Private Cloud (VPC)**.

### **Key Concepts**
- **Amazon EC2**: A scalable compute service that allows you to launch virtual servers in the cloud.
- **Bastion Host**: A secure server that provides access to private instances in a VPC.
- **AWS CLI**: A command-line tool for interacting with AWS services.
- **EC2 Instance Connect**: A secure method to connect to EC2 instances using SSH.

---

## **Objectives**

After completing this lab, you should be able to:
1. Launch an EC2 instance using the **AWS Management Console**.
2. Connect to an EC2 instance using **EC2 Instance Connect**.
3. Launch an EC2 instance using the **AWS CLI**.

---

## **Duration**

This lab will take approximately **45 minutes** to complete.

---

## **Accessing the AWS Management Console**

1. **Start the Lab**:
   - At the top of these instructions, click **Start Lab**.
   - Wait until the message **"Lab status: ready"** appears, then close the **Start Lab** panel by clicking **X**.

2. **Open the AWS Management Console**:
   - Next to **Start Lab**, click **AWS**. This will open the AWS Management Console in a new browser tab.
   - If a new tab does not open, check your browser for a pop-up blocker notification and allow pop-ups for this site.

3. **Arrange Your Workspace**:
   - Position the AWS Management Console alongside these instructions for easy reference.

---

## **Task 1: Launching an EC2 Instance Using the AWS Management Console**

### **Objective**
Launch a **bastion host** EC2 instance using the AWS Management Console.

### **Steps**
1. **Navigate to the EC2 Console**:
   - In the AWS Management Console, search for **EC2** and select it.

2. **Launch an Instance**:
   - From the **Launch instance** dropdown, select **Launch instance**.

3. **Step 1: Name and Tags**:
   - In the **Name and tags** section, enter the name:
     - **Name**: `Bastion host`

4. **Step 2: Choose an AMI**:
   - In the **Application and OS Images (Amazon Machine Image)** section, confirm that **Amazon Linux 2 AMI (HVM)** is selected.

5. **Step 3: Choose an Instance Type**:
   - From the **Instance type** dropdown, select **t3.micro**.

6. **Step 4: Configure a Key Pair**:
   - In the **Key pair (login)** section, select **Proceed without key pair (Not recommended)**.

7. **Step 5: Configure Network Settings**:
   - In the **Network settings** section, click **Edit**.
   - For **VPC**, select **Lab VPC**.
   - For **Subnet**, ensure **Public Subnet** is selected.
   - For **Auto-assign public IP**, ensure **Enable** is selected.
   - In the **Firewall (security groups)** section:
     - **Security group name**: `Bastion security group`
     - **Description**: `Permit SSH connections`

8. **Step 6: Add Storage**:
   - Keep the default storage configuration (8 GiB root volume).

9. **Step 7: Configure Advanced Details**:
   - Expand the **Advanced details** section.
   - For **IAM instance profile**, select **Bastion-Role**.

10. **Step 8: Launch the Instance**:
    - Review the configuration and click **Launch instance**.
    - Click **View all instances** to see the newly launched instance.

---

## **Task 2: Logging in to the Bastion Host**

### **Objective**
Use **EC2 Instance Connect** to securely connect to the bastion host.

### **Steps**
1. **Select the Bastion Host Instance**:
   - In the EC2 Management Console, select the **Bastion host** instance.

2. **Connect to the Instance**:
   - Click **Connect**.
   - On the **EC2 Instance Connect** tab, click **Connect**.

3. **Verify Connection**:
   - You should now be connected to the bastion host via a terminal session.

---

## **Task 3: Launching an EC2 Instance Using the AWS CLI**

### **Objective**
Use the **AWS CLI** to launch a **web server instance** from the bastion host.

### **Steps**
1. **Retrieve the AMI ID**:
   - Run the following script to retrieve the latest Amazon Linux 2 AMI ID:
     ```bash
     # Set the Region
     AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
     export AWS_DEFAULT_REGION=${AZ::-1}

     # Retrieve latest Linux AMI
     AMI=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --query 'Parameters[0].[Value]' --output text)
     echo $AMI
     ```

2. **Retrieve the Subnet ID**:
   - Run the following command to retrieve the subnet ID for the public subnet:
     ```bash
     SUBNET=$(aws ec2 describe-subnets --filters 'Name=tag:Name,Values=Public Subnet' --query Subnets[].SubnetId --output text)
     echo $SUBNET
     ```

3. **Retrieve the Security Group ID**:
   - Run the following command to retrieve the security group ID for the web security group:
     ```bash
     SG=$(aws ec2 describe-security-groups --filters Name=group-name,Values=WebSecurityGroup --query SecurityGroups[].GroupId --output text)
     echo $SG
     ```

4. **Download the User Data Script**:
   - Run the following command to download the user data script:
     ```bash
     wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-1-23732/171-lab-JAWS-create-ec2/s3/UserData.txt
     ```
   - View the script contents:
     ```bash
     cat UserData.txt
     ```

5. **Launch the Web Server Instance**:
   - Run the following command to launch the web server instance:
     ```bash
     INSTANCE=$(\
     aws ec2 run-instances \
     --image-id $AMI \
     --subnet-id $SUBNET \
     --security-group-ids $SG \
     --user-data file:///home/ec2-user/UserData.txt \
     --instance-type t3.micro \
     --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Web Server}]' \
     --query 'Instances[*].InstanceId' \
     --output text \
     )
     echo $INSTANCE
     ```

6. **Wait for the Instance to Be Ready**:
   - Monitor the instance status using the following command:
     ```bash
     aws ec2 describe-instances --instance-ids $INSTANCE --query 'Reservations[].Instances[].State.Name' --output text
     ```
   - Wait until the status changes to **running**.

7. **Test the Web Server**:
   - Retrieve the public DNS name of the instance:
     ```bash
     aws ec2 describe-instances --instance-ids $INSTANCE --query Reservations[].Instances[].PublicDnsName --output text
     ```
   - Copy the DNS name and paste it into a new browser tab to access the web server.

---

## **Optional Challenges**

### **Challenge 1: Connect to a Misconfigured EC2 Instance**
1. **Objective**:
   - Troubleshoot and fix the security configuration of a misconfigured EC2 instance.

2. **Steps**:
   - Attempt to connect to the **Misconfigured Web Server** instance using EC2 Instance Connect.
   - Diagnose and fix the issue.

### **Challenge 2: Fix the Web Server Installation**
1. **Objective**:
   - Troubleshoot and fix the web server installation on the misconfigured instance.

2. **Steps**:
   - Retrieve the public DNS name of the misconfigured instance.
   - Diagnose and fix the issue preventing the web server from functioning.

---

## **Conclusion**

Congratulations! You have successfully:
1. Launched an EC2 instance using the **AWS Management Console**.
2. Connected to an EC2 instance using **EC2 Instance Connect**.
3. Launched an EC2 instance using the **AWS CLI**.

### **Key Takeaways**
- The **AWS Management Console** is ideal for quick, one-off instance launches.
- The **AWS CLI** is powerful for automating instance launches and managing AWS resources programmatically.
- **EC2 Instance Connect** provides a secure and convenient way to connect to EC2 instances.

---

## **Next Steps**
- Explore **AWS CloudFormation** for launching related resources together.
- Use **Amazon CloudWatch** to monitor your EC2 instances.
- Experiment with **Auto Scaling Groups** to automatically adjust the number of EC2 instances based on demand.

Happy learning! 🚀