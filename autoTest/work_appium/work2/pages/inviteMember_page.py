#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
from appium.webdriver.common.mobileby import MobileBy
from work_appium.work2.pages.addMember_page import AddMember
from work_appium.work2.pages.base_page import BasePage


class InviteMember(BasePage):
    _enter_by_hand_element = (MobileBy.XPATH, '//android.widget.TextView[@text="手动输入添加"]')

    def goto_addMember(self):
        # '邀请成员'页面点击'手动输入添加'
        self.find_and_click(self._enter_by_hand_element)
        # 进入'成员信息录入'页面
        return AddMember(self.driver)
