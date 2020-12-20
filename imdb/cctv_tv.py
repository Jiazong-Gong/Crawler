import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import csv
url0 = 'http://api.cntv.cn/epg/getEpgInfoByChannelNew?c=cctvjilu&serviceId=tvcctv&d=201901{}&t=jsonp&cb=setItem1'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
day = 1
date = []
while day <= 27:
    if day <= 9:
        date.append('0' + str(day))
    else:
        date.append(str(day))
    day += 1

with open('schedule.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    for d in date:
        url = url0.format(d)
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        html = r.text
        pattern = re.compile('{.*?}', re.S)
        text = re.findall(pattern, str(html))

        i = 1
        while i < len(text):
            schedule = json.loads(text[i])
            title = schedule['title']
            showtime = schedule['showTime']
            writer.writerow([d, title, showtime])
            i += 1





