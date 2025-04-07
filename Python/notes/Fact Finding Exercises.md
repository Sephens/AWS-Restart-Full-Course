# AWS re/Start Fact Finding Exercises

Below is a comprehensive markdown document covering all the fact-finding exercises from the AWS re/Start curriculum, with detailed explanations, examples, and additional notes for each question.

---

## Python Fact Finding Exercise

### 1. Define a **list** and **tuple** in Python. Provide some examples.

**List**: A list is a mutable, ordered collection of items. Items can be of different data types. Lists are defined using square brackets `[]`.

**Example**:
```python
my_list = [1, 2, 3, "apple", "banana"]
my_list.append("cherry")  # Lists are mutable
print(my_list)  # Output: [1, 2, 3, "apple", "banana", "cherry"]
```

**Tuple**: A tuple is an immutable, ordered collection of items. Tuples are defined using parentheses `()`.

**Example**:
```python
my_tuple = (1, 2, 3, "apple", "banana")
# my_tuple.append("cherry")  # This would raise an error since tuples are immutable
print(my_tuple)  # Output: (1, 2, 3, "apple", "banana")
```

**Note**: Lists are used when you need a collection that can change, while tuples are used for fixed collections (e.g., coordinates, dates).

---

### 2. What is a **namespace** in Python?

A **namespace** is a system that ensures names in a program are unique and can be used without conflict. It maps names to objects (e.g., variables, functions, classes). Python has the following namespaces:

- **Local**: Names defined inside a function.
- **Enclosing**: Names in the local scope of enclosing functions (for nested functions).
- **Global**: Names defined at the top level of a module or script.
- **Built-in**: Names preassigned in Python (e.g., `print`, `len`).

**Example**:
```python
x = 10  # Global namespace

def my_func():
    y = 20  # Local namespace
    print(x, y)  # Accesses global 'x' and local 'y'

my_func()  # Output: 10 20
```

---

### 3. What is the difference between a **local variable** and a **global variable**?

- **Local Variable**: Defined inside a function and accessible only within that function. It exists only while the function is executing.
  
  **Example**:
  ```python
  def my_func():
      local_var = "I am local"
      print(local_var)  # Accessible here

  my_func()
  # print(local_var)  # Error: local_var is not accessible outside the function
  ```

- **Global Variable**: Defined outside any function and accessible throughout the module or script. Use the `global` keyword to modify it inside a function.

  **Example**:
  ```python
  global_var = "I am global"

  def my_func():
      global global_var
      global_var = "Modified global"
      print(global_var)  # Output: "Modified global"

  my_func()
  print(global_var)  # Output: "Modified global"
  ```

---

### 4. What is an IDE? Mention some common IDEs that could be used with Python.

An **IDE (Integrated Development Environment)** is a software application that provides comprehensive tools for coding, debugging, and testing. Common Python IDEs include:

- **PyCharm**: A powerful IDE with features like code completion, debugging, and support for web frameworks.
- **VS Code**: A lightweight, extensible editor with Python support via extensions.
- **Jupyter Notebook**: Ideal for data science, allowing interactive coding and visualization.
- **Spyder**: Designed for scientific computing, with tools like variable explorer and IPython console.
- **IDLE**: Python's built-in IDE, suitable for beginners.

---

### 5. What are **modules** in Python? Provide some examples.

A **module** is a file containing Python code (functions, classes, variables) that can be imported and reused in other programs. Modules help organize code and promote reusability.

**Example**:
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

# main.py
import my_module
print(my_module.greet("Alice"))  # Output: "Hello, Alice!"
```

**Built-in Modules**:
- `math`: Mathematical functions.
- `os`: Operating system interactions.
- `datetime`: Date and time operations.

---

### 6. What is the difference between an **array** and a **list**?

- **List**: A built-in Python data structure that can hold heterogeneous data types (e.g., `[1, "apple", 3.14]`). It is flexible and dynamically sized.
  
- **Array**: Requires the `array` module and holds homogeneous data types (e.g., all integers or floats). It is more memory-efficient for large datasets of the same type.

**Example**:
```python
import array as arr
my_array = arr.array('i', [1, 2, 3])  # 'i' denotes integer type
my_list = [1, "apple", 3.14]
```

**Note**: For numerical computations, libraries like NumPy provide advanced array operations.

---

### 7. What are **operators**? Provide some examples.

Operators are symbols that perform operations on variables and values. Types include:

- **Arithmetic**: `+`, `-`, `*`, `/`, `%` (modulus).
- **Comparison**: `==`, `!=`, `>`, `<`.
- **Logical**: `and`, `or`, `not`.
- **Assignment**: `=`, `+=`, `-=`.
- **Identity**: `is`, `is not` (checks memory location).
- **Membership**: `in`, `not in` (checks presence in a sequence).

**Example**:
```python
x = 10
y = 20
print(x + y)  # Arithmetic: 30
print(x == y)  # Comparison: False
print(x < y and y > 15)  # Logical: True
```

---

## Databases Fact Finding Exercise

### 1. What is the difference between a **relational** and a **non-relational database**?

- **Relational Database (RDBMS)**: Stores data in tables with rows and columns. Uses SQL for queries. Supports ACID transactions (Atomicity, Consistency, Isolation, Durability). Examples: MySQL, PostgreSQL.
  
- **Non-Relational Database (NoSQL)**: Stores data in flexible formats (e.g., key-value, document, graph). Scales horizontally and is schema-less. Examples: MongoDB (document), Redis (key-value).

**Use Case**: RDBMS for structured data with complex queries; NoSQL for unstructured or rapidly changing data.

---

### 2. What are **indexes**?

Indexes are database structures that improve query performance by allowing faster data retrieval. They work like a book's index, pointing to the location of data.

**Example**:
```sql
CREATE INDEX idx_customer_name ON customers (name);
```
**Note**: Overuse can slow down write operations.

---

### 3. What are **primary keys** and **secondary keys**?

- **Primary Key**: A unique identifier for a table row. Cannot be `NULL`. Example: `customer_id`.
- **Secondary Key (Foreign Key)**: A field in one table that references the primary key of another table. Enforces referential integrity.

**Example**:
```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

---

### 4. What are **inner joins** and **outer joins**?

- **Inner Join**: Returns rows where there is a match in both tables.
  
  ```sql
  SELECT orders.order_id, customers.name
  FROM orders
  INNER JOIN customers ON orders.customer_id = customers.customer_id;
  ```

- **Outer Join**: Returns all rows from one table and matched rows from the other. Types:
  - **LEFT JOIN**: All rows from the left table.
  - **RIGHT JOIN**: All rows from the right table.
  - **FULL JOIN**: All rows from both tables.

---

### 5. What is the difference between **DROP TABLE** and **TRUNCATE TABLE**?

- `DROP TABLE`: Deletes the table and its structure from the database.
  
  ```sql
  DROP TABLE customers;
  ```

- `TRUNCATE TABLE`: Deletes all rows but retains the table structure.
  
  ```sql
  TRUNCATE TABLE customers;
  ```

**Note**: `TRUNCATE` is faster and uses fewer system resources.

---

### 6. What are the different **data types in SQL**?

Common SQL data types include:

- **Integer**: `INT`, `BIGINT`.
- **Decimal**: `FLOAT`, `DECIMAL`.
- **Text**: `VARCHAR`, `TEXT`.
- **Date/Time**: `DATE`, `TIMESTAMP`.
- **Boolean**: `BOOLEAN`.

**Example**:
```sql
CREATE TABLE employees (
    id INT,
    name VARCHAR(100),
    salary DECIMAL(10, 2),
    hire_date DATE
);
```

---

### 7. Explain the **WHERE** and **HAVING** clauses.

- `WHERE`: Filters rows before grouping or aggregation.
  
  ```sql
  SELECT * FROM employees WHERE salary > 50000;
  ```

- `HAVING`: Filters groups after aggregation (used with `GROUP BY`).
  
  ```sql
  SELECT department, AVG(salary) 
  FROM employees 
  GROUP BY department 
  HAVING AVG(salary) > 60000;
  ```

---

## AWS Cloud Foundations – One Fact Finding Exercise

### 1. Define what **IaaS, PaaS** and **SaaS** is.

- **IaaS (Infrastructure as a Service)**: Provides virtualized computing resources over the internet (e.g., EC2, VPC).
- **PaaS (Platform as a Service)**: Provides platforms for developing and deploying applications (e.g., Elastic Beanstalk).
- **SaaS (Software as a Service)**: Delivers software applications over the internet (e.g., Gmail, Salesforce).

---

### 2. Provide **6 advantages** of cloud computing.

1. **Cost Savings**: Pay-as-you-go model reduces capital expenditure.
2. **Scalability**: Easily scale resources up or down.
3. **Flexibility**: Access services from anywhere.
4. **Reliability**: High availability and disaster recovery.
5. **Security**: Advanced security measures and compliance.
6. **Performance**: Global infrastructure ensures low latency.

---

### 3. Define what an **AWS region** and an **Availability Zone** is.

- **AWS Region**: A geographical area with multiple data centers (e.g., `us-east-1`).
- **Availability Zone (AZ)**: Isolated locations within a region for fault tolerance (e.g., `us-east-1a`).

**Note**: AZs are connected via high-speed networks.

---

### 4. List all the **AWS regions**.

As of 2023, AWS has 31 regions, including:
- `us-east-1` (N. Virginia)
- `eu-west-1` (Ireland)
- `ap-southeast-1` (Singapore)
- `sa-east-1` (São Paulo)

**Reference**: [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

---

### 5. What are the categories in which the **AWS services are grouped**?

AWS services are grouped into:
- **Compute**: EC2, Lambda.
- **Storage**: S3, EBS.
- **Database**: RDS, DynamoDB.
- **Networking**: VPC, Route 53.
- **Security**: IAM, KMS.
- **Machine Learning**: SageMaker, Rekognition.

---

### 6. What is the difference between **object storage** and **block storage**?

- **Object Storage (S3)**: Stores data as objects with metadata. Ideal for unstructured data (e.g., images, videos).
- **Block Storage (EBS)**: Stores data in fixed-size blocks. Used for databases and file systems.

**Example**: S3 for backups, EBS for EC2 instances.

---

### 7. List two AWS **compute services** and explain them.

- **EC2 (Elastic Compute Cloud)**: Virtual servers in the cloud. Scalable and customizable.
- **Lambda**: Serverless compute service. Runs code in response to events.

**Use Case**: EC2 for long-running apps, Lambda for event-driven tasks.

---

### 8. List two AWS **storage services** and explain them.

- **S3 (Simple Storage Service)**: Scalable object storage for any data type.
- **EBS (Elastic Block Store)**: Persistent block storage for EC2 instances.

**Example**: S3 for static websites, EBS for database storage.

---

## AWS Cloud Foundations – Two Fact Finding Exercise

### 1. Explain the **AWS Shared responsibility model**.

- **AWS Responsibility**: Security "of" the cloud (hardware, software, infrastructure).
- **Customer Responsibility**: Security "in" the cloud (data, access management, OS updates).

**Example**: AWS manages physical data centers; customers manage IAM policies.

---

### 2. Explain an **AWS Identity and Access Management (IAM) Role**.

An IAM Role is an identity with permissions that can be assumed by AWS services or users. It does not have long-term credentials.

**Example**: Assigning an EC2 instance a role to access S3.

---

### 3. Explain an **AWS Identity and Access Management (IAM) Policy**.

An IAM Policy is a document that defines permissions for users, groups, or roles. It uses JSON format.

**Example**:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket/*"
        }
    ]
}
```

---

### 4. Describe an **Amazon Machine Image (AMI)**.

An AMI is a template for launching EC2 instances. It includes the OS, software, and configuration.

**Example**: Using an AMI with pre-installed Apache for a web server.

---

### 5. List the different **Amazon EC2 instance types** with use cases for each type.

- **General Purpose (t3, m5)**: Web servers, small databases.
- **Compute Optimized (c5)**: High-performance computing.
- **Memory Optimized (r5)**: In-memory databases.
- **Storage Optimized (i3)**: NoSQL databases.

---

### 6. Explain **Amazon Virtual Private Cloud (VPC)**.

A VPC is a logically isolated section of AWS where you can launch resources. It provides control over networking (IP ranges, subnets, gateways).

**Example**: Creating a VPC with public and private subnets for a web app.

---

### 7. Differentiate between a **Public** and a **Private** subnet.

- **Public Subnet**: Has a route to the internet via an Internet Gateway (IGW). Hosts resources like web servers.
- **Private Subnet**: No direct internet access. Hosts databases or backend services.

**Note**: Use NAT Gateway for private subnets to access the internet.

---

## AWS Well-Architected Framework Fact Finding Exercise

### 1. What are the **five pillars** of the Well Architected Framework (WAF)?

1. **Operational Excellence**: Run and monitor systems effectively.
2. **Security**: Protect data and systems.
3. **Reliability**: Recover from failures.
4. **Performance Efficiency**: Use resources efficiently.
5. **Cost Optimization**: Avoid unnecessary costs.

---

### 2. What are the 3 areas of **operational excellence** in the cloud?

1. **Prepare**: Understand workloads and business outcomes.
2. **Operate**: Monitor and improve processes.
3. **Evolve**: Learn from experiences and automate.

---

### 3. What are the design principles that **strengthen system security**?

- **Least Privilege**: Grant minimal permissions.
- **Defense in Depth**: Multiple security layers.
- **Encryption**: Protect data at rest and in transit.
- **Incident Response**: Prepare for security events.

---

### 4. What are the design principles that **increase reliability**?

- **Automated Recovery**: Self-healing systems.
- **Horizontal Scaling**: Distribute workload.
- **Assume Failure**: Design for component failures.

---

### 5. What are the areas to focus on to achieve **performance efficiency** in the cloud?

- **Compute**: Right-sizing instances.
- **Storage**: Choose appropriate storage types.
- **Database**: Optimize queries and indexing.
- **Networking**: Use CDN and edge locations.

---

### 6. What are the different approaches to using AWS resources in a **cost-effective manner**?

- **Right-Sizing**: Match resources to workload needs.
- **Reserved Instances**: Discounts for long-term use.
- **Spot Instances**: Use spare capacity at lower cost.
- **Monitor Spending**: Use AWS Cost Explorer.

---

## AWS CloudFormation Fact Finding Exercise

### 1. What is **Configuration Orchestration**?

Configuration Orchestration automates the deployment and management of infrastructure. Tools like AWS CloudFormation define infrastructure as code.

**Example**: Deploying a VPC, subnets, and EC2 instances with a single template.

---

### 2. What is **Configuration Management**? List some commonly used tools for Configuration Management.

Configuration Management ensures systems are configured consistently. Tools include:

- **Ansible**: Agentless, YAML-based.
- **Chef**: Uses "recipes" for configuration.
- **Puppet**: Declarative language for system configuration.

---

### 3. What is **Continuous Integration**?

Continuous Integration (CI) is the practice of merging code changes frequently and automatically testing them. Tools: Jenkins, AWS CodePipeline.

---

### 4. What is **Continuous Delivery**?

Continuous Delivery (CD) extends CI by automatically deploying code to staging or production after passing tests.

---

### 5. What is **AWS CloudFormation**? List 3 advantages of CloudFormation.

AWS CloudFormation is a service for defining and provisioning infrastructure as code.

**Advantages**:
1. **Automation**: Deploy resources consistently.
2. **Version Control**: Track changes to infrastructure.
3. **Cost Management**: Estimate costs before deployment.

---

### 6. What is **JSON** and **YAML**? List 3 differences between them.

- **JSON (JavaScript Object Notation)**: Lightweight data interchange format. Uses `{}` and `[]`.
- **YAML (YAML Ain't Markup Language)**: Human-readable data serialization. Uses indentation.

**Differences**:
1. **Syntax**: JSON uses braces; YAML uses indentation.
2. **Readability**: YAML is more human-friendly.
3. **Comments**: YAML supports comments; JSON does not.

---

### 7. What is a **stack** in AWS CloudFormation?

A **stack** is a collection of AWS resources created and managed as a single unit via a CloudFormation template.

**Example**: A stack could include an EC2 instance, an RDS database, and an S3 bucket.

---

## AWS Billing Fact Finding Exercise

### 1. List the different types of **AWS support plans**.

1. **Basic**: Free, limited support.
2. **Developer**: $29/month, business hours support.
3. **Business**: Starts at $100/month, 24/7 support.
4. **Enterprise**: Custom pricing, dedicated Technical Account Manager (TAM).

---

### 2. Explain the **AWS Simple Monthly Calculator**.

A tool to estimate monthly AWS costs based on service usage. Helps plan budgets and compare pricing options.

**Link**: [AWS Pricing Calculator](https://calculator.aws/)

---

### 3. List and explain the different **Amazon EC2 pricing models**.

1. **On-Demand**: Pay per hour/second with no long-term commitment.
2. **Reserved Instances**: Discounts for 1- or 3-year commitments.
3. **Spot Instances**: Bid for unused capacity at lower prices.
4. **Savings Plans**: Flexible pricing for consistent usage.

**Example**: Use Reserved Instances for steady workloads, Spot Instances for fault-tolerant tasks.

---

## Conclusion

This document provides detailed answers to all the fact-finding exercises in the AWS re/Start curriculum, along with examples and additional notes for clarity. Use it as a reference to deepen your understanding of Python, databases, AWS services, and cloud concepts.