# AWS Resource Tagging Management Lab Guide

## Lab Overview
This lab demonstrates how to use AWS resource tagging to efficiently manage EC2 instances. You'll learn to:
- Query instances based on tags
- Modify tags in bulk
- Stop/start instances using tags
- Implement tag-based compliance policies

## Lab Objectives
After completing this lab, you will be able to:
- Apply and modify tags to AWS resources
- Find resources using tag-based filters
- Perform bulk operations on tagged resources
- Implement tag-based resource management policies

## Architecture
The environment consists of:
- A VPC with public and private subnets
- A CommandHost EC2 instance with AWS CLI pre-installed
- 8 EC2 instances with various tags:
  - Project: ERPSystem or Experiment1
  - Version: 1.0
  - Environment: development, staging, or production

## Detailed Step-by-Step Guide

### Task 1: Using Tags to Manage Resources

#### Step 1.1: Connect to Command Host
**Windows Users:**
1. Download PPK file
2. Use PuTTY to SSH into CommandHost
3. Authenticate with the PPK key

**Mac/Linux Users:**
1. Download PEM file
2. Set permissions: `chmod 400 labsuser.pem`
3. SSH: `ssh -i labsuser.pem ec2-user@<public-ip>`

#### Step 1.2: Query Instances by Tags
1. Find all ERPSystem instances:
   ```bash
   aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem"
   ```

2. Refine query to show only instance IDs:
   ```bash
   aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].InstanceId'
   ```

3. Include multiple fields in output:
   ```bash
   aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}'
   ```

4. Include tag values in output:
   ```bash
   aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value}'
   ```

5. Filter for development environment:
   ```bash
   aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" "Name=tag:Environment,Values=development" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
   ```

#### Step 1.3: Modify Tags in Bulk
1. Examine the tag change script:
   ```bash
   nano change-resource-tags.sh
   ```
   Contents:
   ```bash
   #!/bin/bash
   ids=$(aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" "Name=tag:Environment,Values=development" --query 'Reservations[*].Instances[*].InstanceId' --output text)
   aws ec2 create-tags --resources $ids --tags 'Key=Version,Value=1.1'
   ```

2. Run the script:
   ```bash
   ./change-resource-tags.sh
   ```

3. Verify changes:
   ```bash
   aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
   ```

### Task 2: Stop and Start Resources by Tag

#### Step 2.1: Examine Stopinator Script
1. Navigate to scripts directory:
   ```bash
   cd aws-tools
   ```

2. Review script:
   ```bash
   nano stopinator.php
   ```
   Key features:
   - Uses AWS PHP SDK
   - Takes tag filters as input (-t parameter)
   - Can stop or start instances (-s flag for start)

#### Step 2.2: Stop Development Instances
1. Stop ERPSystem development instances:
   ```bash
   ./stopinator.php -t"Project=ERPSystem;Environment=development"
   ```

2. Verify in AWS Console:
   - Navigate to EC2 → Instances
   - Confirm two instances are stopping/stopped

#### Step 2.3: Restart Development Instances
1. Restart the instances:
   ```bash
   ./stopinator.php -t"Project=ERPSystem;Environment=development" -s
   ```

2. Verify in AWS Console:
   - Confirm instances are starting/running

### Task 3: Challenge - Terminate Non-Compliant Instances

#### Step 3.1: Prepare Environment
1. Select two private subnet instances in AWS Console
2. Remove their Environment tags:
   - EC2 → Instances → Select instance → Tags → Edit
   - Remove Environment tag → Save

#### Step 3.2: Review Terminate Script
1. Examine the script:
   ```bash
   nano terminate-instances.php
   ```
   Key components:
   - Finds all instances with Environment tag
   - Compares against all instances in subnet
   - Terminates untagged instances

#### Step 3.3: Run Terminate Script
1. Get required parameters:
   - Region: Availability Zone minus last letter (e.g., "us-west-2")
   - Subnet ID: From instance details

2. Execute script:
   ```bash
   ./terminate-instances.php -region <region> -subnetid <subnet-id>
   ```

3. Verify in AWS Console:
   - Untagged instances should be terminating/terminated

## Key Concepts and Best Practices

### Tagging Strategies
1. **Consistency**: Use standardized tag names and values
2. **Automation**: Implement tag policies using AWS Organizations
3. **Lifecycle**: Include tags for:
   - Owner (team/department)
   - Environment (dev/test/prod)
   - Cost center
   - Compliance requirements

### Bulk Operations
1. **Query First**: Always verify which resources will be affected
2. **JMESPath**: Powerful query language for filtering AWS CLI output
3. **Scripting**: Create reusable scripts for common operations

### Compliance Enforcement
1. **Tag Policies**: Use AWS Organizations to enforce tagging standards
2. **Automated Remediation**:
   - AWS Config rules to detect non-compliance
   - Lambda functions to remediate issues
3. **Resource Cleanup**: Regularly terminate untagged or non-compliant resources

## Troubleshooting Tips

1. **Permission Issues**:
   - Ensure IAM permissions allow tag operations
   - Verify resource ownership

2. **Script Errors**:
   - Check PHP/AWS SDK versions
   - Validate AWS credentials on CommandHost

3. **Unexpected Results**:
   - Double-check filter syntax
   - Test with --dry-run flag when available

## Conclusion

This lab demonstrated how to:
1. Effectively use tags to organize resources
2. Perform bulk operations using tag filters
3. Implement tag-based compliance policies

Key takeaways:
- Tags enable efficient resource management
- AWS CLI and SDKs provide powerful automation capabilities
- Tag-based policies help maintain security and compliance

By implementing these practices, organizations can better manage their AWS resources at scale while maintaining security and cost control.