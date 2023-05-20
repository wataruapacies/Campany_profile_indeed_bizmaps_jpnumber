import re
pattern = r'[\(]{0,1}[0-9]{2,4}[\)\-\(]{0,1}[0-9]{2,4}[\)\-]{0,1}[0-9]{3,4}'
text = 'ページ番号：123  更新日：2022年2月21日' + '\n' + \
    '○○区役所庁舎案内' + '\n' + \
    'お問い合わせは、庁舎管理係へお願いします'+ '\n' + \
    '電話：03-1234-5566（代表）'+ '\n' + \
    'メールアドレス：abc123def-456ghi@domain.ne.jp' + '\n' + \
    '特設サイト：https://www.city.xxx.tokyo.jp/toiawase/' +"999999999999999999999999999999"
print(text)
tell = re.findall(pattern, text)
print('\n\n')
print(tell)

for catched in range(tell):
    