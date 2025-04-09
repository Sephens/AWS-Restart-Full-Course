# Managing Storage with AWS - Comprehensive Lab Guide

## Table of Contents
- [Managing Storage with AWS - Comprehensive Lab Guide](#managing-storage-with-aws---comprehensive-lab-guide)
  - [Table of Contents](#table-of-contents)
  - [Lab Overview](#lab-overview)
  - [Objectives](#objectives)
  - [Duration](#duration)
  - [Accessing the AWS Management Console](#accessing-the-aws-management-console)
  - [Task 1: Creating and Configuring Resources](#task-1-creating-and-configuring-resources)
    - [Task 1.1: Create an S3 Bucket](#task-11-create-an-s3-bucket)
      - [Step-by-Step Instructions:](#step-by-step-instructions)
    - [Task 1.2: Attach Instance Profile to Processor](#task-12-attach-instance-profile-to-processor)
      - [Step-by-Step Instructions:](#step-by-step-instructions-1)
  - [Task 2: Taking Snapshots of Your Instance](#task-2-taking-snapshots-of-your-instance)
    - [Task 2.1: Connecting to the Command Host EC2 Instance](#task-21-connecting-to-the-command-host-ec2-instance)
      - [Step-by-Step Instructions:](#step-by-step-instructions-2)
    - [Task 2.2: Taking an Initial Snapshot](#task-22-taking-an-initial-snapshot)
      - [Step-by-Step Instructions:](#step-by-step-instructions-3)
    - [Task 2.3: Scheduling the Creation of Subsequent Snapshots](#task-23-scheduling-the-creation-of-subsequent-snapshots)
      - [Step-by-Step Instructions:](#step-by-step-instructions-4)
    - [Task 2.4: Retaining the Last Two Snapshots](#task-24-retaining-the-last-two-snapshots)
      - [Step-by-Step Instructions:](#step-by-step-instructions-5)
  - [Task 3: Challenge: Synchronize Files with Amazon S3](#task-3-challenge-synchronize-files-with-amazon-s3)
    - [Task 3.1: Downloading and Unzipping Sample Files](#task-31-downloading-and-unzipping-sample-files)
      - [Step-by-Step Instructions:](#step-by-step-instructions-6)
    - [Task 3.2: Syncing Files](#task-32-syncing-files)
      - [Step-by-Step Instructions:](#step-by-step-instructions-7)
  - [Conclusion](#conclusion)
  - [Additional Notes and FAQs](#additional-notes-and-faqs)
    - [Best Practices](#best-practices)
    - [Advanced Topics](#advanced-topics)
    - [Frequently Asked Questions](#frequently-asked-questions)

## Lab Overview
This lab focuses on managing storage in AWS using:
- EBS snapshots for backup and recovery
- S3 for object storage
- Versioning for data protection

**Key Components**:
- **Command Host**: EC2 instance used to administer AWS resources
- **Processor**: EC2 instance with EBS volume we'll manage
- **S3 Bucket**: Destination for syncing files

## Objectives
By completing this lab, you will be able to:
1. Create and maintain EBS snapshots
2. Automate snapshot management
3. Sync files between EBS volumes and S3
4. Use S3 versioning for data recovery

## Duration
Approximately 45 minutes (timer may vary based on experience level)

## Accessing the AWS Management Console
1. Click **Start Lab** to begin your session
2. Wait for the "Lab status: ready" message
3. Click the **AWS** button to open the console in a new tab
4. Allow pop-ups if blocked by your browser

## Task 1: Creating and Configuring Resources

### Task 1.1: Create an S3 Bucket

#### Step-by-Step Instructions:
1. Open the S3 Console:
   - Search for "S3" in the AWS console
   - Click "S3" to open the service

2. Create a new bucket:
   - Click "Create bucket"
   - Configure:
     - Bucket name: Unique combination of letters/numbers
     - Region: Leave default
   - Click "Create bucket"

**Technical Details**:
- S3 bucket names must be globally unique across all AWS accounts
- No special characters except periods and hyphens
- Consider naming conventions for your organization

**Common Questions**:
Q: What if my bucket name isn't available?
A: Try adding numbers or different prefixes/suffixes to make it unique

### Task 1.2: Attach Instance Profile to Processor

#### Step-by-Step Instructions:
1. Open the EC2 Console:
   - Search for "EC2" in AWS console
   - Click "EC2" to open the service

2. Locate the Processor instance:
   - In left navigation, select "Instances"
   - Select "Processor" from the list

3. Attach IAM role:
   - Click "Actions" > "Security" > "Modify IAM role"
   - Select "S3BucketAccess" from dropdown
   - Click "Update IAM role"

**Technical Details**:
- IAM roles provide temporary credentials to EC2 instances
- More secure than storing access keys on instances
- The S3BucketAccess role grants S3 permissions

## Task 2: Taking Snapshots of Your Instance

### Task 2.1: Connecting to the Command Host EC2 Instance

#### Step-by-Step Instructions:
1. In EC2 Console, select "Command Host" instance
2. Click "Connect"
3. Select "EC2 Instance Connect" tab
4. Click "Connect"

**Note**: This opens a terminal in your browser where you'll run AWS CLI commands

### Task 2.2: Taking an Initial Snapshot

#### Step-by-Step Instructions:
1. Get the Processor's EBS volume ID:
   ```bash
   aws ec2 describe-instances --filter 'Name=tag:Name,Values=Processor' \
     --query 'Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.{VolumeId:VolumeId}'
   ```
   - Note the VolumeId returned (e.g., "vol-1234abcd")

2. Get the Processor's instance ID:
   ```bash
   aws ec2 describe-instances --filters 'Name=tag:Name,Values=Processor' \
     --query 'Reservations[0].Instances[0].InstanceId'
   ```
   - Note the InstanceId returned (e.g., "i-0b06965263c7ac08f")

3. Stop the Processor instance:
   ```bash
   aws ec2 stop-instances --instance-ids INSTANCE-ID
   ```

4. Wait for instance to stop:
   ```bash
   aws ec2 wait instance-stopped --instance-id INSTANCE-ID
   ```

5. Create snapshot:
   ```bash
   aws ec2 create-snapshot --volume-id VOLUME-ID
   ```
   - Note the SnapshotId returned

6. Wait for snapshot completion:
   ```bash
   aws ec2 wait snapshot-completed --snapshot-id SNAPSHOT-ID
   ```

7. Restart the Processor instance:
   ```bash
   aws ec2 start-instances --instance-ids INSTANCE-ID
   ```

**Technical Details**:
- Stopping the instance ensures data consistency in the snapshot
- The `wait` commands pause execution until the operation completes
- Snapshots are incremental - only changed blocks are saved after the first snapshot

### Task 2.3: Scheduling the Creation of Subsequent Snapshots

#### Step-by-Step Instructions:
1. Create cron job for frequent snapshots (every minute for lab purposes):
   ```bash
   echo "* * * * * aws ec2 create-snapshot --volume-id VOLUME-ID 2>&1 >> /tmp/cronlog" > cronjob
   crontab cronjob
   ```

2. Verify snapshots are being created:
   ```bash
   aws ec2 describe-snapshots --filters "Name=volume-id,Values=VOLUME-ID"
   ```
   - Run multiple times to see new snapshots appear

**Technical Details**:
- Cron syntax: `* * * * *` means "every minute"
- Output is redirected to /tmp/cronlog for debugging
- In production, you would schedule less frequently (e.g., daily)

### Task 2.4: Retaining the Last Two Snapshots

#### Step-by-Step Instructions:
1. Stop the cron job:
   ```bash
   crontab -r
   ```

2. View the Python cleanup script:
   ```bash
   more /home/ec2-user/snapshotter_v2.py
   ```

3. Check current snapshots:
   ```bash
   aws ec2 describe-snapshots --filters "Name=volume-id,Values=VOLUME-ID" \
     --query 'Snapshots[*].SnapshotId'
   ```

4. Run the cleanup script:
   ```bash
   python3 snapshotter_v2.py
   ```
   - This will delete all but the two most recent snapshots

5. Verify only two snapshots remain:
   ```bash
   aws ec2 describe-snapshots --filters "Name=volume-id,Values=VOLUME-ID" \
     --query 'Snapshots[*].SnapshotId'
   ```

**Technical Details**:
- The script:
  1. Lists all EBS volumes
  2. Takes new snapshots
  3. Sorts snapshots by date
  4. Deletes all but the two newest
- In production, you might keep more snapshots based on retention policies

## Task 3: Challenge: Synchronize Files with Amazon S3

### Task 3.1: Downloading and Unzipping Sample Files

#### Step-by-Step Instructions:
1. Connect to the Processor instance using EC2 Instance Connect
2. Download sample files:
   ```bash
   wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-1-23732/183-lab-JAWS-managing-storage/s3/files.zip
   ```

3. Unzip the files:
   ```bash
   unzip files.zip
   ```
   - This creates a "files" directory with three text files

### Task 3.2: Syncing Files

#### Step-by-Step Instructions:
1. Enable versioning on your S3 bucket:
   ```bash
   aws s3api put-bucket-versioning --bucket S3-BUCKET-NAME \
     --versioning-configuration Status=Enabled
   ```

2. Sync files to S3:
   ```bash
   aws s3 sync files s3://S3-BUCKET-NAME/files/
   ```

3. Verify files uploaded:
   ```bash
   aws s3 ls s3://S3-BUCKET-NAME/files/
   ```

4. Delete a local file:
   ```bash
   rm files/file1.txt
   ```

5. Sync with delete option (removes files in S3 that don't exist locally):
   ```bash
   aws s3 sync files s3://S3-BUCKET-NAME/files/ --delete
   ```

6. Verify file was deleted from S3:
   ```bash
   aws s3 ls s3://S3-BUCKET-NAME/files/
   ```

7. List versions of deleted file:
   ```bash
   aws s3api list-object-versions --bucket S3-BUCKET-NAME \
     --prefix files/file1.txt
   ```
   - Note the VersionId of the previous version

8. Restore the previous version:
   ```bash
   aws s3api get-object --bucket S3-BUCKET-NAME \
     --key files/file1.txt --version-id VERSION-ID files/file1.txt
   ```

9. Verify local file restored:
   ```bash
   ls files
   ```

10. Resync to S3:
    ```bash
    aws s3 sync files s3://S3-BUCKET-NAME/files/
    ```

11. Verify file restored in S3:
    ```bash
    aws s3 ls s3://S3-BUCKET-NAME/files/
    ```

**Technical Details**:
- Versioning preserves all versions of an object
- The `--delete` flag makes S3 match the local state exactly
- Restoring requires getting a specific version then re-uploading

## Conclusion

In this lab you successfully:
1. Created and managed EBS snapshots
2. Automated snapshot creation and cleanup
3. Synced files between EBS and S3
4. Used versioning to recover deleted files

**Key Takeaways**:
- Snapshots provide point-in-time recovery for EBS volumes
- Automation ensures regular backups without manual intervention
- S3 versioning protects against accidental deletions
- The `sync` command efficiently manages file transfers

## Additional Notes and FAQs

### Best Practices
1. **Snapshot Scheduling**: Use AWS Backup or Data Lifecycle Manager for production
2. **S3 Versioning**: Enable for critical buckets to prevent data loss
3. **IAM Roles**: Always prefer roles over access keys for EC2 permissions
4. **Monitoring**: Set up alerts for failed sync operations or snapshot jobs

### Advanced Topics
- **Cross-Region Snapshots**: Copy snapshots to other regions for DR
- **S3 Lifecycle Policies**: Automate transition to cheaper storage classes
- **S3 Replication**: Maintain copies in different buckets/regions

### Frequently Asked Questions

**Q: How often should I take EBS snapshots?**
A: Depends on your RPO. Critical systems might need hourly, others daily.

**Q: Does S3 versioning increase storage costs?**
A: Yes, you pay for all versions. Use lifecycle rules to expire old versions.

**Q: Can I automate snapshot cleanup like we did in the lab?**
A: Yes, AWS provides Data Lifecycle Manager for this purpose.

**Q: What's the difference between `aws s3 cp` and `aws s3 sync`?**
A: `sync` only copies changed files and can delete remote files, making it more efficient for ongoing operations.

**Q: How do I estimate my S3 storage costs?**
A: Use the AWS Pricing Calculator with your expected storage size and access patterns.