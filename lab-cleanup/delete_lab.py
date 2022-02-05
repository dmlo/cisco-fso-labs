#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time
from subprocess import call, check_output

outfile_vars="vars"
lab_vars='lab_vars.py'
from lab_vars import *

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
    my_file.write(vpcid_var + "\n"



#Get the NIC ID
#aws ec2 describe-network-interfaces --region us-west-1 --filters Name=description,Values=csr_nic_lan_sub --query "NetworkInterfaces[*].NetworkInterfaceId" --output text
#aws ec2 describe-network-interfaces --region us-east-1 --filters Name=description,Values=csr_nic_lan_sub --query "NetworkInterfaces[*].NetworkInterfaceId" --output text
get_csr_nic='aws ec2 describe-network-interfaces --region' + " " "{}".format(region) + " " + '--filters Name=description,Values=csr_nic_lan_sub' + " " + '--query' + " " + '"NetworkInterfaces[*].NetworkInterfaceId"' + " " '--output text'


#DELETE NETWORK INTERFACES
delete_nic='delete-network-interface --network-interface-id' + " " + "{}".format(nic)
output = check_output("{}".format(delete_nic), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

#DELETE VPC
delete_vpc='aws ec2 delete-vpc' + " " + "{}".format(vpcid)
output = check_output("{}".format(delete_vpc), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

