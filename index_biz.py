from selenium import webdriver
from time import sleep
import csv
import re
import pandas
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import urllib.parse
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from difflib import SequenceMatcher
import os
import glob

options = webdriver.ChromeOptions()

user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',\
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',\
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',\
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3112.113 Safari/537.36'\
    ] 
options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)
driver.maximize_window()

driver.get('https://biz-maps.com/')

sleep(5)

search_bar_biz = driver.find_element_by_id("top_s")
search_bar_biz.send_keys('株式会社エスラボ')

white = driver.find_element_by_class_name("fa-caret-square-down")
white.click()
sleep(5)

biz_area = driver.find_element_by_class_name("top_area")
biz_area.click()
sleep(3)
biz_area_click1 = driver.find_element_by_class_name("modal__item_parent")
biz_area_click1.click()
sleep(3)
biz_area_click2 = driver.find_element_by_class_name("modal__item_child")
biz_area_click2.click()
sleep(3)
biz_area_click3 = driver.find_element(By.CLASS_NAME,"modal_footer.modal_decide_Btn")
biz_area_click3.click()
sleep(15)
search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
print(search_num.text)