from tools.analyse import *
from tools.web_selenium import *
import numpy as np
import sys
import json
import os

f = open('/path/data.json')
data = json.load(f)

web = selenium("https://www.binance.com/fr/support/announcement/nouveaux-listing-de-cryptomonnaies?c=48",10)

cookie_element  = "//button[@id='onetrust-reject-all-handler']"

#True (execution pc) False (serveur)
web.click_items(cookie_element, False)

annonce_link = "//div[2]/div[2]/div[2]/section/div/div/div[3]/a/div"
annonce = web.click_items(annonce_link, False)
web.end()

if data["bool"] == True:
    print("attente d'une execution de paire")
    sys.exit()

var = analyse(annonce)

if var.check_paire(["introduction", "listera"]) == True:
    paire = var.paire()
else:
    print("aucune paire detectée")
    sys.exit()


if data["paire"] == paire[0]:
    print("paire déja executer")
    sys.exit()

with open('/path/data.json', 'r+') as f:
    data = json.load(f)
    data['bool'] = True # add
    data['paire'] = paire[0] # add
    f.seek(0)        
    json.dump(data, f, indent=4)
    f.truncate()     

os.system('/path/loop.sh')
