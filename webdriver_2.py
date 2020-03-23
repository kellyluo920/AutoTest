#!/user/bin/env python
# coding:utf-8

import time
from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(10)


# 通过 webelement 对象选择元素
'''wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
element = wd.find_element_by_id('container')
spans = element.find_elements_by_tag_name('span')
for span in spans:
    print(span.text)'''

wd.get('http://www.baidu.com')
element = wd.find_element_by_id('kw')

element.send_keys('白月黑羽\n')
# id为1的元素，就是第一个搜索结果

# 意外情况下不实用，如1.1s/网络问题
'''time.sleep(1)'''

element = wd.find_element_by_id('1')
print(element.text)

