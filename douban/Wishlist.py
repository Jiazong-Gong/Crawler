import requests
from lxml import etree
import time
from time import ctime, sleep
from threading import Thread
from queue import Queue


class GetTopMovies(Thread):

    title_path = '//*[@id="content"]/div[2]/div[1]/div[2]/div[{}]/div[2]/ul/li[1]/a/em'
    link_path = '//*[@id="content"]/div[2]/div[1]/div[2]/div[{}]/div[2]/ul/li[1]/a'

    def __init__(self, url, q):
        super(GetTopMovies, self).__init__()
        self.url = url
        self.q = q
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
        while pp <= 15:
            n_path = self.title_path.format(str(pp))
            l_path = self.link_path.format(str(pp))

            title = html.xpath(n_path)#[0].text
            link = html.xpath(l_path)#[0].text
            print(title, link)
            pp += 1


def main():
    q = Queue()
    url0 = 'https://movie.douban.com/people/170878516/wish?start='
    url_list = [url0 + str(num) for num in range(0, 195 + 1, 15)]
    # print(len(url_list))
    thread_list = []
    for url in url_list:
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


