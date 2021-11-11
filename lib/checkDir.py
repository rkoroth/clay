#!/usr/bin/python


import yaml 
import os 

output = dict()
def CheckDir(yaml_config):
    with open(yaml_config, "r") as f:
        myval = yaml.safe_load(f)
    output['message'] = myval[0]['Description']
    if os.path.isdir(myval[0]['Dir']):
        output['status'] = True
    else:
        output['status'] = False

    
    return output
