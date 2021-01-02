#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from work_appium.work2.pages.base_page import BasePage
from work_appium.work2.pages.inviteMember_page import InviteMember
from work_appium.work2.pages.membeInfo_page import MemberInfo


class ContactPage(BasePage):
    _add_member_element = (MobileBy.XPATH, '//android.widget.TextView[@text="添加成员"]')

    def goto_inviteMember(self):
        # 点击'添加成员'
        self.find_and_click(self._add_member_element)
        # 进入'邀请成员'页面
        return InviteMember(self.driver)

    def goto_memberInfo(self, memberName):
        # 通讯录页面滚动查找并点击需要删除的成员"姓名"，跳转到'个人信息'页面
        self.scroll_and_click(memberName)
        return MemberInfo(self.driver)

    def check_no_member(self, memberName):
        # 删除成员成功校验
        try:
            self.wait_until_not(15, element=(MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().\
                scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{memberName}").instance(0));'))
            return True
        except TimeoutException:
            return False
