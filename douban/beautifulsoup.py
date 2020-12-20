import re
import requests
from bs4 import BeautifulSoup
import bs4



url = 'https://movie.douban.com/top250?start=0&filter='
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }

response = requests.get(url=url, headers=headers)
html = response.content.decode('utf-8')
l = BeautifulSoup(html, 'lxml')
movie_list = l.select('div.item')

for movie in movie_list:
    rank = movie.find_all('em', {'class': ''})
    title = movie.find_all('div', {'class': 'hd'})
    detail = movie.find_all('p', {'class': ''})
    rating = movie.find_all('div', {'class': 'star'})
    comment = movie.find_all('p', {'class': 'quote'})
    print(rank, title, detail, rating, comment)
