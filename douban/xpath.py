import requests
from lxml import etree

url0 = 'https://movie.douban.com/top250?start=0&filter='
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }


response = requests.get(url=url0, headers=headers)
page = response.content.decode('utf-8')
html = etree.HTML(page)

print(html.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[2]/br')[0].text)
#部分丢失？