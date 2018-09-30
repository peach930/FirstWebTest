#!/usr/bin/bin/env python
#_*_coding:utf-8_*_
#_author_:huangt
#_date_:
#_Use case specification_:

# reload(__import__('sys')).setdefaultencoding('utf-8')
import time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import unittest

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_net_alter = True

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
    # HtmlFile = "D:\\PycharmProjects\\FirstWebTest\\report\\result.html"
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    HtmlFile = r'.\report\ ' + now + 'result.html'
    fp = open(HtmlFile,'wb')
    runner = HTMLTestRunner(stream=fp, title=u'OpenBaiDu_Auto_cases', description=u'用例执行情况：')
    runner.run(testunit)
    fp.close()
