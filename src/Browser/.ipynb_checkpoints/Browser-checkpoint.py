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

        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": self.proxy,
            "ftpProxy": self.proxy,
            "sslProxy": self.proxy,
            "proxyType": "MANUAL",
        }
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True
        options.add_argument("user-agent="+self.fake_agent)
        print(webdriver.DesiredCapabilities.CHROME)

        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})  # set language
        options.add_argument(
            '--no-sandbox')  # required when running as root user. otherwise you would get no sandbox errors.
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("start-maximized")      

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)       
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=self.driver_path)
        sleep(randint(10,30))
        self.driver.get('https://chaturbate.com/')
       
    def simulate_be_human_browser(self,first=False):
        print('true')
        if (first==True):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'I AGREE')]")))\
                        .click()  # close modal start i agree
        try:
            self.driver.find_element_by_xpath("/html/body/div/div[2]/h1[contains(text(),'Something went wrong.')]")
            self.driver.get('https://chaturbate.com/')
        except:
            pass
        
        size = self.driver.execute_script("return document.body.offsetWidth;")
        
    #     movement = randint(size-1)
        movement= randint(0,size-1)
        self.driver.execute_script(f"window.scrollTo(0, {movement});")
        sleep(randint(1,4))
        ## select hashtag
        tags = self.driver.find_elements_by_xpath('//*[@id="hashtag_ticker"]')
        tags = tags[0].find_elements_by_tag_name('a')
        select = randint(2,10)
        tags[select].click()
        
        #show some random
        rooms = self.driver.find_elements_by_xpath('//*[@id="room_list"]')
        self.driver.execute_script(f"window.scrollTo(0, {movement});")    
        sleep(randint(2,8))
        rooms = rooms[0].find_elements_by_xpath(f'//*[@id="room_list"]/li[{randint(1,10)}]/div[3]/div/a')[0].click()
        sleep(randint(30,80))
        
    
  
    def login(self,):    
#         try:
#             print('logining :',self.username)
#     #         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'I AGREE')]")))\
#     #                     .click()  # close modal start i agree
#             sleep(randint(4,10))
#             WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'LOG IN')]"))).click()  # click login
#             sleep(randint(3,7))
#             username_input = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username'")))
#             password_input = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password'")))
#             username_input.clear()
#             password_input.clear()
#             username_input.send_keys(self.username)
#             sleep(randint(4,10))
#             password_input.send_keys(self.password)
#             WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//*[@id="rememberme"]'))).click()  # rememberme
#             sleep(randint(3,7))
#             # submit
#             WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_login_btn"]'))).click()
#             print('loged :',self.username)
#     #         return driver
#         except Exception as err:
#             print('error',err)
            print('logining :',self.username)
    #         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'I AGREE')]")))\
    #                     .click()  # close modal start i agree
            sleep(randint(4,10))
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'LOG IN')]"))).click()  # click login
            sleep(randint(3,7))
            username_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username'")))
            password_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password'")))
            username_input.clear()
            password_input.clear()
            username_input.send_keys(self.username)
            sleep(randint(4,10))
            password_input.send_keys(self.password)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="rememberme"]'))).click()  # rememberme
            sleep(randint(3,7))
            # submit
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_login_btn"]'))).click()
            print('loged :',self.username)

    def show_models(self, idx_model):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        base_url= 'https://chaturbate.com/'
        wait_time = [20, 40]        
        sleep(randint(*wait_time))
        self.driver.execute_script('window.open()')
        try:
            url = f'{base_url}/{self.models[idx_model]}'
            self.driver.switch_to.window(self.driver.window_handles[idx_model + 1])            
            self.driver.get(url)        
            
            sleep(randint(60,220))
        except Exception as err:
            print(f'error in {idx_model}, message: {err}')
      

    def detect_captcha(self):
        try:

            print('Captcha found')

            self.driver.get(self.driver.current_url)
            sleep(20)
            self.driver.find(By.XPATH, "//h1[contains(text(), 'One more step')]")
            print(f'Reloading... {self.driver.current_url}')
            return True  # catcha found
        except Exception:  # captcha no found
            return False
    def reload_all_tabs(self):
        try:
            for idx,data in enumerate(self.driver.window_handles):
                self.driver.switch_to.window(driver.window_handles[idx])
                self.driver.refresh()
        except Exception as err:
            print('error',err)