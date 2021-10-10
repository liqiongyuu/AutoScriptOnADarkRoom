#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Common.BasePage import BasePage
from Pages.Event import Event
from Pages.Header import HeaderEle, Header
from Pages.Menu import Menu
from Pages.Outside import Outside
from Pages.Room import Room


class Main(BasePage):
    def __init__(self):
        self.driver = webdriver.Chrome()
        super().__init__(self.driver)
        self.room = Room(self.driver)
        self.menu = Menu(self.driver)
        self.event = Event(self.driver)
        self.outside = Outside(self.driver)
        self.header = Header(self.driver)
        # super().__init__(self.driver)

    def go_file_url(self, url):
        self.driver.get("file:///{0}".format(os.path.abspath(url)))  # 相对路径转为绝对路径，并拼接成 url 格式

    def go(self):
        self.go_file_url("../adarkroom/index.html?lang=zh_cn")
        self.room.light_fire()
        self.menu.pick_up_speed()  # 设置加速
        sleep(3)
        self.event.click_no()
        self.room.stoke_fire()
        self.room.stoke_fire()
        self.room.stoke_fire()
        self.wait(HeaderEle.LOCATION_OUTSIDE)
        self.header.switch_to_outside()
        self.outside.gather_wood()
        self.outside.gather_wood()
        sleep(20)
        self.driver.quit()


if __name__ == '__main__':
    Main().go()
