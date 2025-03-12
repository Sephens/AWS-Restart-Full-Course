# Amazon DynamoDB - Database Fundamentals

## Overview
Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database service provided by Amazon Web Services (AWS). It is designed to deliver high performance, scalability, and flexibility for applications that require low-latency data access.

---

## Key Concepts

### 1. **Relational vs. Nonrelational (NoSQL) Databases**
   - **Relational Databases**:
     - Data is stored in tables with predefined columns and data types.
     - Relationships between tables are defined using foreign keys.
     - Performance is improved by scaling up (adding more compute or memory to a single server).
   - **Nonrelational (NoSQL) Databases**:
     - Data is stored in tables with a flexible schema.
     - Each item in a table can have a different number and type of attributes.
     - Performance is improved by scaling out (adding more servers to a cluster).

### 2. **DynamoDB as a NoSQL Database**
   - **Fully Managed**: AWS handles all underlying infrastructure, including compute and storage.
   - **Scalability**: Automatically scales to handle growing amounts of data and traffic.
   - **Redundancy**: Data is replicated across multiple AWS Regions for high availability.
   - **Low Latency**: Provides single-digit millisecond latency for data access.
   - **Security**: Integrates with AWS Identity and Access Management (IAM) for access control.
   - **Flexibility**: Supports various data types and allows each item to have different attributes.

---

## Core Concepts in DynamoDB

### 1. **Tables**
   - DynamoDB stores data in tables, similar to relational databases.
   - Each table must have a **primary key** defined at creation.
   - The primary key uniquely identifies each item in the table.

   **Example**:
   - A `Friends` table could use `FriendID` as the primary key to uniquely identify each friend.

### 2. **Attributes**
   - An **attribute** is a fundamental data element in DynamoDB, similar to a column in a relational database.
   - Attributes can be of different types (e.g., string, number, binary).
   - The primary key can consist of one or two attributes.

   **Example**:
   - In the `Friends` table, attributes could include `Name`, `Hobbies`, and `FavoriteColors`.

### 3. **Items**
   - An **item** is a group of attributes that is uniquely identifiable by its primary key.
   - Each item can have a different number and type of attributes.
   - This flexibility is a key difference between NoSQL and relational databases.

   **Example**:
   - In the `Friends` table, one item could have attributes like `Name`, `Hobbies`, and `FavoriteColors`, while another item could have additional attributes like `FavoriteGames` and `FavoriteFoods`.

### 4. **Primary Keys**
   - **Simple Primary Key**: Consists of a single attribute (partition key or hash key).
   - **Composite Primary Key**: Consists of two attributes (partition key and sort key).
   - The primary key uniquely identifies each item in the table.

   **Example**:
   - A simple primary key could be `FriendID`.
   - A composite primary key could be `FriendID` (partition key) and `FriendName` (sort key).

### 5. **Partitions**
   - DynamoDB stores data in **partitions**, which are automatically managed by the service.
   - The partition in which an item is stored is determined by its primary key.
   - As data grows, DynamoDB automatically adds more partitions to maintain performance.

   **Example**:
   - If the `Friends` table has two partitions, the `FriendID` value determines whether an item is stored in `Partition 1` or `Partition 2`.

---

## Advanced Concepts

### 1. **Global Tables**
   - **Global tables** allow you to replicate a DynamoDB table across multiple AWS Regions.
   - This provides low-latency access to data for globally distributed applications.
   - DynamoDB automatically handles data replication and conflict resolution.

   **Example**:
   - A `Friends` global table could have replicas in `us-west-2`, `us-east-1`, and `eu-central-1`. Users in different regions access the closest replica for faster performance.

---

## Checkpoint Questions

1. **Why are nonrelational (NoSQL) databases a good choice when you must get started quickly on a project?**
   - NoSQL databases have flexible schemas, so developers can start working with data immediately without needing to define complex table structures or relationships.

2. **Which table attribute is responsible for determining where item data is partitioned?**
   - The **partition key** determines where item data is stored in DynamoDB partitions.

3. **When you create items in a DynamoDB table, does each entry need to have the same attributes?**
   - No. DynamoDB allows each item to have different attributes, providing flexibility in data storage.

---

## Key Takeaways

- **Fully Managed**: DynamoDB is a fully managed NoSQL database service, meaning AWS handles all infrastructure management.
- **High Performance**: DynamoDB offers consistent, single-digit millisecond latency at any scale.
- **Scalability**: DynamoDB has no table size or throughput limits, making it suitable for applications of any size.
- **Global Tables**: DynamoDB global tables simplify data replication across multiple AWS Regions, improving performance and availability for globally distributed applications.

---

## Examples

### Example 1: Creating a DynamoDB Table
```sql
CREATE TABLE Friends (
    FriendID INT PRIMARY KEY,
    Name STRING,
    Hobbies STRING,
    FavoriteColors STRING
);
```
- In this example, `FriendID` is the primary key, and the table can store attributes like `Name`, `Hobbies`, and `FavoriteColors`.

### Example 2: Adding Items with Different Attributes
```json
{
    "FriendID": 1,
    "Name": "Martha Rivera",
    "Hobbies": "dancing, hiking, sailing",
    "FavoriteColors": "red, blue"
}

{
    "FriendID": 2,
    "Name": "Zhang Wei",
    "Hobbies": "painting, hiking, yoga",
    "FavoriteColors": "green, blue",
    "FavoriteGames": "chess",
    "FavoriteFoods": "pizza, chicken"
}
```
- In this example, the first item has three attributes, while the second item has five attributes. DynamoDB allows this flexibility.

### Example 3: Using Global Tables
- A global table named `Friends` is replicated across `us-west-2`, `us-east-1`, and `eu-central-1`. Users in Europe access the `eu-central-1` replica for faster performance.

---

## Conclusion
Amazon DynamoDB is a powerful NoSQL database service that offers high performance, scalability, and flexibility. Its fully managed nature, combined with features like global tables, makes it an excellent choice for modern applications that require low-latency data access and global availability.

---

## References
- [Amazon DynamoDB Documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [AWS re/Start Program](https://aws.amazon.com/training/restart/)