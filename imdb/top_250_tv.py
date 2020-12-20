import re
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
pattern = re.compile('titleColumn.*?>\s*(.*?)\s*<.*?title.*?>\s*(.*?)\s*<.*?secondaryInfo.*?>\s*(.*?)\s*<.*?imdbRating.*?title="(.*?)"', re.S)

r = requests.get(url, headers=headers)
movies = BeautifulSoup(str(r.content), 'lxml')
movie_list = movies.find_all('tr')
for movie in movie_list:
    movie_detail = re.findall(pattern, str(movie))
    print(movie_detail)


