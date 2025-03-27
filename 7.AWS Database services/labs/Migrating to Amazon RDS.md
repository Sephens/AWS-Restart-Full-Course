# Migrating to Amazon RDS - Comprehensive Lab Guide

## Lab Overview
This lab guides you through migrating a café web application from using a local MySQL database to a fully managed Amazon RDS database instance. The migration involves creating necessary infrastructure components, transferring data, and reconfiguring the application.

## Starting Architecture
- Café web application runs on an EC2 instance with LAMP stack (Linux, Apache, MySQL, PHP)
- Database is local to the application server
- Instance type: T3 small
- Runs in a public subnet for internet access
- CLI Host instance in same subnet for administration

## Final Architecture
- Database migrated to Amazon RDS MariaDB instance
- RDS instance resides in private subnets within same VPC
- Application now connects to external database
- Improved scalability and manageability

## Detailed Step-by-Step Guide

### Task 1: Generating Order Data on the Café Website

**Purpose**: Create test data in the existing database before migration.

**Steps**:
1. Access the café website using the provided URL (e.g., `34.55.102.33/cafe`)
2. Navigate to Menu and add items to your order
3. Submit the order
4. Go to Order History and record the number of orders

**Notes**:
- This creates realistic data to verify successful migration
- Example orders might include:
  - 1 Coffee
  - 2 Sandwiches
  - 1 Dessert
- Recording order count provides a verification point for later

### Task 2: Creating an Amazon RDS Instance Using AWS CLI

#### Task 2.1: Connecting to the CLI Host Instance

**Purpose**: Establish a secure connection to run AWS CLI commands.

**Steps**:
1. Open EC2 Console
2. Navigate to Instances
3. Select CLI Host instance
4. Click Connect → EC2 Instance Connect → Connect

**Notes**:
- CLI Host is pre-configured with AWS CLI
- Alternative connection methods (SSH) are available but not required
- This instance has necessary permissions for lab tasks

#### Task 2.2: Configuring the AWS CLI

**Purpose**: Set up AWS CLI with proper credentials.

**Steps**:
```bash
aws configure
```
Enter:
- AWS Access Key ID: [Provided AccessKey]
- AWS Secret Access Key: [Provided SecretKey]
- Default region name: [LabRegion]
- Default output format: json

**Notes**:
- Credentials are temporary and lab-specific
- JSON output format provides structured responses
- Configuration is stored in ~/.aws/credentials and ~/.aws/config

#### Task 2.3: Creating Prerequisite Components

**Purpose**: Build necessary infrastructure for RDS instance.

**1. Create Security Group**
```bash
aws ec2 create-security-group \
--group-name CafeDatabaseSG \
--description "Security group for Cafe database" \
--vpc-id <CafeVpcID>
```
**Notes**:
- Security groups act as virtual firewalls
- Records GroupId for later use
- Initially has no inbound rules

**2. Add Inbound Rule**
```bash
aws ec2 authorize-security-group-ingress \
--group-id <CafeDatabaseSG Group ID> \
--protocol tcp --port 3306 \
--source-group <CafeSecurityGroup Group ID>
```
**Notes**:
- Allows MySQL traffic (port 3306) only from Café application
- Follows principle of least privilege
- Verify with describe-security-groups command

**3. Create Private Subnet 1**
```bash
aws ec2 create-subnet \
--vpc-id <CafeVpcID> \
--cidr-block 10.200.2.0/23 \
--availability-zone <CafeInstanceAZ>
```
**Notes**:
- CIDR 10.200.2.0/23 chosen to avoid overlap with existing subnets
- Same AZ as Café instance for low latency
- Records SubnetId for later

**4. Create Private Subnet 2**
```bash
aws ec2 create-subnet \
--vpc-id <CafeVpcID> \
--cidr-block 10.200.10.0/23 \
--availability-zone <Different AZ>
```
**Notes**:
- Different AZ for high availability
- Required for RDS multi-AZ deployment option
- CIDR must not overlap with other subnets

**5. Create DB Subnet Group**
```bash
aws rds create-db-subnet-group \
--db-subnet-group-name "CafeDB Subnet Group" \
--db-subnet-group-description "DB subnet group for Cafe" \
--subnet-ids <Subnet1> <Subnet2> \
--tags "Key=Name,Value=CafeDatabaseSubnetGroup"
```
**Notes**:
- RDS requires subnet group spanning at least 2 AZs
- Enables high availability features
- Tags help with resource identification

#### Task 2.4: Creating the Amazon RDS MariaDB Instance

**Purpose**: Launch managed database instance.

```bash
aws rds create-db-instance \
--db-instance-identifier CafeDBInstance \
--engine mariadb \
--engine-version 10.5.20 \
--db-instance-class db.t3.micro \
--allocated-storage 20 \
--availability-zone <CafeInstanceAZ> \
--db-subnet-group-name "CafeDB Subnet Group" \
--vpc-security-group-ids <CafeDatabaseSG Group ID> \
--no-publicly-accessible \
--master-username root --master-user-password 'Re:Start!9'
```
**Notes**:
- db.t3.micro is smallest instance class (suitable for lab)
- 20GB storage is minimum for MariaDB
- Not publicly accessible (private subnet only)
- Strong password required
- Takes ~10 minutes to provision

**Monitoring Creation**:
```bash
aws rds describe-db-instances \
--db-instance-identifier CafeDBInstance \
--query "DBInstances[*].[Endpoint.Address,AvailabilityZone,PreferredBackupWindow,BackupRetentionPeriod,DBInstanceStatus]"
```
**Notes**:
- Status progresses: creating → modifying → backing-up → available
- Records endpoint address (critical for connection)
- Default backup retention: 1 day
- Automatic backups enabled by default

### Task 3: Migrating Application Data to Amazon RDS

**Purpose**: Transfer data from local DB to RDS.

**1. Connect to Café Instance**
- Same method as CLI Host connection

**2. Create Database Backup**
```bash
mysqldump --user=root --password='Re:Start!9' \
--databases cafe_db --add-drop-database > cafedb-backup.sql
```
**Notes**:
- mysqldump creates SQL script of database structure and data
- --add-drop-database ensures clean recreation
- Verify backup with less command

**3. Restore to RDS**
```bash
mysql --user=root --password='Re:Start!9' \
--host=<RDS Endpoint> < cafedb-backup.sql
```
**Notes**:
- Uses mysql client to execute backup script
- Connects to RDS endpoint
- May take time for large databases

**4. Verify Migration**
```bash
mysql --user=root --password='Re:Start!9' \
--host=<RDS Endpoint> cafe_db
```
```sql
SELECT * FROM product;
```
**Notes**:
- Confirm data matches original
- Check order count matches Task 1
- Exit with 'exit' command

### Task 4: Configuring Website to Use RDS

**Purpose**: Update application configuration.

**Steps**:
1. Open AWS Systems Manager → Parameter Store
2. Select /cafe/dbUrl parameter
3. Edit value to RDS endpoint address
4. Save changes

**Verification**:
1. Access café website
2. Check Order History matches pre-migration count
3. (Optional) Place new test orders

**Notes**:
- Parameter Store provides centralized configuration
- Application designed to read DB URL from parameter
- No code changes required
- Zero downtime migration possible with proper design

### Task 5: Monitoring Amazon RDS Database

**Purpose**: Observe database performance metrics.

**Steps**:
1. Open RDS Console → Databases → CafeDBInstance
2. Navigate to Monitoring tab
3. Observe various metrics:
   - CPUUtilization
   - DatabaseConnections
   - FreeStorageSpace
   - FreeableMemory
   - Read/Write IOPS

**Connection Test**:
1. Establish MySQL connection from Café instance
2. Observe DatabaseConnections metric update
3. Close connection
4. Verify metric returns to zero

**Notes**:
- Metrics reported every minute
- CloudWatch provides historical data
- Alarms can be set on critical metrics
- Monitoring helps right-size resources

## Conclusion

**Key Learnings**:
1. Created RDS instance with proper networking (subnets, security groups)
2. Migrated data using mysqldump utility
3. Updated application configuration via Parameter Store
4. Monitored database performance

**Best Practices Demonstrated**:
- Database in private subnets
- Minimal network access (security groups)
- Parameterized configuration
- Monitoring enabled
- Backup retention configured

**Potential Next Steps**:
- Implement read replicas for scaling
- Enable Multi-AZ for high availability
- Set up CloudWatch alarms
- Implement automated backup testing