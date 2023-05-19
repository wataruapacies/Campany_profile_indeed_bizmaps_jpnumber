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


def list_check(list, number):
    compare = []
    for j in range(number):
        compare.append('compare')
    if len(list) == len(compare):
        print('list matched!')
    else:
        if len(list) > len(compare):
            for i in range(len(list)-len(compare)):
                list = list[:-1]
        else:
            for i in range(len(compare)-len(list)):
                list.append("")
    return list


def phone_number_new(string,answer):
    number_10 = ['0','1','2','3','4','5','6','7','8','9']
    exist = 0
    count = 0
    count_hyphen = 0
    phone_number_count = 12
    #answer = ['']
    for i in range(len(string)):
        if i < 15:
            continue
        elif string[i] in number_10 and string[i-1] in number_10 and string[i-2] in number_10 and string[i-3] in number_10:#末尾****
            if string[i-4] == '-':#末尾-****
                if string[i-5] in number_10 and string[i-6] in number_10:#末尾**-****
                    if string[i-7] in number_10 and string[i-8] in number_10:#末尾****-****
                        if string[i-9] == '-':#末尾-****-****
                            if string[i-10] in number_10 and string[i-11] =='0':#0*-****-****
                                digits = 11
                                answer[0] = string[i-digits]
                                for k in range(digits):
                                    answer[0] = answer[0] + string[i-(digits-1-k)]
                                if answer[0].startswith('00'):
                                    answer[0] = ''
                                else:
                                    break
                            elif string[i-10] in number_10 and string[i-11] in number_10 and string[i-12] == '0':#0**-****-****
                                digits = 12
                                answer[0] = string[i-digits]
                                for k in range(digits):
                                    answer[0] = answer[0] + string[i-(digits-1-k)]
                                if answer[0].startswith('000'):
                                    answer[0] = ''
                                else:
                                    break
                        elif string[i-9] ==')':#末尾)****-****
                            if string[i-10] in number_10 and string[i-11] == '0' and string[i-12] == '(':#(0*)****-****
                                digits = 12
                                answer[0] = string[i-digits]
                                for k in range(digits):
                                    answer[0] = answer[0] + string[i-(digits-1-k)]
                                if answer[0].startswith('(00)'):
                                    answer[0] = ''
                                else:
                                    break
                            elif string[i-10] in number_10 and string[i-11] in number_10 and string[i-12] == '0' and string[i-13] == '(':#(0**)****-****
                                digits = 13
                                answer[0] = string[i-digits]
                                for k in range(digits):
                                    answer[0] = answer[0] + string[i-(digits-1-k)]
                                if answer[0].startswith('(000)'):
                                    answer[0] = ''
                                else:
                                    break
                    elif string[i-7] in number_10:#末尾***-****
                        if string[i-8] == '-' and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] == '0':#0**-***-****
                            digits = 11
                            answer[0] = string[i-digits]
                            for k in range(digits):
                                answer[0] = answer[0] + string[i-(digits-1-k)]
                            if answer[0].startswith('000'):
                                answer[0] = ''
                            else:
                                break
                        elif string[i-8] == ')' and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] == '0' and string[i-12] == '(':#(0**)***-****
                            digits = 12
                            answer[0] = string[i-digits]
                            for k in range(digits):
                                answer[0] = answer[0] + string[i-(digits-1-k)]
                            if answer[0].startswith('(000)'):
                                answer[0] = ''
                            else:
                                break
                    elif string[i-7] == '-' and string[i-8] in number_10 and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] =='0':#0***-**-****
                        digits = 11
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('0120'):
                            answer[1] = answer[0]
                            answer[0] = ''
                            print('free dial')
                            print(answer[1])
                        if answer[0].startswith('0000'):
                            answer[0] = ''
                        else:
                            break
                    elif string[i-7] == '(' and string[i-8] in number_10 and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] =='0' and string[i-12] == ')':#(0***)**-****
                        digits = 12
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('(0120)'):
                            answer[1] = answer[0]
                            answer[0] = ''
                            print('free dial')
                            print(answer[1])
                        if answer[0].startswith('(0000)'):
                            answer[0] = ''
                        else:
                            break
            elif string[i-4] == ')':#末尾)****
                if string[i-5] in number_10 and string[i-6] in number_10:#末尾**)****
                    if string[i-7] =='(' and string[i-8] in number_10 and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] == '0':#0***(**)****
                        digits = 11
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('0120'):
                            answer.append(answer[0])
                            answer[0] = ''
                            print('free dial')
                            print(answer[1])
                        if answer[0].startswith('0000'):
                            answer[0] = ''
                        else:
                            break
                    elif string[i-7] in number_10 and string[i-8] =='(' and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] == '0':#0**(***)****
                        digits = 11
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('000'):
                            answer[0] = ''
                        else:
                            break
                    elif string[i-7] in number_10 and string[i-8] in number_10 and string[i-9] =='(' and string[i-10] in number_10 and string[i-11] == '0':#0*(****)****
                        digits = 11
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('00'):
                            answer[0] = ''
                        else:
                            break
                    elif string[i-7] in number_10 and string[i-8] in number_10 and string[i-9] =='(' and string[i-10] in number_10 and string[i-11] in number_10 and string[i-12] == '0':#0**(****)****
                        digits = 12
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('000'):
                            answer[0] = ''
                        else:
                            break
            elif string[i-4] in number_10 and string[i-5] in number_10:#末尾******
                if string[i-6] == ')' and string[i-7] in number_10 and string[i-8] in number_10 and string[i-9] in number_10 and string[i-10] == '0' and string[i-11] == '(':#(0***)******
                    digits = 11
                    answer[0] = string[i-digits]
                    for k in range(digits):
                        answer[0] = answer[0] + string[i-(digits-1-k)]
                    if answer[0].startswith('(0120)'):
                        answer[1] = answer[0]
                        print('free dial')
                        print(answer[1])
                        answer[0] = ''
                    if answer[0].startswith('(0000)'):
                        answer[0] = ''
                    else:
                        break
                elif string[i-6] in number_10 and string[i-7] == ')' and string[i-8] in number_10 and string[i-9] in number_10 and string[i-10] == '0' and string[i-11] == '(':#(0**)*******
                    digits = 11
                    answer[0] = string[i-digits]
                    for k in range(digits):
                        answer[0] = answer[0] + string[i-(digits-1-k)]
                    if answer[0].startswith('(000)'):
                        answer[0] = ''
                    else:
                        break
                elif string[i-6] in number_10 and string[i-7] in number_10 and string[i-8] == ')' and string[i-9] in number_10 and string[i-10] == '0' and string[i-11] == '(':#(0*)********
                    digits = 11
                    answer[0] = string[i-digits]
                    for k in range(digits):
                        answer[0] = answer[0] + string[i-(digits-1-k)]
                    if answer[0].startswith('(00)'):
                        answer[0] = ''
                    else:
                        break
                elif string[i-6] in number_10 and string[i-7] in number_10 and string[i-8] == ')' and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] == '0' and string[i-12] == '(':#(0**)********
                    digits = 12
                    answer[0] = string[i-digits]
                    for k in range(digits):
                        answer[0] = answer[0] + string[i-(digits-1-k)]
                    if answer[0].startswith('(000)'):
                        answer[0] = ''
                    else:
                        break
    return answer

        


options = webdriver.ChromeOptions()

user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',\
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',\
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',\
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.3112.113 Safari/537.36'\
    ] 
options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
#options.add_argument('--headless')



box_search_what = "IT エンジニア 外国人"
box_search_where = "東京都"

# indeedで会社名抽出するなら True しないなら False
indeed_judge = False

box_search_what_url = urllib.parse.quote(box_search_what)
box_search_where_url = urllib.parse.quote(box_search_where)

if indeed_judge:
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
    first_url = 'https://jp.indeed.com/jobs?q=' + box_search_what_url + '&l=' + box_search_where_url

    driver.get(first_url)



    name = []
    name_num = 1
    page_num = 1
    OK = 0
    while page_num < 101:
        sleep(5)
        driver.maximize_window()
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
        next_page_text = next_pages[len(next_pages)-1].get_attribute('href')
        print(next_page_text)
        page_num = page_num + 1
        driver.close()
        sleep(3)
        driver = webdriver.Chrome(options=options)
        driver.get(next_page_text)
        
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

#sleep(2)

# indeedから企業名はここまでで取得，nameにリストとしてはいってる．

csv_file_name = box_search_where + '_' + box_search_what + '.csv'

cols = ['indeed_会社名','業種','会社名','郵便番号','住所','URL','電話番号','bizmapsなら1 junumberなら2']
df = pandas.DataFrame(index=[], columns=cols)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)
driver.maximize_window()

#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
text_company = ['/company/','/about/','/company/outline','company.php']

for i in range(len(name)):
    if i == 0:
        print(name[i])
        continue
    biz_name_exist = False
    biz_address_exist = False
    url_exist = False
    biz_click = True
    row = []
    row.append(name[i])
    indeed = name[i]
    row.append(box_search_what)
    sleep(1)
    try:
        driver.get('https://biz-maps.com/')
        sleep(3)
        #search_bar_biz = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "top_s")))
        #search_bar_biz.send_keys(name[i])
        search_bar_biz = driver.find_element_by_id("top_s")
        search_bar_biz.send_keys(name[i])
        print(i)
        print(name[i])
        #sleep(1)
        white = driver.find_element_by_class_name("fa-caret-square-down")
        white.click()
        sleep(5)
        element = driver.find_element_by_class_name("TopSearchBtn")
        search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
        if search_num.text == "":
            print("not_yet.... wait 5 seconds...")
            sleep(5)
        search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
        if search_num.text == "":
            print("not_yet.... wait 10 seconds...")
            sleep(10)
        search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
        if search_num.text == "":
            print("not_yet.... wait 25 seconds...")
            sleep(25)
        search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
        if search_num.text == "":
            print("not_yet.... biz_data impossible!!")
            biz_click = False
        search_num_text = search_num.text
        print(search_num_text)
        if search_num.text == '0':
            print("biZ_data = 0 !! biz_data impossible!!")
            biz_click = False
        if len(search_num_text)>1:
            print("big_data more imformation input!!!!")
            biz_area = driver.find_element_by_class_name("top_city")
            biz_area.click()
            sleep(1)
            biz_area_click1 = driver.find_element_by_class_name("modal__item_parent")
            biz_area_click1.click()
            sleep(1)
            biz_area_click2 = driver.find_element_by_class_name("modal__item_child")
            biz_area_click2.click()
            sleep(1)
            biz_area_click3 = driver.find_element(By.CLASS_NAME,"modal_footer.modal_decide_Btn")
            biz_area_click3.click()
            sleep(2)
            search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
            if search_num.text == "":
                print("not_yet.... wait 5 seconds...")
                sleep(5)
            search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
            if search_num.text == "":
                print("not_yet.... wait 10 seconds...")
                sleep(10)
            search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
            if search_num.text == "":
                print("not_yet.... wait 25 seconds...")
                sleep(25)
            search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
            if search_num.text == "":
                print("not_yet.... biz_data impossible!!")
                biz_click = False
            search_num_text = search_num.text
            print(search_num_text)
            if search_num.text == '0':
                print("biZ_data = 0 !! biz_data impossible!! ---------->sorry....")
                #biz_click = False
                driver.get('https://biz-maps.com/')
                sleep(3)
                #search_bar_biz = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "top_s")))
                #search_bar_biz.send_keys(name[i])
                search_bar_biz = driver.find_element_by_id("top_s")
                search_bar_biz.send_keys(name[i])
                print(i)
                print(name[i])
                #sleep(1)
                white = driver.find_element_by_class_name("fa-caret-square-down")
                white.click()
                sleep(2)
                element = driver.find_element_by_class_name("TopSearchBtn")
                search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
                if search_num.text == "":
                    print("not_yet.... wait 5 seconds...")
                    sleep(5)
                search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
                if search_num.text == "":
                    print("not_yet.... wait 10 seconds...")
                    sleep(10)
                search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
                if search_num.text == "":
                    print("not_yet.... wait 25 seconds...")
                    sleep(25)
                search_num = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
                if search_num.text == "":
                    print("not_yet.... biz_data impossible!!")
                    biz_click = False
                search_num_text = search_num.text
                print(search_num_text)
        if len(search_num_text)>4:
            biz_click = False
            print("big_data more biz_click-->False...")
        
        #最初の情報入力処理終了
            
        if biz_click:
            try:
                print("click_before")
                element.click()
                print("click_after")
            except:
                print('i cant click')
                element.click()
            sleep(2)
            try:
                search_results = driver.find_elements(By.CLASS_NAME,"results__headArea")
                #sleep(1)
                biz_index_num = 0
                for biz_index in range(len(search_results)):
                    try:
                        xpath = "//div/div[3]/div[2]/ul/li[" + str(biz_index+1) + "]/div[1]/table[1]/tbody/tr[2]/td"
                        address = driver.find_element(by=By.XPATH, value=xpath)
                        print('yeahllllll')
                        print(address.text)
                        if box_search_where in address.text:
                            biz_index_num = biz_index
                            print('target catched!!!')
                            break
                    except:
                        print('terget NON')
                search_results[biz_index_num].click()
                #住所が東京なのをクリック なければ一番上の
                biz_name = driver.find_element(By.CLASS_NAME,"company__name")
                print(biz_name.text)
                row = list_check(row,2)
                row.append(biz_name.text)
                biz_name_exist = True
            except:
                row = list_check(row,2)
                row.append("")
                print("cant_read_name")
            try:
                xpath = "//div[1]/div[1]/section[1]/div/div[1]/table/tbody/tr[1]/td"
                address = driver.find_element(by=By.XPATH, value=xpath)
                address_list = address.text.splitlines()
                try:
                    post_code = address_list[0]
                    if post_code.startswith('〒'):
                        post_code = post_code.lstrip('〒 ')
                        print(post_code)
                        row = list_check(row,3)
                        row.append(post_code)
                    else:
                        row = list_check(row,3)
                        print('cant Get postcode')
                        row.append('')
                except:
                    row = list_check(row,3)
                    row.append("")
                    print("cant_read_post_code")
                    biz_exist = False
                try:
                    if address_list[0].startswith('〒'):
                        print(address_list[1])
                        row = list_check(row,4)
                        row.append(address_list[1])
                        biz_address_exist = True
                    else:
                        print('Address Is This ????')
                        print(address_list[0])
                        row = list_check(row,4)
                        row.append(address_list[0])
                except:
                    row = list_check(row,4)
                    row.append("")
                    print("cant_read_address")
            except:
                row = list_check(row,3)
                row.append("")
                row.append("")
                print("post_code_and_address_cant_read")
            #sleep(1)
            
            #URL取得
            try:
                j =3
                while True:
                    j = j + 1
                    try:
                        if j > 7:
                            print('no_URL')
                            break
                        xpath_url = "//div[1]/div[1]/section[1]/div/div[1]/table/tbody/tr[" + str(j) + "]/td/a"
                        url = driver.find_element(by=By.XPATH, value=xpath_url)
                        url_text = url.get_attribute('href')
                        print(url_text)
                        row = list_check(row,5)
                        row.append(url_text)
                        url_exist = True
                        print('break URL capture!!')
                        break
                    except:
                        print(j)
            except:
                print("cant_read_URL")
            #ここまででURL取得
        if url_exist:
            #URL取得できた場合
            try:
                driver.close()
                sleep(1)
                driver = webdriver.Chrome(options=options)
                driver.implicitly_wait(3)
                driver.maximize_window()
                driver.get(url_text)
                sleep(3)
                page_text = driver.page_source
                page_result = ['','']
                page_result = phone_number_new(page_text,page_result)
                if page_result[0] == '':
                    print(page_text[10])
                    #URLのルートページ
                    ok = True
                    url_change = False
                    if url_text.startswith("http://"):
                        url_text = url_text.lstrip("http://")
                        ok = False
                    if url_text.startswith("https://"):
                        url_text = url_text.lstrip("https://")
                        ok = True
                    #print(url_text)
                    for url_text_index in range(len(url_text)):
                        if url_text[url_text_index] =='/':
                            print("slash ------> True in URL")
                            url_change = True
                            break
                    try:
                        url_text = url_text[:url_text_index]
                    except:
                        print('URL change error')
                    #print(url_text)
                    if ok:
                        url_text = 'https://' + url_text
                    else:
                        url_text = 'http://' + url_text
                    print(url_text)
                    if url_change:
                        driver.get(url_text)
                        sleep(3)
                        page_text = driver.page_source
                        page_result = phone_number_new(page_text,page_result)
                if page_result[0] == '':
                    jj = 0
                    while True:
                        try:
                            driver.close()
                            driver = webdriver.Chrome(options=options)
                            driver.implicitly_wait(3)
                            driver.maximize_window()
                            company_link_next = url_text + text_company[jj]
                            driver.get(company_link_next)
                            sleep(3)
                            page_text = driver.page_source
                            page_result = phone_number_new(page_text,page_result)
                            if page_result[0] != '':
                                print('break because phone_number capture!! from URL')
                                break
                        except:
                            print('driver.get error!')
                        jj = jj + 1
                        if jj == len(text_company):
                            break
                row = list_check(row,6)
                if page_result[0] == '':
                    print('phone_numebr non......')
                row.append(page_result[0])
                row.append(page_result[1])#フリーダイヤル追加
                if page_result != '':
                    print('phone_exist_continue!!')
                    #------------------------------ここまで
                else:
                    #URLから取れなかった場合
                    row = list_check(row,7)
                    
                    if biz_name_exist and biz_address_exist:
                        #biz検索ヒットあった場合
                        print('biz_name_nothing!!--------> biz_name---->phone _nothing_from URL')
                        try:
                            driver.close()
                            driver = webdriver.Chrome(options=options)
                            driver.implicitly_wait(3)
                            driver.maximize_window()
                            phone_summary_site = 'https://www.jpnumber.com/'
                            phone_summary_site = phone_summary_site + 'searchnumber.do?number='
                            phone_seach_keyword_url = urllib.parse.quote(biz_name.text)
                            phone_summary_site_url = phone_summary_site + phone_seach_keyword_url
                            driver.get(phone_summary_site_url)
                            sleep(2)
                            phone_contents = driver.find_elements_by_class_name("frame-728-orange-l")
                            max_num = 15
                            company_address = address_list[1]
                            ii = 0
                            correct_number = 0
                            remember = 3
                            match_ratio = 0
                            #for i in range(max_num):
                            while True:
                                try:
                                    xpath = "//div[" + str(ii) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
                                    phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
                                    print(phone_company_name.text)
                                    correct_number = correct_number + 1
                                    xpath = "//div[" + str(ii) + "]/table/tbody/tr/td[1]/div/dt[5]"
                                    phone_company_address = driver.find_element(by=By.XPATH, value=xpath)
                                    phone_company_address_text = phone_company_address.text
                                    phone_company_address_text = phone_company_address_text.lstrip('住所：')
                                    if phone_company_address_text.startswith('〒'):
                                        index = phone_company_address_text.find(' ')
                                        phone_company_address_text = phone_company_address_text[index + 1:]
                                    #print(phone_company_address_text)
                                    #下の二行いらんかったなあ
                                    #phone_company_address_text_head = divide_addess(phone_company_address_text)
                                    #phone_company_address_text = phone_company_address_text_head[0] + phone_company_address_text_head[1] + phone_company_address_text_head[2]
                                    print(phone_company_address_text)
                                    compare = SequenceMatcher(None, company_address, phone_company_address_text)
                                    if match_ratio < compare.ratio():
                                        match_ratio = compare.ratio()
                                        remember = ii
                                except:
                                    #print(i)
                                    pass
                                ii = ii + 1
                                if correct_number == len(phone_contents) or ii > 30:
                                    break
                            #rememberが一番似ている番号になった．
                            xpath = "//div[" + str(remember) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
                            phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
                            print(phone_company_name.text)
                            try:
                                row.append(phone_company_name.text)
                            except:
                                row.append("")
                            xpath = "//div[" + str(remember) + "]/table/tbody/tr/td[1]/div/dt[5]"
                            phone_company_address = driver.find_element(by=By.XPATH, value=xpath)
                            phone_company_address_text = phone_company_address.text
                            phone_company_address_text = phone_company_address_text.lstrip('住所：')
                            if phone_company_address_text.startswith('〒'):
                                index = phone_company_address_text.find(' ')
                                phone_company_address_text = phone_company_address_text[index + 1:]
                            print(phone_company_address_text)
                            try:
                                row.append(phone_company_address_text)
                            except:
                                row.append("")
                            xpath = "//div[" + str(remember) + "]/div/span/a"
                            phone_company_phone = driver.find_element(by=By.XPATH, value=xpath)
                            index = phone_company_phone.text.find(' | ')
                            phone_company_phone_text = phone_company_phone.text[index + 3:]
                            print(phone_company_phone_text)
                            try:
                                row.append(phone_company_phone_text)
                            except:
                                row.append("")
                        except:
                            print("jpnumber_error!! _nothing_from URL")
                            
                            
                            
                    #indeed_name
                    else:
                        #biz検索ヒット無かった場合
                        print('biz_name_nothing!!--------> indeed_name---->phone _nothing_from URL')
                        try:
                            driver.close()
                            driver = webdriver.Chrome(options=options)
                            driver.implicitly_wait(3)
                            driver.maximize_window()
                            phone_summary_site = 'https://www.jpnumber.com/'
                            phone_summary_site = phone_summary_site + 'searchnumber.do?number='
                            phone_seach_keyword_url = urllib.parse.quote(indeed)
                            phone_summary_site_url = phone_summary_site + phone_seach_keyword_url
                            driver.get(phone_summary_site_url)
                            sleep(2)
                            phone_contents = driver.find_elements_by_class_name("frame-728-orange-l")
                            max_num = 15
                            iii = 0
                            correct_number = 0
                            remember = 3
                            match_ratio = 0
                            #for i in range(max_num):
                            while True:
                                try:
                                    xpath = "//div[" + str(iii) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
                                    phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
                                    print(phone_company_name.text)
                                    correct_number = correct_number + 1
                                    compare = SequenceMatcher(None, indeed, phone_company_name.text)
                                    if match_ratio < compare.ratio():
                                        match_ratio = compare.ratio()
                                        remember = iii
                                except:
                                    pass
                                iii = iii + 1
                                if correct_number == len(phone_contents) or iii > 30:
                                    break
                            #rememberが一番似ている番号になった．
                            xpath = "//div[" + str(remember) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
                            phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
                            print(phone_company_name.text)
                            try:
                                row.append(phone_company_name.text)
                            except:
                                row.append("")
                            try:
                                xpath = "//div[" + str(remember) + "]/table/tbody/tr/td[1]/div/dt[5]"
                                phone_company_address = driver.find_element(by=By.XPATH, value=xpath)
                                phone_company_address_text = phone_company_address.text
                                phone_company_address_text = phone_company_address_text.lstrip('住所：')
                                if phone_company_address_text.startswith('〒'):
                                    index = phone_company_address_text.find(' ')
                                    phone_company_address_text = phone_company_address_text[index + 1:]
                                print(phone_company_address_text)
                                row.append(phone_company_address_text)
                            except:
                                row.append("")
                            try:
                                xpath = "//div[" + str(remember) + "]/div/span/a"
                                phone_company_phone = driver.find_element(by=By.XPATH, value=xpath)
                                index = phone_company_phone.text.find(' | ')
                                phone_company_phone_text = phone_company_phone.text[index + 3:]
                                print(phone_company_phone_text)
                                row.append(phone_company_phone_text)
                            except:
                                row.append("")
                        except:
                            print("jpnumber_error!! _nothing_from URL")
                            
                    #ここまで
            except:
                print('failure!! from URL!!!!')
                pass
        else:
            #URL取得できなかった場合
            #biz_exist
            row = list_check(row,6)
            row.append("")
            #URLないもん
            if biz_name_exist and biz_address_exist:
                #biz検索ヒットあった場合
                print('biz_name_nothing!!--------> biz_name---->phone')
                try:
                    driver.close()
                    driver = webdriver.Chrome(options=options)
                    driver.implicitly_wait(3)
                    driver.maximize_window()
                    phone_summary_site = 'https://www.jpnumber.com/'
                    phone_summary_site = phone_summary_site + 'searchnumber.do?number='
                    phone_seach_keyword_url = urllib.parse.quote(biz_name.text)
                    phone_summary_site_url = phone_summary_site + phone_seach_keyword_url
                    driver.get(phone_summary_site_url)
                    sleep(2)
                    phone_contents = driver.find_elements_by_class_name("frame-728-orange-l")
                    max_num = 15
                    company_address = address_list[1]
                    ii = 0
                    correct_number = 0
                    remember = 3
                    match_ratio = 0
                    #for i in range(max_num):
                    while True:
                        try:
                            xpath = "//div[" + str(ii) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
                            phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
                            print(phone_company_name.text)
                            correct_number = correct_number + 1
                            xpath = "//div[" + str(ii) + "]/table/tbody/tr/td[1]/div/dt[5]"
                            phone_company_address = driver.find_element(by=By.XPATH, value=xpath)
                            phone_company_address_text = phone_company_address.text
                            phone_company_address_text = phone_company_address_text.lstrip('住所：')
                            if phone_company_address_text.startswith('〒'):
                                index = phone_company_address_text.find(' ')
                                phone_company_address_text = phone_company_address_text[index + 1:]
                            #print(phone_company_address_text)
                            #下の二行いらんかったなあ
                            #phone_company_address_text_head = divide_addess(phone_company_address_text)
                            #phone_company_address_text = phone_company_address_text_head[0] + phone_company_address_text_head[1] + phone_company_address_text_head[2]
                            print(phone_company_address_text)
                            compare = SequenceMatcher(None, company_address, phone_company_address_text)
                            if match_ratio < compare.ratio():
                                match_ratio = compare.ratio()
                                remember = ii
                        except:
                            #print(i)
                            pass
                        ii = ii + 1
                        if correct_number == len(phone_contents) or ii > 30:
                            break
                    #rememberが一番似ている番号になった．
                    xpath = "//div[" + str(remember) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
                    phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
                    print(phone_company_name.text)
                    try:
                        row.append(phone_company_name.text)
                    except:
                        row.append("")
                    xpath = "//div[" + str(remember) + "]/table/tbody/tr/td[1]/div/dt[5]"
                    phone_company_address = driver.find_element(by=By.XPATH, value=xpath)
                    phone_company_address_text = phone_company_address.text
                    phone_company_address_text = phone_company_address_text.lstrip('住所：')
                    if phone_company_address_text.startswith('〒'):
                        index = phone_company_address_text.find(' ')
                        phone_company_address_text = phone_company_address_text[index + 1:]
                    print(phone_company_address_text)
                    try:
                        row.append(phone_company_address_text)
                    except:
                        row.append("")
                    xpath = "//div[" + str(remember) + "]/div/span/a"
                    phone_company_phone = driver.find_element(by=By.XPATH, value=xpath)
                    index = phone_company_phone.text.find(' | ')
                    phone_company_phone_text = phone_company_phone.text[index + 3:]
                    print(phone_company_phone_text)
                    try:
                        row.append(phone_company_phone_text)
                    except:
                        row.append("")
                except:
                    print("jpnumber_error!!")
                    
                    
                    
            #indeed_name
            else:
                #biz検索ヒット無かった場合
                print('biz_name_nothing!!--------> indeed_name---->phone')
                try:
                    driver.close()
                    driver = webdriver.Chrome(options=options)
                    driver.implicitly_wait(3)
                    driver.maximize_window()
                    phone_summary_site = 'https://www.jpnumber.com/'
                    phone_summary_site = phone_summary_site + 'searchnumber.do?number='
                    phone_seach_keyword_url = urllib.parse.quote(indeed)
                    phone_summary_site_url = phone_summary_site + phone_seach_keyword_url
                    driver.get(phone_summary_site_url)
                    sleep(2)
                    phone_contents = driver.find_elements_by_class_name("frame-728-orange-l")
                    max_num = 15
                    iii = 0
                    correct_number = 0
                    remember = 3
                    match_ratio = 0
                    #for i in range(max_num):
                    while True:
                        try:
                            xpath = "//div[" + str(iii) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
                            phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
                            print(phone_company_name.text)
                            correct_number = correct_number + 1
                            compare = SequenceMatcher(None, indeed, phone_company_name.text)
                            if match_ratio < compare.ratio():
                                match_ratio = compare.ratio()
                                remember = iii
                        except:
                            pass
                        iii = iii + 1
                        if correct_number == len(phone_contents) or iii > 30:
                            break
                    #rememberが一番似ている番号になった．
                    xpath = "//div[" + str(remember) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
                    phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
                    print(phone_company_name.text)
                    try:
                        row.append(phone_company_name.text)
                    except:
                        row.append("")
                    try:
                        xpath = "//div[" + str(remember) + "]/table/tbody/tr/td[1]/div/dt[5]"
                        phone_company_address = driver.find_element(by=By.XPATH, value=xpath)
                        phone_company_address_text = phone_company_address.text
                        phone_company_address_text = phone_company_address_text.lstrip('住所：')
                        if phone_company_address_text.startswith('〒'):
                            index = phone_company_address_text.find(' ')
                            phone_company_address_text = phone_company_address_text[index + 1:]
                        print(phone_company_address_text)
                        row.append(phone_company_address_text)
                    except:
                        row.append("")
                    try:
                        xpath = "//div[" + str(remember) + "]/div/span/a"
                        phone_company_phone = driver.find_element(by=By.XPATH, value=xpath)
                        index = phone_company_phone.text.find(' | ')
                        phone_company_phone_text = phone_company_phone.text[index + 3:]
                        print(phone_company_phone_text)
                        row.append(phone_company_phone_text)
                    except:
                        row.append("")
                except:
                    print("jpnumber_error!!")
    except:
        print('where i dont know error exist???')
    
    #row追加処理
    try:
        row = list_check(row,10)
        print(row)
        df = df.append(pandas.Series(row, index=df.columns), ignore_index=True)
        print("dataframe saved................................")
    except:
        print('row--->dataframe_error!!!')
    try:
        if i % 10 == 0 and i != 0:
            i_str = str(i)
            csv_file_name_log = box_search_where + '_' + box_search_what + '_' + i_str.zfill(4) + '.csv'
            df.to_csv(csv_file_name_log,index=False,encoding="cp932",errors="ignore")
    except:
        print('log_save_error!')
df.to_csv(csv_file_name,index=False,encoding="cp932",errors="ignore")

print("fin")
driver.close()