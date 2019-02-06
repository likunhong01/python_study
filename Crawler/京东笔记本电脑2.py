#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/2/6 22:32'
__author__ = 'likunkun'

from bs4 import BeautifulSoup

import requests

#请求数据
def get_data():
    url = 'https://search.jd.com/Search?keyword=笔记本电脑&enc=utf-8&wq=笔记本电脑&pvid=296a4ac7f45d420da0e00b3813ba900b'
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400"
    }
    data = requests.get(url, headers=headers)
    return data


# 解析数据
'''
图片img、价格price、名称name、评价commit、店铺shop
'''
def parse_data(data):
    soup = BeautifulSoup(data.text, 'html.parser')

    #网页上的书籍按左右两边分布，按照标签分别提取
    computer = soup.find('ul', {'class': 'gl-warp clearfix'})
    computer = computer.find_all("li")

    img_urls = []
    prices = []
    names = []
    commits = []
    shops = []

    computers = list(computer)

    for computeri in computers:
        img_url = computeri.find_all('a')[0].get('href')
        print(img_url)

        price = computeri.find_all('i')[0].get_text()
        print(price)

        name = computeri.find_all('em')[0].get_text()
        print(name)


def run():
    data = get_data()
    parse_data(data)

run()

