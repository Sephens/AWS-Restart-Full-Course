# Data Interaction and Database Transaction

This module focuses on how users interact with relational databases, the roles involved, and the concept of database transactions, including their properties and states.

---

## 1. **Introduction**
- **Objective**: Learn how to interact with relational databases and understand the characteristics of transactions.
- **Key Terms**:
  - Database analyst
  - Database administrator
  - Transaction
  - ACID properties (Atomicity, Consistency, Isolation, Durability)

---

## 2. **Data Sharing**
- **Data Accessibility**: Modern databases allow multiple users to access and update data efficiently.
- **Use Cases**: Developers, end users, and analysts can interact with databases in various ways, enabling timely data updates and analysis.

---

## 3. **Roles Interacting with Relational Databases**
Different roles interact with databases in unique ways:
- **Application Developer**:
  - Creates applications that populate and manipulate data.
  - Embeds SQL commands in application code.
- **End User**:
  - Uses applications to query and update data.
  - May occasionally interact directly with the database if they know SQL.
- **Data Analyst**:
  - Collects, cleans, and interprets data.
  - Uses SQL commands to view and manipulate data.
- **Database Administrator (DBA)**:
  - Designs, implements, and monitors databases.
  - Ensures data consistency, quality, and security.
  - Uses all SQL commands to manage the database.

---

## 4. **Database Interaction Models**
### **Client-Server Model**
1. Users run client applications that send SQL requests to the server.
2. The server processes the SQL and returns the results.
3. Example: A user queries a database through a desktop application.

### **Three-Tier Web Application Model**
1. User interacts with a web browser, which sends requests to a web server.
2. The web server forwards the request to an application server.
3. The application server sends SQL commands to the database server.
4. The database server processes the SQL and returns results to the application server.
5. The application server formats the results and sends them back to the web server.
6. The web server displays the results in the user’s browser.

---

## 5. **Embedded SQL in Application Code**
- **Application Development**: Developers embed SQL commands in application code to allow users to interact with databases without needing to know SQL.
- **Use Cases**: Both client-server and three-tier web applications use embedded SQL to perform database tasks.

---

## 6. **Transactions in Databases**
### **What is a Transaction?**
- A transaction is a collection of changes made to a database that must be performed as a unit.
- **Example**: Transferring $100 from a checking account to a savings account requires two operations:
  1. Reduce the checking account balance by $100.
  2. Increase the savings account balance by $100.
- Both operations must succeed or fail together to maintain database integrity.

### **Transaction States**
- **Active**: The transaction is being executed.
- **Partially Committed**: The transaction is completing its final operation.
- **Failed**: A check by the database recovery system fails.
- **Aborted**: The transaction is rolled back to its original state.
- **Committed**: All operations in the transaction are successfully completed.

---

## 7. **Use Cases for Transactions**
- **Ensuring Data Integrity**: Transactions ensure that the database never contains partial results of operations.
- **Isolation**: Transactions provide isolation between programs accessing the database simultaneously, preventing data corruption.

---

## 8. **ACID Properties of Transactions**
Transactions follow the **ACID** properties:
- **Atomicity**: All changes in a transaction are completed together or not at all.
- **Consistency**: Transactions ensure the database remains in a valid state, adhering to constraints.
- **Isolation**: Transactions are isolated from each other, preventing interference.
- **Durability**: Once a transaction is committed, the changes are permanent.

---

## 9. **Checkpoint Questions**
1. **What are two roles that interact with databases?**
   - End users, data analysts, database administrators, and application developers.
2. **What are the different transaction states?**
   - Active, partially committed, failed, aborted, and committed.
3. **What are the two primary models for database interaction?**
   - Client-server model and three-tier web application model.

---

## 10. **Key Takeaways**
- **Roles**: Database administrators, application developers, data analysts, and end users interact with databases.
- **Interaction Models**: Databases are accessed through client-server or three-tier web applications.
- **Transactions**: A transaction is a logical unit of work that ensures all operations succeed or fail together.
- **ACID Properties**: Transactions follow Atomicity, Consistency, Isolation, and Durability to maintain database integrity.

---

## 11. **Conclusion**
This module emphasizes the importance of understanding how different roles interact with databases, the models for database interaction, and the critical role of transactions in maintaining data integrity. Transactions, governed by ACID properties, ensure that databases remain consistent and reliable, even when multiple users access and modify data simultaneously.