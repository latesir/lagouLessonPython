#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
from appium.webdriver.common.mobileby import MobileBy
from work_appium.work2.pages.base_page import BasePage
from work_appium.work2.pages.memberSetting_page import MemberSetting


class MemberInfo(BasePage):
    _more_operation_button = (MobileBy.ID, 'com.tencent.wework:id/ice')

    def goto_memberSetting(self):
        # 点击右上角进入更多操作页
        self.find_and_click(self._more_operation_button)
        return MemberSetting(self.driver)
