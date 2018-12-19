#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
from bs4 import BeautifulSoup

__date__ = '2018/12/19 9:59'
__author__ = 'likunkun'

import requests
url = 'https://book.douban.com/latest'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400"
}
data = requests.get(url, headers=headers)
# print(data.text)

soup = BeautifulSoup(data.text, "html.parser")
# print(soup)

# 网页上的书籍按左右两边分布，按照标签分别提取
books_left = soup.find('ul', {'class': 'cover-col-4 clearfix'})
books_left = books_left.find_all("li")
books_right = soup.find('ul', {'class': 'cover-col-4 pl20 clearfix'})
books_right = books_right.find_all('li')

books = list(books_left) + list(books_right)