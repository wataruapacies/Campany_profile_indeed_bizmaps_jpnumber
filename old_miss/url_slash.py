url_text = 'https://biz-maps.com/s/prefs/13,27'

ok = True

if url_text.startswith("http://"):
    url_text = url_text.lstrip("http://")
    ok = False
if url_text.startswith("https://"):
    url_url_text = url_url_text.lstrip("https://")
    ok = True
print(url_text)
for url_text_index in range(len(url_text)):
    if url_text[url_text_index] =='/':
        print("slash ------> True in URL")
        break
url_text = url_text[:url_text_index]
print(url_text)
if ok:
    url_text = 'https://' + url_text
else:
    url_text = 'http://' + url_text
print(url_text)