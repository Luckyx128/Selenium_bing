from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Bing:
    
    def __init__(self) -> None:
        self.driver = webdriver.Edge()
    def get(self,url:str)->str:
        self.driver.get(url)


