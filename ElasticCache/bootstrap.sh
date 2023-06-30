#!/bin/bash
yum install postgresql-devel postgresql15 gcc git python3-devel python3-pip -y 
pip3 install psycopg2 redis flask
yum update -y