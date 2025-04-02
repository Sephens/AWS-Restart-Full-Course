# AWS re/Start Fact Finding Exercises - Comprehensive Guide

## Table of Contents
1. [Python Concepts](#python-concepts)
2. [Database Fundamentals](#database-fundamentals)
3. [AWS Cloud Foundations Part 1](#aws-cloud-foundations-part-1)
4. [AWS Cloud Foundations Part 2](#aws-cloud-foundations-part-2)
5. [AWS Well-Architected Framework](#aws-well-architected-framework)
6. [AWS CloudFormation](#aws-cloudformation)
7. [AWS Billing](#aws-billing)
8. [Additional Notes and Examples](#additional-notes-and-examples)
9. [Frequently Asked Questions](#frequently-asked-questions)

---

## Python Concepts

### 1. Lists vs Tuples
- **List:** Mutable sequence (`[1, 2, 3]`)
- **Tuple:** Immutable sequence (`(1, 2, 3)`)
```python
# Example
shopping_list = ["milk", "eggs"]  # Can modify
coordinates = (40.7128, -74.0060)  # Fixed values
```

### 2. Namespaces
A mapping from names to objects (like a dictionary). Three types:
- **Local:** Inside function
- **Global:** Module level
- **Built-in:** Python built-ins

### 3. Local vs Global Variables
```python
global_var = "I'm global"

def func():
    local_var = "I'm local"
    print(global_var)  # Accessible
```

### 4. Python IDEs
- **PyCharm:** Full-featured IDE
- **VS Code:** Lightweight with extensions
- **Jupyter Notebook:** Interactive computing

### 5. Python Modules
Reusable code files (`math.py`, `datetime.py`). Example:
```python
import math
print(math.sqrt(16))  # 4.0
```

### 6. Arrays vs Lists
- **Lists:** Built-in, heterogeneous
- **Arrays:** From `array` module, homogeneous
```python
from array import array
numbers = array('i', [1, 2, 3])  # Typed array
```

### 7. Python Operators
- **Arithmetic:** `+`, `-`, `*`, `/`
- **Comparison:** `==`, `!=`, `>`
- **Logical:** `and`, `or`, `not`

---

## Database Fundamentals

### 1. Relational vs Non-Relational
| Feature | Relational (SQL) | Non-Relational (NoSQL) |
|---------|------------------|-----------------------|
| Structure | Tables | Documents/Key-Value/Graph |
| Schema | Fixed | Flexible |
| Example | MySQL, PostgreSQL | MongoDB, DynamoDB |

### 2. Indexes
Data structures improving search speed. Example:
```sql
CREATE INDEX idx_customer_name ON customers(name);
```

### 3. Primary vs Secondary Keys
- **Primary Key:** Unique identifier (e.g., `customer_id`)
- **Secondary Key:** Non-unique index for queries

### 4. Join Types
- **INNER JOIN:** Matching rows only
- **LEFT JOIN:** All left table + matching right
```sql
SELECT orders.*, customers.name 
FROM orders
LEFT JOIN customers ON orders.customer_id = customers.id;
```

### 5. DROP vs TRUNCATE
- **DROP:** Deletes table structure
- **TRUNCATE:** Removes all rows but keeps table

### 6. SQL Data Types
- Numeric: `INT`, `DECIMAL`
- String: `VARCHAR`, `TEXT`
- Temporal: `DATE`, `TIMESTAMP`

### 7. WHERE vs HAVING
- **WHERE:** Filters rows before grouping
- **HAVING:** Filters after grouping
```sql
SELECT department, AVG(salary) 
FROM employees 
GROUP BY department 
HAVING AVG(salary) > 50000;
```

---

## AWS Cloud Foundations Part 1

### 1. Cloud Service Models
| Model | Control Level | Example |
|-------|--------------|---------|
| IaaS | Infrastructure | EC2 |
| PaaS | Platform | Elastic Beanstalk |
| SaaS | Software | Salesforce |

### 2. Cloud Advantages
1. Cost savings
2. Global scalability
3. Elasticity
4. High availability
5. Security
6. Pay-as-you-go

### 3. Regions & AZs
- **Region:** Geographic area (e.g., us-east-1)
- **AZ:** Isolated data centers within a region

### 4. AWS Service Categories
1. Compute
2. Storage
3. Database
4. Networking
5. Security

### 5. Storage Types
| Type | Characteristics | AWS Service |
|------|----------------|------------|
| Object | Flat namespace, metadata | S3 |
| Block | Low latency, modifiable | EBS |

### 6. Compute Services
- **EC2:** Virtual servers
- **Lambda:** Serverless functions

### 7. Storage Services
- **S3:** Object storage
- **EBS:** Block storage for EC2

---

## AWS Cloud Foundations Part 2

### 1. Shared Responsibility Model
| AWS Responsibility | Customer Responsibility |
|--------------------|-------------------------|
| Hardware | Data |
| Global infrastructure | Access control |
| Software updates | Application security |

### 2. IAM Components
- **Role:** Temporary credentials
- **Policy:** Permission document (JSON)
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "s3:GetObject",
    "Resource": "*"
  }]
}
```

### 3. EC2 Instance Types
| Type | Use Case |
|------|----------|
| T3 | Burstable workloads |
| M5 | General purpose |
| C5 | Compute optimized |

### 4. VPC Networking
- **Public Subnet:** Route to Internet Gateway
- **Private Subnet:** No direct internet access

---

## AWS Well-Architected Framework

### Five Pillars
1. **Operational Excellence**
   - Run/monitor systems
   - Continuous improvement
2. **Security**
   - Least privilege
   - Data protection
3. **Reliability**
   - Fault tolerance
   - Recovery planning
4. **Performance Efficiency**
   - Right-sizing
   - Advanced technologies
5. **Cost Optimization**
   - Resource matching
   - Reserved capacity

### Cost Optimization Approaches
1. Right-sizing instances
2. Using Spot Instances
3. Implementing auto-scaling

---

## AWS CloudFormation

### Infrastructure as Code
```yaml
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-0abcdef1234567890
```

### JSON vs YAML
| Feature | JSON | YAML |
|---------|------|------|
| Readability | Lower | Higher |
| Comments | No | Yes |
| Syntax | Braces | Indentation |

---

## AWS Billing

### Support Plans
| Plan | Cost | Features |
|------|------|----------|
| Basic | Free | Documentation |
| Developer | $29+ | Business hours support |
| Enterprise | $15K+ | 15-min response |

### EC2 Pricing Models
1. **On-Demand:** Pay by the hour
2. **Reserved:** 1-3 year commitment
3. **Spot:** Bid for unused capacity

---

## Additional Notes and Examples

### Python Best Practices
```python
# Use list comprehension instead of loops
squares = [x**2 for x in range(10)]

# Context managers for resource handling
with open('file.txt') as f:
    content = f.read()
```

### Database Optimization
```sql
-- Composite index example
CREATE INDEX idx_name_age ON employees(last_name, age);
```

### CloudFormation Template Structure
```yaml
Parameters:
  InstanceType:
    Type: String
    Default: t2.micro

Resources:
  MyBucket:
    Type: AWS::S3::Bucket
```

---

## Frequently Asked Questions

**Q: When to use tuple vs list in Python?**
A: Use tuples for fixed data (coordinates), lists for mutable collections.

**Q: What's the advantage of NoSQL?**
A: Horizontal scaling and flexible schema for unstructured data.

**Q: How many Availability Zones should I use?**
A: At least 2 for production workloads for high availability.

**Q: What's the difference between IAM user and role?**
A: Users are permanent identities, roles are temporary assumed credentials.

**Q: How often should I review Well-Architected workloads?**
A: Quarterly for production, annually for others.

**Q: Can CloudFormation update existing resources?**
A: Yes, through stack updates if the resource supports it.

**Q: What's the break-even point for Reserved Instances?**
A: Typically 7-9 months of continuous usage.