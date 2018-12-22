#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/20 14:53'
__author__ = 'likunkun'

import re
import  datetime
import seaborn as sns
import matplotlib .pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread

# import matplotlib as mpl
# mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
# mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams['axes.unicode_minus'] = False

# 数据提取
def get_data(data):
    # 日期
    dates = re.findall(r'\d{4}-\d{2}-\d{2}', data)
    # 天
    days = [date[-2:] for date in dates]
    plt.subplot(221)
    sns.countplot(days)
    # plt.title('日期')
    plt.title('day')

    # 周几
    weekdays = [datetime.date(int(date[:4]),int(date[5:7]),int(date[-2:])).isocalendar()[-1]for date in dates]
    plt.subplot(222)
    sns.countplot(weekdays)
    plt.title('周')
    plt.title('weekdays')

def get_time(data):
    times = re.findall(r'\d{2}:\d{2}:\d{2}',data)
    # 小时
    print(times)
    hours = [time[:2] for time in times]
    plt.subplot(223)
    sns.countplot(hours,order=['6','7','8','9','10','11','12','13'
        ,'14','15','16','17','18','19','20','21','22','23','00'
        ,'1','2','3','4','5'])

    # plt.title('小时')
    plt.title('hours')

# 词云
def get_wordclound(text_data):
    word_list = [" ".join(jieba.cut(sentence)) for sentence in text_data]
    new_text = ' '.join(word_list)

    pic_path = "QQQ.jpg"
    mang_mask = imread(pic_path)
    plt.subplot(224)
    wordcloud = WordCloud(background_color="white",
                          font_path = '/home/shen/Downloads/fonts/msyh.ttc',  #中文字体的路径
                          mask = mang_mask, stopwords=STOPWORDS).generate(new_text)
    plt.imshow(wordcloud)
    plt.axis('off')

# 内容及词云
def get_content(data):
    pa = re.compile(r'\d{4}-\d{2}-\d{2}.*?\(\d+\)\n(.*?)\n\n', re.DOTALL)
    content = re.findall(pa,data)
    get_wordclound(content)

#最后定义一个run函数实现整个流程
def run():
    filename = '假装正经的科技协会.txt'
    with open(filename,encoding='utf-8') as f:
        data = f.read()

    get_data(data)
    get_time(data)
    get_content(data)
    plt.show()

run()
