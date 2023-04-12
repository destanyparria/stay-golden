#!/usr/bin/env python3.7

import os 

# Get current working directory
cwd = os.getcwd( )

# Creates an empty list 
dict_list = [ ] 

for file_name in os.listdir(cwd):
    file_path = os.path.join(cwd, file_name) 
    
    file_size = os.path.getsize(file_path)
    
    dict_file = {
        'file_name' : file_name,
        'file_path' : file_path,
        'file_size' : file_size
    }
    
    # Add the dictionary to the list
    dict_list.append(dict_file)
    
    print(dict_list, sep="\n") 

