from src.Bot.Bot  import Bot
import sys, json
from time import sleep
import logging
import threading
import pandas as pd
from random import randint

with open(f'{sys.path[0]}/fakeuseragent.json')as f:
    fake_agents = json.load(f)
with  open(f'{sys.path[0]}/settings.json') as settings_file:
    settings =json.load(settings_file)

fake_agents = fake_agents['browsers']['chrome']

# In[2]:
#n_creation = number of proxies by thread
#number of browsers = n_creation*4
def workerCreateBot(n_creation):
    colnames = ['USER','PASSWORD']
    accounts= pd.read_csv(f'{sys.path[0]}/accounts.csv',sep=';',skiprows=n_creation*20,nrows=20*(n_creation+1),names=colnames, header=None)
    proxies = settings['proxies'][n_creation*5:(5*(n_creation+1))]
    models_csv= f'{sys.path[0]}/models.csv'
    bot = Bot(settings['base_url'] , settings['bot_name'],fake_agents,proxies,accounts,models_csv)
    # print('-'*100)
    
    # print(bot.accounts)
    # print(type(bot.accounts))
    # print('-'*100)
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

  

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='(%(threadName)-10s) %(message)s',
# )



threads= []
for i in range(int(settings['n_accounts']/20)):
    t = threading.Thread(target=workerCreateBot,args=(i,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
# main_thread = threading.main_thread()
# for t in threading.enumerate():
#     if t is main_thread:
#         continue
#     logging.debug('joining %s', t.getName())
#     t.join()
