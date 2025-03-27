# AWS Database Migration Service (DMS) - Complete Guide

## Overview
This document provides a comprehensive look at AWS Database Migration Service (DMS), covering its features, migration types, components, and integration with AWS Schema Conversion Tool (SCT) for seamless database migrations to AWS.

---

## Core Learning Objectives
By the end of this guide, you will be able to:
- **Describe AWS DMS** and its key features
- **Differentiate** between homogeneous and heterogeneous migrations
- **Explain** the role of AWS Schema Conversion Tool (SCT)

---

## What is AWS DMS?
AWS Database Migration Service (DMS) is a fully managed service that enables **secure, fast database migrations** to AWS with **minimal downtime**.

**Key Capabilities**:
- Supports most commercial and open-source databases
- Performs **one-time migrations** or **continuous replication**
- Maintains source database availability during migration
- Handles **schema conversion** (with AWS SCT)

**Example**: A bank migrates its on-premises Oracle database to Amazon Aurora with zero downtime using DMS.

---

## AWS DMS Features
| Feature | Description | Business Benefit |
|---------|-------------|------------------|
| **Wide Database Support** | Works with 20+ database engines | Future-proof migrations |
| **Minimal Downtime** | Continuous data replication | No business disruption |
| **High Availability** | Multi-AZ deployment options | 99.99% SLA |
| **Consolidation** | Merge multiple databases | Cost optimization |
| **Transformation** | Filter/modify data during migration | Data quality improvement |

**Real-World Use**: An e-commerce company consolidates 5 MySQL instances into one Amazon RDS MySQL database during a merger.

---

## Migration Architecture Components
### 1. **Replication Instance**
- The "engine" that performs the migration
- EC2 instance managed by AWS
- Sizes from dms.t2.micro to dms.r5.24xlarge

### 2. **Endpoints**
- **Source Endpoint**: Connection to origin database
- **Target Endpoint**: Connection to destination database

### 3. **Replication Tasks**
- Defines what data to migrate
- Specifies migration type (full load/CDC)
- Includes transformation rules

**Data Flow**:
```
[Source DB] → [Source Endpoint] → [Replication Instance] → [Target Endpoint] → [Target DB]
```

---

## Migration Types
### 1. Homogeneous Migrations
- **Same database engine** (e.g., MySQL to Amazon RDS for MySQL)
- **Simple process**: Direct data transfer
- **Use Case**: Cloud migration with same technology stack

**Example**: On-premises PostgreSQL → Amazon Aurora PostgreSQL

### 2. Heterogeneous Migrations
- **Different database engines** (e.g., Oracle to Aurora PostgreSQL)
- **Two-step process**:
  1. **AWS SCT** converts schema/code
  2. **AWS DMS** migrates data
- **Use Case**: Modernization projects

**Example**: Microsoft SQL Server → Amazon Aurora MySQL

---

## AWS Schema Conversion Tool (SCT)
### Key Functions
1. **Schema Conversion**:
   - Tables, views, stored procedures
   - Data type mappings
   - Code translation (PL/SQL to PL/pgSQL)

2. **Application Assessment**:
   - Scans application code for SQL statements
   - Identifies compatibility issues

3. **Conversion Report Generation**:
   - Details manual intervention needed
   - Estimates effort for migration

**Supported Conversions**:
| Source | Target |
|--------|--------|
| Oracle | Aurora, Redshift |
| SQL Server | PostgreSQL, MySQL |
| Teradata | Redshift |
| MongoDB | DocumentDB |

**Example**: Converting 500 Oracle stored procedures to PostgreSQL equivalents automatically.

---

## Migration Process Walkthrough
### Homogeneous Migration
1. Create replication instance
2. Configure source/target endpoints
3. Create and run replication task
4. Validate data consistency
5. Cutover applications

### Heterogeneous Migration
1. Use AWS SCT to convert schema
2. Apply converted schema to target
3. Configure DMS for data migration
4. Run test migrations
5. Execute final cutover

**Pro Tip**: Use **AWS DMS Fleet Advisor** to discover and analyze source databases before migration.

---

## Checkpoint Questions (Answered)
1. **What are the steps in heterogeneous database migration?**  
   **Answer**:  
   1. Convert schema using AWS SCT  
   2. Migrate data using AWS DMS  

2. **Why use AWS DMS?**  
   **Answer**: For minimal-downtime migrations, continuous replication, database consolidation, and cross-engine migrations.

3. **What does AWS SCT do?**  
   **Answer**: Converts database schemas and code between different database engines, and analyzes application SQL dependencies.

---

## Key Ideas
- **AWS DMS** simplifies database migrations with minimal downtime
- **Homogeneous migrations** are direct transfers between compatible databases
- **Heterogeneous migrations** require AWS SCT for schema conversion
- **Continuous replication** enables near-real-time data synchronization
- **SCT** handles complex conversions (e.g., Oracle→PostgreSQL)

**Migration Strategy**: Always test with a **proof-of-concept** migration before full cutover.

---

## Conclusion
AWS DMS and SCT provide a complete solution for database migrations to AWS, whether you're moving to the cloud, modernizing your database technology, or consolidating environments. With features like continuous replication and automated schema conversion, organizations can migrate with confidence and minimal disruption.

For assistance:  
[AWS Training Support](https://support.aws.amazon.com/#/contacts/aws-training)

**All trademarks are the property of their owners.**  
©2023, Amazon Web Services, Inc. or its affiliates. All rights reserved.