#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
from appium.webdriver.common.mobileby import MobileBy
from work_appium.work2.pages.base_page import BasePage
from work_appium.work2.pages.memberEdit_page import MemberEdit


class MemberSetting(BasePage):
    _member_edit_button = (MobileBy.XPATH, '//android.widget.TextView[@text="编辑成员"]')

    def goto_MemberEdit(self):
        # 点击'编辑成员',进入编辑成员页面
        self.find_and_click(self._member_edit_button)
        return MemberEdit(self.driver)
