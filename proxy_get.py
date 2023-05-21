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

proxy_ip = "139.162.78.109"
proxy_port = "3128"


PROXY="139.162.78.109:3128"
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True


box_search_what = "IT エンジニア 外国人受入企業"
box_search_where = "東京都"

# indeedで会社名抽出するなら True しないなら False
indeed_judge = True

box_search_what_url = urllib.parse.quote(box_search_what)
box_search_where_url = urllib.parse.quote(box_search_where)

if indeed_judge:
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
    first_url = 'https://jp.indeed.com/jobs?q=' + box_search_what_url + '&l=' + box_search_where_url

    driver.get(first_url)
    now_url = first_url


    name = []
    name_num = 1
    page_num = 1
    OK = 0
    while page_num <= 2:
        print(page_num)
        sleep(2)
        indeed_name = []
        for new_name in driver.find_elements_by_class_name("companyName"):
            indeed_name.append(new_name.text)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        name_replace = [item.replace('\u3000',' ') for item in indeed_name]
        
        
        for i in range(len(name_replace)):
            
            if name_replace[i] not in name:
                name.append(name_replace[i])
        
        print(name)
        csv_file_name_a = box_search_where + '_' + box_search_what + '_' + '名前' + str(page_num) + '.csv'
        file = open(csv_file_name_a, 'w', encoding='utf-8_sig') 
        write = csv.writer(file)
        try:
            write.writerow(name)
        except:
            print("\nerror!!!\n")
        if OK == 1:
            break
        if page_num % 10 ==0:
            try:
                mytext = box_search_where + '_' + box_search_what + '_' + '名前' + str(page_num) + '.txt'
                f = open(mytext,'w')
                f.writelines(name)
                f.close()
            except:
                print("write_text_error\n")
        
        sleep(5)
        next_pages = driver.find_elements(By.CLASS_NAME,"css-13p07ha.e8ju0x50")
        driver.implicitly_wait(60)
        try:
            next_page_text = next_pages[len(next_pages)-1].get_attribute('href')
            print(next_page_text)
            page_num = page_num + 1
            driver.close()
            sleep(3)
            driver = webdriver.Chrome(options=options)
            driver.get(next_page_text)
            now_url = next_page_text
        except:
            print('cant read....')
            driver.close()
            sleep(5)
            driver = webdriver.Chrome(options=options)
            driver.get(now_url)

        
    driver.close()
    

    print(len(name))
    csv_file_name_a = box_search_where + '_' + box_search_what + '_' + 'result' + '.csv'
    file = open(csv_file_name_a, 'w', encoding='utf-8_sig') 
    write = csv.writer(file)
    try:
        write.writerow(name)
    except:
        print('last writing error!!')
else:
    cwd = os.getcwd()
    path_list=glob.glob(cwd + '\*')
    name_list=[]
    for i in path_list:
        file = os.path.basename(i)          # ファイル名(拡張子あり)を取得
        #name, ext = os.path.splitext(file)  # 拡張子なしファイル名と拡張子を取得
        name_list.append(file)              # 拡張子なしファイル名をリスト化
    print(name_list)
    
    
    for k in range(len(name_list)):
        if 'result.csv' in name_list[k]:
            file_name = name_list[k]
    
    #file_name = 'result.csv'
    with open(file_name,'r',encoding='utf-8_sig') as f:
        reader = csv.reader(f)
        for line in reader:
            #print(line)
            name = line
            #print("yes")
            break
    #print("\nOK?\n")
    print(name)
    print(len(name))
    #print('OK')
