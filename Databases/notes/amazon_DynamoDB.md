# Amazon DynamoDB - Comprehensive Notes and Examples

This document provides a detailed summary of the "Amazon DynamoDB" module, including key concepts, features, use cases, and examples.

---

## **Key Takeaways**
1. **DynamoDB**: A fully managed, serverless, **NoSQL database** designed for high performance, scalability, and low latency.
2. **Key Features**:
   - **Flexible Schema**: Each item can have different attributes.
   - **High Availability**: Data is replicated across multiple Availability Zones (AZs).
   - **Global Tables**: Automatically replicate data across AWS Regions.
   - **Scalability**: Automatically scales to handle millions of requests per second.
3. **Core Concepts**:
   - **Tables**: Store data in a flexible, schema-less structure.
   - **Items**: Individual records in a table, identified by a **primary key**.
   - **Attributes**: Data elements within an item (similar to columns in relational databases).
   - **Partitioning**: Data is distributed across partitions based on the **partition key**.

---

## **DynamoDB Overview**

### **What is DynamoDB?**
- A **NoSQL database** that stores data in key-value pairs.
- **Fully Managed**: AWS handles infrastructure, scaling, backups, and maintenance.
- **Serverless**: No need to provision or manage servers.
- **Use Cases**:
  - Real-time applications (e.g., gaming, IoT).
  - High-traffic web applications.
  - Applications requiring low-latency data access.

### **Key Features**
| Feature | Description |
|---------|-------------|
| **Flexible Schema** | Each item in a table can have different attributes. |
| **High Performance** | Single-digit millisecond latency for read/write operations. |
| **Scalability** | Automatically scales to handle millions of requests per second. |
| **Global Tables** | Replicate data across multiple AWS Regions for low-latency access. |
| **Security** | Data is encrypted at rest and in transit. |

---

## **Core Concepts**

### **Tables**
- **Definition**: A collection of items (similar to a table in relational databases).
- **Primary Key**: Uniquely identifies each item in the table.
  - **Simple Primary Key**: Consists of a single attribute (partition key).
  - **Composite Primary Key**: Consists of two attributes (partition key + sort key).

### **Items**
- **Definition**: A single record in a table, identified by a primary key.
- **Attributes**: Data elements within an item (e.g., name, age, hobbies).
- **Flexibility**: Each item can have different attributes.

### **Attributes**
- **Definition**: Data elements within an item (similar to columns in relational databases).
- **Types**: Strings, numbers, binary data, lists, maps, etc.
- **Example**:
  ```json
  {
    "FriendID": "123",
    "Name": "Martha Rivera",
    "Hobbies": ["dancing", "hiking", "sailing"],
    "FavoriteColors": ["red", "blue"]
  }
  ```

### **Partitioning**
- **Definition**: Data is distributed across partitions based on the **partition key**.
- **How It Works**:
  - DynamoDB applies a hash function to the partition key to determine the partition.
  - Data is evenly distributed across partitions for optimal performance.
- **Example**:
  - Partition Key: `FriendID`.
  - Items with `FriendID = 1` → Partition 1.
  - Items with `FriendID = 2` → Partition 2.

---

## **Global Tables**

### **What are Global Tables?**
- **Definition**: A feature that automatically replicates data across multiple AWS Regions.
- **Benefits**:
  - **Low Latency**: Users access the nearest replica.
  - **High Availability**: Data is available even if an entire Region fails.
  - **Automatic Sync**: Data is automatically synchronized across Regions.

### **Example**
- **Scenario**: A global application with users in the US, Europe, and Asia.
- **Setup**:
  - Create a global table with replicas in `us-east-1`, `eu-central-1`, and `ap-southeast-1`.
- **Result**:
  - Users in Europe access the `eu-central-1` replica.
  - Users in Asia access the `ap-southeast-1` replica.

---

## **Examples**

### **Creating a DynamoDB Table**
1. **Steps**:
   - Navigate to AWS Management Console → DynamoDB → **Create table**.
   - Enter table name (e.g., `Friends`).
   - Define primary key (e.g., `FriendID` as partition key).
   - Click **Create**.
2. **Result**:
   - A table named `Friends` is created with a simple primary key.

### **Adding Items to a Table**
1. **Steps**:
   - In DynamoDB console, select the `Friends` table → **Create item**.
   - Add attributes (e.g., `Name`, `Hobbies`, `FavoriteColors`).
   - Example item:
     ```json
     {
       "FriendID": "1",
       "Name": "Martha Rivera",
       "Hobbies": ["dancing", "hiking", "sailing"],
       "FavoriteColors": ["red", "blue"]
     }
     ```
2. **Result**:
   - The item is added to the `Friends` table.

### **Querying Data**
1. **Steps**:
   - In DynamoDB console, select the `Friends` table → **Query**.
   - Enter partition key (e.g., `FriendID = 1`).
   - Click **Run**.
2. **Result**:
   - The item with `FriendID = 1` is returned.

---

## **Checkpoint Questions**
1. **Why are NoSQL databases a good choice for quick project starts?**
   - NoSQL databases have flexible schemas, so developers can start working with data immediately without defining a rigid structure.

2. **Which attribute determines where item data is partitioned?**
   - The **partition key** determines the partition where item data is stored.

3. **Do items in a DynamoDB table need to have the same attributes?**
   - No, DynamoDB allows items to have different attributes.

---

## **Key Takeaways**
- **DynamoDB** is a fully managed, serverless NoSQL database designed for high performance and scalability.
- **Flexible Schema**: Each item can have different attributes.
- **Global Tables**: Automatically replicate data across AWS Regions for low-latency access.
- **Partitioning**: Data is distributed across partitions based on the partition key.

---

**Next Steps**: Explore hands-on labs for creating DynamoDB tables, adding items, and querying data in the AWS Management Console.