
import pandas as pd
import os

import sys

from ..Browser.Browser import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from time import sleep
from itertools import cycle

class Bot:
    def __init__(self, base_url, fake_agent,proxy,account,models,use_four):
        print('bot init')
        self.base_url = base_url
        
        
        self.account = account
        self.use_four = use_four
        
        print('accounts loaded')
        self.models = models
        print('models loaded')
        # self.browsers = []
        self.browser = ''
        print('finished load ..')
        self.chrome_driver_path = f'{sys.path[0]}/drivers/chromedriver'        
        self.fake_agents = cycle(fake_agent)
        self.proxy = proxy
        self.count = 0

    def counter(self):
        self.count= self.count+1     

    def openBrowser(self,):
        print('opening browsers')
        username = self.account[0]
        password = self.account[1]                   
        fake_ag =next(self.fake_agents)
        
        
        self.browser = Browser(self.chrome_driver_path,username,password,self.base_url,self.proxy,fake_ag,self.models)
        

    def show_models(self):
        print('Start show models')
        for i,data in enumerate(self.models):
            try:
                self.browser.show_models(i)
            except:
                print(f'Error showing model',i)
        print('Finish show models')
    
        
                
    def login(self,):
        print('Start login')
        self.browser.login()
        print('Finish login')
    
    def reload_tabs(self,):
        print('Start reloading tabs')
        try:
            self.browser.reload_all_tabs()
        except:
            print('Error reloading tabs')
        print('Finsh reloading tabs') 



    def detect_captcha(self,):
        print('Start detecting captchas')
        try:
            self.browser.detect_captcha()
        except:
            pass
        print('Finish detect captchas')

    
