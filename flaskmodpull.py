#!/usr/bin/python2


import sys
def modpull(a, b):
    import requests
    import sys
    import json
    URL = 'https://api.warframestat.us/mods'
    r = requests.get(URL)
    wf_objs = r.json()
    for obj in wf_objs:
        if obj['category'] == u'Mods' and a in obj['name'].lower() :
            if b == "name":
              return "Name: %s" % obj['name']
            elif b == "Polarity":
              return ("Polarity: %s") % obj['polarity']
            elif b == "Rarity":
              return ("Rarity: %s") % obj['rarity']
            elif b  == "Description":
              return ("Description: %s") % obj['description']
    if len(sys.argv) > 2:
        if sys.argv[2] == "all":
            for obj in wf_objs:
                if obj['category'] == u'Mods' and a in obj['name'].lower() :
                    print obj
def main():
  inputname = sys.argv[1].lower()
  x=modpull(inputname, "name")
  print (x)
  x=modpull(inputname, "Polarity")
  print(x)
  x=modpull(inputname, "Rarity")
  print(x)
  x=modpull(inputname, "Description")
  print(x)

if __name__  == "__main__":
  main()
