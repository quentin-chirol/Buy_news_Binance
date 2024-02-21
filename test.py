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
print(annonce)
