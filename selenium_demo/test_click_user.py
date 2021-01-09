from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import json,pytest

class TestWeixin():
    def setup_method(self):
        self.driver = webdriver.Chrome()
    # def teardown_method(self):
    #     self.driver.quit()

    def test_testbaidu(self):
        self.driver.get('https://work.weixin.qq.com/')
        with open('cookie.json','r') as r:
            cookies = json.load(r)
        #注入cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.XPATH,"//*[@id='menu_customer']").click()
        sleep(5)
        self.driver.close()



