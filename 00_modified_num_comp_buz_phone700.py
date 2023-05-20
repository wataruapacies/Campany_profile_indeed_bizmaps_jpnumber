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
        print('--------------list NOT matched!-------------------')
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
        elif string[i] in number_10 and string[i-1] in number_10 and string[i-2] in number_10 and string[i-3] == '-' and string[i-4] in number_10 and string[i-5] in number_10 and string[i-6] in number_10 and string[i-7] == '-' and string[i-8] == '0' and string[i-9] == '2' and string[i-10] == '1' and string[i-11] == '0':
            digits = 11
            answer[1] = string[i-digits]
            for k in range(digits):
                answer[1] = answer[1] + string[i-(digits-1-k)]
            print('free dial')
            print(answer[1])
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
    while page_num < 50:
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

cols = ['indeed_会社名','業種','会社名','郵便番号','住所','URL','電話番号','フリーダイヤル','bizmapsで得たURLからの電話番号なら1 junumberからの電話番号なら2']
df = pandas.DataFrame(index=[], columns=cols)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)
driver.set_page_load_timeout(90)
driver.maximize_window()

#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
text_company = ['/company/','/about/','/company/outline','/company.php','/company-profile']
i = 0
while i < len(name):
    url_exist = False
    phone_exist = False
    biz_click = True
    row = ['','','','','','','','','']
    row[0] = name[i]
    indeed = name[i]
    row[1] = box_search_what
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
            print("not_yet.... wait 20 seconds...")
            sleep(20)
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
            biz_area = driver.find_element_by_class_name("top_area")
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
            search_num_new = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
            search_num_new_text = search_num_new.text
            if search_num_new_text == "" or search_num_new_text==search_num_text:
                print("not_yet.... wait 5 seconds...")
                sleep(5)
            search_num_new = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
            search_num_new_text = search_num_new.text
            if search_num_new_text == "" or search_num_new_text==search_num_text:
                print("not_yet.... wait 10 seconds...")
                sleep(10)
            search_num_new = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
            search_num_new_text = search_num_new.text
            if search_num_new_text == "" or search_num_new_text==search_num_text:
                print("not_yet.... wait 20 seconds...")
                sleep(20)
            search_num_new = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
            search_num_new_text = search_num_new.text
            if search_num_new_text == "" or search_num_new_text==search_num_text:
                print("not_yet.... wait 45 seconds...")
                sleep(45)
            search_num_new = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
            search_num_new_text = search_num_new.text
            if search_num_new_text == "" or search_num_new_text==search_num_text:
                print("not_yet.... biz_data impossible!!")
                biz_click = False
            search_num_new_text = search_num_new.text
            print(search_num_new_text)
            if search_num_new_text == '0':
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
                    print("not_yet.... wait 20 seconds...")
                    sleep(20)
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
                search_num_new = driver.find_element(By.CLASS_NAME,"searchArea__number--num")
            if len(search_num_new.text)>4:
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
                row[2] = biz_name.text
            except:
                print("cant_read_name")
                print('return retry')
                print(i)
                driver.close()
                print('chromedriver reboot!!!')
                driver = webdriver.Chrome(options=options)
                driver.implicitly_wait(2)
                driver.set_page_load_timeout(90)
                driver.maximize_window()
                continue
            try:
                xpath = "//div[1]/div[1]/section[1]/div/div[1]/table/tbody/tr[1]/td"
                address = driver.find_element(by=By.XPATH, value=xpath)
                address_list = address.text.splitlines()
                try:
                    if address_list[0].startswith('〒'):
                        try:
                            address_list[0] = address_list[0].lstrip('〒 ')
                        except:
                            print('top post_code cant delete....')
                        print(address_list[0])
                        row[3] = address_list[0]
                        print(address_list[1])
                        row[4] = address_list[1]
                        biz_address_exist = True
                    else:
                        print('Address Is This ????')
                        print(address_list[0])
                        row[4] = (address_list[0])
                except:
                    print("cant_read_address")
            except:
                print("post_code_and_address_cant_read")
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
                        row[5] = (url_text)
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
                driver.get(url_text)
                sleep(5)
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
                        sleep(5)
                        page_text = driver.page_source
                        page_result = phone_number_new(page_text,page_result)
                if page_result[0] == '':
                    jj = 0
                    while True:
                        try:
                            company_link_next = url_text + text_company[jj]
                            print(company_link_next)
                            driver.get(company_link_next)
                            sleep(5)
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
                if page_result[0] == '':
                    print('phone_numebr non......')
                else:
                    print('phone_exist_continue!!')
                    phone_exist = True
                row[6] = page_result[0]
                row[7] = page_result[1]#フリーダイヤル追加
                row[8] = '1'
            except:
                print('company_homepage existence error')
                    #------------------------------ここまで
        if phone_exist:
            print('already phone_number exist!! jpnumber dont need!!')
        #ここからjp_number
        else:
            #URL取得できなかった場合
            try:
                phone_summary_site = 'https://www.jpnumber.com/'
                phone_summary_site = phone_summary_site + 'searchnumber.do?number='
                phone_seach_keyword_url = urllib.parse.quote(name[i])
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
                    correct_number = 0
                    table_exist = 0
                    #for i in range(max_num):
                    ii = 2
                    while True:
                        if ii > 30:
                            print('jpnumber loop too much break!')
                            break
                        try:
                            xpath = "//div[" + str(ii) + "]/table/tbody/tr/td[1]/div/dt[2]/strong/a"
                            phone_company_name = driver.find_element(by=By.XPATH, value=xpath)
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
                            if box_search_where in phone_company_address_text:
                                print('target_address exist!! break!!')
                                print(phone_company_name)
                                print(phone_company_address_text)
                                correct_number = ii
                                break
                            table_exist = table_exist + 1
                            ii = ii + 1
                            if table_exist == len(phone_contents):
                                print('all checked.... break')
                                ii = ii - 1
                                break
                        except:
                            print(ii)
                            print('jpnumber_loop error....?????')
                            ii = ii + 1
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
                    if '\u3000' in jp_postcode:
                        phone_company_address_text = phone_company_address.text
                        phone_company_address_text = phone_company_address_text.lstrip('住所：')
                        index = phone_company_address_text.find('\u3000')
                        jp_postcode = phone_company_address_text[:index]
                        phone_company_address_text = phone_company_address_text[index + 1:]
                    if jp_postcode.startswith('〒'):
                        jp_postcode = phone_company_address_text.lstrip('〒')
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
    except:
        print('where i dont know error exist???')
    try:
        row = list_check(row,9)
        print('How are you ?')
        print(row)
        df = df.append(pandas.Series(row, index=df.columns), ignore_index=True)
        print("dataframe saved................................")
    except:
        print('row--->dataframe_error!!!')
    #driver.close()
    #print('chromedriver reboot!!!')
    #driver = webdriver.Chrome(options=options)
    #driver.implicitly_wait(2)
    #driver.set_page_load_timeout(90)
    #driver.maximize_window()
    try:
        if i % 5 == 0 and i != 0:
            i_str = str(i)
            csv_file_name_log = box_search_where + '_' + box_search_what + '_' + i_str.zfill(4) + '.csv'
            df.to_csv(csv_file_name_log,index=False,encoding="cp932",errors="ignore")
    except:
        print('log_save_error!')
    print('NEXT')
    i = i + 1
df.to_csv(csv_file_name,index=False,encoding="cp932",errors="ignore")

print("fin")
driver.close()