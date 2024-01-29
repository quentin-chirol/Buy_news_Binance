from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class selenium:
    def __init__(self,lien,time):
        self.driver = webdriver.Chrome()
        self.driver.get(lien)
        self.check_time = time

    def check_url_appear(self,path):
        wait = WebDriverWait(self.driver,1)
        for i in range(self.check_time):   
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, path)))
                return True
            except:
                pass
        return False
    
    def get_elemment(self,path):
        return self.driver.find_element(By.XPATH, path).text

    def click_items(self,path,click):
        if self.check_url_appear(path) == True:
            txt = self.get_elemment(path)
            if  click == True:
                self.driver.find_element(By.XPATH, path).click()
            return txt 
            
    def click_items_css(self,path,click): 
        txt = self.driver.find_element(By.CSS_SELECTOR, path).text
        if  click == True:
            self.driver.find_element(By.CSS_SELECTOR, path).click()
        return txt 
        
    def end(self):
        self.driver.close()


