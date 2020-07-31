# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from time import sleep
from ddt import ddt,data,unpack
from AnHui_Account.testcases.get_the_lpart import get_lpart_detail

class AnhuiNewCrossConnectBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_anhui_new_cross_connect_box(self):
        driver = self.driver
        #登录
        driver.get("http://192.168.0.2:10812/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"韩磊")
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")
        # driver.find_element_by_id("input-password").send_keys(Keys.ENTER)
        driver.find_element_by_id("a-login").click()
        #电缆及通道管理
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div/ul/li[3]/div").click()
        #电缆管理
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div/ul/li[3]/ul/li[2]").click()
        #运维检修部
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/span[2]/span").click()
        #输入线路名称
        sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("测试新增线路达1回线")
        sleep(1)
        #查询
        driver.find_element_by_xpath("//div[@id='search-all-part']/div/div/form/div[6]/div/button/span/i").click()
        #线路详情
        driver.find_element_by_xpath("//table/tbody/tr/td[12]/div/div/i").click()
        #电缆信息
        sleep(1)
        driver.find_element_by_xpath("//div[@id='line-container']/div[3]/div/div/ul/li[2]/p").click()
        #电缆详情
        driver.find_element_by_xpath("//table/tbody/tr/td[10]/div/p/i").click()
        sleep(1)
        #电缆段信息
        driver.find_element_by_xpath("//div[@id='line-container']/div[2]/div/div/ul/li[2]/p").click()
        sleep(1.5)
        #获取指定电缆段【详情】按钮的xpath定位
        LineID = "19b75799-faf2-4552-9562-e9c6e8268d0a"
        CableID = "acd9b32c-2063-4aed-b841-3b9aae2ba6f5"
        lpartname = "测试新增达1回线电缆电缆段"
        detail_xpath = get_lpart_detail(LineID,CableID,lpartname)
        #电缆段详情
        driver.find_element_by_xpath(detail_xpath).click()
        sleep(1)
        driver.find_element_by_xpath("//div[@id='line-container']/div[2]/div/div/ul/li[5]/p").click()
        driver.find_element_by_xpath("//div[@id='line-container']/div[2]/div/div/div/button/span/i").click()
        driver.find_element_by_xpath("(//input[@type='text'])[77]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[77]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[77]").send_keys(u"资产编号")
        driver.find_element_by_xpath("(//input[@type='text'])[78]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[78]").send_keys(u"设施名称")
        driver.find_element_by_xpath("(//input[@type='text'])[85]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[85]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[85]").send_keys("type")
        driver.find_element_by_xpath("(//input[@type='text'])[86]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[86]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[86]").send_keys(u"生产厂家")
        driver.find_element_by_xpath("(//input[@name=''])[20]").click()
        sleep(1)
        driver.find_element_by_xpath("//tr[6]/td[6]/div/span").click()
        driver.find_element_by_xpath("(//input[@type='text'])[88]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[88]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[88]").send_keys(u"出厂编号")
        driver.find_element_by_xpath("(//input[@name=''])[21]").click()
        driver.find_element_by_xpath("//div[5]/div/div/div[2]/table/tbody/tr[6]/td[6]/div/span").click()
        driver.find_element_by_xpath("(//input[@type='text'])[90]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[90]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[90]").send_keys(u"设施编号")
        driver.find_element_by_xpath("(//input[@name=''])[22]").click()
        sleep(1)
        driver.find_element_by_xpath("//div[6]/div/div/div[2]/table/tbody/tr[6]/td[6]/div/span").click()
        driver.find_element_by_xpath("(//input[@type='text'])[92]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[92]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[92]").send_keys(u"电压等级代码")
        driver.find_element_by_xpath("(//input[@type='text'])[93]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[93]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[93]").send_keys(u"设备类型编码")
        driver.find_element_by_xpath("(//input[@type='text'])[94]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[94]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[94]").send_keys("33")
        driver.find_element_by_xpath("(//input[@type='text'])[95]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[95]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[95]").send_keys("113")
        driver.find_element_by_xpath("(//input[@type='text'])[96]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[96]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[96]").send_keys(u"备注")
        driver.find_element_by_xpath("//div[3]/span/button[2]/span").click()
        sleep(2)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
