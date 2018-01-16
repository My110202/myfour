# -*- coding: UTF-8 -*-
print '--------------------------------------------------'
var1='hello world'
print var1
print '更新字符串：',var1[:6]+'wang'

print '--------------------------------------------------'
# 字符串格式化
print "My name is %s and weight is %d kg!" % ('wanggang', 21)

print '--------------------------------------------------'
str='mAYUE'
print str.capitalize()              # capitalize将第一个字母大写，其他的字母小写

print '--------------------------------------------------'
str='good you are very good'
print '字母o的个数：',str.count('o')

print '--------------------------------------------------'
# 编码与解码
str = "this is string example....wow!!!";
str = str.encode('base64','strict');

print "Encoded String: " + str;
print "Decoded String: " + str.decode('base64','strict')

print '--------------------------------------------------'
# tab默认数字是8     expandtabs()扩充标签
str = "this is\tstring example....wow!!!"
print "Original string: " + str
print "Defualt exapanded tab: " +  str.expandtabs()
print "Double exapanded tab: " +  str.expandtabs(16)  # tab空格设置为16个

print '--------------------------------------------------'
# format函数  格式化字符串
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list)) # "0" 是必须的

print '--------------------------------------------------'
# Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
str = "-"
seq = ("ma", "yue", "ok") # 字符串序列
print str.join( seq )

print '--------------------------------------------------'
# 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
str = "this is string example....wow!!!"
print str.ljust(20, '1')

print '--------------------------------------------------'
# partition(str) 方法用来根据指定的分隔符将字符串进行分割,如果字符串包含指定的分隔符，则返回一个3元的元组，
# 第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。str为指定分隔符
str = "http://www.w3cschool.cc/"
print str.partition("://")

print '--------------------------------------------------'
# Python maketrans() 方法用于创建字符映射的转换表
from string import maketrans   # 必须调用 maketrans 函数。
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!"
print str.translate(trantab)
print str.translate(trantab,'xm')    # 去除字符串中的xm

print '--------------------------------------------------'
# swapcase()大小写字母转换 swap交换
str = "this is string example....wow!!!";
print str.swapcase();
str = "THIS IS STRING EXAMPLE....WOW!!!";
print str.swapcase();


