#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/19 16:59'
__author__ = 'likunkun'


from tkinter import *

root = Tk()
text = Text(root, width = 30 , height = 10)
text.pack()
text.insert(INSERT, 'I LOVE YOU')

'''Indexes用来指向Text组件文本的位置'''
# （1）行.列：注意行是1开始，列是0开始
print(text.get('1.2', 1.6))  # 可以用浮点代替字符串
# （2）line.end某行末尾
print(text.get('1.2', '1.end'))
# （3）INSERT对应插入光标的位置
# （4）CURRENT对应与鼠标坐标最接近的位置，如果按住鼠标，会等松开才响应
# （5）END文本缓冲区的最后一个字符的下一个位置
# （6）user-defined marks自定义位置
# （7）User-defined tags可以分配给text组件的特殊事件绑定和风格
# （8）selection（SEL_FIRST，SEL_LAST）当前被选中的范围
# （9）window coordinate（"@x，y"）
# （10）embedded object name（window， images）用于指向在text组件中放入的window和image对象。
# （11）expressions修改任何格式的索引