import numpy as np
import sys
import ccxt
import json

f = open('/home/you_server_name/Buy_news_Binance/config.json',)
mdp = json.load(f)
f.close()

audenthifiation =  {
    'apiKey': mdp["API"],
    'secret': mdp["API_secret"],
    'options': {
        'defaultType': 'spot',  #margin, spot, future, per, ect
    }
}
binance = ccxt.binance(audenthifiation)

loaded_bool= np.load("/home/you_server_name/Buy_news_Binance/numpy/bool.npy")
loaded_paire  =  np.load("/home/you_server_name/Buy_news_Binance/numpy/paire.npy")

if loaded_bool  ==  True:
    #market order
    current_price = (binance.fetch_ticker(loaded_paire[0])["ask"] + binance.fetch_ticker(loaded_paire[0])["bid"]) / 2
    amount_usdt  =  100
    amount = amount_usdt / current_price
    order = binance.create_order(loaded_paire[0], "market", "buy", amount)
    np.save("/home/you_server_name/Buy_news_Binance/numpy/bool.npy", False)

    #limit order
    entry_price = order['price']
    order_size = order['amount']
    target_1000 =  entry_price  +  entry_price*10
    binance.create_order(loaded_paire[0], "limit", "sell", order_size, target_1000)
    
else:
    print("attente de trouver de paire")
    sys.exit()





