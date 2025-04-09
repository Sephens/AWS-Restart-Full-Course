# AWS Resource Optimization Lab Guide

## Lab Overview
This lab demonstrates how to optimize AWS resources to reduce costs while maintaining performance. You'll:
- Remove unnecessary software from an EC2 instance
- Downsize the instance type
- Calculate cost savings using AWS Pricing Calculator

## Lab Objectives
After completing this lab, you will be able to:
- Identify optimization opportunities in AWS resources
- Modify EC2 instance configurations
- Use AWS CLI for resource management
- Estimate costs with AWS Pricing Calculator
- Calculate potential savings from optimizations

## Architecture
The environment consists of:
- Café web application running on EC2 (originally t3.small)
- Previously migrated database (now on RDS)
- CLI Host instance for management tasks

## Detailed Step-by-Step Guide

### Task 1: Optimize the Website

#### Step 1.1: Connect to Café Instance
**Windows Users:**
1. Download PPK file
2. Use PuTTY to SSH into CafeInstance
3. Authenticate with the PPK key

**Mac/Linux Users:**
1. Download PEM file
2. Set permissions: `chmod 400 labsuser.pem`
3. SSH: `ssh -i labsuser.pem ec2-user@<public-ip>`

#### Step 1.2: Configure AWS CLI
1. Discover region:
   ```bash
   curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region
   ```

2. Configure AWS CLI:
   ```bash
   aws configure
   ```
   Enter:
   - Access Key ID (from lab details)
   - Secret Access Key (from lab details)
   - Default region name (from above)
   - Default output format: json

#### Step 1.3: Remove Unused Database
1. Stop MariaDB service:
   ```bash
   sudo systemctl stop mariadb
   ```

2. Uninstall MariaDB:
   ```bash
   sudo yum -y remove mariadb-server
   ```
   Verify "Complete!" message

#### Step 1.4: Downsize Instance
1. Connect to CLI Host instance (repeat connection steps)

2. Get CafeInstance ID:
   ```bash
   aws ec2 describe-instances --filters "Name=tag:Name,Values=CafeInstance" --query "Reservations[*].Instances[*].InstanceId"
   ```

3. Stop instance:
   ```bash
   aws ec2 stop-instances --instance-ids <instance-id>
   ```

4. Change instance type:
   ```bash
   aws ec2 modify-instance-attribute --instance-id <instance-id> --instance-type "{\"Value\": \"t3.micro\"}"
   ```

5. Start instance:
   ```bash
   aws ec2 start-instances --instance-ids <instance-id>
   ```

6. Verify new configuration:
   ```bash
   aws ec2 describe-instances --instance-ids <instance-id> --query "Reservations[*].Instances[*].[InstanceType,PublicDnsName,PublicIpAddress,State.Name]"
   ```

7. Test website:
   - Access `http://<new-public-dns>/cafe`
   - Verify all functionality

### Task 2: Calculate Cost Savings

#### Step 2.1: Before Optimization Costs
1. Open AWS Pricing Calculator: https://calculator.aws
2. Create new estimate
3. Add EC2 service:
   - Region: (your lab region)
   - OS: Linux
   - Instance: t3.small
   - Pricing: On-Demand
   - Storage: 40GB gp2
4. Add RDS service:
   - Engine: MariaDB
   - Instance: db.t3.micro
   - Storage: 20GB gp2
5. Save estimate and record total (~$35.50)

#### Step 2.2: After Optimization Costs
1. Edit EC2 service in calculator:
   - Change to t3.micro instance
   - Reduce storage to 20GB
2. Save estimate and record total (~$25.18)

#### Step 2.3: Calculate Savings
```
Before optimization: $35.50/month
After optimization:  $25.18/month
Savings:            $10.32/month (29% reduction)
```

## Key Optimization Techniques

1. **Right-Sizing**:
   - Downsize instances when workload decreases
   - Monitor CPU/memory usage to identify opportunities
   - Use AWS Compute Optimizer for recommendations

2. **Resource Cleanup**:
   - Remove unused software
   - Delete unattached storage volumes
   - Terminate unused instances

3. **Storage Optimization**:
   - Right-size EBS volumes
   - Implement lifecycle policies
   - Use appropriate storage classes

## Best Practices

1. **Continuous Monitoring**:
   - Use CloudWatch metrics
   - Set up billing alerts
   - Regularly review AWS Cost Explorer

2. **Automated Scaling**:
   - Implement Auto Scaling groups
   - Use scheduled scaling for predictable workloads
   - Consider Spot Instances for fault-tolerant workloads

3. **Tagging Strategy**:
   - Tag resources by purpose, owner, environment
   - Use tags for cost allocation
   - Implement tag-based policies

## Troubleshooting Tips

1. **Instance Modification Issues**:
   - Verify instance is stopped before modifying type
   - Check for instance limits in your account
   - Confirm new instance type is available in your region

2. **Website Verification**:
   - Check system logs if website doesn't come up
   - Verify security groups allow HTTP traffic
   - Confirm web server service is running

3. **Pricing Calculator**:
   - Double-check region selection
   - Verify all services are accounted for
   - Compare with actual billing data

## Conclusion

This lab demonstrated how to:
1. Identify optimization opportunities
2. Remove unused resources
3. Right-size EC2 instances
4. Calculate cost savings

Key takeaways:
- Regular optimization can significantly reduce costs
- AWS provides tools to identify savings opportunities
- Changes should be validated for performance impact

By implementing these practices, organizations can maintain optimal performance while minimizing AWS costs.