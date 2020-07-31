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

        driver.find_element_by_xpath(detail_xpath).click() #电缆段列表
        #终端
        sleep(1.5)
        driver.find_element_by_xpath("//div[@id='line-container']/div[2]/div/div/ul/li[4]").click()  #
        #添加
        driver.find_element_by_xpath("//div[@id='line-container']/div[2]/div/div/div/button/span").click()
        #资产编号
        driver.find_element_by_xpath("(//input[@type='text'])[77]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[77]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[77]").send_keys(u"资产编号")
        #设施名称
        driver.find_element_by_xpath("(//input[@type='text'])[78]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[78]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[78]").send_keys(u"终端1")
        #连接设施
        driver.find_element_by_xpath("(//input[@type='text'])[88]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[88]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[88]").send_keys(u"连接设施")
        #投运日期
        driver.find_element_by_xpath("(//input[@name=''])[20]").click()
        sleep(1)
        driver.find_element_by_xpath("//tr[5]/td[6]/div/span").click()
        #监理单位
        driver.find_element_by_xpath("(//input[@type='text'])[90]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[90]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[90]").send_keys(u"监理单位")
        #设备型号
        driver.find_element_by_xpath("(//input[@type='text'])[94]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[94]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[94]").send_keys("type")
        #生产厂家
        driver.find_element_by_xpath("(//input[@type='text'])[95]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[95]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[95]").send_keys(u"生产厂家")
        #出厂日期
        driver.find_element_by_xpath("(//input[@name=''])[21]").click()
        sleep(1)
        driver.find_element_by_xpath("//div[5]/div/div/div[2]/table/tbody/tr[6]/td[6]/div/span").click()
        #出厂编号
        driver.find_element_by_xpath("(//input[@type='text'])[97]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[97]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[97]").send_keys(u"出厂编号")
        #终端类型
        driver.find_element_by_xpath("(//input[@type='text'])[99]").click()
        sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
        # #制作工艺
        # driver.find_element_by_xpath("(//input[@type='text'])[100]").click()
        # sleep(0.5)
        # driver.find_element_by_xpath("/html/body/div[6]/div[1]/div/ul/li[2]").click()
        #制作单位
        driver.find_element_by_xpath("(//input[@type='text'])[101]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[101]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[101]").send_keys(u"制作单位")
        #制作人
        driver.find_element_by_xpath("(//input[@type='text'])[102]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[102]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[102]").send_keys(u"制作人")
        #设施编号
        driver.find_element_by_xpath("(//input[@type='text'])[103]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[103]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[103]").send_keys(u"设施编号")
        #登记时间
        driver.find_element_by_xpath("(//input[@name=''])[22]").click()
        sleep(5)
        driver.find_element_by_xpath("//div[7]/div/div/div[2]/table/tbody/tr[6]/td[6]/div/span").click()
        #电压等级代码
        driver.find_element_by_xpath("(//input[@type='text'])[105]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[105]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[105]").send_keys(u"电压等级代码")
        #设施类型编码
        driver.find_element_by_xpath("(//input[@type='text'])[106]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[106]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[106]").send_keys(u"设施类型编码")
        #纬度
        driver.find_element_by_xpath("(//input[@type='text'])[107]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[107]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[107]").send_keys("33")
        #经度
        driver.find_element_by_xpath("(//input[@type='text'])[108]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[108]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[108]").send_keys("113")
        #备注
        driver.find_element_by_xpath("(//input[@type='text'])[109]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[109]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[109]").send_keys(u"备注")
        #确定
        driver.find_element_by_xpath("//div[3]/span/button[2]/span").click()
        sleep(2)



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
