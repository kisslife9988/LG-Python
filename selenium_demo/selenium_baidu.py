
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestTestbaidu():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
    def teardown_method(self):
        self.driver.quit()

    def test_testbaidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID,'kw').send_keys('python')
        self.driver.find_element(By.ID,'kw').send_keys(Keys.ENTER)
        sleep(5)
        self.driver.close()