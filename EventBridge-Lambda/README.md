# AWS EventBus & Lambda Project

Welcome to the EventBus and Lambda project! This is a simple project that leverages AWS EventBus and Lambda to create an Event trigger System, which can help application to decuple to create alternative tasks. (See Demo folder for a quick view of the end product)

## Getting Started

To get started, you will need an AWS account to create an IAM User, EventBus w/ Rules, and Lambda Services. You will also need access to an IDE, to run the application code. 

Note your IDE must have the following packages installed to function:

	re, os, json, boto3, datetime, uuid, datetime, json

-------------

## Step by Step 

**Creating IAM User**
1. Login into AWS
2. Create a user w/ no groups or permission
3. Once Created, Establish Access Keys
	Users > User Created > Security Credentials > Access Keys > Local Code
	**Note: This is not a recommended method, this method was used as proof of concept**
4. Copy the Secret Information and save it for later use
5. Then add the following policy to the user: AmazonEventBridgeFull Access

**Creating a Lambda Service**
1. Navigate to Lambda
2. Create Lambda Service
3. Select Author From Sracth
4. Under Basic Informaiton 
	a. Enter Name
	b. Runtime = Python
5. Accept Defaults and Create

**Creating Event Bus**
1. Navigate to Amazon EventBridge
2. Select "Event Buses"
3. Name the Bus > Create

**Creating Bus Rules**
1. Select Rules from the left navigation page
2. In the Event Bus field select your newly created bus
3. Create New Rule
4. Name the rule
5. In Step 2 "Build event Pattern" scroll to Creating Method and select "Custom Pattern"
      ```bash
    {
    "detail":{
        "status":["new order"]
    }

    }  
      ```
6. In Event Pattern Section enter the JSON code 
7. In Step 3, "Select targets" In Trigger Section add Lambda > select previously created function.

**Modifying Code**
1. Open EventBus file and modify the following sections with your service information. 
      ```bash
        # Enter Your User Key Access and Event Bus ARN
        self.AWS_ACCESS_KEY = "xxxxx"
        self.AWS_SECRET_KEY = "xxxxx"
        self.AWS_REGION_NAME = "us-east-1"
        self.EventBusName = 'xxxx'
      ```


**Executing Code and Reviewing Results**
1. Run the Code within an IDE
2. Navigate to the Lambda Funciton > Monitor > View CloudWatch Logs
3. View the Latest Log and Review the Message



