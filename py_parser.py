#!/usr/bin/python

import sys, getopt
import subprocess
import json
import httplib, urllib

headers = {
    "Content-type": "application/json"
}
try:
    conn = httplib.HTTPConnection("212.193.163.6", 80)
    conn.request("GET", "/")
    res = conn.getresponse()
    print res.status, res.reason
    print res.read()
except Exception as e:
    print e.__doc__
    print e.message
#print 
sys.exit()


#special application to get bac net server information
BAC_EPICS = 'bacepics'

device = -1
bac_epics = 'bacepics'
out = ''
format = "json"

def cmd(argv):
    global device
    global bac_epics
    global format
    
    try:
        opts, args = getopt.getopt\
        (argv, "hd:b:f:", ["device=", "bacepics=", "format="])
    except getopt.GetoptError:
        print __file__, '-d <device> -b <bacepics>'

    for opt, arg in opts:
        if opt == '-h':
            print __file__, '-d <device> -b [bacepics] -f [json]'
            sys.exit()
        elif opt in ("-d", "--device"):
            device = int(arg)
        elif opt in ("-b", "--bacepics"):
            bac_epics = arg
        elif opt in ("-f", "--format"):
            format = arg
            if format <> "json":
                print "unsopported format: ", arg
                sys.exit()


def run():
    global out
    out = subprocess.check_output([bac_epics, str(device)])

def parse():
    global format
    if format == 'json':
        parseJson()

def parseJson():
    global out
    js = json.load(out)

def pasreOut():
    global out


def main(argv):
    global format
    
    cmd(argv)
    run()
    parse()
    post()
    
if __name__ == "__main__":
    main(sys.argv[1:]);
