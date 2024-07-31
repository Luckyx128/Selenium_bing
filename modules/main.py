from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Bing:
    
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.email = 'luckyxam128@gmail.com'
        self.senha = 'Ps2pcwii'
        self.search_bar = '//*[@id="sb_form_q"]'
    def get(self,url:str)->str:
        self.driver.get(url)
    def try_click(self,xpath:str)->None:
        attempts = 0
        while attempts < 10:    
            try:
                self.driver.find_element('xpath',xpath).click()
                break
            except Exception:
              attempts =  attempts + 1
    def try_send(self,xpath:str,text)->None:
        attempts = 0
        while attempts < 10:    
            try:
                self.driver.find_element('xpath',xpath).send_keys(text)
                break
            except Exception:
                attempts= attempts + 1
    
    def try_clear(self,xpath:str)->None:
        attempts = 0
        while attempts < 10:    
            try:
                self.driver.find_element('xpath',xpath).clear()
                break
            except Exception:
                attempts= attempts + 1

    def login(self):
        """ Dois click para chegar a tela de login """
        self.try_click('//*[@id="id_s"]')
        self.try_click('//*[@id="b_idProviders"]/li[1]/a/span')
        sleep(1)
        """Digita email e confirma """
        self.try_send('//*[@id="i0116"]',self.email)
        self.try_click('//*[@id="idSIButton9"]')
        sleep(1)
        """Digita senha e confirma """
        self.try_send('//*[@id="i0118"]',self.senha)
        self.try_click('//*[@id="idSIButton9"]')
        sleep(1)
        """"Confirmação do manter sempra ativo"""
        self.try_click('//*[@id="acceptButton"]')

        """Aceitar popup"""
        self.try_click('//*[@id="bnp_btn_accept"]')

    def search_ini(self,text:str)->None:
        self.try_send(self.search_bar,text)
        sleep(2)
        self.try_click('//*[@id="sa_5004"]/div[2]')

    def search_loop(self,text:str)->None:
        self.try_clear(self.search_bar)
        self.try_send(self.search_bar,text)
        self.try_click('//*[@id="sa_5003"]')
bing = Bing()

bing.get('https://www.bing.com')
sleep(5)
bing.login()
sleep(5)
bing.search_ini('Iniciando')
pesquisas = 0
while pesquisas < 50:
    bing.search_loop(f'a{pesquisas}')
    pesquisas= pesquisas + 1





sleep(300)