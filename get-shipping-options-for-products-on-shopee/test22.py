from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import csv 

with open('input.csv', newline='') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
     url = row[0]
     
  
     driver = webdriver.Chrome(executable_path='./chromedriver')
     time.sleep(5)
     driver.get(url)
     time.sleep(5)
     svgg = """//*[@id="pc-drawer-id-1"]/div/svg"""
     shipping = driver.find_elements(By.CLASS_NAME, 'shopee-drawer')[2]
     
    #  print(shipping.text)
     action = ActionChains(driver)
     action.move_to_element(shipping).perform()
     
     delivery_date = driver.find_element(By.CLASS_NAME, 'shopee-drawer__contents')
     contents = delivery_date.find_elements(By.CLASS_NAME, 'AAaUS1')
     
     titles = ""
     for i in contents:
       x = i.get_attribute("innerHTML")
       titles += x+', '

     print(titles)
