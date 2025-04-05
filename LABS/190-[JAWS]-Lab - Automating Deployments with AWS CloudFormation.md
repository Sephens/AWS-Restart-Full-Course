# AWS CloudFormation Automation Lab Guide

## Lab Overview
This lab demonstrates how to use AWS CloudFormation to automate infrastructure deployment. You'll learn to:
- Deploy a CloudFormation stack with VPC and security group
- Modify templates to add S3 buckets and EC2 instances
- Delete stacks and their resources
- Understand Infrastructure as Code (IaC) principles

## Lab Objectives
After completing this lab, you will be able to:
- Create and manage CloudFormation stacks
- Author and modify CloudFormation templates
- Reference resources within templates
- Use AWS Systems Manager Parameter Store for AMI IDs
- Clean up resources by deleting stacks

## Architecture Components
The lab builds this infrastructure:
1. VPC with public subnet
2. Security group
3. S3 bucket (added in Task 2)
4. EC2 instance (added in Task 3)

## Detailed Step-by-Step Guide

### Task 1: Deploy Initial CloudFormation Stack

#### Step 1.1: Download and Review Template
1. Download the starter template: [task1.yaml]
2. Open in a text editor (VS Code, Sublime, etc.)
3. Examine key sections:
   - Parameters: Defines input values (VPC CIDR, subnet CIDR)
   - Resources: Declares infrastructure (VPC, security group)
   - Outputs: Exports useful information

#### Step 1.2: Create Stack
1. Navigate to CloudFormation in AWS Console
2. Click "Create stack" → "Upload a template file"
3. Select the downloaded task1.yaml
4. Configure:
   - Stack name: "Lab"
   - Keep default parameter values
5. Acknowledge IAM capabilities
6. Click "Create stack"

#### Step 1.3: Monitor Deployment
1. View stack events in chronological order
2. Watch resource creation progress:
   - VPC created first
   - Then dependent resources
3. Verify status changes to CREATE_COMPLETE

**Key Concept:** CloudFormation automatically handles dependencies and creation order.

### Task 2: Add S3 Bucket to Stack

#### Step 2.1: Modify Template
1. Edit task1.yaml to add S3 bucket resource
2. Add under Resources section:
   ```yaml
   MyBucket:
     Type: AWS::S3::Bucket
   ```
3. Save as task2.yaml

#### Step 2.2: Update Stack
1. In CloudFormation console, select "Lab" stack
2. Choose "Update"
3. Select "Replace current template"
4. Upload modified task2.yaml
5. Review changes (should show only bucket addition)
6. Execute update

#### Step 2.3: Verify
1. Check Resources tab for new S3 bucket
2. Optional: View bucket in S3 console

**Best Practice:** Minimal templates make changes predictable and reduce errors.

### Task 3: Add EC2 Instance to Stack

#### Step 3.1: Add AMI Parameter
1. Edit template (task2.yaml)
2. Add to Parameters section:
   ```yaml
   AmazonLinuxAMIID:
     Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
     Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
   ```

#### Step 3.2: Add EC2 Resource
1. Add under Resources section:
   ```yaml
   WebServer:
     Type: AWS::EC2::Instance
     Properties:
       ImageId: !Ref AmazonLinuxAMIID
       InstanceType: t3.micro
       SecurityGroupIds:
         - !Ref AppSecurityGroup
       SubnetId: !Ref PublicSubnet
       Tags:
         - Key: Name
           Value: App Server
   ```
2. Save as task3.yaml

#### Step 3.3: Update Stack
1. Update stack with new template
2. Review changes (should show EC2 addition)
3. Execute update

#### Step 3.4: Verify
1. Check Resources tab for new EC2 instance
2. Optional: View instance in EC2 console

**Key Concept:** !Ref allows referencing other resources in the template.

### Task 4: Clean Up Resources

#### Step 4.1: Delete Stack
1. Select "Lab" stack in CloudFormation console
2. Choose "Delete"
3. Confirm deletion

#### Step 4.2: Monitor Deletion
1. View stack events during deletion
2. Resources deleted in reverse dependency order
3. Stack disappears when complete

**Important:** Deleting the stack removes all created resources.

## Key CloudFormation Concepts

### Template Structure
1. **Parameters**: User-provided values
2. **Resources**: AWS components to create
3. **Outputs**: Useful exported values

### Resource Dependencies
- Implicit: Through references (!Ref)
- Explicit: Using DependsOn attribute

### Update Behaviors
- **No interruption**: Add new resources
- **Some interruption**: Modify certain properties
- **Replacement**: Critical changes (e.g., instance type)

## Best Practices

1. **Use Parameters** for customizable values
2. **Leverage SSM Parameter Store** for AMI IDs
3. **Modularize templates** for complex infrastructures
4. **Validate templates** before deployment
5. **Use Change Sets** to preview modifications

## Troubleshooting Tips

1. **Check Events Tab**: Detailed error messages
2. **Validate Templates**: AWS CLI `validate-template`
3. **IAM Permissions**: Ensure proper capabilities
4. **Name Conflicts**: Avoid hardcoded names
5. **Region Compatibility**: Verify resource availability

## Conclusion

This lab demonstrated how to:
1. Deploy infrastructure using CloudFormation
2. Modify templates to add resources
3. Reference resources within templates
4. Clean up resources by deleting stacks

Key benefits of CloudFormation:
- **Reproducible deployments**
- **Version-controlled infrastructure**
- **Automated dependency management**
- **Consistent environments**

By adopting Infrastructure as Code with CloudFormation, organizations can achieve more reliable, auditable, and maintainable AWS environments.