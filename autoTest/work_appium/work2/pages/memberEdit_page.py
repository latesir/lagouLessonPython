#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
from appium.webdriver.common.mobileby import MobileBy
from work_appium.work2.pages.base_page import BasePage


class MemberEdit(BasePage):
    _del_member_button = (MobileBy.XPATH, '//android.widget.TextView[@text="删除成员"]')
    _confirm_button = (MobileBy.XPATH, '//android.widget.TextView[@text="确定"]')

    def click_delMember(self):
        # 点击'删除成员'
        self.find_and_click(self._del_member_button)
        return self

    def click_confirmButton(self):
        # 二次确认弹框点击'确定'
        self.find_and_click(self._confirm_button)
        from work_appium.work2.pages.contact_page import ContactPage
        return ContactPage(self.driver)
