# Café and Bakery - AWS Resource Optimization Guide

## Table of Contents
- [Café and Bakery - AWS Resource Optimization Guide](#café-and-bakery---aws-resource-optimization-guide)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Business Need: Cost Reduction](#business-need-cost-reduction)
  - [Current Architecture Analysis](#current-architecture-analysis)
  - [Optimization Strategies](#optimization-strategies)
    - [Method 1: Right-Sizing Instance Type](#method-1-right-sizing-instance-type)
    - [Method 2: Storage Optimization](#method-2-storage-optimization)
  - [Implementation Steps](#implementation-steps)
  - [Cost Savings Calculation](#cost-savings-calculation)
  - [Key Takeaways](#key-takeaways)
  - [Additional Notes and Examples](#additional-notes-and-examples)
    - [Real-World Implementation](#real-world-implementation)
    - [Troubleshooting Knowledge Base Entry](#troubleshooting-knowledge-base-entry)
  - [Frequently Asked Questions](#frequently-asked-questions)

---

## Project Overview

**Scenario:**  
The Café and Bakery business has migrated their database to Amazon RDS but still maintains legacy components on their EC2 instance. This project focuses on optimizing their AWS resource utilization to reduce costs while maintaining performance.

**Learning Objectives:**
- Translate business requirements into technical solutions
- Apply AWS cost optimization best practices
- Present technical solutions to non-technical stakeholders
- Implement frugal, resilient, and secure architectures

**Project Components:**
1. Analysis of current resource utilization
2. Identification of optimization opportunities
3. Implementation of cost-saving measures
4. Calculation of projected savings

---

## Business Need: Cost Reduction

**Stakeholder Dialogue:**
```
Sofia (Business Owner):
"I would like to reduce the cost of the AWS services that we use."

Olivia (AWS Solutions Architect):
"After migrating to RDS, we can:
1. Remove the local MariaDB database
2. Downsize the EC2 instance
3. Estimate savings using AWS Simple Monthly Calculator"
```

**Key Points:**
- Completed database migration to Amazon RDS
- Legacy database still installed but unused
- Current instance size may be over-provisioned
- Need to quantify potential savings

---

## Current Architecture Analysis

**Before Optimization:**
```
Café VPC
├── Availability Zone 1
│   └── Public Subnet
│       └── EC2 Instance (t2.small)
│           ├── Web Application
│           └── MariaDB (decommissioned)
└── Internet Gateway
```

**Problem Areas:**
1. **Redundant Components:** Local database after RDS migration
2. **Over-Provisioning:** t2.small instance for web app only
3. **Storage Waste:** Disk space allocated for unused database

**Visual Comparison:**
```diff
- t2.small ($0.023/hour) with unused database
+ t2.micro ($0.0116/hour) with clean installation
```

---

## Optimization Strategies

### Method 1: Right-Sizing Instance Type

**Considerations:**
- Current workload: Web application only
- CPU/Memory requirements after DB migration
- Performance metrics from CloudWatch

**Instance Type Comparison:**
| Type | vCPUs | Memory | Hourly Cost | Monthly Cost |
|------|-------|--------|-------------|--------------|
| t2.small | 1 | 2GB | $0.023 | ~$16.56 |
| t2.micro | 1 | 1GB | $0.0116 | ~$8.35 |

**Savings:** ~50% reduction in compute costs

### Method 2: Storage Optimization

**Steps:**
1. Uninstall MariaDB package:
   ```bash
   sudo yum remove mariadb-server
   ```
2. Resize EBS volume:
   ```bash
   # After creating snapshot and modifying volume in AWS Console
   sudo growpart /dev/xvda 1
   sudo resize2fs /dev/xvda1
   ```
3. Remove unused database files

**Potential Savings:**
- Reduced storage needs by 20-30GB
- Lower backup costs due to smaller volume size

---

## Implementation Steps

1. **Pre-Optimization Tasks:**
   - Take EBS snapshot for backup
   - Document current configuration
   - Notify stakeholders of maintenance window

2. **Database Cleanup:**
   ```bash
   # Stop database service
   sudo systemctl stop mariadb
   
   # Remove packages
   sudo yum remove mariadb-server
   
   # Clean up data files
   sudo rm -rf /var/lib/mysql
   ```

3. **Instance Resizing:**
   - Stop instance in AWS Console
   - Change instance type to t2.micro
   - Start instance and verify functionality

4. **Post-Optimization Verification:**
   - Test web application functionality
   - Monitor CloudWatch metrics
   - Update documentation

---

## Cost Savings Calculation

**Using AWS Simple Monthly Calculator:**

| Component | Before | After | Monthly Savings |
|-----------|--------|-------|-----------------|
| EC2 Instance (t2.small → t2.micro) | $16.56 | $8.35 | $8.21 |
| EBS Storage (50GB → 30GB) | $5.00 | $3.00 | $2.00 |
| Backups (50GB → 30GB) | $2.50 | $1.50 | $1.00 |
| **Total Monthly Savings** | | | **$11.21** |

**Annual Impact:** $134.52 savings (~46% reduction)

**Additional Benefits:**
- Simplified maintenance
- Reduced backup windows
- Better resource utilization

---

## Key Takeaways

1. **Right-Sizing is Continuous:**
   - Regularly review instance utilization
   - Use AWS Compute Optimizer recommendations
   - Monitor with CloudWatch metrics

2. **Clean Up After Migrations:**
   - Remove unused software
   - Reclaim storage space
   - Update security groups

3. **Quantify Your Savings:**
   - Use AWS pricing tools
   - Document before/after metrics
   - Report value to stakeholders

4. **Automate Where Possible:**
   - Instance scheduling for non-prod environments
   - Lifecycle policies for backups
   - Lambda functions for cleanup tasks

---

## Additional Notes and Examples

### Real-World Implementation

**Case Study: Online Retailer**
1. **Challenge:** Over-provisioned instances after holiday season
2. **Solution:**
   - Analyzed CloudWatch metrics
   - Downsized 12 t2.medium → t2.small
   - Implemented auto-scaling
3. **Result:** $3,200 annual savings

**Automation Script Example:**
```python
import boto3

def check_for_unused_volumes():
    ec2 = boto3.client('ec2')
    unused = []
    
    volumes = ec2.describe_volumes(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )['Volumes']
    
    for vol in volumes:
        if (time.now() - vol['CreateTime']).days > 30:
            unused.append(vol['VolumeId'])
    
    return unused
```

### Troubleshooting Knowledge Base Entry

**Category:** Automation & Optimization  
**Title:** EC2 Right-Sizing Procedure  
**Content:**
1. Check CloudWatch metrics (CPU < 30%, Network < 5MB)
2. Create AMI backup
3. Stop instance
4. Modify instance type
5. Verify application functionality
6. Monitor for 48 hours
7. Delete old AMI if no issues

---

## Frequently Asked Questions

**Q: How often should we review instance sizing?**
A: Monthly for production, quarterly for non-production environments.

**Q: What metrics indicate an instance is underutilized?**
A: CPU < 30%, memory < 50%, network < 10MB sustained for 14+ days.

**Q: Is t2.micro sufficient for production workloads?**
A: For low-traffic websites yes, but consider auto-scaling for variable loads.

**Q: How do we estimate storage requirements?**
A: Use `df -h` to check current usage, add 20-30% for growth.

**Q: What's the risk of downsizing too aggressively?**
A: Performance degradation during peak loads - always monitor after changes.

**Q: Can we automate this optimization process?**
A: Yes, using AWS Systems Manager and Lambda functions to:
1. Identify underutilized instances
2. Create backup
3. Downsize
4. Notify team

**Q: Should we consider Spot Instances for further savings?**
A: Only for fault-tolerant, interruptible workloads like batch processing.