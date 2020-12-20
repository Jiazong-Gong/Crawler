import re
import requests
from bs4 import BeautifulSoup
url = 'https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=DQ9CAYQA0MWMNRHESAY8&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_3'
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


