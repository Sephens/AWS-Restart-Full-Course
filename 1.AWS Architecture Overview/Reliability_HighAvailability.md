# AWS Reliability and High Availability

## What You Will Learn

### At the Core of the Lesson
You will learn how to:
- Compare and contrast between reliability and high availability.
- Explore the prime factors of high availability.

---

## Reliability and High Availability Defined

Werner Vogels, CTO of Amazon.com, said, “Everything fails, all the time.”

Failures are costly to businesses. **Reliability** and **high availability** are crucial to preventing and mitigating failures.

---

## Reliability

### Definition
- **Reliability** is the probability that an entire system (including hardware, firmware, and software) functions for a specified period of time.
- It measures how long the system performs its intended function.

### Common Measures of Reliability
1. **Mean Time Between Failure (MTBF):** Total time in service divided by the number of failures.
2. **Failure Rate:** Number of failures divided by the total time in service.

**Example:**
- When you purchase a vehicle, the reliability of subsystems (e.g., cooling, ignition, brakes) determines the overall reliability of the vehicle. If the ignition fails, reliability is negatively impacted.

---

## Reliability Compared to Availability

### Reliability
- **Reliability** measures how long a resource performs its intended function.

### Availability
- **Availability** measures the percentage of time that a resource is operating normally.
- It is expressed as a percentage of uptime (e.g., 99.9%) over a period of time (commonly a year).
- **Shorthand Notation:** The number of 9s (e.g., five 9s = 99.999% availability).

**Example:**
- AWS services often advertise availability numbers like 99.99%, indicating the percentage of time the service is operational.

---

## High Availability (HA)

### Definition
- **High Availability (HA)** ensures that your application's downtime is minimized as much as possible without the need for human intervention.
- It is not about replicated physical components but about system-wide, shared resources that cooperate to guarantee essential services.

### Availability Metrics
| Number of 9s | Percentage of Uptime | Maximum Downtime Per Year | Equivalent Downtime Per Day |
|--------------|----------------------|---------------------------|-----------------------------|
| One 9        | 90%                  | 36.5 days                 | 2.4 hours                   |
| Two 9s       | 99%                  | 3.65 days                 | 14 minutes                  |
| Three 9s     | 99.9%                | 8.77 hours                | 1.4 minutes                 |
| Four 9s      | 99.99%               | 52.6 minutes              | 8.6 seconds                 |
| Five 9s      | 99.999%              | 5.25 minutes              | 0.86 seconds                |

**Example:**
- A system with **five 9s** availability (99.999%) will have a maximum downtime of only 5.25 minutes per year.

---

## HA Goals

### High Availability aims to ensure:
1. **Systems are generally functioning and accessible.**
2. **Downtime is minimized.**
3. **Minimal human intervention is required.**

**Example:**
- AWS allows users to build fault-tolerant, highly available systems with minimal human interaction and upfront financial investment.

---

## High Availability Prime Factors

### The following factors contribute to HA:
1. **Fault Tolerance:** The built-in redundancy of an application's components and its ability to remain operational even if some components fail.
2. **Scalability:** The ability of an application to accommodate growth without changing its design.
3. **Recoverability:** The process, policies, and procedures related to restoring service after a catastrophic event.

**Example:**
- **Fault Tolerance:** A system with redundant hardware components can continue operating even if one component fails.
- **Scalability:** An application that can handle increased traffic by automatically scaling resources.
- **Recoverability:** A disaster recovery plan that ensures data and services can be restored quickly after a failure.

---

## On-Premises HA Compared to HA on AWS

### Traditional (On-Premises) IT
- **Expensive:** Ensuring HA in local data centers can be costly.
- **Limited to Mission-Critical Applications:** HA is typically reserved for critical systems due to high costs.

### AWS Cloud
- **Cost-Effective:** AWS provides multiple options to enhance availability and recoverability.
- **Scalable:** AWS offers multiple servers, Availability Zones, Regions, and fault-tolerant services.

**Example:**
- **Amazon RDS:** Automatically deploys databases with a standby replica in a different Availability Zone to ensure high availability.

---

## Checkpoint Questions

1. **What is the definition of reliability?**
   - Reliability is a measure of how long a resource performs its intended function.

2. **What is the difference between high availability and fault tolerance?**
   - Fault tolerance refers to the built-in redundancy of an application's components and its ability to remain operational even if some components fail. High availability combines fault tolerance, scalability, and recoverability to minimize downtime.

3. **How is high availability made possible in the cloud?**
   - High availability in the cloud is achieved through:
     - Multiple servers
     - Isolated redundant data centers within each Availability Zone
     - Multiple Availability Zones within each Region
     - Multiple Regions around the world
     - Fault-tolerant services

---

## Key Ideas

- **Reliability** measures how long a resource performs its intended function.
- **Availability** measures the percentage of time that a resource is in an operable state.
- **High availability** can be achieved in the AWS Cloud by using:
  - Multiple servers
  - Isolated redundant data centers within each Availability Zone
  - Multiple Availability Zones within each Region
  - Multiple Regions around the world
  - Fault-tolerant services

---

## Thank You

---
© 2025, RiseTechnon. All rights reserved.