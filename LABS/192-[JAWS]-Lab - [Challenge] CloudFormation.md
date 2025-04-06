# AWS re/Start CloudFormation Challenge Lab - Comprehensive Guide

## Table of Contents
- [AWS re/Start CloudFormation Challenge Lab - Comprehensive Guide](#aws-restart-cloudformation-challenge-lab---comprehensive-guide)
  - [Table of Contents](#table-of-contents)
  - [Lab Overview](#lab-overview)
  - [Lab Objectives](#lab-objectives)
  - [Lab Restrictions](#lab-restrictions)
  - [Accessing the AWS Management Console](#accessing-the-aws-management-console)
  - [Using the Browser Terminal](#using-the-browser-terminal)
  - [Creating the CloudFormation Template](#creating-the-cloudformation-template)
    - [Template Structure](#template-structure)
    - [VPC Configuration](#vpc-configuration)
    - [Internet Gateway](#internet-gateway)
    - [Subnet Configuration](#subnet-configuration)
    - [Security Group](#security-group)
    - [EC2 Instance](#ec2-instance)
  - [Full](#full)
  - [Another version](#another-version)
  - [Deploying the Stack](#deploying-the-stack)
  - [Troubleshooting](#troubleshooting)
  - [Validation](#validation)
  - [Cleanup](#cleanup)
  - [Conclusion](#conclusion)

## Lab Overview
This challenge lab requires you to create an AWS CloudFormation template that provisions:
- A complete VPC with networking components
- An EC2 instance in a private subnet
- All necessary supporting infrastructure

## Lab Objectives
By completing this lab, you will demonstrate ability to:
1. Author a CloudFormation template in YAML
2. Configure core VPC components
3. Deploy an EC2 instance with proper networking
4. Troubleshoot template errors
5. Validate successful deployment

## Lab Restrictions
You only have access to services needed for:
- VPC components
- EC2 instances
- Security groups
- CloudFormation operations

## Accessing the AWS Management Console
1. Click **Start Lab** to begin your session
2. Wait for "Lab status: in creation" message
3. Click the **AWS** button to open the console
4. Allow pop-ups if blocked by your browser

## Using the Browser Terminal
The terminal to the right provides:
- Pre-configured AWS CLI access
- Python 3 with boto3
- Direct shell access

Verify your credentials:
```bash
aws sts get-caller-identity
```

## Creating the CloudFormation Template

### Template Structure
Create a new file `vpc-ec2.yml` with this basic structure:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: VPC with EC2 instance in private subnet
Resources:
  # Resources will be added here
```

### VPC Configuration
Add the VPC resource:
```yaml
  MyVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: MyVPC
```

### Internet Gateway
Add the Internet Gateway and attachment:
```yaml
  MyInternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: MyIGW

  GatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref MyVPC
      InternetGatewayId: !Ref MyInternetGateway
```

### Subnet Configuration
Add a private subnet:
```yaml
  PrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs '']
      Tags:
        - Key: Name
          Value: PrivateSubnet
```

### Security Group
Create a security group allowing SSH:
```yaml
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable SSH access
      VpcId: !Ref MyVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
```

### EC2 Instance
Add the EC2 instance:
```yaml
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t3.micro
      ImageId: ami-0c55b159cbfafe1f0 # Amazon Linux 2 in us-west-2
      SubnetId: !Ref PrivateSubnet
      SecurityGroupIds:
        - !Ref InstanceSecurityGroup
      Tags:
        - Key: Name
          Value: MyInstance
```
## Full
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: VPC with EC2 instance in private subnet
Resources:
  MyVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: MyVPC

  MyInternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: MyIGW

  GatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref MyVPC
      InternetGatewayId: !Ref MyInternetGateway

  PrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs '']
      Tags:
        - Key: Name
          Value: PrivateSubnet

  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable SSH access
      VpcId: !Ref MyVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0

  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t3.micro
      ImageId: ami-09dc20c616c152018
      SubnetId: !Ref PrivateSubnet
      SecurityGroupIds:
        - !Ref InstanceSecurityGroup
      Tags:
        - Key: Name
          Value: MyInstance
```
## Another version
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: VPC with EC2 instance in private subnet
Parameters:
  KeyName:
    Type: 'AWS::EC2::KeyPair::KeyName'
    Description: '(Optional) Name of an existing EC2 KeyPair'
    Default: ''

Resources:
  MyVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: MyVPC

  MyInternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: MyIGW

  GatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref MyVPC
      InternetGatewayId: !Ref MyInternetGateway

  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone: !Select [0, !GetAZs '']
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: PublicSubnet

  PrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs '']
      Tags:
        - Key: Name
          Value: PrivateSubnet

  NatGatewayEIP:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc

  NatGateway:
    Type: AWS::EC2::NatGateway
    DependsOn: GatewayAttachment
    Properties:
      AllocationId: !GetAtt NatGatewayEIP.AllocationId
      SubnetId: !Ref PublicSubnet
      Tags:
        - Key: Name
          Value: MyNATGateway

  PrivateRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref MyVPC
      Tags:
        - Key: Name
          Value: PrivateRouteTable

  PrivateRoute:
    Type: AWS::EC2::Route
    DependsOn: NatGateway
    Properties:
      RouteTableId: !Ref PrivateRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGateway

  PrivateSubnetRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PrivateSubnet
      RouteTableId: !Ref PrivateRouteTable

  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable SSH access
      VpcId: !Ref MyVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0

  MyEC2Instance:
    Type: AWS::EC2::Instance
    DependsOn: 
      - NatGateway
      - PrivateSubnetRouteTableAssociation
    Properties:
      InstanceType: t2.micro
      ImageId: !FindInMap [RegionMap, !Ref 'AWS::Region', AMI]
      SubnetId: !Ref PrivateSubnet
      SecurityGroupIds:
        - !Ref InstanceSecurityGroup
      KeyName: !If [HasKeyName, !Ref KeyName, !Ref 'AWS::NoValue']
      Tags:
        - Key: Name
          Value: MyInstance

Mappings:
  RegionMap:
    us-east-1:
      AMI: ami-0aa7d40eeae50c9b9
    us-west-2:
      AMI: ami-0c55b159cbfafe1f0
    eu-west-1:
      AMI: ami-0d1ddd83282187d18

Conditions:
  HasKeyName: !Not [!Equals [!Ref KeyName, '']]
```

Find the latest Amazon Linux 2 AMI for your region:

```bash
aws ec2 describe-images \
  --owners amazon \
  --filters "Name=name,Values=amzn2-ami-hvm-2.0.*-x86_64-gp2" \
  --query 'sort_by(Images, &CreationDate)[-1].ImageId' \
  --output text
```
## Deploying the Stack
Deploy your template:
```bash
aws cloudformation create-stack \
  --stack-name VPC-EC2-Lab \
  --template-body file://vpc-ec2.yml \
  --capabilities CAPABILITY_IAM
```

Monitor deployment:
```bash
aws cloudformation describe-stack-events \
  --stack-name VPC-EC2-Lab \
  --query 'StackEvents[?ResourceStatus==`CREATE_FAILED`]'
```

## Troubleshooting
Common issues and solutions:

1. **AMI Not Found**:
   - Verify the AMI ID is correct for your region
   - Use AWS CLI to find AMIs: `aws ec2 describe-images --owners amazon`

2. **Subnet Configuration Errors**:
   - Ensure CIDR blocks don't overlap
   - Verify AZ availability

3. **Resource Limits**:
   - Check your account's VPC/EC2 limits
   - Request limit increases if needed

## Validation
Verify successful deployment:

1. Check stack status:
```bash
aws cloudformation describe-stacks \
  --stack-name VPC-EC2-Lab \
  --query 'Stacks[0].StackStatus'
```

2. Verify resources:
```bash
aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=MyInstance"
```

## Cleanup
Delete the stack when complete:
```bash
aws cloudformation delete-stack --stack-name VPC-EC2-Lab
```

## Conclusion

You've successfully:
1. Created a CloudFormation template for VPC and EC2
2. Configured networking components
3. Deployed an EC2 instance in a private subnet
4. Troubleshot deployment issues
5. Validated the infrastructure

**Key Takeaways**:
- CloudFormation enables infrastructure as code
- VPC components must be properly connected
- Template validation catches syntax errors early
- Incremental testing reduces troubleshooting complexity