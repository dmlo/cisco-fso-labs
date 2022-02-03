#!/usr/bin/env python
#This Script creates the CSR from AMI and the key - split out the key
import json, re, sys, os, json, subprocess, time, sys
from subprocess import call, check_output

outfile_vars="vars"
lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *

#get the vpc id then search for all instances in that vpc and delete them

#Get the default vpc for the us-east region
outfile_get_vpcid = 'get_vpcid.json'
#def_vpcid='aws ec2 describe-vpcs --region us-east-1 --filters Name=tag:Name,Values=DEFAULT'
get_vpcid='aws ec2 describe-vpcs --region' + " " + "{}".format(region) + " " + '--filters Name=tag:Name,Values=' + "{}".format(name)
output = check_output("{}".format(get_vpcid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_def_vpcid, 'w') as my_file:
    my_file.write(output)
with open (outfile_def_vpcid) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['Vpcs']
    print(question_access)
    replies_access = question_access[0]
    print(replies_access)
    replies_data=replies_access['VpcId']
    vpcid=replies_data
    get_vpcid_var=('vpcid=' + "'" + "{}".format(vpcid) + "'")
    print(get_vpcid_var)

#get the instance IDs for the region and the vpc
aws ec2 describe-instances --filters Name=availability-zone,Values=us-east-2b



get_instances='aws ec2 describe-instances --region' + " " +  "{}".format(region) + " " + '--filters Name=tag:availability-zone,Values=' + "{}".format(az)
'aws ec2 run-instances --region' + " " + "{}".format(region) + " " + '--image-id' + " " + "{}".format(ubuntu_ami_id) + " " + '--instance-type' + " " + "{}".format(instance_type) + " " + '--subnet-id' + " " + "{}".format(subnetid_router) + " " + '--security-group-ids' + " " + "{}".format(sgid) + " " + '--associate-public-ip-address' + " " + '--key-name' + " " + "{}".format(keypair_name) + " " + '--placement AvailabilityZone=' + "{}".format(az)