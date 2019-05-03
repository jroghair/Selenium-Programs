# -*- coding: utf-8 -*-
"""
Created on Sun May 02 00:02:17 2019

@author: Jeremy Roghair
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

#users = pd.read_csv("C:\\Users\\jrogh\\OneDrive\\Documents\\RA Position - Sukul\\Question 2 - Scraper Output.csv")
os.chdir(os.getcwd())
#Users.csv contains list of first/last names, emails and passwords
users = pd.read_csv("Users.csv")

chrome_driver_path = "C:\Program Files (x86)\Google\ChromeDriver\chromedriver.exe"
options = Options()
driver = webdriver.Chrome(chrome_driver_path, options=options)
#Navigate to google account creation website
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com%2F&hl=en&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")  

#Find the elements for all required fields
first = driver.find_element_by_id('firstName')
last = driver.find_element_by_id('lastName')
userName = driver.find_element_by_id('username')
pw1 = driver.find_element_by_name('Passwd')
pw2 = driver.find_element_by_name('ConfirmPasswd')

#Runs through list of users and fills the google account creation for each
for i in range(len(users)):
    first.send_keys(users.iloc[i]['First_Name'])
    last.send_keys(users.iloc[i]['Last_Name'])
    userName.send_keys(users.iloc[i]['Email'])
    pw1.send_keys(users.iloc[i]['Password'])
    pw2.send_keys(users.iloc[i]['Password'])
    sleep(2) 
    first.clear()
    last.clear()
    userName.clear()
    pw1.clear()
    pw2.clear()
