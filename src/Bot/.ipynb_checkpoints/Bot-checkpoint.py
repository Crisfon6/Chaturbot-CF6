import pandas as pd

import os

import sys

from ..Browser.Browser import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from proxy_checker import ProxyChecker
from time import sleep
from itertools import cycle

class Bot:
    def __init__(self, base_url, name_bot, fake_agent,n_accounts,proxies):
        print('bot init')
        self.base_url = base_url
        self.bot_name = name_bot
        self.create_folder_bot()
        self.n_accounts = n_accounts
        self.accounts = self.load_accounts()
        print('accounts loaded')
        self.models = self.load_models()
        print('models loaded')
        self.browsers = []
        print('finished load ..')
        self.chrome_driver_path = f'{sys.path[0]}/drivers/chromedriver'        
        self.fake_agents = cycle(fake_agent)
        
        self.proxies = proxies
        self.count = -1

    def counter(self):
        self.count= self.count+1
    def create_folder_bot(self):
        print('creating folder...')
        current_path = os.getcwd()
        path_name = f'{current_path}/data/{self.bot_name}'
        try:
            os.mkdir(path_name)
        except  OSError:
            print("Creation of the directory %s failed" % path_name)
        else:
            print("Successfully created the directory %s" % path_name)
            print('folder created...')
            return path_name



    def load_accounts(self):
        return pd.read_csv(f'{sys.path[0]}/data/{self.bot_name}/accounts.csv',sep=';',nrows=self.n_accounts)

    def load_models(self):
        models = pd.read_csv(f'{sys.path[0]}/data/{self.bot_name}/models.csv')
        return models['account_name'].to_list()

    def openBrowser(self,):
        print('opening browsers')

        final_list_browser = [[],[],[],[],[],[],[]]

        for i in range(1):

            for idx,proxy in  enumerate(self.proxies[:4]):
                browser_temp =''        
                self.counter()               
                
                final_list_browser[idx].append(Browser(self.chrome_driver_path,self.accounts.iloc[self.count].USER,self.accounts.iloc[self.count].PASSWORD,self.base_url,proxy,next(self.fake_agents),self.models) )                
        self.browsers =    final_list_browser     
        print(f'Browsers opened : {len(self.browsers)}')

    def simulate_be_human(self):
        print('Start simulate be human')
        total_browsers = len(self.browsers[0])-1
        if (total_browsers==0):
            for packages_of_browser in range(len(self.browsers)-1):
                print('entro2')
                self.browsers[packages_of_browser][0].simulate_be_human_browser(True)
        else: 
            for idx in range(total_browsers):
                print('entro1')
                for packages_of_browser in range(len(self.browsers)-1):
                    print('entro2')
                    self.browsers[packages_of_browser][idx].simulate_be_human_browser(True)
        print('Finish simulate be human')
                          
        
                

    def show_models(self):
        print('Start show models')
        total_accounts = len(self.browsers[0])-1
        if (total_accounts==0):
            for i in range(5):
                for j in range(len(self.browsers)):
                    self.browsers[j][0].show_models(i) 
        else:           
            for i in range(5):
                for j in range(len(self.browsers)):
                    self.browsers[j][i].show_models(self.models[i]) 
        print('Finish show models')       
        
                
    def login(self,):
        print('Start login')
        total_accounts = len(self.browsers[0])-1
        if (total_accounts==0):
            for j in range(len(self.browsers)):
                self.browsers[j][0].login() 
        else:
            for i in range(5):
                for j in range(len(self.browsers)):
                    self.browsers[j][i].login()
        print('Finish login')

    def reload_tabs(self,):
        print('Start reloading tabs')
        total_accounts = len(self.browsers[0])-1
        if (total_accounts==0):
            for i in range(5):
                for j in range(len(self.browsers)):
                    self.browsers[j][0].reload_all_tabs() 
        else:           
            for i in range(total_accounts):
                for j in range(len(self.browsers)):
                    self.browsers[j][i].reload_all_tabs()
        print('Finsh reloading tabs') 
                    
        
    