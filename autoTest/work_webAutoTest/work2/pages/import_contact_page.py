#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/13


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from work_webAutoTest.work2.pages.base_page import BasePage
from work_webAutoTest.work2.pages.contact_page import ContactPage


class ImportContactPage(BasePage):

    def import_contact(self, filePath=None):
        if filePath is None:
            filePath = 'E:/Hogwarts/python/projectSpace/autoTest/work_webAutoTest/work2/testData/通讯录批量导入模板.xlsx'
        self.find(By.XPATH, '//*[@class="ww_fileImporter_fileContainer_uploadInputMask"]').send_keys(
            filePath)
        self.find(By.LINK_TEXT, '导入').click()
        self.wait((By.LINK_TEXT, '完成'), 15)
        self.find(By.LINK_TEXT, '完成').click()
        return ContactPage()
