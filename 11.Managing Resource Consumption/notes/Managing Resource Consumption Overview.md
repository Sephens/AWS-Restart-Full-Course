# Managing AWS Resource Consumption - Comprehensive Guide

## Table of Contents
- [Managing AWS Resource Consumption - Comprehensive Guide](#managing-aws-resource-consumption---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [AWS Organizations for Cost Management](#aws-organizations-for-cost-management)
    - [Consolidated Billing Features:](#consolidated-billing-features)
  - [Billing \& Cost Management Tools](#billing--cost-management-tools)
    - [Core Services:](#core-services)
  - [Tagging Strategy](#tagging-strategy)
    - [Effective Tagging Approach:](#effective-tagging-approach)
  - [Cost Optimization with Trusted Advisor](#cost-optimization-with-trusted-advisor)
    - [Key Checks:](#key-checks)
  - [AWS Support Plans](#aws-support-plans)
    - [Plan Comparison:](#plan-comparison)
  - [Hands-on Implementation](#hands-on-implementation)
    - [Lab: Managing Resources with Tagging](#lab-managing-resources-with-tagging)
  - [Key Takeaways](#key-takeaways)

---

## AWS Organizations for Cost Management

### Consolidated Billing Features:
- **Single Payment Method**: All accounts bill to master account
- **Volume Discounts**: Aggregate usage across all accounts
- **Cost Visibility**: Cross-account cost allocation reports

**Implementation Example**:
```bash
# Create organization
aws organizations create-organization --feature-set ALL

# Create organizational unit (OU)
aws organizations create-organizational-unit \
  --parent-id r-1234 \
  --name "Production"
```

**Best Practices**:
- Use Service Control Policies (SCPs) to enforce cost controls
- Implement AWS Budgets at OU level
- Enable Cost Explorer for visualization

---

## Billing & Cost Management Tools

### Core Services:
| Tool | Purpose | Example Use |
|------|---------|-------------|
| **Cost Explorer** | Visualization & forecasting | Identify EC2 spending trends |
| **AWS Budgets** | Alert when exceeding thresholds | Get alerts at 80% of monthly budget |
| **Cost & Usage Reports** | Detailed line-item data | Finance department reporting |
| **Savings Plans** | Commit to usage for discounts | 1-3 year EC2/Fargate commitments |

**Sample Budget Alert**:
```bash
aws budgets create-budget \
  --account-id 123456789012 \
  --budget '{
    "BudgetName": "Monthly-Production-Limit",
    "BudgetLimit": {"Amount": "5000", "Unit": "USD"},
    "CostFilters": {"Service": ["AmazonEC2", "AmazonRDS"]},
    "TimeUnit": "MONTHLY",
    "BudgetType": "COST"
  }' \
  --notifications '[
    {
      "NotificationType": "ACTUAL",
      "ComparisonOperator": "GREATER_THAN",
      "Threshold": 80,
      "NotificationState": "ALARM"
    }
  ]'
```

---

## Tagging Strategy

### Effective Tagging Approach:
1. **Required Tags** (enforced via SCPs):
   - `CostCenter`
   - `Environment` (prod/dev/test)
   - `Owner`

2. **Automated Tagging**:
   ```bash
   # Tag new EC2 instances automatically
   aws config put-config-rule \
     --config-rule '{
       "ConfigRuleName": "ec2-auto-tag",
       "Source": {
         "Owner": "AWS",
         "SourceIdentifier": "REQUIRED_TAGS"
       },
       "InputParameters": "{\"tag1Key\":\"CostCenter\",\"tag2Key\":\"Owner\"}"
     }'
   ```

3. **Cost Allocation**:
   - Generate reports filtered by tags
   - Identify untagged resources

**Sample Tag-Based Report Query**:
```sql
SELECT line_item_product_code, SUM(line_item_unblended_cost) 
FROM cost_and_usage_report
WHERE resource_tags_user_Environment = 'production'
GROUP BY line_item_product_code
```

---

## Cost Optimization with Trusted Advisor

### Key Checks:
| Category | Savings Potential | Example |
|----------|-------------------|---------|
| **Idle Resources** | Up to 70% | Unused ELBs |
| **Underutilized Instances** | 30-50% | Right-size EC2 |
| **Reserved Instances** | Up to 75% | Convert on-demand |

**Automating Recommendations**:
```python
import boto3
support = boto3.client('support')

checks = support.describe_trusted_advisor_checks(language='en')

for check in checks['checks']:
    if 'cost' in check['category']:
        result = support.describe_trusted_advisor_check_result(
            checkId=check['id']
        )
        print(f"{check['name']}: {result['result']['resourcesSummary']['resourcesFlagged']} issues")
```

---

## AWS Support Plans

### Plan Comparison:
| Feature | Basic | Developer | Business | Enterprise |
|---------|-------|-----------|----------|------------|
| **Cost** | Free | $29-$100/mo | $100-$15,000/mo | $15,000+/mo |
| **Response Time** | N/A | 12-24 hrs | <1 hr critical | <15 min critical |
| **Architecture Guidance** | No | Limited | Full | Full + TAM |

**When to Upgrade**:
- Production workloads → Business tier
- Mission-critical systems → Enterprise
- 24/7 operations → Enterprise with rapid response

---

## Hands-on Implementation

### Lab: Managing Resources with Tagging
1. **Create Tag Policy**:
   ```bash
   aws organizations create-policy \
     --name "Tagging-Compliance" \
     --description "Enforces required tags" \
     --content '{
       "tags": {
         "CostCenter": {"tag_key": {"@@assign": "CostCenter"}},
         "Owner": {"tag_key": {"@@assign": "Owner"}}
       }
     }'
   ```

2. **Apply to OU**:
   ```bash
   aws organizations attach-policy \
     --policy-id p-12345678 \
     --target-id ou-1234-567890
   ```

3. **Verify Compliance**:
   ```bash
   aws resourcegroupstaggingapi get-compliance-summary \
     --target-id ou-1234-567890
   ```

---

## Key Takeaways

1. **Centralized Governance**:
   - AWS Organizations enables cross-account cost management
   - SCPs prevent budget overruns

2. **Visibility**:
   - Tagging provides resource-level cost attribution
   - Cost Explorer visualizes spending patterns

3. **Optimization**:
   - Trusted Advisor identifies savings opportunities
   - Savings Plans reduce compute costs

4. **Support Alignment**:
   - Match support plan to workload criticality
   - Enterprise support provides architectural reviews

**Implementation Roadmap**:
1. Set up Organizations with OUs
2. Implement mandatory tagging
3. Configure budget alerts
4. Run monthly Trusted Advisor reviews
5. Establish cost allocation reports

**Final Note**: Regular cost reviews should be part of operational cadence, with AWS Cost Anomaly Detection providing automated monitoring for unexpected spending patterns.