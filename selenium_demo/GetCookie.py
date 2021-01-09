import time,json
from selenium import webdriver
from selenium.webdriver.common.by import By
from OpenChrom import open_chrome

class TestGetCookie():
    #通过调试模式获取cookie信息
    def get_cookies(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_args)
        #访问企业微信页面
        self.driver.get("https://work.weixin.qq.com/")
        #点击企业微信的登录按钮
        self.driver.find_element(By.XPATH,'//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        time.sleep(10)  #目的是为了可以手动扫描登录
        # 登录成功后获取cookie并写入文件
        cookies = self.driver.get_cookies()
        with open('cookie.json','w') as f:
            json.dump(cookies,f)
        time.sleep(2)


if __name__ == '__main__':
    T = TestGetCookie()
    T.get_cookies()

