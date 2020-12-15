#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/13


from selenium.webdriver.common.by import By
from work_webAutoTest.work2.pages.base_page import BasePage
from work_webAutoTest.work2.pages.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self, name='harry', id=2020121401, phone=13912142101):
        self.find(By.XPATH, '//*[@id="username"]').send_keys(name)
        self.find(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(id)
        self.find(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(phone)
        self.find(By.LINK_TEXT, '保存').click()
        return ContactPage()
