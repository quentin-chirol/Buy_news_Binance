#Consol Ubuntu <br>
wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb <br> 
sudo apt update <br>
sudo apt install -f ./google-chrome-stable_current_amd64.deb <br>
sudo apt pip <br>
sudo apt python3 <br>
pip install numpy  <br>
pip install ccxt <br>
pip install selenium webdriver-manager  <br>
crontab  -e  <br>
1 <br>
* * * * python3 /home/your_serveur_name/Buy_news_Binance/execute.py <br>
0 * * * python2 /home/your_serveur_name/Buy_news_Binance/check.py  <br>
