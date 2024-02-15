
# 🤖 Sniper BOT 🤖 

Ce programme vous permet d'acheter ces nouvelles cryptos dès leur sortie sur les plateformes d'échange, et ce, de manière rapide et économique. Plus besoin de surveiller constamment, le bot s'occupe de tout pour vous.

# Installation packages 

GOOGLE 

```bash
  wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
  sudo apt update 
  sudo apt install -f ./google-chrome-stable_current_amd64.deb 
```
PYTHON

```bash
  sudo apt pip 
  sudo apt python3 
  pip install numpy 
  pip install ccxt 
  pip install selenium webdriver-manager
```

JQ

```bash
  sudo apt --fix-broken install 
  sudo apt update 
  sudo apt install libc6-dev libjq1 
  sudo apt install jq build-essential libstdc++-11-dev
```

SPONGE

```bash
  sudo apt install moreutils
```

GIT

```bash
  sudo apt git 
  git clone https://github.com/quentin-chirol/Buy_news_Binance
  chmod +x loop.sh
  chmoe +x check.py
```

# Localisation Serveur 

| PLATFORM | SERVEUR | TIME REQUEST |
|:-|:-:|-:|
| BINANCE |  AWS TOKYO  |  ~2ms  |


"""* * * * python3 /home/your_serveur_name/Buy_news_Binance/execute.py""" <br>
"""0 * * * python2 /home/your_serveur_name/Buy_news_Binance/check.py""" <br>

