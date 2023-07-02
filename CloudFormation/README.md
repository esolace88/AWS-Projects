# AWS Cloud Formation (IaC)

Welcome to the Cloud Formaiton Project! This is a simple project that leverages AWS native IaC tool CloudFormation to rapidly build AWS Services via code in yml or json format. This project will cover how to deploy premade files to create AWS resources. 

## Getting Started

To get started, you will need an AWS account to gain access to AWS CloudFormation, and the pre-made files located in this repository. 

      ```bash
      git clone https://github.com/esolace88/AWS-Projects.git
      cd CloudFormation/Simple-s3-db/
      ```

-------------

## Step by Step 

### Intial Creation
1. Log Into your AWS account
2. Navigate to CloudFormation
3. Create a "New Stack"
	Create Stack > With New Resources
4. Select Template is Ready > Upload a Template File
![alt text](https://github.com/esolace88/AWS-Projects/blob/main/CloudFormation/img/InitialCreation.png)
5. Name the Stack in Step 2 "Specify Stack Details" > Stack Name
6. Accept the Defaults and hit Submit on the last page. 
7. Wait for the task to complete and review services

### Update to Stacks

1. Select Stack to Update
2. Select Stack Actions > Create change for current Stack 
3. Replace Current Template > Upload Template
![alt text](https://github.com/esolace88/AWS-Projects/blob/main/CloudFormation/img/UpdateStack.png)
4. Accept defaults and Submit 
5. Wait for page to loag, Then Select Execute Change Set