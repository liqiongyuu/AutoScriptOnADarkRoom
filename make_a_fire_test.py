from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By


class Room:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.open_url()
        self.driver.implicitly_wait(3)
        self.sound()
        self.speed()

    def open_url(self):
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.driver.get(os.path.normpath('file:///{0}/adarkroom/index.html?lang=zh_cn'.format(project_path)))  # 加载到小黑屋
        time.sleep(2)

    def click(self, by, value):
        self.driver.find_element(by, value).click()

    def click_id(self,id):
        self.click(By.ID, id)

    def click_css(self, css):
        self.click(By.CSS_SELECTOR, css)

    def sound(self):
        self.click_id('yes')
        time.sleep(1)

    def speed(self):
        self.click_css('.hyper')
        self.click_css('.hyper')
        self.click_id('yes')
        print("已加速")
    
if __name__ == '__main__':
    room = Room()
    