#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import os
from time import sleep

from selenium import webdriver
from Pages.Event import Event
from Pages.Menu import Menu
from Pages.Outside import Outside
from Pages.Room import Room


class Main:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.room = Room(self.driver)
        self.menu = Menu(self.driver)
        self.event = Event(self.driver)
        self.outside = Outside(self.driver)

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
        # self.room.stoke_fire()
        # self.room.wait_outside()
        # for _ in range(2):
        #     self.menu.switch_to_outside()
        #     self.outside.gather_wood()
        #     self.menu.switch_to_room()
        #     self.room.stoke_fire()
        #     self.room.stoke_fire()
        #     self.menu.switch_to_outside()
        #     sleep(2)
        #     self.menu.switch_to_room()
        #     self.room.stoke_fire()
        #     self.room.stoke_fire()
        # self.menu.switch_to_outside()
        # self.outside.gather_wood()
        # self.menu.switch_to_room()
        # self.room.build_cart()
        # self.room.stoke_fire()
        # self.menu.switch_to_outside()
        # self.outside.gather_wood()
        # self.menu.switch_to_room()
        # self.room.build_trap()
        self.menu.save("001")
        sleep(200)
        self.driver.quit()


if __name__ == '__main__':
    Main().go()
