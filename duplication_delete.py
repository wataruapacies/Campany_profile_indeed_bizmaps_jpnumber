import csv
import os
import glob
import pandas

cwd = os.getcwd()
path_list=glob.glob(cwd + '\*')
name_list=[]
for i in path_list:
    file = os.path.basename(i)          # ファイル名(拡張子あり)を取得
    #name, ext = os.path.splitext(file)  # 拡張子なしファイル名と拡張子を取得
    name_list.append(file)              # 拡張子なしファイル名をリスト化

print(name_list)
count_col = 0
phone_col = 0
cols = ['','indeed_会社名数','電話番号取得数','取得率']
df = pandas.DataFrame(index=[], columns=cols)
phone_list = []
for j in range(len(name_list)):
    if '.csv' in name_list[j]:
        file_name = name_list[j]
        print(file_name)
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        #file_name = '東京都_製造業.csv'
        with open(file_name,'r',encoding='cp932') as f:
            reader = csv.reader(f)
            i = 0
            count = 0
            phone = 0
            for line in reader:
                if i == 0:
                    result = pandas.DataFrame(index=[], columns=line)
                    print(name_list[j])
                else:
                    phone_raw_num = line[6]
                    phone_raw_num = phone_raw_num.replace('-','')
                    phone_raw_num = phone_raw_num.replace('(','')
                    phone_raw_num = phone_raw_num.replace(')','')
                    if line[6] != '':
                        if phone_raw_num not in phone_list:
                            phone_list.append(phone_raw_num)
                            result = result.append(pandas.Series(line, index=result.columns), ignore_index=True)
                            phone = phone + 1
                            count = count + 1
                        else:
                            print('double')
                            print(line)
                    else:
                        count = count + 1
                        result = result.append(pandas.Series(line, index=result.columns), ignore_index=True)
                i = i + 1
            row = []
            row.append(name_list[j])
            row.append(count)
            row.append(phone)
            percent = phone / count
            row.append(percent)
            count_col = count_col + count
            phone_col = phone_col + phone
            df = df.append(pandas.Series(row, index=df.columns), ignore_index=True)
        result_name = name_list[j].replace('.csv','')
        result_name = result_name + '_番号重複消去.csv'
        result.to_csv(result_name,index=False,encoding="cp932",errors="ignore")
row = []
row.append('合計')
row.append(count_col)
row.append(phone_col)
percent = phone_col / count_col
row.append(percent)
df = df.append(pandas.Series(row, index=df.columns), ignore_index=True)
file_name = '電話番号取得率.txt'
df.to_csv(file_name,index=False,encoding="cp932",errors="ignore")
                        