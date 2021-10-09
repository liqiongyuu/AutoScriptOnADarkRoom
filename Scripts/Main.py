#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Page.Common import Common
from Page.Room import Room


class Main(Common):
    def __init__(self):
        self.driver = webdriver.Chrome()
        Common.__init__(self, self.driver)

    def go_file_url(self, url):
        self.driver.get("file:///{0}".format(os.path.abspath(url)))  # 相对路径转为绝对路径，并拼接成 url 格式

    def go(self):
        self.go_file_url("../adarkroom/index.html?lang=zh_cn")
        self.click(By.ID, "lightButton")
        self.accelerate()  # 设置加速
        sleep(3)
        self.click(By.ID, "no")
        Room.fire()
        sleep(20)
        self.driver.quit()


if __name__ == '__main__':
    Main().go()
