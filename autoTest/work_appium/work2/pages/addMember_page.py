#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from work_appium.work2.pages.base_page import BasePage


class AddMember(BasePage):
    _name_input_element = (By.XPATH, '//android.widget.TextView[@text="姓名　"]/../android.widget.EditText')
    _phoneNum_input_element = (By.XPATH, '//android.widget.TextView[@text="手机　"]/..//android.widget.EditText')
    _male_element = (By.XPATH, '//android.widget.TextView[@text="男"]')
    _female_element = (By.XPATH, '//android.widget.TextView[@text="女"]')
    _save_button = (By.XPATH, '//android.widget.TextView[@text="保存"]')

    def enter_name(self, name):
        # 录入姓名
        self.find_and_sendKeys(self._name_input_element, name)
        return self

    def enter_phoneNum(self, phoneNum):
        # 录入手机号
        self.find_and_sendKeys(self._phoneNum_input_element, phoneNum)
        return self

    def choose_sex(self, sex):
        # 点击性别选择栏
        self.find_and_click(self._male_element)
        if sex == '男':
            self.wait_until(5, element=self._male_element)
            # 选择'男'
            self.find_and_click(self._male_element)
        elif sex == '女':
            self.wait_until(5, element=self._female_element)
            # 选择'女'
            self.find_and_click(self._female_element)
        else:
            raise Exception('预置数据的性别有误，请核查')
        return self

    def click_save(self):
        # 点击'保存'按钮
        self.find_and_click(self._save_button)
        # 返回toast提示语
        return self.get_toast()
