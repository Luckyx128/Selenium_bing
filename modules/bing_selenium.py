from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import logging
import json
logger = logging.getLogger(__name__)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Habilitar o modo headless
# chrome_options.add_argument("--disable-gpu")

class Bing:

    def __init__(self) -> None:
        with open("../config.json",'r') as configs:
            credentials = json.load(configs)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.email = credentials['general']['email']
        self.password = credentials['general']['pass']
        self.search_bar = '//*[@id="sb_form_q"]'
    def get(self, url: str) -> None:
        self.driver.get(url)

    def try_click(self, xpath: str) -> None:
        attempts = 0
        while attempts < 10:
            try:
                self.driver.find_element('xpath', xpath).click()
                break
            except Exception as e:
                logger.debug('exception: %s',e)
                attempts = attempts + 1

    def try_send(self, xpath: str, text) -> None:
        attempts = 0
        while attempts < 10:
            try:
                self.driver.find_element('xpath', xpath).send_keys(text)
                break
            except Exception as e:
                logger.debug('exception: %s', e)
                attempts = attempts + 1

    def try_clear(self, xpath: str) -> None:
        attempts = 0
        while attempts < 10:
            try:
                self.driver.find_element('xpath', xpath).clear()
                break
            except Exception as e:
                logger.debug('exception: %s', e)

                attempts = attempts + 1

    def login(self):
        """ Dois click para chegar a tela de login """
        self.try_click('//*[@id="id_s"]')
        sleep(3)
        self.try_click('//*[@id="b_idProviders"]/li[1]/a/span')
        sleep(3)
        """Digita email e confirma """
        self.try_send('//*[@id="i0116"]', self.email)
        sleep(3)
        self.try_click('//*[@id="idSIButton9"]')
        sleep(1)
        """Digita password e confirma """
        self.try_send('//*[@id="i0118"]', self.password)
        sleep(3)
        self.try_click('//*[@id="idSIButton9"]')
        sleep(3)
        """"Confirmação do manter sempra ativo"""
        self.try_click('//*[@id="acceptButton"]')
        sleep(3)
        """Aceitar popup"""
        self.try_click('//*[@id="bnp_btn_accept"]')

    def search_ini(self, text: str) -> None:
        self.try_send(self.search_bar, text)
        sleep(10)
        self.try_click('//*[@id="sa_5004"]/div[2]')

    def search_loop(self, text: str) -> None:
        self.try_clear(self.search_bar)
        self.try_send(self.search_bar, text)
        self.try_click('//*[@id="sb_form_go"]')

    def start(self) -> None:
        logging.info('get https://www.bing.com')
        self.get('https://www.bing.com')
        sleep(5)
        logging.info('starting login')
        self.login()
        sleep(5)
        self.search_ini('Iniciando')
        searchs = 0
        while searchs < 50:
            logging.debug('buscando %s',f'a{searchs}')
            self.search_loop(f'a{searchs}')
            sleep(15)
            searchs = searchs + 1