#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/22
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, baseDriver: WebDriver = None):
        self.driver = baseDriver

    def find(self, element):
        return self.driver.find_element(*element)

    def find_and_click(self, element):
        return self.find(element).click()

    def find_and_sendKeys(self, element, value):
        return self.find(element).send_keys(value)

    def scroll_and_click(self, text):
        return self.find((MobileBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector().\
            scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));')).click()

    def get_toast(self):
        return self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text

    def wait_until(self, time, method=None, element=None):
        if method is None:
            WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(element))
        else:
            WebDriverWait(self.driver, time).until(method)

    def wait_until_not(self, time, method=None, element=None):
        if method is None:
            WebDriverWait(self.driver, time).until_not(expected_conditions.element_to_be_clickable(element))
        else:
            WebDriverWait(self.driver, time).until_not(method)

    def back(self):
        self.driver.back()
