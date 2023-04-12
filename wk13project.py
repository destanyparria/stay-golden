#!/usr/bin/env python

import os

# Get current working directory
path = os.getcwd( ) 

# Creates an empty list 
list_of_dict = [ ] 

for file in os.listdir( ):
    file_dict = { }
    file_dict['path'] = os.path.realpath(file)
    file_dict['size'] = os.path.getsize(file) 
    list_of_dict.append(file_dict)
    
    print(*list_of_dict, sep="\n") 
