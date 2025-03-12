# Introduction to Amazon DynamoDB

## Lab Overview

Amazon DynamoDB is a fast and flexible NoSQL database service designed for applications that require consistent, single-digit millisecond latency at any scale. It is fully managed and supports both document and key-value data models. Its flexible data model and reliable performance make it suitable for a wide range of applications, including mobile, web, gaming, ad-tech, and IoT.

In this lab, you will:
1. Create a table in DynamoDB to store information about a music library.
2. Enter data into the DynamoDB table.
3. Query the music library.
4. Delete the DynamoDB table.

### Topics Covered
- Creating an Amazon DynamoDB table
- Entering data into an Amazon DynamoDB table
- Querying an Amazon DynamoDB table
- Deleting an Amazon DynamoDB table

### Duration
This lab requires approximately **35 minutes** to complete.

---

## Accessing the AWS Management Console

1. At the upper-right corner of these instructions, choose **Start Lab**.
   - **Troubleshooting Tip**: If you get an Access Denied error, close the error box and choose **Start Lab** again.
2. The lab status is indicated by a circle next to **AWS**:
   - **Red Circle**: Lab has not been started.
   - **Yellow Circle**: Lab is starting.
   - **Green Circle**: Lab is ready.
3. Wait for the lab to be ready (green circle), then choose the green circle next to **AWS** to open the AWS Management Console in a new browser tab.
   - **Tip**: If a new tab does not open, check for a banner or icon indicating that pop-ups are blocked. Allow pop-ups for this site.
4. Arrange the AWS Management Console tab alongside these instructions for easy reference.
5. **Do not change the lab Region** unless instructed.

---

## Task 1: Create a New Table

In this task, you will create a new table named **Music** in DynamoDB.

### Steps:
1. In the AWS Management Console, go to **Services** > **Database** > **DynamoDB**.
2. Choose **Create table**.
3. Enter the following details:
   - **Table name**: `Music`
   - **Partition key**: `Artist` (leave the type as **String**)
   - **Sort key**: `Song` (leave the type as **String**)
4. Leave the default settings for indexes and provisioned capacity.
5. Scroll down and choose **Create table**.
6. Wait for the **Music** table to become **Active** (less than 1 minute).

---

## Task 2: Add Data

In this task, you will add data to the **Music** table.

### Key Concepts:
- **Table**: A collection of data on a particular topic.
- **Item**: A group of attributes uniquely identifiable among all items in the table (similar to a row in other databases).
- **Attribute**: A fundamental data element (similar to a column in other databases). Each item can have different attributes.

### Steps:
1. In the DynamoDB dashboard, select the **Music** table.
2. Choose **Actions** > **Create item**.
3. Add the following attributes for the first item:
   - **Artist**: `Pink Floyd` (String)
   - **Song**: `Money` (String)
   - **Album**: `The Dark Side of the Moon` (String)
   - **Year**: `1973` (Number)
4. Choose **Create item**.
5. Add a second item with the following attributes:
   - **Artist**: `John Lennon` (String)
   - **Song**: `Imagine` (String)
   - **Album**: `Imagine` (String)
   - **Year**: `1971` (Number)
   - **Genre**: `Soft rock` (String)
6. Add a third item with the following attributes:
   - **Artist**: `Psy` (String)
   - **Song**: `Gangnam Style` (String)
   - **Album**: `Psy 6 (Six Rules), Part 1` (String)
   - **Year**: `2011` (Number)
   - **LengthSeconds**: `219` (Number)

### Notes:
- Only the **Partition Key** (`Artist`) and **Sort Key** (`Song`) are required.
- Additional attributes can vary between items, demonstrating the flexibility of NoSQL databases.

---

## Task 3: Modify an Existing Item

In this task, you will correct an error in the data.

### Steps:
1. In the DynamoDB dashboard, go to **Tables** > **Explore Items**.
2. Select the **Music** table.
3. Find the item for **Psy** and change the **Year** from `2011` to `2012`.
4. Choose **Save changes**.

---

## Task 4: Query the Table

There are two ways to retrieve data from a DynamoDB table:
1. **Query**: Finds items based on the primary key (and optionally the sort key). It is fully indexed and very fast.
2. **Scan**: Looks through every item in the table, which is less efficient and slower for larger tables.

### Query Example:
1. In the DynamoDB dashboard, go to **Tables** > **Explore Items** > **Music**.
2. Expand **Scan/Query items** and choose **Query**.
3. Enter the following details:
   - **Artist (Partition key)**: `Psy`
   - **Song (Sort key)**: `Gangnam Style`
4. Choose **Run**. The song will appear in the list.

### Scan Example:
1. In the same section, choose **Scan**.
2. Expand **Filters** and enter the following:
   - **Attribute name**: `Year`
   - **Type**: `Number`
   - **Value**: `1971`
3. Choose **Run**. Only the song released in 1971 will be displayed.

---

## Task 5: Delete the Table

In this task, you will delete the **Music** table and all its data.

### Steps:
1. In the DynamoDB dashboard, go to **Tables** > **Update settings**.
2. Select the **Music** table.
3. Choose **Actions** > **Delete table**.
4. On the confirmation panel, enter `delete` and choose **Delete table**.
5. The table will be deleted.

---

## Conclusion

Congratulations! You have successfully:
1. Created an Amazon DynamoDB table.
2. Entered data into the table.
3. Queried the table.
4. Deleted the table.

For more information, refer to the [DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/).

---

## Lab Complete

1. Choose **End Lab** at the top of this page.
2. Select **Yes** to confirm that you want to end the lab.
3. A message will briefly display: **Ended AWS Lab Successfully**.

---

### Key Takeaways:
- DynamoDB is a fully managed NoSQL database with flexible data models.
- It supports both key-value and document data structures.
- You can add, modify, query, and delete data without needing to define a schema.
- Queries are faster than scans because they use indexes.
- DynamoDB is ideal for applications requiring low-latency access to data at any scale.