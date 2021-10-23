#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver

from Common.BasePage import BasePage
from Pages.Event import Event
from Pages.Menu import Menu, MenuEle
from Pages.Outside import Outside
from Pages.Room import Room


class Main(BasePage):
    def __init__(self):
        self._chrome_options = webdriver.ChromeOptions()
        # 取消 “Chrome正受到自动测试软件的控制。”的提示
        self._chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=self._chrome_options)
        super(Main, self).__init__(self.driver)
        self.room = Room(self.driver)
        self.menu = Menu(self.driver)
        self.event = Event(self.driver)
        self.outside = Outside(self.driver)

    def go(self):
        self.go_file_url("../ADarkRoom/index.html?lang=zh_cn")
        self.room.light_fire()
        self.click(MenuEle.HYPER)
        self.menu.pick_up_speed()  # 设置加速
        sleep(3)
        self.event.click_no()
        self.room.stoke_fire()
        self.room.stoke_fire()
        self.room.stoke_fire()
        self.room.wait_outside()
        for _ in range(2):
            self.menu.switch_to_outside()
            self.outside.gather_wood()
            self.menu.switch_to_room()
            self.room.stoke_fire()
            self.room.stoke_fire()
            self.menu.switch_to_outside()
            sleep(2)
            self.menu.switch_to_room()
            self.room.stoke_fire()
            self.room.stoke_fire()
        self.menu.switch_to_outside()
        self.outside.gather_wood()
        self.menu.switch_to_room()
        self.room.build_cart()
        self.room.stoke_fire()
        self.menu.switch_to_outside()
        self.outside.gather_wood()
        self.menu.switch_to_room()
        self.room.build_trap()
        self.menu.save("01.json")
        self.driver.quit()


if __name__ == '__main__':
    Main().go()
