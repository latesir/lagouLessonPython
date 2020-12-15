#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/13


from selenium.webdriver.common.by import By
from work_webAutoTest.work2.pages.base_page import BasePage


class ContactPage(BasePage):

    def del_member(self):
        self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[1]')[0].click()
        self.finds(By.XPATH, '//*[@class="qui_btn ww_btn js_delete"]')[0].click()
        self.find(By.XPATH, '//*[@class="qui_btn ww_btn ww_btn_Blue"]').click()
        return ContactPage()

    def get_members(self):
        memberList1 = self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[2]')
        memberList2 = self.finds(By.XPATH, '//*[@class="js_unsortable js_list"]/tr/td[2]')
        memberList = memberList1 + memberList2
        return [e.get_attribute('title') for e in memberList]
