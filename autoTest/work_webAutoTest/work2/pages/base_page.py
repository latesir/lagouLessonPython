#!/usr/bin/env python
# -- coding:utf-8 --
# Author: latesir
# Date: 2020/12/13

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 定义BasePage
class BasePage:
    # 定义init方法，参数名baseDriver，参数类型为WebDriver实例，默认值None
    def __init__(self, baseDriver: WebDriver = None):
        # 声明私有变量base_url，默认空值
        _base_url = ""
        # 变量baseDriver为None时，则创建debug属性的chromeWebDriver
        if baseDriver is None:
            # 创建chromeWebDriver的Options实例option
            self.option = Options()
            # 设置option的调试地址和端口为"localhost:9222"
            self.option.debugger_address = "localhost:9222"
            # 创建chromeWebDriver实例driver，并将option配置赋值给driver
            self.driver = webdriver.Chrome(options=self.option)
            # 设置driver的隐式等待时长为5s
            self.driver.implicitly_wait(5)
        # 如果base_url有值，则访问对应url
        if _base_url != "":
            # 访问base_url对应的网页
            self.driver.get(_base_url)

    # 封装driver.find_element方法，by为元素定位方式，value为元素定位表达式
    def find(self, by, value):
        # 返回元素(by, value)
        return self.driver.find_element(by, value)

    # 封装driver.find_elements方法，by为元素定位方式，value为元素定位表达式
    def finds(self, by, value):
        # 返回满足定位条件的元素列表
        return self.driver.find_elements(by, value)

    # 封装显示等待方法，需传元素实例，默认等待10s
    def wait(self, element, waitTime=10):
        # 显示等待直到element可见或超时报错
        WebDriverWait(self.driver, waitTime).until(expected_conditions.visibility_of_element_located(element))
