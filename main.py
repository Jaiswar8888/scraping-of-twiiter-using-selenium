from selenium import webdriver
from  bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests
from openpyxl import Workbook
import time
import pandas as pd 


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://twitter.com/sachin_rt")
time.sleep(6)

followers=driver.find_elements(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span') # find the title of only first page of vivo phone 
for index,follower in enumerate(followers): # this will print the title with index 
    print(index,follower.text)
time.sleep(6)

followings=driver.find_elements(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[1]/a/span[1]/span') # find the title of only first page of vivo phone 
for index,following in enumerate(followings): # this will print the title with index 
    print(index,following.text)
time.sleep(6)

user_id=driver.find_elements(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/span') # find the title of only first page of vivo phone 
for index,user in enumerate(user_id): # this will print the title with index 
    print(index,user.text)
time.sleep(6)

likes=driver.find_elements(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div/div') # find the title of only first page of vivo phone 
for index,like in enumerate(likes): # this will print the title with index 
    print(index,like.text)
time.sleep(6)
