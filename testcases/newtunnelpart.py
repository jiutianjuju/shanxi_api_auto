# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ddt
from ddt import ddt,data
from time import sleep

class Newtunnelpart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.driver.maximize_window()
        self.accept_next_alert = True
    # @data
    def test_newtunnelpart(self):
        """新建通道段"""
        driver = self.driver
        #登录
        driver.get("http://192.168.0.2:10812/#/login")
        driver.find_element_by_id("input-username").click()
        driver.find_element_by_id("input-username").clear()
        driver.find_element_by_id("input-username").send_keys(u"韩磊")
        driver.find_element_by_id("input-password").clear()
        driver.find_element_by_id("input-password").send_keys("admin123")
        driver.find_element_by_id("a-login").click()

        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div/ul/li[3]/div").click()
        driver.find_element_by_xpath("//div[@id='newMenuBox']/div/div/ul/li[3]/ul/li[3]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/span[2]/span").click()
        #输入通道名称查询
        sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(u"测试新增通道名称1")
        #点击查询
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        #点击通道详情
        driver.find_element_by_xpath("//div[@id='app']/div/div/div[2]/section/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/table/tbody/tr/td[12]/div/div/i").click()
        #通道段信息
        driver.find_element_by_xpath("//div[@id='line-container']/div[3]/div/div/ul/li[2]/p").click()
        #新建通道段
        driver.find_element_by_xpath("//div[@id='line-container']/div[3]/div/div/div/button/span").click()
        #通道段名称
        driver.find_element_by_xpath("(//input[@type='text'])[23]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[23]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[23]").send_keys(u"测试新增通道段1")
        #通道编号
        driver.find_element_by_xpath("(//input[@type='text'])[24]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[24]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[24]").send_keys("1")
        #敷设类型
        driver.find_element_by_xpath("(//input[@type='text'])[25]").click()
        #隧道
        driver.find_element_by_xpath("//div[4]/div/div/ul/li").click()
        #资产编号
        driver.find_element_by_xpath("(//input[@type='text'])[30]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[30]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[30]").send_keys(u"资产编号")
        #资产单位
        driver.find_element_by_xpath("(//input[@type='text'])[31]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[31]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[31]").send_keys(u"资产单位")
        #设备增加方式
        driver.find_element_by_xpath("(//input[@type='text'])[32]").click()
        #基本建设
        driver.find_element_by_xpath("//div[5]/div/div/ul/li/span").click()
        #投运日期
        driver.find_element_by_xpath("(//input[@name=''])[3]").click()
        driver.find_element_by_xpath("//tr[2]/td[4]/div/span").click()
        #档案名称
        driver.find_element_by_xpath("(//input[@type='text'])[36]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[36]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[36]").send_keys(u"档案名称")
        #起点位置
        driver.find_element_by_xpath("(//input[@type='text'])[37]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[37]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[37]").send_keys(u"起点位置")
        #终点位置
        driver.find_element_by_xpath("(//input[@type='text'])[38]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[38]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[38]").send_keys(u"终点位置")
        #悬挂方式
        driver.find_element_by_xpath("(//input[@type='text'])[40]").click()
        #支架
        driver.find_element_by_xpath("//div[7]/div/div/ul/li").click()
        #断面尺寸
        driver.find_element_by_xpath("(//input[@type='text'])[42]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[42]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[42]").send_keys("3*3")
        #通道段长度
        driver.find_element_by_xpath("(//input[@type='text'])[43]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[43]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[43]").send_keys("500")
        #井数量
        driver.find_element_by_xpath("(//input[@type='text'])[44]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[44]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[44]").send_keys("3")
        #施工单位
        driver.find_element_by_xpath("(//input[@type='text'])[45]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[45]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[45]").send_keys(u"施工单位")
        #竣工日期
        driver.find_element_by_xpath("(//input[@name=''])[4]").click()
        sleep(1)
        driver.find_element_by_xpath("//div[8]/div/div/div[2]/table/tbody/tr[6]/td[2]/div/span").click()
        #图纸编号
        driver.find_element_by_xpath("(//input[@type='text'])[47]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[47]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[47]").send_keys(u"图纸编号")
        #设备编码
        driver.find_element_by_xpath("(//input[@type='text'])[48]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[48]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[48]").send_keys(u"设备编码")
        #设备主人
        driver.find_element_by_xpath("(//input[@type='text'])[49]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[49]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[49]").send_keys(u"设备主人")
        #登记时间
        driver.find_element_by_xpath("(//input[@name=''])[5]").click()
        sleep(1)
        driver.find_element_by_xpath("//div[9]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[2]/div/span").click()
        #设备类型编码
        driver.find_element_by_xpath("(//input[@type='text'])[51]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[51]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[51]").send_keys(u"设备类型编码")
        #PM编码
        driver.find_element_by_xpath("(//input[@type='text'])[52]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[52]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[52]").send_keys(u"PM编码")
        #Sort No
        driver.find_element_by_xpath("(//input[@type='text'])[53]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[53]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[53]").send_keys("1")
        #子站ID
        driver.find_element_by_xpath("(//input[@type='text'])[54]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[54]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[54]").send_keys("1")
        #重要程度
        driver.find_element_by_xpath("(//input[@type='text'])[56]").click()
        driver.find_element_by_xpath("//div[10]/div/div/ul/li").click()
        #备注
        driver.find_element_by_xpath("(//input[@type='text'])[57]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[57]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[57]").send_keys(u"备注")
        #确定
        sleep(1)
        driver.find_element_by_xpath("//span/button[2]/span").click()
        time.sleep(2)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
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
