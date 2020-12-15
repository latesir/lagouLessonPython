"""
分别使用浏览器复用和cookie登录企业微信。
将所有的死等都封装成显式等待
"""
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWechatLogin():
    def test_debug_login(self):
        self.option = Options()
        self.option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'menu_index')))

    def test_get_cookies(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((By.ID, 'menu_index')))
        with open('wxCookies.json', 'w') as f:
            json.dump(self.driver.get_cookies(), f)
        self.driver.quit()

    def test_cookie_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open('wxCookies.json', 'r') as f:
            cookieList = json.load(f)
            for cookie in cookieList:
                self.driver.add_cookie(cookie)
        while True:
            self.driver.refresh()
            if WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, 'menu_index'))):
                break
        self.driver.quit()
