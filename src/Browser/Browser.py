# from fake_useragent import UserAgent
from selenium import webdriver
from random import randint
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser:
    def __init__(self, driver_path, user, password, base_url, proxy, fake_agent,models):
        self.driver_path = driver_path
                
        self.username = user
        self.password = password
        self.base_url = base_url
        self.timeWaiting = [5, 10]
        self.proxy = proxy
        self.options = ''
        self.fake_agent = fake_agent
        self.models = models
        self.driver = ''
        self.setup_browser()
        
        

    def setup_browser(self):
        options = webdriver.ChromeOptions()
        # user_agent = 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
        options.add_argument('--proxy-server={}'.format(self.proxy))
        # webdriver.DesiredCapabilities.CHROME['proxy'] = {
        #     "httpProxy": self.proxy,
        #     "ftpProxy": self.proxy,
        #     "sslProxy": self.proxy,
        #     "proxyType": "MANUAL",
        # }
        # webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True
        
        options.add_argument("user-agent="+self.fake_agent)
        

        # options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})  # set language
        # options.add_argument(      '--no-sandbox')  # required when running as root user. otherwise you would get no sandbox errors.
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument("start-maximized")      
        
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)       
        

        # #options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=self.driver_path)
        
        try:
            self.driver.get(self.base_url)
        except :
            print(f"proxy {self.proxy} no work")



       
    def simulate_be_human_browser(self,first=False):
        try:
            self.driver.find_element_by_xpath("/html/body/div/div[2]/h1[contains(text(),'Something went wrong.')]")
            
            sleep(randint(5,12))
            self.driver.refresh()
	        
#            print('something went wrong simulating be human')
        except:            
            pass
        size = self.driver.execute_script("return document.body.offsetWidth;")
        
    #     movement = randint(size-1)
        movement= randint(0,size-1)
        self.driver.execute_script(f"window.scrollTo(0, {movement});")
        sleep(randint(10,20))
        ## select hashtag
        print('selecting  random hashtag')
        tags = self.driver.find_elements_by_xpath('//*[@id="hashtag_ticker"]')
        tags = tags[0].find_elements_by_tag_name('a')
        select = randint(10,15)
        tags[select].click()
        
        #show some random
        print('selecting  random video')
        rooms = self.driver.find_elements_by_xpath('//*[@id="room_list"]')
        self.driver.execute_script(f"window.scrollTo(0, {movement});")    
        sleep(randint(3,10))
        rooms = rooms[0].find_elements_by_xpath(f'//*[@id="room_list"]/li[{randint(1,10)}]/div[3]/div/a')[0].click()
        sleep(randint(20,35))  
        print('next simulate human')     
  
    def login(self,):   
            print('logining :',self.username)
            try:
                try:
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'I AGREE')]")))\
                        .click() 
                except Exception as err:
                    print  ('no locate iagree',err)           
                sleep(randint(1,4))
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'LOG IN')]"))).click()  # click login
                sleep(randint(2,6))
                username_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
                password_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
                username_input.clear()
                password_input.clear()
                username_input.send_keys(self.username)
                sleep(randint(2,5))
                password_input.send_keys(self.password)
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="rememberme"]'))).click()  # rememberme
                sleep(randint(2,5))
                # submit
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_login_btn"]'))).click()
                print('loged :',self.username)
            except Exception as err:
                print(f'error loading {self.username}. message: {err}')

    def show_models(self, idx_model):
#         print(idx_model)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        base_url= 'https://chaturbate.com/'       
        
        url = f'{base_url}/{self.models[idx_model]}'
        self.driver.get(url)        
        sleep(randint(15,30))
        
        print(f'show  model {self.models[idx_model]}')
        try:     
            if(idx_model<4):
                self.driver.execute_script('window.open()')
                self.driver.switch_to.window(self.driver.window_handles[idx_model + 1])            
        except Exception as err:
            print(f'error in {idx_model}, message: {err}')    


    def reload_all_tabs(self):
        try:
            for idx,_ in enumerate(self.driver.window_handles):
                self.driver.switch_to.window(self.driver.window_handles[idx])
                self.driver.refresh()
                sleep(randint(10,20))
        except Exception as err:
            print('error',err)

    def detect_captcha(self):
        try:
            self.driver.find_element(By.XPATH,  "//a[contains(text(), 'SWAG')]")
            
        except:
            self.driver.refresh()
