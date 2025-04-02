# AWS Organizations - Comprehensive Guide

## Table of Contents
- [AWS Organizations - Comprehensive Guide](#aws-organizations---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Introduction to AWS Organizations](#introduction-to-aws-organizations)
  - [Key Features and Benefits](#key-features-and-benefits)
  - [Security with AWS Organizations](#security-with-aws-organizations)
  - [Organizations Setup](#organizations-setup)
    - [Step-by-Step Implementation Guide](#step-by-step-implementation-guide)
  - [Naming Rules and Limits](#naming-rules-and-limits)
  - [Accessing AWS Organizations](#accessing-aws-organizations)
  - [Key Takeaways](#key-takeaways)
  - [Additional Notes and Examples](#additional-notes-and-examples)
  - [Frequently Asked Questions](#frequently-asked-questions)

---

## Introduction to AWS Organizations

AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. 

**Key Concepts:**
- **Organization (Root):** The parent container for all accounts in your organization
- **Organizational Units (OUs):** Containers for accounts within a root (can be nested)
- **Accounts:** Standard AWS accounts that contain your AWS resources
- **Policies:** Rules that can be attached to OUs or accounts to control access

**Example Structure:**
```
Root (Management Account)
├── Production OU
│   ├── App1 Account
│   ├── App2 Account
│   └── Database Account
├── Development OU
│   ├── Dev Account
│   └── Test Account
└── Sandbox OU
    └── Experiment Account
```

**How Policies Flow:**  
When you attach a policy to a node in the hierarchy, it affects all child nodes (accounts and OUs) beneath it. This enables centralized policy management.

---

## Key Features and Benefits

1. **Policy-Based Management**
   - Create Service Control Policies (SCPs) to centrally control AWS services
   - Example: Deny access to EC2 in all Dev accounts while allowing in Prod

2. **Group Account Management**
   - Organize accounts into OUs for logical grouping
   - Example: Create separate OUs for Finance, HR, and Engineering departments

3. **Account Management Through APIs**
   - Automate account creation and management
   - Example: Script to create new accounts with standardized configurations

4. **Consolidated Billing**
   - Single payment method for all accounts
   - Volume pricing discounts across all accounts
   - Example: Get discounted S3 pricing by combining usage across accounts

**Additional Benefits:**
- Centralized visibility and control
- Simplified compliance management
- Easier cost tracking and optimization

---

## Security with AWS Organizations

**IAM vs SCPs:**

| Feature | IAM Policies | SCPs |
|---------|-------------|------|
| Scope | Single account | Multiple accounts |
| Applies to | IAM users/groups/roles | Entire accounts |
| Can restrict root user? | No | Yes |
| Example Use | Allow Bob to access S3 buckets | Prevent all Dev accounts from creating EC2 instances |

**Important Notes:**
- SCPs don't replace IAM policies - they work together
- SCPs set the maximum permissions for accounts
- IAM policies further restrict within those boundaries

**Example SCP:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "ec2:TerminateInstances"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```
This SCP prevents terminating EC2 instances in any region except us-east-1 for all accounts it's applied to.

---

## Organizations Setup

### Step-by-Step Implementation Guide

**Step 1: Create Your Organization**
1. Sign in to AWS Management Console as root user
2. Navigate to AWS Organizations service
3. Click "Create organization"
4. Your current account becomes the management account

**Step 2: Add Accounts**
- **Option A:** Create new accounts
  - AWS generates root credentials for each
  - Best for new projects/greenfield deployments
- **Option B:** Invite existing accounts
  - Account owner must accept invitation
  - Best for migrating existing infrastructure

**Step 3: Create OUs**
1. In AWS Organizations console, select "Organize accounts"
2. Click "Create new"
3. Name your OU (e.g., "Production", "Development")
4. Drag accounts into appropriate OUs

**Step 4: Create and Apply SCPs**
1. Navigate to "Policies" section
2. Create new SCP using visual editor or JSON
3. Attach policy to root, OU, or specific account
4. Test policies using IAM Policy Simulator

**Pro Tip:** Start with allow-all SCPs and gradually restrict permissions as you understand your requirements.

---

## Naming Rules and Limits

**Naming Rules:**
- Unicode characters only
- Max 250 characters
- Must be unique within its scope

**Important Limits:**

| Entity | Limit |
|--------|-------|
| AWS accounts per organization | 4 (soft limit, can be increased) |
| Roots per organization | 1 |
| Policies per organization | 1,000 |
| SCP document size | 5,120 bytes |
| OU nesting depth | 5 levels |
| Invitations per day | 20 |
| Concurrent account creations | 5 |

**Workarounds for Limits:**
- For account limits: Contact AWS Support to increase
- For SCP size: Use wildcards and concise syntax
- For OU depth: Flatten structure where possible

---

## Accessing AWS Organizations

**Available Interfaces:**

1. **AWS Management Console**
   - Best for initial setup and visualization
   - User-friendly graphical interface
   - Access at: https://console.aws.amazon.com/organizations/

2. **AWS CLI**
   - Best for automation and scripting
   - Example commands:
     ```bash
     aws organizations create-organization
     aws organizations create-account --email admin@example.com --account-name "Prod Account"
     ```

3. **AWS SDKs**
   - Available for multiple languages (Python, Java, etc.)
   - Example Python code:
     ```python
     import boto3
     client = boto3.client('organizations')
     response = client.create_organizational_unit(
         ParentId='r-examplerootid111',
         Name='NewOU'
     )
     ```

4. **HTTPS API**
   - Direct programmatic access
   - Requires request signing
   - Documentation: https://docs.aws.amazon.com/organizations/latest/APIReference/Welcome.html

---

## Key Takeaways

1. **Centralized Management**
   - Single pane of glass for multiple accounts
   - Consistent policies across your AWS environment

2. **Security Benefits**
   - SCPs provide guardrails for all accounts
   - Prevent dangerous actions at scale

3. **Cost Optimization**
   - Consolidated billing simplifies financial management
   - Volume pricing discounts

4. **Compliance**
   - Enforce standards across teams
   - Simplify audit processes

**Best Practices:**
- Start with a simple OU structure and expand as needed
- Implement least privilege through SCPs
- Regularly review and update policies
- Use tagging standards across accounts

---

## Additional Notes and Examples

**Real-World Use Cases:**

1. **Enterprise IT Governance**
   - Finance OU: Restrict to only necessary services (e.g., block EC2)
   - Dev OU: Allow full access but with budget alarms
   - Prod OU: Strict change controls and monitoring

2. **SaaS Multi-Tenancy**
   - Separate account per customer
   - Apply tenant-specific policies
   - Isolate resources for security

3. **Regulatory Compliance**
   - HIPAA accounts with specific controls
   - PCI-DSS accounts with restricted access
   - Isolate environments by compliance requirement

**Troubleshooting Tips:**
- If policies aren't working as expected:
  1. Check policy inheritance flow
  2. Verify no conflicting SCPs
  3. Confirm IAM policies aren't overriding
  4. Use IAM Policy Simulator to test

**Integration with Other AWS Services:**
- AWS Control Tower: Implements best practices on top of Organizations
- AWS SSO: Centralized access management across accounts
- AWS Budgets: Cross-account cost monitoring

---

## Frequently Asked Questions

**Q: Can I move an account between OUs?**
A: Yes, accounts can be moved between OUs at any time. Policy changes may take a few minutes to propagate.

**Q: How does consolidated billing work?**
A: All charges flow to the management account, but each account maintains its own usage reports. Volume discounts apply to combined usage.

**Q: Can SCPs restrict the management account?**
A: No, SCPs don't apply to the management account. Protect this account with strong IAM policies and MFA.

**Q: What happens when I leave an organization?**
A: Your account becomes standalone again. Any SCPs no longer apply, but existing IAM policies remain.

**Q: How do I handle account limits?**
A: Contact AWS Support to increase your account limit. Typical enterprise organizations have hundreds of accounts.

**Q: Can I use AWS Organizations with AWS China regions?**
A: AWS Organizations works with standard AWS regions but has limited functionality in AWS China regions.

**Q: How do I monitor changes in my organization?**
A: Enable AWS CloudTrail on the management account to log all Organizations API calls.