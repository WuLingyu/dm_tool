# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:16:43 2017

@author: lingyu
"""
import os, sys

def full_file(full_path, files):
    temp = []
    for f in files:
        temp.append(os.path.join(full_path, f))
    return temp

def clear_cache():
    q_list = [] # common queue
    t_list = [] # list used to store target file 

    # current folder as root
    cur = os.path.split(sys.path[0])[0]
    q_list.extend(full_file(cur, os.listdir(cur)))

    # find all .pyc files
    while 1:
        if q_list == []:
            break;
        f = q_list.pop()
        if os.path.isdir(f) == True:
            q_list.extend(full_file(f, os.listdir(f)))
        else:
            if f.endswith('.pyc'):
                t_list.append(f)
    # remove all these files
    for f in t_list:
        os.remove(f)

