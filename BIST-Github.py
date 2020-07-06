# Basic Info Search Tool

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
print("""\n  ____    ___   ____    _____ 
 | __ )  |_ _| / ___|  |_   _|
 |  _ \   | |  \___ \    | |  
 | |_) |  | |   ___) |   | |  
 |____/  |___| |____/    |_|  \n""")
name = input("Enter name here: ")
name.replace(" ", "%20")
driver = webdriver.Chrome('PATHTOCHROMEDRIVER')
driver.get('https://www.linkedin.com/login/');
usernameField = driver.find_element_by_id("username")
with open('emails/email.txt', 'r') as myfile:
  data = myfile.read()
usernameField.send_keys(data)
with open('passwords/password1.txt', 'r') as myfile:
  data = myfile.read()
passwordField = driver.find_element_by_id("password")
passwordField.send_keys(data)
driver.get("https://www.linkedin.com/search/results/all/?keywords=" + name + "&origin=GLOBAL_SEARCH_HEADER")
driver.find_element_by_class_name("name").click()
time.sleep(2)
linkedin = driver.current_url
time.sleep(2)
driver.get("https://rocketreach.co/login")
with open('emails/email1.txt', 'r') as myfile:
  data = myfile.read()
usernameField = driver.find_element_by_id("id_email")
usernameField.send_keys(data)
with open('passwords/password2.txt', 'r') as myfile:
  data = myfile.read()
passwordField = driver.find_element_by_id("id_password")
passwordField.send_keys(data)
time.sleep(1)
passwordField.send_keys(Keys.ENTER)
rocketreach = "https://rocketreach.co/?tags=!((incexc:include,keyword:%27" + name + "%27,type:keywords))&page_size=10&start=1&mode=default"
driver.get(rocketreach)
time.sleep(2)
atag = driver.find_element_by_class_name("contact-list__entry__link")
longemail = atag.get_attribute("href")
email = longemail.replace("mailto:", "")
print("\nName: " + name.title())
print("Linkedin URL: " + linkedin)
print("Email: " + email + "\n")
driver.close()