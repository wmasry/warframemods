#!/usr/env python2

import requests
import sys
import json

URL = 'https://api.warframestat.us/mods'

if len(sys.argv) > 1:
    mod_name = sys.argv[1].lower()
else:
    print ("Please pass a mod name (full or partial)")
    sys.exit(1)

try:
    r = requests.get(URL)
except ex:
    print 'exception: ' + ex
    sys.exit(1)

print("\n")
wf_objs = r.json()
for obj in wf_objs:
    if obj['category'] == u'Mods' and mod_name in obj['name'].lower() :
        print ("Name: %s") % obj['name']
        print ("Polarity: %s") % obj['polarity']
        print ("Rarity: %s") % obj['rarity']
        print ("Description: %s\n\n") % obj['description']    

if len(sys.argv) > 2:
    if sys.argv[2] == "all":
        for obj in wf_objs:
            if obj['category'] == u'Mods' and mod_name in obj['name'].lower() :
                print obj
