#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
from appium import webdriver
from work_appium.work2.pages.base_page import BasePage
from work_appium.work2.pages.main_page import MainPage


class App(BasePage):
    # 定义运行设备和app
    _desire_cap = {
            # 默认是Android
            "platformName": "android",
            # adb devices的sn名称
            "deviceName": "127.0.0.1:7555",
            # 包名
            "appPackage": "com.tencent.wework",
            # activity名字
            "appActivity": ".launch.WwMainActivity",
            # 指定自动化引擎
            "automationName": "uiautomator2",
            # 执行前后不初始化app数据
            "noReset": True
        }

    def start(self):
        if self.driver is None:
            # 运行appium，前提是要打开appium server
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self._desire_cap)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(3)
        return self

    def close(self):
        self.driver.quit()

    def main(self):
        return MainPage(self.driver)
