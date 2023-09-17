import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pandas as pd
import csv
import time

def sleep(sleep_min, sleep_max):
    time.sleep(random.uniform(sleep_min, sleep_max))

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://login.auth.vonage.com/authenticationendpoint/login.do?amplitude_api_key=f477e84bbbdfb385a3f9969d6b5f9ee9&client_id=mJgsiYCZkq01d48LjREPCtCD5kUa&commonAuthCallerPath=%2Foauth2%2Fauthorize&forceAuth=false&passiveAuth=false&redirect_uri=https%3A%2F%2Fapp.vonage.com%2Flogin%3Fsso%3Dtrue&response_type=code&scope=openid&tenantDomain=vbc.prod&sessionDataKey=de1b1655-f847-46cd-8499-f3903de40f51&relyingParty=mJgsiYCZkq01d48LjREPCtCD5kUa&type=oidc&sp=Web&isSaaSApp=false")
# driver.maximize_window()

# Propstream ID and password.
id = "pehutch1958"
password = "Jmh_195888"

# Login element selection.
login_input_id = driver.find_element(By.NAME, "userid")
login_input_pass = driver.find_element(By.NAME, "password")
submit = driver.find_element(By.CLASS_NAME, "sso-log-in")

# login Input details writing.
for character in id:
    login_input_id.send_keys(character)
    sleep(0.1, 0.2)

# login Input details writing.
for character in password:
    login_input_pass.send_keys(character)
    sleep(0.1, 0.2)



time.sleep(60)
with open('C:/Users/J3/Desktop/Project/products.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for line in csv_reader:
            driver.find_element("xpath",'/html/body/div[1]/div/div[6]/div[1]/div[1]/div[1]/div[2]/div[2]/button/span').click()
            driver.find_element("xpath",'/html/body/div[1]/div/div[6]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]/div/span').click()
            time.sleep(1)
            phone = driver.find_element("xpath",'/html/body/div[1]/div/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div/div[2]/input')
            phone.send_keys(line[0])
            driver.find_element("xpath",'/html/body/div[1]/div/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div/div[3]').click()           
            time.sleep(20)
            #driver.find_element(By.TAG_NAME,'p[0]').send_keys("Hi")
            #file_input =driver.find_element(By.XPATH("/html/body/div[2]/div[4]/div[3]/div[2]/div[3]/div[2]/input"))
            file_input = driver.find_element(By.CLASS_NAME,'ProseMirror')
            file_input.send_keys("H")
            time.sleep(10)
     
time.sleep(10)
driver.close()