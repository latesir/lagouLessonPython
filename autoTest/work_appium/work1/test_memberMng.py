#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWechat:
    def setup_class(self):
        # 设置caps的值  1
        self.desire_cap = {
            # 默认是Android
            "platformName": "android",
            # adb devices的sn名称
            "deviceName": "127.0.0.1:7555",
            # 包名
            "appPackage": "com.tencent.wework",
            # activity名字
            "appActivity": ".launch.WwMainActivity",
            # # 指定自动化引擎
            "automationName": "uiautomator2",
            # 执行前后不初始化app数据
            "noReset": True
        }
        # 运行appium，前提是要打开appium server
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_cap)
        self.driver.implicitly_wait(3)
        # 点击主页上"通讯录"，跳转到通讯录页面
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="通讯录"]').click()

    def teardown_class(self):
        self.driver.quit()

    def teardown(self):
        WebDriverWait(self.driver, 15).until(self.back_to_contact)

    def back_to_contact(self, a):
        try:
            return self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="通讯录"]')
        except NoSuchElementException:
            self.driver.back()
            return False

    @pytest.mark.parametrize("name, phone, sex", yaml.safe_load(open("./testData.yaml", encoding="utf-8"))['addMember'])
    def test_addMember(self, name, phone, sex):
        # 通讯录页面滚动查找并点击"添加成员"，跳转到添加页面
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance('
                                                        '0)).scrollIntoView(new UiSelector().text("添加成员").instance('
                                                        '0));').click()
        # 添加页面选择"手动输入添加"，调整到成员信息录入页面
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="手动输入添加"]').click()
        # 成员信息录入页面，录入'姓名'
        self.driver.find_element(By.XPATH,
                                 '//android.widget.TextView[@text="姓名　"]/../android.widget.EditText').send_keys(name)
        # 成员信息录入页面，录入'手机'
        self.driver.find_element(By.XPATH,
                                 '//android.widget.TextView[@text="手机　"]/..//android.widget.EditText').send_keys(
            phone)
        # 成员信息录入页面，录入'性别'
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="男"]').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, f'//android.widget.TextView[@text="{sex}"]')))
        self.driver.find_element(By.XPATH, f'//android.widget.TextView[@text="{sex}"]').click()
        # 成员信息录入页面，点击'保存'
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="保存"]').click()
        # 添加成员成功toast校验
        assert '添加成功' == self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text

    @pytest.mark.parametrize("name", yaml.safe_load(open("./testData.yaml", encoding="utf-8"))['delMember'])
    def test_delMember(self, name):
        # 通讯录页面滚动查找并点击需要删除的成员"姓名"，跳转到'个人信息'页面
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView\
            (new UiSelector().text("{name}").instance(0));').click()
        # 点击右上角进入更多操作页
        self.driver.find_element(By.ID, 'com.tencent.wework:id/ice').click()
        # 点击'编辑成员',进入编辑成员页面
        self.driver.find_element(By.XPATH,
                                 '//android.widget.TextView[@text="编辑成员"]').click()
        # 点击'删除成员'
        self.driver.find_element(By.XPATH,
                                 '//android.widget.TextView[@text="删除成员"]').click()
        # 二次确认弹框点击'确定'
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="确定"]').click()
        # 删除成员成功校验
        WebDriverWait(self.driver, 10).until_not(expected_conditions.element_to_be_clickable(
            (By.XPATH, f'//android.widget.TextView[@text="{name}"]')))
