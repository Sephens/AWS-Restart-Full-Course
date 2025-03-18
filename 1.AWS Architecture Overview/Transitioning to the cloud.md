# Transitioning a Data Center to the Cloud

## What You Will Learn

### At the Core of the Lesson
You will walk through an example of transitioning a data center to the cloud. You will:
1. Learn about the components and characteristics of a corporate data center.
2. Explore how to set up and run a similar environment on Amazon Web Services (AWS).

---

## Corporate Data Center Example

### Traditional On-Premises Infrastructure
A traditional corporate data center typically follows a **three-tier, client-server architecture**. The diagram below represents a typical setup:

- **Database Tier:** Includes primary and secondary databases with tape backup storage.
- **Application Tier:** Contains application servers and network-attached storage (NAS) for file sharing.
- **Web Tier:** Includes web servers and load balancers for distributing traffic.

**Components:**
- **Load Balancers:** Distribute incoming network traffic across backend servers.
- **Web Servers:** Handle presentation logic.
- **Application Servers:** Provide middleware services, business logic, and data access.
- **NAS Servers:** Centralized file storage for network users.
- **Primary and Secondary Databases:** Store and manage data.
- **Tape Backup Storage:** Used for data backup.
- **Microsoft Active Directory or LDAP Server:** Manages user authentication and resource access.
- **Storage Area Network (SAN):** High-speed network for block-level storage access.

---

## Corporate Data Center Example: Discussion

### Cloud Computing Advantages
In a previous lesson, you learned about the advantages of cloud computing. Consider how these benefits apply to transitioning a data center to the cloud:

1. **Trade Upfront Costs for Variable Costs:** Stop buying hardware and pay only for what you use.
2. **Benefit from Massive Economies of Scale:** Leverage AWS's purchasing power to reduce costs.
3. **Eliminate Guessing Capacity Needs:** Use scaling to create flexible, highly available solutions.
4. **Increase Speed and Agility:** Deploy and decommission resources with a few clicks.
5. **Stop Spending on Data Center Maintenance:** Focus on your core business instead of managing infrastructure.
6. **Go Global in Minutes:** Deploy applications worldwide with minimal effort.

---

## Activity: Transitioning a Corporate Data Center

### Objective
Using what you have learned about AWS core services and architecture best practices, migrate the corporate data center to the cloud.

### Steps
1. **Whiteboard the Diagram:** In small groups, draw the corporate data center diagram.
2. **Replace Components with AWS Services:** Identify which AWS services can replace each on-premises component.
3. **Discuss with the Class:** Share your findings and discuss the transition process.

---

## Corporate Data Center Transition Considerations

### On-Premises Components and AWS Replacements
| On-Premises Item | AWS Service or Resource |
|------------------|-------------------------|
| Servers          | Amazon EC2 Instances    |
| LDAP Server      | AWS Directory Service   |
| Software-based Load Balancers | Elastic Load Balancing (ELB) |
| SAN Solutions    | Amazon Elastic Block Store (Amazon EBS) |
| NAS File Server  | Amazon Elastic File System (Amazon EFS) |
| Databases        | Amazon Relational Database Service (Amazon RDS) |
| Tape Backup Storage | Amazon Simple Storage Service (Amazon S3) |

---

## Transitioning a Corporate Data Center to the Cloud

### AWS Services for Each Component
1. **Servers (Web and App Servers):** Replace with **Amazon EC2 Instances**.
   - EC2 instances can run various operating systems (Windows Server, Linux, etc.) and host server applications.
   
2. **LDAP Server:** Replace with **AWS Directory Service**.
   - Supports LDAP authentication and integrates with Microsoft Active Directory.

3. **Load Balancers:** Replace with **Elastic Load Balancing (ELB)**.
   - ELB automatically scales and performs health checks on backend resources.

4. **SAN Solutions:** Replace with **Amazon EBS**.
   - EBS provides block-level storage for EC2 instances, suitable for long-term data storage.

5. **NAS File Server:** Replace with **Amazon EFS**.
   - EFS offers scalable file storage for EC2 instances, automatically adjusting storage size as needed.

6. **Databases:** Replace with **Amazon RDS**.
   - RDS supports multiple database engines (Aurora, MySQL, PostgreSQL, etc.) and is fully managed by AWS.

7. **Tape Backup Storage:** Replace with **Amazon S3**.
   - S3 provides object storage with versioning and automatic backups.

---

## Corporate Data Center Example on AWS

### Diagram of the Transitioned Data Center
After transitioning to AWS, the data center might look like this:

- **ELB Load Balancer:** Distributes traffic to EC2 instances running web servers.
- **AWS Directory Service:** Replaces the LDAP server.
- **Amazon EBS:** Replaces SAN solutions for block storage.
- **Amazon EFS:** Replaces the NAS file server for scalable file storage.
- **Amazon RDS:** Replaces the primary and secondary databases.
- **Amazon S3:** Replaces tape backup storage for object storage.

---

## Checkpoint Questions

1. **Which AWS services can organizations use to transition a data center to the cloud?**
   - Organizations can transition components of traditional data centers to AWS services by selecting the appropriate service to fulfill the business need. For example:
     - Replace traditional web servers with **Amazon EC2 Instances**.
     - Replace LDAP with **AWS Directory Service**.
     - Replace software-based load balancers with **Elastic Load Balancing (ELB)**.
     - Replace SAN solutions with **Amazon EBS**.
     - Replace NAS file servers with **Amazon EFS**.
     - Replace databases with **Amazon RDS**.
     - Replace tape backup storage with **Amazon S3**.

2. **What are some of the benefits of transitioning a data center to the cloud?**
   - **Trade upfront costs for variable costs:** Stop buying hardware and pay only for what you use.
   - **Benefit from massive economies of scale:** Leverage AWS's purchasing power to reduce costs.
   - **Eliminate guessing capacity needs:** Use scaling to create flexible, highly available solutions.
   - **Increase speed and agility:** Deploy and decommission resources with a few clicks.
   - **Stop spending on data center maintenance:** Focus on your core business instead of managing infrastructure.
   - **Go global in minutes:** Deploy applications worldwide with minimal effort.

3. **Which AWS service can replace a data center SAN system?**
   - **Amazon Elastic Block Store (Amazon EBS)** can replace a data center SAN system.

---

## Key Ideas

- You can replace traditional on-premises data center components with AWS services to transition to the cloud and gain the benefits of cloud computing.
- Use the principles and best practices defined in the **AWS Cloud Adoption Framework (AWS CAF)** and the **AWS Well-Architected Framework** to guide your transition to the cloud.

---

## Thank You

© 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. Correlation, feedback, or other questions? Contact us at [http://anazon.aws.amazon.com/fr/corrector/aws-routing](https://anazon.aws.amazon.com/fr/corrector/aws-routing). All trademarks are the property of their owners.