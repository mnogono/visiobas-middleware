#!/usr/bin/env python

"""
tools for working with BACnet devices
"""

import subprocess
import json

global bacnet_stack_folder
bacnet_stack_folder = '~/w/bacnet-stack-0.8.3/bin'

def device_list(host, port, device):
    global bacnet_stack_folder
    
    epics = backnet_stack_folder + '/bacepics'
    print 'epics: ', epics
    cout = subprocess.check_output([epics, str(device)])
    return cout
