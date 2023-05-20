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
driver.set_page_load_timeout(90)
driver.maximize_window()

row = ['','','','','','','','','']

try:
    phone_summary_site = 'https://www.jpnumber.com/'
    phone_summary_site = phone_summary_site + 'searchnumber.do?number='
    phone_seach_keyword_url = urllib.parse.quote('株式会社ビサイズ')
    phone_summary_site_url = phone_summary_site + phone_seach_keyword_url
    driver.get(phone_summary_site_url)
    sleep(2)
    jpnumber_hit = driver.find_element_by_class_name("number-text15")
    jpnumber_hit_text = jpnumber_hit.text
    if jpnumber_hit_text == '0':
        jp_search = False
        print('jpnumber_search dont go...')
    else:
        jp_search = True
    if jp_search:
        print('jpnumber_serch go!!!')
        phone_contents = driver.find_elements_by_class_name("frame-728-orange-l")
        print(len(phone_contents))
        max_num = 15
        #company_address = address_list[1]
        correct_number = 0
        table_exist = 0
        #for i in range(max_num):
        ii = 3
        while True:
            try:
                #//*[@id="result-main-right"]/div[3]/div/span/a
                #//*[@id="result-main-right"]/div[3]/table/tbody/tr/td[1]/div/dt[2]/strong/a/span
                xpath = "//div[" + str(ii) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
                phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
                print(phone_company_name)
                phone_company_name_text = phone_company_name.text.replace('\u3000',' ')
                print(phone_company_name_text)
                xpath = "//div[" + str(ii) + "]/table/tbody/tr/td[1]/div/dt[5]"
                phone_company_address = driver.find_element(by=By.XPATH, value=xpath)
                phone_company_address_text = phone_company_address.text
                phone_company_address_text = phone_company_address_text.lstrip('住所：')
                jp_postcode = ''
                if phone_company_address_text.startswith('〒'):
                    jp_postcode = phone_company_address_text.lstrip('〒')
                    index = phone_company_address_text.find(' ')
                    jp_postcode = phone_company_address_text[:index]
                    phone_company_address_text = phone_company_address_text[index + 1:]
                print(jp_postcode)
                print(phone_company_address_text)
                if '東京都' in phone_company_address_text:
                    print('target_address exist!! break!!')
                    print(phone_company_name)
                    print(phone_company_address_text)
                    correct_number = ii
                    break
                table_exist = table_exist + 1
                ii = ii + 1
                if table_exist == len(phone_contents):
                    print('all checked.... break')
            except:
                print(ii)
                print('jpnumber_loop target non... next!')
                ii = ii + 1
        #rememberが一番似ている番号になった．
        xpath = "//div[" + str(correct_number) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
        phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
        print(phone_company_name.text)
        for k in range(len(row)):
            if k < 2:
                continue
            row[k] = ''
        try:
            row[2] = phone_company_name.text
        except:
            print('jpnumber company_name input error')
        xpath = "//div[" + str(correct_number) + "]/table/tbody/tr/td[1]/div/dt[5]"
        phone_company_address = driver.find_element(by=By.XPATH, value=xpath)
        phone_company_address_text = phone_company_address.text
        phone_company_address_text = phone_company_address_text.lstrip('住所：')
        jp_postcode = ''
        if phone_company_address_text.startswith('〒'):
            jp_postcode = phone_company_address_text.lstrip('〒')
            index = phone_company_address_text.find(' ')
            jp_postcode = phone_company_address_text[:index]
            phone_company_address_text = phone_company_address_text[index + 1:]
        print('||||||||||||||||||||||| this data is saved ||||||||||||||||||||||||')
        print(jp_postcode)
        print(phone_company_address_text)
        try:
            row[3] = jp_postcode
            row[4] = phone_company_address_text
        except:
            print('jpnumber address and postcode input error')
        xpath = "//div[" + str(correct_number) + "]/div/span/a"
        phone_company_phone = driver.find_element(by=By.XPATH, value=xpath)
        index = phone_company_phone.text.find(' | ')
        phone_company_phone_text = phone_company_phone.text[index + 3:]
        print(phone_company_phone_text)
        try:
            row[6] = phone_company_phone_text
            row[8] = '2'
        except:
            print('jpnumber phone_number input error')
except:
    print("jpnumber_error!!")
print(row)