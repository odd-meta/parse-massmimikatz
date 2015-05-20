#!/usr/bin/env python

import sys
from pprint import pprint

FILENAME = sys.argv[1]

f = open(FILENAME, "r")

credentials = []

"""
credentials are stored in the form of

{ 
    'machine_name' : "DESKTOPMACHINE01",
    'domain'       : "CONTOSO",
    'username'     : "john.doe",
    'password'     : "Password1"
}

"""

_machine_name = ""
_domain = ""
_username = ""
_password = ""

for line in f:
    if line.find("* Username : ") != -1:
        raw_username = line.split("* Username : ")
        _username = raw_username[1][:-1]
        raw_machine_name = raw_username[0].split(".txt-")
        _machine_name = raw_machine_name[0]
    elif line.find("* Password : ") != -1:
        raw_password = line.split("* Password : ")
        _password = raw_password[1][:-1]
    elif line.find("* Domain   : ") != -1:
        raw_domain = line.split("* Domain   : ")
        _domain = raw_domain[1][:-1]
    elif line == "--\n":
        if _machine_name == "" or _domain == "" or _username == "" or _password == "":
            print "Not enough information given for credential"
            pprint(_machine_name)
            pprint(_domain)
            pprint(_username)
            pprint(_password)
            break
        else:
            print("Appended credential for %s" % _username)
            credentials.append( { 
                'machine_name' : _machine_name,
                'domain'       : _domain,
                'username'     : _username,
                'password'     : _password
            })
            
            _machine_name = ""
            _domain = ""
            _username = ""
            _password = ""
            
def get_unique_users(creds):
    users = []
    
    for credential in creds:
        username = credential['username']
        if username in users:
            pass
        else:
            if len(credential['password']) < 40 and credential['password'] != "(null)":
    
                print credential['password']
            users.append(username)


get_unique_users(credentials)














