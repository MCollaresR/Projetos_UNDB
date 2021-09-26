from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Lib():
    
    WEBDRIVER_PATH = './TRAB_PY/chromedriver.exe'

    def start_browser(self):
        self.driver = webdriver.Chrome(self.WEBDRIVER_PATH)
        return self.driver
    
    def open_page(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    def click(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()
    
    def doubleClick(self, locator): 
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).doubleClick()
    
    def fill(self, locator, text):
        elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)
