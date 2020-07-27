
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:12:15 2020
@author: williamchung
"""
import urllib as urllib
from fb_env import env_data
from time import sleep
#from bs4 import BeautifulSoup as z
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
#import legit_sheets as legit
credentials = '/Users/niharj/miniconda3/bin/chromedriver'

username = env_data['email']
password = env_data['password']
group_name = 'Umich Memes for Wolverteens'
account = 'wolverineshub'
SCROLL_PAUSE_TIME = 1
count = 0
index = 1

class Instabot:
    def __init__(self, username, password, account, count, index):
        #self.driver = browser = webdriver.Chrome(credentials)
        
        #caps = webdriver.DesiredCapabilities.CHROME.copy()
       # caps['disable-notifications'] = True
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.driver = browser =  webdriver.Chrome(chrome_options=chrome_options)        
        #self.driver = browser = webdriver.Chrome(executable_path = credentials)
       # browser.chrome.options.set_capability('disable-notifications', 'true')
        #self.driver.find_element_by_xpath('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[3]/settings-privacy-page//settings-animated-pages/settings-subpage[3]/category-default-setting//settings-toggle-button[2]').click()
        #self.driver.find_element_by_xpath('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[3]/settings-privacy-page//settings-animated-pages/settings-subpage[3]/category-setting-exceptions//site-list[1]//add-site-dialog//cr-dialog/div[2]/cr-input//div[2]/div/div[1]/input').send_keys('facebook.com')
        #self.driver.find_element_by_xpath('/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[3]/settings-privacy-page//settings-animated-pages/settings-subpage[3]/category-setting-exceptions//site-list[1]//add-site-dialog//cr-dialog/div[3]/cr-button[2]').click()
        browser.get('https://www.facebook.com/')
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input').click()
        sleep(2)
        browser.get('https://www.facebook.com/groups/1812699475720343/')

        #self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/label/input').click()
        #self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/label/input').send_keys(group_name)
        sleep(2)
        #self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/ul/li[1]/div/a/div/div[2]/span').click()
        sleep(2)
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]').click()
        sleep(1)
        count = 0
        
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        num_scrolls = 1
        while count< num_scrolls:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            count+=1
        images = self.driver.find_elements_by_tag_name('img')
        filename = 'filename'
        indexing = 0
        for image in images:
            urllib.request.urlretrieve(image.get_attribute('src'),filename+str(indexing)+'.png' )
            indexing+=1
            #Down_image=urllib.URLopener()
            #Down_image.retrieve(image)
            print(image.get_attribute('src'))
        for i in range(0, len(images)):
            urllib.request.urlretrieve(image.get_attribute('src'), "filename + .png")

        
    def go_to_new_link(self, url):
        sleep(1)
        self.driver.get(url)
        
        
    def quit_search(self):
        self.driver.quit()
    
    def go_to_account(self, account):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(account)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[2]/span').click()
        sleep(1)
        
    def scrape_info(self, name):
        sleep(1)
        
        variable = self.driver.find_element_by_tag_name(name)
        return variable.text
        
    
    def sleep(self):
        sleep(300)
    def scroll(self, num_scrolls):
        count = 0
        
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while count< num_scrolls:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            count+=1
        #//*[@id="react-root"]/section/main/div/div[4]/article/div[1]/div/div[11]/div[3]/a/div[1]/div[2]
        #/html/body/div[5]/div/div/div[2]/div/div/div[9]/div[2]/div[1]/div/span/a
        data = []
        for a in range(2, 5):
            for b in range(1, 16):
                for c in range (1, 5):
                    try:
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[' +str(a) +']/article/div[1]/div/div['+ str(b)+ ']/div[' +str(c) + ']/a/div/div[2]').click()
                        sleep(1)
                          
                        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button').click()
                        self.popup = WebDriverWait(self.driver, 5). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div')))
                        for i in range(11):
                            sleep(1)
                            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-i)), self.popup)
                            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div")))
                            self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div')))
                            #b_popup = z(self.popup.get_attribute('innerHTML'), 'html.parser')
                            try:
                                for index in range(0, 100):
                                    dic = {}
                                    #dic['Username'] = b_popup.find_all('a')[index]['href']
                                    if dic in data:
                                        pass
                                    else:
                                        data.append( dic)
                            except:
                                pass
                        for h in range(70):
                            sleep(2)
                            try:
                                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div")))
                                self.popup = WebDriverWait(self.driver, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div')))
                                #b_popup = z(self.popup.get_attribute('innerHTML'), 'html.parser')
                                try:
                                    for index in range(0, 100):
                                        dic = {}
                                        #dic['Username'] = b_popup.find_all('a')[index]['href']
                                        if dic in data:
                                            pass
                                        else:
                                            data.append( dic)
                                except:
                                    pass
                            except:
                                pass
                            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', self.popup)
                       
                           
                            
                        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
                        sleep(1)
                        self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
                        sleep(1)
                    except Exception as e:
                        pass
                    
        return data
            
insta = Instabot(username, password, group_name, count, index)         
#insta = Instabot(username, password, account, count, index)
#insta.go_to_account(account)
#data = insta.scroll(5)

#df = pd.DataFrame(data)

#legit.upload_df('Sheet3', df, '1OQSC21Bs4wGst_IvcdikMlX5TL1ogjnvNRfxY5BmPZ0')

