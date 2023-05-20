jp_postcode = '〒103-0013\u3000東京都中央区日本橋人形町３丁目３－１３'
phone_company_address_text = '〒103-0013\u3000東京都中央区日本橋人形町３丁目３－１３'
if '\u3000' in jp_postcode:
    index = jp_postcode.find('\u3000')
    jp_postcode = jp_postcode[:index]
    phone_company_address_text = phone_company_address_text[index + 1:]
print(jp_postcode)
print(phone_company_address_text)