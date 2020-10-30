# from selenium.webdriver.support.ui import WebDriverWait
# import time
# import unittest
# import os
# from appium import webdriver
# #from .appium_config import appium_start
# #import uiautomator2 as u2
# # noinspection PyUnresolvedReferences
# from selenium.common.exceptions import NoSuchElementException
# class test01(unittest.TestCase):
#     def setUp(self) :
#         desired_caps={'platformName':'Android',
#                       'platformVersion':'7.7.1',
#                       'deviceName':'605SH',
#                       'appPackage':'com.mildom.android',
#                       'appActivity':'com.nono.android.modules.main.MainActivity',
#                       'autoGrantPermissions':True,
#                       'noReset':True,
#                       'automationName':"UiAutomator2"
#                                     }
#         self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#         self.driver.implicitly_wait(8)  # 全局隐式等待8s
#
#         def login(self):
#             driver = self.driver
#             time.sleep(10)
#             driver.find_element_by_xpath('//*[@resource-id="com.mildom.android:id/fl_right_one"]').click()
#             time.sleep(2)
#         def tearDown(self):
#             self.driver.quit()
#
# if __name__ == "__main__":
#         unittest.main(verbosity=2)
import unittest
from lib2to3.pgen2 import driver

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests
# s = requests.session()
# s.keep_alive = False
#初始化信息
def window_alert(driver):   #判断是否有评价弹窗
    try:
        driver.find_element_by_xpath('d(resourceId="com.mildom.android:id/iv_rate_close")')
        driver.find_element_by_xpath('d(resourceId="com.mildom.android:id/iv_rate_close")').click()
    except:
        pass
class mytest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="7.7.1"
        desired_caps["deviceName"]="605SH"
        desired_caps["appPackage"]="com.mildom.android"
        desired_caps["appActivity"]="com.nono.android.modules.splash.SplashActivity"
        desired_caps["autoGrantPermissions"]="True"
        desired_caps["noReset"]  ="True"
        desired_caps["automationName"]= "UiAutomator2"
        # unicode编码方式发送字符串
        desired_caps["unicodeKeyboard"] = "True"
        # resetKeyboard是将键盘隐藏起来
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(8) #隐式等待
    def test_login(self):
        driver=self.driver
        window_alert(driver)
        driver.find_element_by_xpath('//*[@resource-id="com.mildom.android:id/fl_right_one"]').click()
        time.sleep(3)
        try:#判断是否已登录
            driver.find_element_by_xpath('//*[@resource-id="com.mildom.android:id/iv_me_v2_user_head"]')
            driver.find_element_by_xpath('//*[@resource-id="com.mildom.android:id/back_btn"]').click()
            print("已登录")
        except:
            driver.find_element_by_xpath('//*[@resource-id="com.mildom.android:id/btn_me_login"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@resource-id="com.mildom.android:id/rl_phone"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@resource-id="com.mildom.android:id/et_phone_input"]').send_keys('1234567890')
            driver.find_element_by_xpath('//*[@resource-id="com.mildom.android:id/tv_next"]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@resource-id="com.mildom.android:id/et_password_input"]').send_keys('123456')
            driver.find_element_by_xpath('//*[@resource-id="com.mildom.android:id/tv_next"]').click()
            time.sleep(3)
            print("登录成功")
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main(verbosity=2)

