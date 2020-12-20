import re
import requests
import csv

url1 = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,'
url2 = '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        }
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.content.decode("gbk")
        return None
    except RequestException:
        return None


def  parse_one_page(html):
        pattern = re.compile(
            '<p.*?t1.*?title="(.*?)".*?.html">(.*?)</a>.*?t3">(.*?)</span>.*?t4">(.*?)</span>.*?t5">(.*?)</span>',
            re.S
        )
        items = re.findall(pattern, html)
        print(items)

        with open('data.csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Job', '  Company', '  Location', '  Salary', '  Date'])
            for i in range(len(items)):
                job = items[i][0]
                company = items[i][1]
                location = items[i][2]
                salary = items[i][3]
                date = items[i][4]
                writer.writerow([job, company, location, salary, date])


if __name__ == '__main__':
    i = 1
    while i <= 736:
        url = url1 + str(i) + url2
        page = get_one_page(url)
        parse_one_page(page)
        i += 1
