# coding=utf-8
from selenium import webdriver

# 创建 webdeiver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()
wd.get('http://www.baidu.com')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element_by_id('kw')

# 通过该 element 对象，就可以对页面元素进行操作
# 比如输入字符串到 这个输入框里
# 方法一：element.send_keys('白月黑羽\n')
# 方法二：将'百度一下'作为一个元素，进行元素点击操作
element.send_keys('白月黑羽')
element = wd.find_element_by_id('su')
element.click()


pass