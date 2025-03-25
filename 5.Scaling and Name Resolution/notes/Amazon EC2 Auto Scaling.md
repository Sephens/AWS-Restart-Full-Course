# Amazon EC2 Auto Scaling - Comprehensive Guide

## Table of Contents
- [Amazon EC2 Auto Scaling - Comprehensive Guide](#amazon-ec2-auto-scaling---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Scaling Options](#scaling-options)
  - [Key Concepts](#key-concepts)
  - [Scaling Policies](#scaling-policies)
  - [Instance Health](#instance-health)
  - [Termination Policies](#termination-policies)
  - [Lifecycle Hooks](#lifecycle-hooks)
  - [Launch Templates](#launch-templates)
  - [Best Practices](#best-practices)
  - [Checkpoint Questions \& Answers](#checkpoint-questions--answers)
  - [Key Takeaways](#key-takeaways)

---

## Overview
Amazon EC2 Auto Scaling ensures application availability by automatically adjusting the number of EC2 instances based on defined conditions. It helps maintain optimal performance while minimizing costs by scaling out (adding instances) during high demand and scaling in (removing instances) during low demand.

**Example**: An e-commerce website experiences increased traffic during holiday sales. Auto Scaling adds more instances to handle the load and removes them when traffic returns to normal.

---

## Scaling Options
Auto Scaling provides four scaling options:

1. **Manual Scaling**: Manually adjust the desired capacity.
   - *Use case*: Temporary adjustments for planned maintenance.
   
2. **Scheduled Scaling**: Scale based on predictable load changes.
   - *Example*: Scaling out every weekday at 9 AM to handle increased office hours traffic.
   
3. **Dynamic Scaling**: Scale based on real-time metrics.
   - *Types*:
     - **Target Tracking**: Maintain a target metric (e.g., CPU at 50%).
     - **Step Scaling**: Adjust capacity in steps based on metric breaches.
     - **Simple Scaling**: Single adjustment per alarm.
   
4. **Predictive Scaling**: Use machine learning to forecast traffic and scale proactively.
   - *Example*: Scaling up before a scheduled product launch based on historical data.

---

## Key Concepts
- **Capacity**: Defines the minimum, maximum, and desired number of instances.
  - *Example*: Min=2, Desired=4, Max=10 ensures at least 2 instances and scales up to 10 during peak loads.
  
- **Scaling In/Out**: Adding or removing instances based on demand.
  
- **Instance Health**: Monitors instances using EC2 status checks, ELB health checks, or custom checks.
  - *Example*: An unhealthy instance (failed status check) is terminated and replaced.
  
- **Termination Policy**: Determines which instance to terminate during scale-in.
  - *Example*: `OldestInstance` policy removes the oldest instance during scale-in.
  
- **Launch Template**: Defines instance configuration (AMI, instance type, security groups, etc.).
  - *Example*: A launch template specifies a t3.large instance with a specific AMI and security group.

---

## Scaling Policies
Auto Scaling policies define how and when to scale:

1. **CloudWatch Alarms**: Scale based on alarms (e.g., CPU > 70% for 5 minutes).
2. **Target Tracking**: Maintain a target metric (e.g., average CPU at 50%).
3. **Scheduled Actions**: Scale at specific times (e.g., scale out at 8 AM daily).

**Example**: A target tracking policy keeps CPU utilization at 60% by adding instances when CPU exceeds 60% and removing them when it falls below.

---

## Instance Health
Auto Scaling monitors instance health using:
- **EC2 Status Checks**: Detect hardware/software issues.
- **ELB Health Checks**: Ensure instances can handle traffic.
- **Custom Health Checks**: Monitor application-specific metrics.

**Example**: An instance failing ELB health checks is replaced to maintain application availability.

---

## Termination Policies
Determines which instance to terminate during scale-in:
- **Default**: Terminates instances in the AZ with the most instances.
- **OldestInstance**: Terminates the oldest instance.
- **NewestInstance**: Terminates the newest instance (useful for testing).
- **ClosestToNextInstanceHour**: Maximizes billing efficiency.

**Example**: Using `ClosestToNextInstanceHour` minimizes costs by terminating instances near the end of their billing hour.

---

## Lifecycle Hooks
Allow custom actions during instance lifecycle events:
- **Scale-Out**: Perform actions (e.g., install software) before an instance enters service.
- **Scale-In**: Perform actions (e.g., backup logs) before an instance terminates.

**Example**: A lifecycle hook backs up logs from an instance before it is terminated during scale-in.

---

## Launch Templates
Define instance configurations for Auto Scaling:
- **Required**: AMI, instance type.
- **Optional**: Key pairs, security groups, user data, tags.

**Example**: A launch template specifies an Ubuntu AMI, t3.medium instance type, and a security group allowing HTTP traffic.

**Best Practice**: Use launch templates instead of launch configurations for flexibility (e.g., versioning).

---

## Best Practices
1. **Metrics & Monitoring**:
   - Use 1-minute CloudWatch metrics for faster scaling.
   - Enable Auto Scaling group metrics for accurate forecasts.
   
2. **Instance Types**:
   - Avoid burstable instances (e.g., T3) for consistent workloads.
   
3. **Steady-State Groups**:
   - Set min=max=desired for critical instances (e.g., NAT servers).
   
4. **Avoid Thrashing**:
   - Use alarm sustain periods, cooldown periods, and instance warmup.

**Example**: A cooldown period of 5 minutes prevents rapid scaling fluctuations.

---

## Checkpoint Questions & Answers
1. **Q**: Which termination policy removes the newest instance?  
   **A**: `NewestInstance`. Useful for removing failed configurations quickly.

2. **Q**: How to force a new server creation?  
   **A**: Increase the desired capacity. To remove it, decrease the desired capacity.

3. **Q**: What if new servers fail?  
   **A**: Revert the launch template to a working version.

4. **Q**: How to avoid thrashing?  
   **A**: Use alarm sustain periods, cooldown periods, and instance warmup.

---

## Key Takeaways
- Auto Scaling maintains availability and optimizes costs.
- Scaling options include manual, scheduled, dynamic, and predictive.
- Launch templates define instance configurations.
- Avoid thrashing with cooldown and warmup periods.
- Termination policies control which instances are removed during scale-in.

**Example Workflow**:
1. Create a launch template with desired configurations.
2. Set up an Auto Scaling group with dynamic scaling policies.
3. Monitor and adjust based on performance metrics.