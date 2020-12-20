import requests
from lxml import etree
import time
from time import ctime, sleep
from threading import Thread
from queue import Queue
import re
from fake_useragent import UserAgent
import random

# //*[@id="content"]/div[2]/div[1]/div[2]/div[1]/div[2]/ul/li[1]/a
class GetTopMovies(Thread):

    title_path = '//*[@id="content"]/div[2]/div[1]/div[2]/div[{}]/div[2]/ul/li[1]/a/em'
    link_path = '//*[@id="content"]/div[2]/div[1]/div[2]/div[{}]/div[2]/ul/li[1]/a'

    def __init__(self, url, q):
        super(GetTopMovies, self).__init__()
        self.url = url
        self.q = q
        ua = UserAgent()
        self.headers = {
                    'User-Agent': ua.random
                }
        proxyIPs = ['http://113.207.44.70:3128', 'http://39.80.33.145:81',
                    'http://115.231.218.102:1080', 'http://113.107.166.245:1080',
                    'http://183.230.177.170:8081', 'http://123.57.254.211:8118']
        # 从代理池中随机取出一个IP
        proxyIP = random.choice(proxyIPs)
        self.proxies = {
            'http': proxyIP,
            'https': proxyIP
        }
    def run(self):
        self.get_one_page()

    def send_requests(self, url):
        jar = requests.cookies.RequestsCookieJar()
        jar.set('bid', 'ehjk9OLdwha', domain='.douban.com', path='/')
        jar.set('11', '25678', domain='.douban.com', path='/')

        html = requests.get(url, headers=self.headers, cookies=jar)
        print(html.text)
        return html.content

    def get_one_page(self):
        pattern = re.compile(
            '.*?href="(.*?)".*?',
            re.S
        )

        content = self.send_requests(self.url)
        html = etree.HTML(content)
        pp = 1
        while pp <= 15:
            n_path = self.title_path.format(str(pp))
            l_path = self.link_path.format(str(pp))

            title = html.xpath(n_path)[0].text
            link = html.xpath(l_path)[0]
            link = str(etree.tostring(link))
            link = re.findall(pattern, link)

            print(title, link)
            pp += 1


def main():
    q = Queue()
    url = 'https://movie.douban.com/people/170878516/wish?start=15'
    thread_list = []

    p = GetTopMovies(url, q)
    p.start()
    thread_list.append(p)

    # 让主线程等待子线程执行完成html.xpath(l_path)#[0].text
    for i in thread_list:
        i.join()

    while not q.empty():
        print(q.get())


if __name__ == "__main__":
    start = time.time()
    main()
    print('[info]耗时：%s' % (time.time() - start))


