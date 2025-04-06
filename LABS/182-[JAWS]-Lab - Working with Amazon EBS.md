# Working with Amazon EBS - Comprehensive Lab Guide

## Table of Contents
- [Working with Amazon EBS - Comprehensive Lab Guide](#working-with-amazon-ebs---comprehensive-lab-guide)
  - [Table of Contents](#table-of-contents)
  - [Lab Overview](#lab-overview)
  - [Objectives](#objectives)
  - [Duration](#duration)
  - [Accessing the AWS Management Console](#accessing-the-aws-management-console)
  - [Task 1: Creating a New EBS Volume](#task-1-creating-a-new-ebs-volume)
    - [Step-by-Step Instructions:](#step-by-step-instructions)
  - [Task 2: Attaching the Volume to an EC2 Instance](#task-2-attaching-the-volume-to-an-ec2-instance)
    - [Step-by-Step Instructions:](#step-by-step-instructions-1)
  - [Task 3: Connecting to the Lab EC2 Instance](#task-3-connecting-to-the-lab-ec2-instance)
    - [Step-by-Step Instructions:](#step-by-step-instructions-2)
  - [Task 4: Creating and Configuring the File System](#task-4-creating-and-configuring-the-file-system)
    - [Step-by-Step Instructions:](#step-by-step-instructions-3)
  - [Task 5: Creating an Amazon EBS Snapshot](#task-5-creating-an-amazon-ebs-snapshot)
    - [Step-by-Step Instructions:](#step-by-step-instructions-4)
  - [Task 6: Restoring the Amazon EBS Snapshot](#task-6-restoring-the-amazon-ebs-snapshot)
    - [Task 6.1: Creating a Volume Using the Snapshot](#task-61-creating-a-volume-using-the-snapshot)
    - [Task 6.2: Attaching the Restored Volume](#task-62-attaching-the-restored-volume)
    - [Task 6.3: Mounting the Restored Volume](#task-63-mounting-the-restored-volume)
  - [Conclusion](#conclusion)
  - [Additional Notes and FAQs](#additional-notes-and-faqs)
    - [Best Practices](#best-practices)
    - [Advanced Topics](#advanced-topics)
    - [Frequently Asked Questions](#frequently-asked-questions)
   - [Task 6.1: Creating a Volume Using the Snapshot](#task-61-creating-a-volume-using-the-snapshot)
   - [Task 6.2: Attaching the Restored Volume](#task-62-attaching-the-restored-volume)
   - [Task 6.3: Mounting the Restored Volume](#task-63-mounting-the-restored-volume)
11. [Conclusion](#conclusion)
12. [Additional Notes and FAQs](#additional-notes-and-faqs)

## Lab Overview
Amazon Elastic Block Store (EBS) is a persistent block storage service designed for use with Amazon EC2 instances. In this lab, you'll learn how to:
- Create and attach an EBS volume to an EC2 instance
- Create a filesystem and mount the volume
- Create snapshots for backup
- Restore volumes from snapshots

**Key Concept**: EBS volumes are network-attached storage that persist independently from the life of an EC2 instance. They provide durable, block-level storage that can be attached to running instances.

## Objectives
By completing this lab, you will be able to:
1. Create and configure EBS volumes
2. Attach volumes to EC2 instances
3. Create and manage EBS snapshots
4. Restore data from snapshots

## Duration
Approximately 45 minutes (timer may vary based on experience level)

## Accessing the AWS Management Console
1. Click **Start Lab** to begin your lab session
2. Wait for the **AWS** icon to indicate resources are ready (green checkmark)
3. Click the **AWS** button to open the console in a new tab
4. If blocked by pop-up blocker, allow pop-ups for the lab site

**Note**: Arrange your browser windows to see both the lab instructions and AWS console simultaneously for easier navigation.

## Task 1: Creating a New EBS Volume

### Step-by-Step Instructions:
1. Open the EC2 Console:
   - Search for "EC2" in the AWS Management Console search bar
   - Click on "EC2" to open the service console

2. Verify the existing EC2 instance:
   - In the left navigation pane, select "Instances"
   - Note the "Lab" instance and its Availability Zone (e.g., us-west-2a)
   
   **Important**: The new EBS volume must be created in the same AZ as the instance it will attach to.

3. Navigate to EBS Volumes:
   - In the left navigation pane, under "Elastic Block Store", select "Volumes"
   - Observe the existing 8 GiB volume attached to the "Lab" instance

4. Create a new volume:
   - Click "Create volume"
   - Configure settings:
     - Volume type: General Purpose SSD (gp2)
     - Size: 1 GiB (minimum size for gp2)
     - Availability Zone: Must match the EC2 instance's AZ
   - Add tags:
     - Key: "Name"
     - Value: "My Volume"
   - Click "Create volume"

5. Verify volume creation:
   - New volume appears with "Creating" status
   - Status changes to "Available" when ready (refresh if needed)

**Technical Details**:
- gp2 volumes provide a balance of price and performance for most workloads
- EBS volumes are AZ-bound - they can only attach to instances in the same AZ
- The 1 GiB size is for lab purposes only (production volumes are typically larger)

**Common Questions**:
Q: Why can't I see my new volume?
A: Try refreshing the page. Volume creation typically takes a few seconds.

Q: What happens if I choose the wrong AZ?
A: The volume won't be able to attach to your instance. You would need to create a new volume in the correct AZ or migrate the instance.

## Task 2: Attaching the Volume to an EC2 Instance

### Step-by-Step Instructions:
1. Select your new volume:
   - In the Volumes list, select "My Volume"

2. Initiate attachment:
   - From the "Actions" menu, select "Attach volume"

3. Configure attachment:
   - Instance: Select the "Lab" instance
   - Device name: Enter "/dev/sdb"
     - **Important**: This is the device identifier the OS will use
   - Click "Attach volume"

4. Verify attachment:
   - Volume state changes to "in-use"
   - The instance ID appears in the attachment information

**Technical Details**:
- Linux devices are typically named /dev/sdX (where X is a letter)
- /dev/sda is usually the root volume
- Subsequent volumes get subsequent letters (/dev/sdb, /dev/sdc, etc.)
- In modern systems with NVMe, the volume may appear as /dev/nvme1n1

**Common Questions**:
Q: What if I choose the wrong device name?
A: You can detach and reattach with the correct name. Device names must be unique per instance.

Q: Why doesn't my instance see the new storage immediately?
A: The storage is attached but not yet mounted - we'll do that in the next task.

## Task 3: Connecting to the Lab EC2 Instance

### Step-by-Step Instructions:
1. Navigate to EC2 Instances:
   - Search for "EC2" in the AWS console if needed
   - Select "Instances" in the left navigation pane

2. Select your instance:
   - Choose the "Lab" instance from the list

3. Connect using EC2 Instance Connect:
   - Click the "Connect" button
   - Select the "EC2 Instance Connect" tab
   - Click "Connect"

4. Terminal opens:
   - A new browser tab opens with a terminal session
   - You're now logged into your EC2 instance

**Alternative Connection Methods**:
- SSH: You can also connect using an SSH client with the instance's key pair
- Session Manager: AWS Systems Manager provides another connection method

**Troubleshooting**:
- If the terminal freezes, refresh the browser tab
- If connection fails, verify the instance state is "running"
- Ensure your network allows outbound SSH connections (port 22)

## Task 4: Creating and Configuring the File System

### Step-by-Step Instructions:
1. Check existing storage:
   ```bash
   df -h
   ```
   - Shows mounted filesystems and their usage
   - Note the absence of your new 1 GiB volume

2. Create a filesystem on the new volume:
   ```bash
   sudo mkfs -t ext3 /dev/sdb
   ```
   - Formats the volume with ext3 filesystem
   - Output shows filesystem creation details

3. Create a mount point:
   ```bash
   sudo mkdir /mnt/data-store
   ```
   - Creates a directory to mount the new volume

4. Mount the volume:
   ```bash
   sudo mount /dev/sdb /mnt/data-store
   ```
   - Makes the volume available at the mount point

5. Make mount persistent:
   ```bash
   echo "/dev/sdb   /mnt/data-store ext3 defaults,noatime 1 2" | sudo tee -a /etc/fstab
   ```
   - Adds entry to /etc/fstab for automatic mounting at boot
   - "noatime" improves performance by not updating access times

6. Verify the mount:
   ```bash
   df -h
   ```
   - Now shows /dev/nvme1n1 mounted at /mnt/data-store
   - The device may show as nvme even though we specified /dev/sdb

7. Create a test file:
   ```bash
   sudo sh -c "echo some text has been written > /mnt/data-store/file.txt"
   ```
   - Writes text to a new file on the volume

8. Verify the file:
   ```bash
   cat /mnt/data-store/file.txt
   ```
   - Displays the file contents

**Technical Details**:
- `mkfs` creates a new filesystem on the blank volume
- ext3 is a journaling filesystem good for general use
- Mounting makes the filesystem accessible at a directory
- /etc/fstab ensures the volume mounts automatically after reboots
- The "1 2" at the end of the fstab line controls filesystem checks

**Common Questions**:
Q: Why does my device show as nvme instead of sdb?
A: Modern instances use NVMe drivers that rename devices. The OS maintains both names for compatibility.

Q: What if I get "mount: wrong fs type" errors?
A: Verify you created the filesystem with mkfs. A blank volume needs formatting before mounting.

## Task 5: Creating an Amazon EBS Snapshot

### Step-by-Step Instructions:
1. Navigate to EBS Volumes:
   - Return to the EC2 console
   - Select "Volumes" in the left navigation

2. Select your volume:
   - Choose "My Volume" from the list

3. Create snapshot:
   - From "Actions" menu, select "Create snapshot"
   - Add tags:
     - Key: "Name"
     - Value: "My Snapshot"
   - Click "Create snapshot"

4. Monitor snapshot creation:
   - Navigate to "Snapshots" in the left navigation
   - Status shows "Pending" then changes to "Completed"
   - Only used blocks are copied, saving time and space

5. Delete test file (in terminal):
   ```bash
   sudo rm /mnt/data-store/file.txt
   ```
   - Removes our test file from the volume

6. Verify deletion:
   ```bash
   ls /mnt/data-store/file.txt
   ```
   - Should show "No such file or directory"

**Technical Details**:
- Snapshots are incremental - only changed blocks are saved
- Snapshots are stored in S3 (though not directly visible)
- First snapshot copies all used blocks, subsequent snapshots only changes
- Snapshots can be used to create new volumes or migrate between AZs

**Common Questions**:
Q: How long do snapshots take to create?
A: Depends on volume size and changed data. Small volumes typically complete in seconds.

Q: Are snapshots point-in-time consistent?
A: Yes, EBS snapshots are point-in-time and crash-consistent.

## Task 6: Restoring the Amazon EBS Snapshot

### Task 6.1: Creating a Volume Using the Snapshot

1. Select your snapshot:
   - In the EC2 console, navigate to "Snapshots"
   - Select "My Snapshot"

2. Create new volume:
   - From "Actions" menu, select "Create volume from snapshot"
   - Configure:
     - Availability Zone: Same as original (e.g., us-west-2a)
   - Add tags:
     - Key: "Name"
     - Value: "Restored Volume"
   - Click "Create volume"

3. Verify volume creation:
   - Navigate to "Volumes"
   - New volume appears with "Available" status

**Note**: You can modify volume type or size when restoring from snapshot.

### Task 6.2: Attaching the Restored Volume

1. Select restored volume:
   - Choose "Restored Volume" from the volumes list

2. Attach to instance:
   - From "Actions" menu, select "Attach volume"
   - Configure:
     - Instance: "Lab" instance
     - Device name: "/dev/sdc"
   - Click "Attach"

3. Verify attachment:
   - Volume status changes to "in-use"

### Task 6.3: Mounting the Restored Volume

1. Create mount point:
   ```bash
   sudo mkdir /mnt/data-store2
   ```

2. Mount the volume:
   ```bash
   sudo mount /dev/sdc /mnt/data-store2
   ```

3. Verify restored data:
   ```bash
   ls /mnt/data-store2/file.txt
   ```
   - The file we deleted from the original volume is restored!

**Technical Details**:
- Restoring from snapshot creates an independent copy of the data
- You can restore to different volume types/sizes
- The restored volume has all data from the snapshot moment
- Multiple volumes can be created from the same snapshot

**Common Questions**:
Q: Can I restore a snapshot to a different AZ?
A: Yes, but you must create the new volume in the target AZ first.

Q: Why is my restored file back even though I deleted it?
A: The snapshot captured the volume state before deletion. Restoring reverts to that state.

## Conclusion

In this lab you successfully:
1. Created and attached an EBS volume
2. Formatted and mounted the volume
3. Created a snapshot backup
4. Restored data from the snapshot

**Key Takeaways**:
- EBS volumes provide persistent block storage
- Snapshots enable point-in-time backups
- Volumes are AZ-specific but snapshots are region-wide
- Proper mounting and fstab configuration ensures persistence

## Additional Notes and FAQs

### Best Practices
1. **Regular Snapshots**: Schedule regular snapshots for critical data
2. **Monitoring**: Set up CloudWatch alarms for volume metrics
3. **Lifecycle Policies**: Automate snapshot lifecycle management
4. **Encryption**: Enable encryption for sensitive data

### Advanced Topics
- **Multi-Attach**: Some volume types can attach to multiple instances
- **Throughput Optimization**: Adjust volume types based on workload needs
- **Fast Snapshot Restore**: Reduces restore latency for critical volumes

### Frequently Asked Questions

**Q: How do I increase my EBS volume size?**
A: You can modify volume size in the console (requires OS-level expansion afterwards).

**Q: Can I move an EBS volume to another AZ?**
A: Not directly. You must create a snapshot, then create a new volume from it in the target AZ.

**Q: What's the difference between EBS and instance store?**
A: EBS persists independently from the instance. Instance store is ephemeral and tied to the instance lifecycle.

**Q: How do I encrypt an EBS volume?**
A: Enable encryption when creating the volume, or create an encrypted snapshot and restore from it.

**Q: Can I share EBS volumes between accounts?**
A: Not directly, but you can share snapshots between accounts.

**Q: What happens if my instance terminates?**
A: EBS volumes persist by default (unless configured for deletion on termination).

**Q: How do I monitor EBS performance?**
A: Use Amazon CloudWatch metrics like VolumeReadBytes, VolumeWriteBytes, VolumeQueueLength.