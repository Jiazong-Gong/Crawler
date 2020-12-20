from queue import Queue
import time
from lxml import etree
import requests
import gevent

from gevent import monkey
monkey.patch_all()


class GetTopMovies(object):
    rank_path = '/html/body/div[3]/div[1]/div/div[1]/ol/li[{}]/div/div[1]/em'
    title_path = '/html/body/div[3]/div[1]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[1]'
    rating_path = '/html/body/div[3]/div[1]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/div/span[2]'
    counting_path = '/html/body/div[3]/div[1]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/div/span[4]'
    comment_path = '/html/body/div[3]/div[1]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[2]/span'

    def __init__(self):
        self.q = Queue()
        self.headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
                }

    def run(self):
        self.get_one_page()

    def send_requests(self, url):
        html = requests.get(url, headers=self.headers).content
        return html

    def get_one_page(self):
        content = self.send_requests(self.url)
        html = etree.HTML(content)
        pp = 1
        while pp <= 25:
            r_path1 = self.rank_path.format(str(pp))
            n_path = self.title_path.format(str(pp))
            r_path2 = self.rating_path.format(str(pp))
            c_path1 = self.counting_path.format(str(pp))
            c_path2 = self.comment_path.format(str(pp))
            rank = html.xpath(r_path1)[0].text
            title = html.xpath(n_path)[0].text
            rating = html.xpath(r_path2)[0].text
            counting = html.xpath(c_path1)[0].text
            comment = html.xpath(c_path2)[0].text if html.xpath(c_path2) != [] else ''
            self.q.put(rank, title, rating, counting, comment)
            pp += 1

    def main(self):
        q = Queue()
        url0 = 'https://movie.douban.com/top250?start='
        url_list = [url0 + str(num) for num in range(0, 225 + 1, 25)]
        job_list = [gevent.spawn(self.run, url) for url in url_list]
        # 让线程等待所有任务完成，再继续执行。
        gevent.joinall(job_list)

        while not self.q.empty():
            print(self.q.get())


if __name__ == "__main__":
    start = time.time()
    d = GetTopMovies()
    d.main()
    print('[info]耗时：%s' % (time.time() - start))


