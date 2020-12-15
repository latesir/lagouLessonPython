#!/usr/bin/env python
#-- coding:utf-8 --
# Author: latesir
# Date: 2020/12/13
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from work_webAutoTest.work2.pages.add_member_page import AddMemberPage
from work_webAutoTest.work2.pages.base_page import BasePage
from work_webAutoTest.work2.pages.contact_page import ContactPage
from work_webAutoTest.work2.pages.import_contact_page import ImportContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact(self):
        self.find(By.XPATH, '//*[@id="menu_contacts"]').click()
        return ContactPage()

    def goto_add_member(self):
        self.find(By.LINK_TEXT, '添加成员').click()
        return AddMemberPage()

    def goto_import_contact(self):
        self.find(By.LINK_TEXT, '导入通讯录').click()
        return ImportContactPage()

    def return_mainPage(self):
        self.find(By.XPATH, '//*[@id="menu_index"]').click()