# Migrating to Amazon RDS - Detailed Lab Walkthrough

## Lab Overview
This lab guides you through migrating a café web application from using a local MariaDB database to a fully managed Amazon RDS MariaDB instance. The process involves generating test data, creating the necessary AWS infrastructure, migrating the data, and reconfiguring the application.

## Objectives
- Create an Amazon RDS MariaDB instance using AWS CLI
- Migrate data from a local MariaDB database to Amazon RDS
- Monitor the RDS instance using Amazon CloudWatch metrics

## Task 1: Generating Order Data on the Café Website

### Purpose
Create test data in the existing local database that will be migrated to RDS.

### Steps:
1. **Access the Café Website**:
   - Copy the `CafeInstanceURL` from the lab details (format: `34.55.102.33/cafe`)
   - Paste this URL into a new browser tab

2. **Create Test Orders**:
   - Click "Menu"
   - Add at least one of each menu item to your order
   - Click "Submit Order"
   - Repeat to create multiple test orders

3. **Record Order Count**:
   - Navigate to "Order History"
   - Note the number of orders displayed (you'll verify this count after migration)

### Notes:
- This creates real data in the local database that we'll migrate
- The more orders you create, the better you can verify the migration

## Task 2: Creating an Amazon RDS Instance Using AWS CLI

### Purpose
Set up the infrastructure needed for the RDS instance including security groups, subnets, and the database itself.

### Task 2.1: Connecting to the CLI Host Instance

1. **Access EC2 Console**:
   - Search for "EC2" in AWS Console
   - Navigate to "Instances"

2. **Connect to CLI Host**:
   - Select the "CLI Host" instance
   - Click "Connect"
   - Choose "EC2 Instance Connect" tab
   - Click "Connect"

*Alternative*: You could use SSH with a key pair if preferred.

### Task 2.2: Configuring the AWS CLI

1. **Run Configuration Command**:
   ```bash
   aws configure
   ```

2. **Enter Credentials**:
   - AWS Access Key ID: [Use provided AccessKey]
   - AWS Secret Access Key: [Use provided SecretKey]
   - Default region name: [Use provided LabRegion]
   - Default output format: `json`

*Note*: Right-click to paste in EC2 Instance Connect terminal.

### Task 2.3: Creating Prerequisite Components

#### 1. Create Security Group for RDS
```bash
aws ec2 create-security-group \
--group-name CafeDatabaseSG \
--description "Security group for Cafe database" \
--vpc-id <CafeVpcID>
```
- Records the `GroupId` from output for later use

#### 2. Add Inbound Rule to Security Group
```bash
aws ec2 authorize-security-group-ingress \
--group-id <CafeDatabaseSG Group ID> \
--protocol tcp --port 3306 \
--source-group <CafeSecurityGroup Group ID>
```
- This allows MySQL connections (port 3306) only from instances with CafeSecurityGroup

#### 3. Verify Security Group
```bash
aws ec2 describe-security-groups \
--query "SecurityGroups[*].[GroupName,GroupId,IpPermissions]" \
--filters "Name=group-name,Values='CafeDatabaseSG'"
```
- Confirm the inbound rule is properly configured

#### 4. Create Private Subnet 1
```bash
aws ec2 create-subnet \
--vpc-id <CafeVpcID> \
--cidr-block 10.200.2.0/23 \
--availability-zone <CafeInstanceAZ>
```
- Uses CIDR 10.200.2.0/23 (doesn't overlap with existing 10.200.0.0/24)
- Records `SubnetId` from output

#### 5. Create Private Subnet 2 (in different AZ)
```bash
aws ec2 create-subnet \
--vpc-id <CafeVpcID> \
--cidr-block 10.200.10.0/23 \
--availability-zone <different AZ than first subnet>
```
- Uses CIDR 10.200.10.0/23
- Must be in different AZ (e.g., if first was us-west-2a, use us-west-2b)

#### 6. Create DB Subnet Group
```bash
aws rds create-db-subnet-group \
--db-subnet-group-name "CafeDB Subnet Group" \
--db-subnet-group-description "DB subnet group for Cafe" \
--subnet-ids <Subnet1 ID> <Subnet2 ID> \
--tags "Key=Name,Value=CafeDatabaseSubnetGroup"
```
- Combines both private subnets into a group RDS can use

### Task 2.4: Creating the Amazon RDS MariaDB Instance

#### 1. Create RDS Instance
```bash
aws rds create-db-instance \
--db-instance-identifier CafeDBInstance \
--engine mariadb \
--engine-version 10.5.13 \
--db-instance-class db.t3.micro \
--allocated-storage 20 \
--availability-zone <CafeInstanceAZ> \
--db-subnet-group-name "CafeDB Subnet Group" \
--vpc-security-group-ids <CafeDatabaseSG Group ID> \
--no-publicly-accessible \
--master-username root --master-user-password 'Re:Start!9'
```
- Creates a MariaDB 10.5.13 instance
- db.t3.micro instance class (smallest/cheapest)
- 20GB storage
- Not publicly accessible
- Uses the security group and subnet group we created

#### 2. Monitor Creation Status
```bash
aws rds describe-db-instances \
--db-instance-identifier CafeDBInstance \
--query "DBInstances[*].[Endpoint.Address,AvailabilityZone,PreferredBackupWindow,BackupRetentionPeriod,DBInstanceStatus]"
```
- Initially shows "creating" status
- Progresses through "modifying", "backing-up", to "available"
- May take 10-15 minutes
- Records the `Endpoint.Address` when available

## Task 3: Migrating Application Data to Amazon RDS

### Purpose
Transfer data from local MariaDB to the new RDS instance.

### Steps:

1. **Connect to CafeInstance**:
   - Repeat connection process used for CLI Host but connect to CafeInstance

2. **Create Database Backup**:
   ```bash
   mysqldump --user=root --password='Re:Start!9' \
   --databases cafe_db --add-drop-database > cafedb-backup.sql
   ```
   - Creates SQL file with all database schema and data

3. **(Optional) Review Backup File**:
   ```bash
   less cafedb-backup.sql
   ```
   - View the SQL commands that would recreate the database

4. **Restore to RDS**:
   ```bash
   mysql --user=root --password='Re:Start!9' \
   --host=<RDS Endpoint Address> \
   < cafedb-backup.sql
   ```
   - Executes the SQL commands against the RDS instance

5. **Verify Migration**:
   ```bash
   mysql --user=root --password='Re:Start!9' \
   --host=<RDS Endpoint Address> \
   cafe_db
   ```
   Then run:
   ```sql
   select * from product;
   ```
   - Confirm data matches what you saw before migration
   - Exit with `exit` command

## Task 4: Configuring the Website to Use Amazon RDS

### Purpose
Update the application configuration to point to the new database.

### Steps:

1. **Update Parameter Store**:
   - Navigate to AWS Systems Manager
   - Go to "Parameter Store"
   - Select `/cafe/dbUrl`
   - Click "Edit"
   - Replace value with RDS endpoint address
   - Click "Save changes"

2. **Test Website**:
   - Reload café website
   - Check "Order History" - count should match pre-migration
   - (Optional) Place new orders to verify full functionality

## Task 5: Monitoring the Amazon RDS Database

### Purpose
Explore RDS monitoring capabilities in CloudWatch.

### Steps:

1. **Access RDS Console**:
   - Navigate to RDS service
   - Select "Databases"
   - Choose "cafedbinstance"

2. **Review Monitoring Tab**:
   - View various metrics including:
     - CPUUtilization
     - DatabaseConnections
     - FreeStorageSpace
     - FreeableMemory
     - Read/Write IOPS

3. **Test Database Connections Metric**:
   - From CafeInstance, connect to RDS:
     ```bash
     mysql --user=root --password='Re:Start!9' \
     --host=<RDS Endpoint> \
     cafe_db
     ```
   - Run a query (e.g., `select * from product;`)
   - Observe `DatabaseConnections` graph update to show 1 connection
   - Exit MySQL session
   - After 1 minute, refresh to see connection count drop to 0

## Conclusion

### Key Accomplishments:
1. Successfully created an RDS MariaDB instance with proper networking
2. Migrated database schema and data from local to RDS
3. Reconfigured application to use RDS
4. Verified monitoring capabilities

### Best Practices Demonstrated:
- Using private subnets for databases
- Restricting database access with security groups
- Using parameter store for configuration
- Monitoring database performance

### Potential Next Steps:
- Set up automated backups with longer retention
- Configure read replicas for improved performance
- Implement database authentication with IAM
- Set up CloudWatch alarms for key metrics