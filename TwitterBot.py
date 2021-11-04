from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Twitterbot:

    def __init__(self,email,username,password):
        self.password = password
        self.username = username
        self.email = email
        self.bot = webdriver.Firefox()

    def login(self):
        usemail_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input '
        UE_Enter = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div'
        unusual_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        US_Enter = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div'
        pasw_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input'
        PW_Enter = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div'
        bot = self.bot
        bot.get('https://twitter.com/i/flow/login')
        
        time.sleep(10)
        
        bot.find_element_by_xpath(usemail_xpath).send_keys(self.email)
        time.sleep(2)
        bot.find_element_by_xpath(UE_Enter).click()
        time.sleep(3)
        bot.find_element_by_xpath(unusual_xpath).send_keys(self.username)
        time.sleep(2)
        bot.find_element_by_xpath(US_Enter).click()
        time.sleep(3)
        bot.find_element_by_xpath(pasw_xpath).send_keys(self.password)
        time.sleep(2)
        bot.find_element_by_xpath(PW_Enter).click()
        time.sleep(3)
    def likeTheTweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)
        #for i in range(3):
            #bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            #time.sleep(2)
            #tweets = bot.find_element_by_class_name('tweet')
            #links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            #print(links)   
        #xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[4]/div/div/section/div/div/div[1]/div/div/article'
        #bot.find_element_by_xpath(xpath).click()




email = 'pubgnew1001@gmail.com'
username = '@bot_tcom'
pasw = 'Bot@2021@2021'
#email = input('Enter the email Properly : ')
#username = input('Enter the username Properly : ')
#pasw = input('Enter the Password Properly : ')
#hashtag = input('Enter the Hashtag Properly : ')
a = Twitterbot(email,username,pasw)  
a.login() 
hashtag = 'Thala'
a.likeTheTweet(hashtag)     
    
