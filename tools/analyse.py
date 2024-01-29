import re

class analyse:
    def __init__(self,txt):
        self.txt = re.split(" ", txt)

    def paire(self): 
        tab = []
        for i in range(len(self.txt)):
            if "(" in self.txt[i] and ")" in self.txt[i]:
                tab.append(re.sub(r"\(|\)", "", self.txt[i])+"/USDT")
        return tab

    def check_paire(self,tab):
        for i in range(len(self.txt)):
            for j in range(len(tab)):
                if tab[j].upper() == self.txt[i].upper():
                    return True


