#!/usr/bin/python


import yaml
import sys
sys.path.append("/myscripts/Clay/lib")
import checkDir


#read sequence 
#identify the first task 
#check the type from the first task yaml
#if the type is CheckDir use an if statement to process it 
#then use CheckDir module and execute the process.
# process will return a diction with status and messages

#*** This is the main wrapper of the doll ***


with open("../conf/sequence.yaml", "r") as f:
    myval = yaml.safe_load(f)
    print ('"""""""LIST OF TASKS""""""""')
    for Task in myval['Task']:
        print (Task['desc'])
        print (myval)

print ('"""""""""""Running Tasks"""""""""""""""')
for task in myval['Task']:
   play_file = f"/myscripts/Clay/conf/play/{task['conf']}"
   with open(play_file , "r") as ss:
       tas = yaml.safe_load(ss) 
       mod_type = (tas[0]['type'])
       if mod_type == "checkDir":
          output = checkDir.CheckDir(play_file)
          print (output['message'])
          print (output['status'])

