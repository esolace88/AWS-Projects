# AWS Elastic Cache Project

Welcome to the Elastic Cache project! This is a simple project that leverages AWS Elastic Cache to improve an application's performance. (See Demo folder for a quick view of the end product)

## Getting Started

To get started, you will need an AWS account to create an EC2 instance, RDS service, and ElastiCache.

The environment used in the Project:

EC-2
  Image: Amazon Linux 2023
  Architecture: x86
  Instance Type: t2.micro

RDS
  Engine: PostgreSQL
  Templates: Free tier
  Instance Type: db.t3.micro

Redis cluster
  Method: Configure and Create New Cluster
  Instance Type: cache.t3.micro

-------------

## Step by Step 

1. Log Into your AWS account

2. Create an EC-2 Instance 
	a. Select Image 
	b. Download Keys
	c. Define Network Settings
		1. Ensure Auto Public IP is Enabled
		2. Rename Security Group for ease of identification i.e SG-Application
	d. Add Custom Data i.e bootstrap
      ```bash
      #!/bin/bash
      yum install postgresql-devel postgresql15 gcc git python3-devel python3-pip -y 
      pip3 install psycopg2 redis flask
      yum update -y      
      ```

3. Modify RDS Security Group to allow EC2 PostgreSQL access

4. Create a Security Group for Cache Service
	a. Inbound Rule, Custom TCP 6379, Source = Application Security Group
      
5. Create ElasticCache Server 
	a. Redis Cluster & Name
	b. Accept Default with 2 replicas
	c. Create a new subnet group and select all available group
	d. Choose Created Recently Created Security Group
	e. Take note of the Primary Endpoint

6. Create RDS with PostgreSQL Engine
	a. Name DB
	b. Define Username
	c. Define Password
	d. Name Security Group ease of identification i.e SG-PostgreSQL
	f. Take note of the Endpoint

7. Configure Application -
	a. SSH into Sever
      ```bash
      chmod 400 </path/to/key>
      ssh -L 5000:127.0.0.1:5000 ec2-user@<publicIP> -i <key>
      ```
	b. Verify packages are installed
      ```bash
      dnf list <package name>
      pip list | grep -F package_name
      ```
	c. Define Variable to connect to RDS
      ```bash
      export PGHOST=project.cgsil5kpp9xl.us-east-1.rds.amazonaws.com
      ```
	d. Log into the RDS server
	e. Create a db and name it
	f. Create a user and define a password
      ```bash
      psql -U <enterdb user of rds service>
      create database <enter a name for db>;
      create user <enter a name for user> password '<input password>';
      grant all on DATABASE <db name> to <db user>;
      \q
      ```
	g. Test new user login
      ```bash
       psql -U <enterdb newly created user>
      ```
	h. Clone Git Hub Repo
      ```bash
      git clone https://github.com/esolace88/AWS-Projects.git
      cd ElasticCache
      ```
	i. Modify database init file
      ```bash
      [postgresql]
      host=<enter endpoint name from 6f>
      database=<enter db name from step 7f>
      user=<enter username from step 7f>
      password=<enter password from step 7f>

      ```
	j. Apply config to RDS
      ```bash
      psql -U project -f install.sql
      ```
8. Test Application without Elastic Cache:
-- Open a browser tab to 127.0.0.1:5000 & check load times 
   ```bash
   python3 app.py
   ```
9. Test Application with Elastic Cache:
-- Modify the database init file and add the "Redis" field
-- Verify we can connect to the Redis cluster
-- Modify App fetch settings (See 'def fetch(sql).py' file)
-- Run the app & view the results
     
   	 ```bash
	[redis]
	redis_url=redis://<enter redis enpoint>

	python3
   	import redis
	cache = redis.Redis.from_url('redis://<paste end point>')
	cache.ping()

    	python3 app.py
   	```

