#!/usr/bin/bin/env python
#_*_coding:utf-8_*_
#_author_:huangt
#_date_:
#_Use case specification_:

import time
from selenium import webdriver
import unittest

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_net_alter = True
    '''百度搜索selenium用例'''
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
# if __name__=='__FirstWebTest__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu('test_baidu_search'))
    print("用例运行完成")
