from tools.analyse import *
from tools.web_selenium import *
import numpy as np
import sys

web = selenium("https://www.binance.com/fr/support/announcement/nouveaux-listing-de-cryptomonnaies?c=48",10)

cookie_element  = "//button[@id='onetrust-reject-all-handler']"
# Cas spécial
web.click_items(cookie_element, False)

annonce_link = "//div[2]/div[2]/div[2]/section/div/div/div[3]/a/div"
annonce = web.click_items(annonce_link, False)
web.end()

bool = np.load("numpy/bool.npy")
if bool == True:
    print("attente d'une execution de paire")
    sys.exit()

var = analyse(annonce)

if var.check_paire(["introduction", "listera"]) == True:
    paire = var.paire()
else:
    print("aucune paire detectée")
    sys.exit()

previous_paire  =  np.load("numpy/paire.npy")
if previous_paire == paire:
    print("paire déja executer")
    sys.exit()


data_paire = np.array(paire)
np.save("numpy/paire.npy", data_paire)
np.save("numpy/bool.npy", True)
