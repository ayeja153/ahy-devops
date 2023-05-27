# This code prints instance id, instance name and instance status 
# using aws lambda functions

import boto3
import logging

ec2 = boto3.resource('ec2')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    instances = ec2.instances.all()
    logger.info("Instances list")
    for instance in instances: 
        instance_name = ''
        for tag in instance.tags:
            if tag['Key'] == 'Name':
              instance_name = tag['Value']
            break
        logger.info(f"Instance {instance.id} with name {instance_name} is {instance.state['Name']}")
