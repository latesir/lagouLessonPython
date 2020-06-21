import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWeixin:
    # def test_debugging(self):
    #     self.option=Options()
    #     self.option.debugger_address='localhost:9222'
    #     self.driver=webdriver.Chrome(options=self.option)
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame#voipMeeting')

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')

    # def teardown(self):
    #     self.driver.quit()

    # def test_wx_login(self):
    #     time.sleep(15)
    #     myCookie = self.driver.get_cookies()
    #     with open('./wxCookies.json', 'w') as f:
    #         json.dump(myCookie, f)

    def test_wx_login(self):
        with open('./wxCookies.json', 'r') as f:
            cookies=json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            # self.driver.refresh()
            while True:
                self.driver.refresh()
                aa=WebDriverWait(self.driver, 2).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="menu_contacts"]/span1')))
                print(f'aa value is {aa}')
                if aa is not None:
                    break
            self.driver.find_element(By.XPATH,'//*[@id="menu_contacts"]/span').click()
            # time.sleep(200)