# **Lab Guide: Introduction to Amazon DynamoDB**  

## **Lab Overview**  
This lab introduces **Amazon DynamoDB**, a fully managed **NoSQL database** service. You will:  
✔ **Create a DynamoDB table**  
✔ **Insert and modify data**  
✔ **Query data using different methods**  
✔ **Delete the table**  

### **Key Features of DynamoDB**  
🔹 **Serverless** – No infrastructure management  
🔹 **Single-digit millisecond latency**  
🔹 **Auto-scaling** – Handles any workload  
🔹 **Flexible schema** – No rigid table structure  

---

## **Task 1: Create a DynamoDB Table**  

### **Objective**  
Create a **Music** table with **Artist (Partition Key)** and **Song (Sort Key)**.  

### **Step-by-Step Instructions**  

1. **Open DynamoDB Console:**  
   - Go to **AWS Management Console** > **Services** > **DynamoDB**.  

2. **Create Table:**  
   - Click **Create table**.  
   - **Table name:** `Music`  
   - **Partition key:** `Artist` (String)  
   - **Sort key (optional):** `Song` (String)  
   - Keep default settings.  
   - Click **Create table**.  

3. **Wait for Table Activation:**  
   - Status changes to **Active** (~1 minute).  

### **Key Notes**  
📌 **Partition Key (Primary Key):** Distributes data across partitions.  
📌 **Sort Key:** Enables sorting and range queries.  

---

## **Task 2: Add Data to the Table**  

### **Objective**  
Insert **three songs** with different attributes (flexible schema).  

### **Step-by-Step Instructions**  

1. **Open the Music Table:**  
   - Go to **Tables** > **Music** > **Explore items**.  

2. **Add First Item (Pink Floyd - Money):**  
   - Click **Create item**.  
   - Enter:  
     - `Artist`: `Pink Floyd`  
     - `Song`: `Money`  
   - **Add extra attributes:**  
     - `Album` (String): `The Dark Side of the Moon`  
     - `Year` (Number): `1973`  
   - Click **Create item**.  

3. **Add Second Item (John Lennon - Imagine):**  
   - Click **Create item**.  
   - Enter:  
     - `Artist`: `John Lennon`  
     - `Song`: `Imagine`  
     - `Album`: `Imagine`  
     - `Year`: `1971`  
     - `Genre`: `Soft rock` *(New attribute!)*  
   - Click **Create item**.  

4. **Add Third Item (Psy - Gangnam Style):**  
   - Click **Create item**.  
   - Enter:  
     - `Artist`: `Psy`  
     - `Song`: `Gangnam Style`  
     - `Album`: `Psy 6 (Six Rules), Part 1`  
     - `Year`: `2011`  
     - `LengthSeconds`: `219` *(New attribute!)*  
   - Click **Create item**.  

### **Why This Matters**  
🔸 **No fixed schema** – Each item can have different attributes.  
🔸 **Easy to modify** – No need for `ALTER TABLE` commands.  

---

## **Task 3: Modify an Existing Item**  

### **Objective**  
Fix incorrect data (change **Psy’s song year** from `2011` to `2012`).  

### **Step-by-Step Instructions**  

1. **Find the Item:**  
   - Go to **Explore items** > **Music** > **Psy**.  

2. **Edit the Year:**  
   - Change `Year` from `2011` to `2012`.  
   - Click **Save changes**.  

### **Key Notes**  
📌 **No schema locks** – Changes are immediate.  

---

## **Task 4: Query the Table**  

### **Objective**  
Retrieve data using **Query** (fast) and **Scan** (slower).  

### **Step 1: Query (Fast, Indexed Lookup)**  

1. **Go to Query Tab:**  
   - Under **Scan/Query items**, select **Query**.  

2. **Search for Psy - Gangnam Style:**  
   - `Artist`: `Psy`  
   - `Song`: `Gangnam Style`  
   - Click **Run**.  

### **Step 2: Scan (Slower, Full Table Search)**  

1. **Go to Scan Tab:**  
   - Under **Scan/Query items**, select **Scan**.  

2. **Filter by Year = 1971:**  
   - Expand **Filters**.  
   - `Attribute`: `Year`  
   - `Type`: `Number`  
   - `Value`: `1971`  
   - Click **Run**.  

### **Key Differences**  
| **Query** | **Scan** |  
|-----------|----------|  
| Uses **primary key** | Searches **entire table** |  
| **Fast & efficient** | **Slower for large tables** |  
| Best for known keys | Best for filtering |  

---

## **Task 5: Delete the Table**  

### **Objective**  
Clean up by deleting the **Music** table.  

### **Step-by-Step Instructions**  

1. **Go to Tables:**  
   - Select **Music**.  

2. **Delete Table:**  
   - Click **Actions** > **Delete table**.  
   - Type `delete` to confirm.  
   - Click **Delete table**.  

### **Why This Matters**  
🔹 **Avoid unnecessary costs** – DynamoDB charges for storage & throughput.  

---

## **Conclusion**  
✅ **Created a DynamoDB table**  
✅ **Inserted flexible schema data**  
✅ **Modified an item**  
✅ **Queried data (Query vs. Scan)**  
✅ **Deleted the table**  

### **Next Steps for Production**  
🔹 **Enable DynamoDB Streams** for real-time updates.  
🔹 **Use Global Tables** for multi-region replication.  
🔹 **Set up Auto Scaling** for variable workloads.  

🚀 **You’re now ready to use DynamoDB in real applications!**