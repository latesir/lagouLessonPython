import selenium
from selenium import webdriver

class TestSelm():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.get("https://ceshiren.com/t/topic/58")
        self.driver.find_element_by_id("site-logo").click()
        self.driver.find_element_by_link_text("欢迎光临霍格沃兹测试学院").click()
        self.driver.find_element_by_link_text("爱测社区（ceshiren.com）").click()