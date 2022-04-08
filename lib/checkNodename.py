#!/usr/bin/python


import yaml
import os

output = dict()
def CheckNodename(yaml_config):
    with open(yaml_config, "r") as f:
        myval = yaml.safe_load(f)
    output['message'] = myval[0]['Description']
    if os.uname:
        output['status'] = True
    else:
        output['status'] = False


    return output

