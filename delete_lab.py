#!/usr/bin/env python
#This Script creates the CSR from AMI and the key - split out the key
import json, re, sys, os, json, subprocess, time, sys
from subprocess import call, check_output

outfile_vars="vars"
lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *

#Delete the instances
#Get the CSR Instance Id
#Get the ubuntu lan instance id
#Get the ubuntu router instance id


outfile_key_pair = 'keypair_name' + '.json'
outfile_get_vpcid = 'vpcid' + '.json'
outfile_get_subnetid_router = 'subnetid_router' + '.json'
outfile_get_sgid= 'sgid' + '.json'
outfile_get_subnetid_lan= 'subnetid_lan' + '.json'
outfile_csr_pub_ip= 'csr_pub_ip' + '.json'
outfile_csr_instance_id= 'csr_instance_id' + '.json'






#get the router security group id
#aws ec2 describe-security-groups --filters "Name=vpc-id,Values=vpc-01bdad153448ce387" --filters "Name=group-name,Values=sg01
get_sgid='aws ec2 describe-security-groups --region' + " " + "{}".format(region) + " " + '--filters "Name=group-name,Values=' + "{}".format(sg_name) + '"'
output = check_output("{}".format(get_sgid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_get_sgid, 'w') as my_file:
    my_file.write(output)
with open (outfile_get_sgid) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['SecurityGroups']
    question_replies=question_access[0]
    question_data=question_replies['GroupId']
    sgid=question_data
    print(sgid)
    sgid_var=('sgid=' + "'" + "{}".format(sgid) + "'")
with open(outfile_vars, 'a+') as my_file:
    my_file.write(sgid_var + "\n")









#Delete the CSR

#Delete the Ubuntu LAN

#Delete the Ubuntu Router



#Delete the secondary NiC on the CSR


#Delete the Security Group


#Delete the key


#Get the VPC Id
#get the vars and write them to a file for import
#get the vpcid for vpc01
get_vpcid='aws ec2 describe-vpcs --region' + " " + "{}".format(region) + " " + '--filters Name=tag:Name,Values=' + "{}".format(name)
output = check_output("{}".format(get_vpcid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_get_vpcid, 'w') as my_file:
    my_file.write(output)
with open (outfile_get_vpcid) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['Vpcs']
    question_data=question_access[0]
    replies_access=question_data['VpcId']
    vpcid=replies_access
    print(vpcid)
    vpcid_var=('vpcid=' + "'" + "{}".format(vpcid) + "'")

with open(outfile_vars, 'w') as my_file:
    my_file.write(vpcid_var + "\n")

