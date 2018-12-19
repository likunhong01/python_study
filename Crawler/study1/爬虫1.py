#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/11/16 10:51'
__author__ = 'likunkun'

import requests
import pandas as pd
from bs4 import BeautifulSoup

#请求数据
def get_data():
    url = 'https://book.douban.com/latest'
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6784.400 QQBrowser/10.3.2667.400"
    }
    data = requests.get(url, headers=headers)
    return data


# 解析数据
def parse_data(data):
    soup = BeautifulSoup(data.text, 'html.parser')

    #网页上的书籍按左右两边分布，按照标签分别提取
    books_left = soup.find('ul', {'class': 'cover-col-4 clearfix'})
    books_left = books_left.find_all("li")
    books_right = soup.find('ul', {'class': 'cover-col-4 pl20 clearfix'})
    books_right = books_right.find_all('li')

    books = list(books_left) + list(books_right)

    # 每个图书
    img_urls = []
    titles = []
    ratings = []
    authors = []
    details = []
    for book in books:
        # 图书封面url地址
        img_url = book.find_all('a')[0].find('img').get('src')
        img_urls.append(img_url)

        #图书标题
        title = book.find_all('a')[1].get_text()
        titles.append(title)

        #评价星级
        rating = book.find('p', {'class':'rating'}).get_text()
        # print(rating)
        rating = rating.replace('\n','').replace(" ", "")
        ratings.append(rating)
        # print('xingji：'+rating)

        #作者和出版信息
        author = book.find('p', {'class':'color-gray'}).get_text()
        # print(type(author))
        author = author.replace('\n','').replace(' ', '')
        authors.append(author)

        #图书简介
        detail = book.find_all('p')[2].get_text()
        detail = detail.replace('\n', '').replace(' ', '')
        details.append(detail)


    print('图片URL:', img_urls)
    print('标题：', titles)
    print('评价星级：', ratings)
    print('作者', authors)
    print('简介', details)
    return img_urls,titles, ratings, authors, details

# 存储数据
def save_data(img_urls, titles, ratings, authors, details):
    result = pd.DataFrame()

    result['img_urls'] = img_urls
    result['titles'] = titles
    result['ratings'] = ratings
    result['authors'] = authors
    result['details'] = details

# 开始爬数据
def run():
    data = get_data()
    img_urls, titles, ratings, authors, details = parse_data(data)
    save_data(img_urls, titles, ratings, authors, details)

run()
