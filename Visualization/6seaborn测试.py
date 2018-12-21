#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/20 14:25'
__author__ = 'likunkun'

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 密度估计图
# x = np.random.normal(0,1,100)
# y = np.random.normal(1,2,100)
#
# sns.kdeplot(x)
# sns.kdeplot(y)
# plt.show()

# 分类数据频数分布
# tips = sns.load_dataset('tips')
# plt.subplots(121)
# sns.countplot('day', data=tips)
# plt.subplots(122)
# sns.countplot('sex', data=tips)
# plt.show()

# 自动拟合数据
# tips = sns.load_dataset('tips')
# sns.lmplot(x='total_bill', y='tip', hue='day', data=tips, fit_reg=True)
# plt.show()

# 小提琴图
# tips = sns.load_dataset('tips')
# # sns.violinplot(x='day', y='tip', data=tips)
# sns.boxplot(x='day', y='tip', data=tips)    # 箱线图
# plt.show()

# 进行各变量之间的对比
tips = sns.load_dataset('tips')
sns.factorplot('day', 'total_bill', 'sex', data=tips,kind='violin')
ax = sns.countplot('day', 'total_bill', 'sex', data=tips)
plt.show()

