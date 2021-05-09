from ..Bot.Bot  import Bot
import sys, json
from time import sleep
import logging
import threading
import pandas as pd
from random import randint

class Setup:
    def __init__(self,proxies_path,models_path,accounts_path,await_browser,oneproxybybrowser):
        colnamesAcc = ['USER','PASSWORD']
        colnamesModel = ['MODEL']
        colnamesProxies = ['PROXY']
        self.proxies =pd.read_csv(proxies_path,sep=";",names=colnamesProxies, header=None)
        self.models = pd.read_csv(models_path,sep=";",names=colnamesModel, header=None)
        self.accounts = pd.read_csv(accounts_path,sep=";",names=colnamesAcc, header=None)
        self.awaitBrowser = await_browser
        self.oneproxybybrowser = oneproxybybrowser
        self.fake_agents = ''
        self.settings = ''
        self.loadJson()
        self.threads= []
        self.baseUrl = "https://www.chaturbate.com/"

    def loadJson(self):
        with open(f'{sys.path[0]}/fakeuseragent.json')as f:
            fake_agents = json.load(f)
        with  open(f'{sys.path[0]}/settings.json') as settings_file:
            self.settings =json.load(settings_file)

        self.fake_agents = fake_agents['browsers']['chrome']


    #n_creation = number of proxies by thread
    #number of browsers = n_creation*4
    def workerCreateBot(self,proxy,account):          
        use_four = True        
        bot = Bot(self.baseUrl , self.fake_agents,proxy,account,self.models, True)
    
        bot.openBrowser()
        print('-'*100)
        print(bot.browsers)
        print(bot.proxies)
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
        n_accounts = 5
        if (self.oneproxybybrowser==True):
            for i in range(self.proxies):
                proxy = self.proxies.values[i]
                account = self.accounts.values[i]
                t = threading.Thread(target=self.workerCreateBot,args=(proxy,account))
                t.start()
                self.threads(t)
        else:
            pass
        for t in self.threads:
            t.join()


        # for i in range(int(settings['n_accounts']/n_accounts)):
        #     settings['proxies'][n_creation*n_accounts:(n_accounts*(n_creation+1))]
        #     t = threading.Thread(target=self.workerCreateBot,args=(i,))
        #     t.start()
        #     threads.append(t)
        # for t in threads:
        #     t.join()

