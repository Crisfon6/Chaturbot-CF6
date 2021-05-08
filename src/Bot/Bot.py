
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
    def __init__(self, base_url, name_bot, fake_agent,proxies,accounts,models_csv,use_four):
        print('bot init')
        self.base_url = base_url
        self.bot_name = name_bot
        self.models_csv =models_csv
        self.accounts = accounts
        self.user_four = use_four
        
        print('accounts loaded')
        self.models = self.load_models()
        print('models loaded')
        self.browsers = []
        print('finished load ..')
        self.chrome_driver_path = f'{sys.path[0]}/drivers/chromedriver'        
        self.fake_agents = cycle(fake_agent)
        self.proxies = proxies
        self.count = 0

    def counter(self):
        self.count= self.count+1 
    def load_models(self):      
        models = pd.read_csv(self.models_csv ,nrows=5)
        return models['account_name'].to_list()

    def openBrowser(self,):
        print('opening browsers')
        final_list_browser = []#10
        for _ in self.proxies:
            final_list_browser.append([])
        if (self.use_four):

            browser_by_list=4
        else:

            browser_by_list=1
        for _ in range(browser_by_list):
            for idx,proxy in  enumerate(self.proxies):    
                try:                  
                    username = self.accounts.iloc[self.count].USER
                    password = self.accounts.iloc[self.count].PASSWORD                    
                    fake_ag =next(self.fake_agents)

                    final_list_browser[idx].append(Browser(self.chrome_driver_path,username,password,self.base_url,proxy,fake_ag,self.models))                
                    self.counter()                               
                except Exception as err:
                    print(f'error loading browsers {self.count}',err)
        self.browsers = final_list_browser     
        print(f'--------------------------Browsers opened : {len(self.browsers)*len(self.browsers[0])}----------------')

    def simulate_be_human(self):
        print('Start simulate be human')
        total_browser_by_list = len(self.browsers[0])-1
        if (total_browser_by_list<2):
            for packages_of_browser in range(len(self.browsers)):   
                try:              
                    self.browsers[packages_of_browser][0].simulate_be_human_browser(True)
                except Exception as err:
                    print(f'error in {packages_of_browser}' ,err)

        else: 
            for idx in range(total_browser_by_list):                
                for packages_of_browser in range(len(self.browsers)):   
                    try:             
                        self.browsers[packages_of_browser][idx].simulate_be_human_browser(True)
                    except Exception as err:
                        print('error simulating be human',err)
        print('Finish simulate be human')     

    def show_models(self):
        print('Start show models')
        total_accounts = len(self.browsers[0])-1
        if (total_accounts<1):
            for i in range(len(self.models)-1):
                for j in range(len(self.browsers)):
                    print(i)
                    self.browsers[j][0].show_models(i) 
        else:           
#             for i in range(4):
#                 for j in range(len(self.browsers)):
#                     print(f'{j}-{i}')
#                     self.browsers[j][i].show_models() 
              for i in range(len(self.browsers[0])):#browsers by list
                  for j in range(len(self.models)):# models
                      for k in range(len(self.browsers)):#
                          
                        try:
                            self.browsers[k][i].show_models(j)
                            
                    
                        except Exception as err:
                            print(f'Error in fors j >{j} i->{i} j->{j}msg-> {err}')
        print('Finish show models,.')       
        
                
    def login(self,):
        print('Start login')
        total_accounts = len(self.browsers[0])-1
        if (total_accounts==0):
            for j in range(len(self.browsers)):
                self.browsers[j][0].login() 
        else:
            for i in range(len(self.browsers[0])):
                for j in range(len(self.browsers)):
                    try:
                        self.browsers[j][i].login()
                    except Exception as err:
                        print(f'Error in fors j >{j} i->{i} msg-> {err}')
        print('Finish login')

    def reload_tabs(self,):
        print('Start reloading tabs')
        total_accounts = len(self.browsers[0])-1
        if (total_accounts==0):            
            for j in range(len(self.browsers)):
                try:
                    self.browsers[j][0].reload_all_tabs() 
                except:
                    pass
        else:           
            for i in range(len(self.browsers[0])):
                for j in range(len(self.browsers)):
                    try:
                        self.browsers[j][i].reload_all_tabs()
                    
                    except Exception as err:
                        print(f'Error in fors j >{j} i->{i} msg-> {err}')
        print('Finsh reloading tabs') 

    def detect_captcha(self,):
        print('Start detecting captchas')
        total_accounts = len(self.browsers[0])-1
        if (total_accounts==0):            
            for j in range(len(self.browsers)):
                try:
                    self.browsers[j][0].detect_captcha() 
                except:
                    pass 
        else:           
            for i in range(len(self.browsers[0])):
                for j in range(len(self.browsers)):
                    try:
                        self.browsers[j][i].detect_captcha()                    
                    except Exception as err:
                        print(f'Error in fors j >{j} i->{i} msg-> {err}')                     
        print('Finish detect captchas')
    
