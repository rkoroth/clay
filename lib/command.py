#!/usr/bin/python


import yaml
import os

output = dict()
def Command(yaml_config):
    with open(yaml_config, "r") as f:
        myval = yaml.safe_load(f)
    output['message'] = myval[0]['Description']
    if os.system(myval[0]['Cmd']):
        output['status'] = True
    else:
        output['status'] = False

    return output

