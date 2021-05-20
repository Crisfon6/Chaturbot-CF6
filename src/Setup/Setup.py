from ..Bot.Bot import Bot
import sys, json
from time import sleep
import logging
import threading
import pandas as pd
from random import randint
import json
class Setup:
    def __init__(self,proxiesPath,modelsPath,accountsPath,await_browser,fourproxybybrowser):
        colnamesAcc = ['USER','PASSWORD']
        colnamesModel = ['MODEL']
        colnamesProxies = ['PROXY']
        self.proxiesPath= proxiesPath
        self.modelsPath =modelsPath
        self.accountsPath =accountsPath        
        self.awaitBrowser = await_browser
        self.fourproxybybrowser = fourproxybybrowser
        if(self.fourproxybybrowser==''):
            self.fourproxybybrowser = 0

        self.fake_agents = self.loadFakeAg()      
        self.readCSV() 
        self.threads= []
        self.baseUrl = "https://www.chaturbate.com/"
    

    def readCSV(self):
        if(self.proxiesPath==""):
            with open('settings.json') as json_file:
                data = json.load(json_file)
            self.proxiesPath = data['proxies']
            self.modelsPath = data['models']
            self.accountsPath = data['accounts']
            self.awaitBrowser = float(data['await_browser'])

            data ={'proxies':str(self.proxiesPath),
                     'models':str(self.modelsPath),
                    'accounts':str(self.accountsPath),
                    'awaitBrowser':str(self.awaitBrowser)
                    }
        else:
            data ={'proxies':str(self.proxiesPath.name),
                     'models':str(self.modelsPath.name),
                    'accounts':str(self.accountsPath.name),
                    'awaitBrowser':str(self.awaitBrowser)
                    }
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)

        self.proxies =pd.read_csv(self.proxiesPath,sep=";")
        self.models = pd.read_csv(self.modelsPath,sep=";")
        self.models =self.models['MODEL'].to_list()
        self.accounts = pd.read_csv(self.accountsPath,sep=";")

    def saveLastSetup(self):     
        
        
        data ={'proxies':str(self.proxiesPath.name),
        'models':str(self.modelsPath.name),
        'accounts':str(self.accountsPath.name)
        }
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)

    def loadFakeAg(self):
        with open(f'{sys.path[0]}/fakeuseragent.json')as f:
            fake_ag = json.load(f)      
            fakeAgents = fake_ag['browsers']['chrome']
            return fakeAgents


    #n_creation = number of proxies by thread
    #number of browsers = n_creation*4
    def workerCreateBot(self,proxy,account):          
        print('WORKER')
        bot = Bot(self.baseUrl , self.fake_agents,proxy,account,self.models, self.fourproxybybrowser)
        
        
        bot.openBrowser()
        print('-'*100)
        print(bot.browser)
        print(bot.proxy)
        print('-'*100)
       
        bot.login()
    #    bot.simulate_be_human()
        bot.models
        bot.show_models()
        sleep(randint(4,10))
        bot.detect_captcha()
        while True:
            sleep(randint(20,40))
            bot.detect_captcha()

    def run(self):
        n_accounts = 4
        print('RUNNING')
        proxyCount = 0
        self.saveLastSetup()
        if(self.awaitBrowser==''):
            self.awaitBrowser = 2
        # print('ONE PROXY',self.oneproxybybrowser)
        if (self.fourproxybybrowser==0):
            print(self.proxies.values)
            for i,data in enumerate(self.proxies.values):     
                
                proxy = data[0]
                account = self.accounts.values[i]
                t = threading.Thread(target=self.workerCreateBot,args=(proxy,account))
                sleep(float(self.awaitBrowser))
                t.start()
                self.threads.append(t)
        else:
            for i,data in enumerate(self.accounts.values): 
                if(i%4==0 and i!=0):
                    proxyCount+=1     
                proxy = self.proxies.values[proxyCount][0]
                account = data               
                t = threading.Thread(target=self.workerCreateBot,args=(proxy,account))
                sleep(float(self.awaitBrowser))
                t.start()
                self.threads.append(t)          
                
        for t in self.threads:
            t.join()

