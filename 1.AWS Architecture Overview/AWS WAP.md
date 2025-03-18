# AWS Well-Architected Principles

## What You Will Learn

### At the Core of the Lesson
You will learn how to:
- Identify key design principles of the AWS Well-Architected Framework.
- Describe the details of key well-architected design principles.

---

## Key Design Principles

The AWS Well-Architected Framework identifies a set of general design principles to facilitate good design in the cloud:

1. **Stop guessing your capacity needs.**
2. **Test systems at production scale.**
3. **Automate to make architectural experimentation easier.**
4. **Provide for evolutionary architectures.**
5. **Drive architectures by using data.**
6. **Improve through game days.**

---

## Well-Architected Design Principles Details

### 1. Stop Guessing Your Capacity Needs

#### Traditional Environment
- **Wasted Resources:** Making capacity decisions before deploying a system can lead to expensive idle resources.
- **Performance Issues:** Limited capacity can result in performance problems.

#### Cloud Environment
- **Flexibility:** You can scale up and down automatically based on demand.
- **Efficiency:** Monitor demand and system usage to maintain optimal resource levels.

**Example:**
- **Traditional:** A company preparing for a sale must estimate customer traffic and build infrastructure accordingly. Overestimating leads to wasted resources; underestimating leads to performance issues.
- **Cloud:** The company sets workload thresholds to automatically adjust resources, ensuring efficient expenditure and resource utilization.

---

### 2. Test Systems at Production Scale

#### Traditional Environment
- **Cost-Prohibitive:** Creating a duplicate environment for testing is expensive.
- **Limited Testing:** Test environments are often not tested at live production levels.

#### Cloud Environment
- **On-Demand Testing:** Create a duplicate environment, test, and decommission resources as needed.
- **Cost-Effective:** Pay only for the test environment while it is running.

**Example:**
- **Traditional:** Testing new updates at production scale is rarely done due to high costs.
- **Cloud:** Simulate the production environment at a fraction of the cost, allowing thorough testing of updates before rollout.

---

### 3. Automate

#### Traditional Environment
- **Complex Automation:** Separate structures and components require more effort to automate.
- **Lack of Common API:** No unified API for all infrastructure parts.

#### Cloud Environment
- **Efficient Automation:** Create and replicate systems with minimal manual effort.
- **Track Changes:** Monitor and audit automation changes, reverting when necessary.

**Example:**
- **Traditional:** Manual setup and updates are time-consuming and error-prone.
- **Cloud:** Automation tools can spin up test environments and roll out updates, with the ability to revert if issues arise.

---

### 4. Provide for Evolutionary Architectures

#### Traditional Environment
- **Static Decisions:** Architectural decisions are often one-time events.
- **Limited Versions:** Few major versions of a system during its lifetime.
- **Rigidity:** Initial decisions may hinder meeting changing business requirements.

#### Cloud Environment
- **Dynamic Evolution:** Automate and test on demand to lower the risk of design changes.
- **Continuous Improvement:** Systems evolve to take advantage of new innovations.

**Example:**
- **Traditional:** Updating physical infrastructure can take hours or days.
- **Cloud:** Infrastructure updates can be done with a click, keeping pace with technological advancements.

---

### 5. Drive Architectures by Using Data

#### Traditional Environment
- **Default Choices:** Architectural decisions are often based on organizational defaults.
- **Lack of Data:** Datasets for informed decisions are generally unavailable.
- **Assumptions:** Models and assumptions are used to size architecture.

#### Cloud Environment
- **Data-Driven Decisions:** Collect data on how architectural choices affect workload behavior.
- **Fact-Based Improvements:** Use data to inform architecture choices and improvements over time.

**Example:**
- **Traditional:** Decisions are made based on assumptions rather than real data.
- **Cloud:** Real-time data collection allows for informed, fact-based architectural decisions.

---

### 6. Improve Through Game Days

#### Traditional Environment
- **Reactive Testing:** Runbooks are exercised only when something goes wrong in production.

#### Cloud Environment
- **Proactive Testing:** Schedule game days to simulate production events and test architecture and processes.
- **Continuous Improvement:** Develop organizational experience in dealing with events.

**Example:**
- **Traditional:** Issues are addressed only after they occur in production.
- **Cloud:** Tools like Chaos Monkey simulate failures to test system resilience and recoverability.

---

## Checkpoint Questions

1. **What is the benefit of a cloud environment when it comes to understanding capacity?**
   - In a cloud environment, developers do not need to guess their infrastructure capacity needs. They can monitor demand and system usage and scale up and down automatically as needed.

2. **How can developers effectively test their system at a production scale in a cloud environment?**
   - Developers can create a duplicate environment on demand, complete testing, and then decommission the resources, paying only for the time the environment is running.

3. **How does a cloud environment facilitate future design changes?**
   - The ability to automate and test on demand lowers the risk of impact from design changes, allowing systems to evolve over time.

4. **How can developers use game days to improve their design?**
   - By regularly scheduling game days to simulate production events, developers can identify areas for improvement and develop organizational experience in dealing with events.

---

## Key Ideas

The key design principles promoted in the AWS Well-Architected Framework include:
- **Stop guessing** your **capacity** needs.
- **Test** systems at **production scale**.
- **Automate** to make architectural **experimentation** easier.
- Provide for **evolution using data**.
- Drive **architectures using data**.
- Improve through **game days**.

---

## Thank You

© 2022 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copyright, lending, or selling is prohibited. Correlation, feedback, or other questions? Contact us at [http://anazon.aws.amazon.com/products/aws-raising](https://anazon.aws.amazon.com/products/aws-raising). All trademarks are the property of their owners.