#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.mobileby import MobileBy
from work_appium.work2.pages.base_page import BasePage
from work_appium.work2.pages.contact_page import ContactPage


class MainPage(BasePage):
    _contact_element = (MobileBy.XPATH, '//android.widget.TextView[@text="通讯录"]')

    def goto_contact(self):
        # 主页面点击'通讯录'
        self.find_and_click(self._contact_element)
        return ContactPage(self.driver)

    def back_to_main(self):
        # 定义回退方法
        def check_and_back(a):
            try:
                return self.find(self._contact_element)
            except NoSuchElementException:
                self.back()
                return False
        # 显示等待回退到主页面
        self.wait_until(15, check_and_back)
        return self
