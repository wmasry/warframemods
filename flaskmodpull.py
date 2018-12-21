
import sys
def modpull(a):
    import requests
    import sys
    import json
    URL = 'https://api.warframestat.us/mods'
    r = requests.get(URL)
    print("\n")
    wf_objs = r.json()
    for obj in wf_objs:
        if obj['category'] == u'Mods' and a in obj['name'].lower() :
            print ("Name: %s") % obj['name']
            print ("Polarity: %s") % obj['polarity']
            print ("Rarity: %s") % obj['rarity']
            print ("Description: %s") % obj['description']
            return obj['name'] , obj['polarity']
    if len(sys.argv) > 2:
        if sys.argv[2] == "all":
            for obj in wf_objs:
                if obj['category'] == u'Mods' and a in obj['name'].lower() :
                    print obj
def main():
  inputname = sys.argv[1].lower()
  x=modpull(inputname)
  print x
if __name__ == "__main__":
  main()
