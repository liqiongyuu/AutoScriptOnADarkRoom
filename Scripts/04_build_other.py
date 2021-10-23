#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver

from Common.BasePage import BasePage
from Pages.Event import Event, EventEle
from Pages.Menu import Menu
from Pages.Outside import Outside, OutsideEle
from Pages.Room import Room, RoomEle


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
        self.wait(EventEle.NO)  # 等待必出的弹窗
        self.click(EventEle.NO)
        sleep(1)  # 必须等待一秒，等待弹窗消失再点保存，否则会报错
        self.menu.import_data("03.json")
        self.menu.pick_up_speed()  # 设置加速
        sleep(1)
        self.click(RoomEle.TRADING_POST)
        self.click(RoomEle.COMPASS)
        self.click(RoomEle.TANNERY)
        self.click(RoomEle.SMOKE_HOUSE)
        self.menu.switch_to_outside()
        self.outside.clear_worker()
        # self.outside.add_worker_count("workers_row_trapper", 1)
        self.outside.add_worker_count("workers_row_hunter", 20)
        self.outside.add_worker_count("workers_row_tanner", 50)
        leather_count = self.get_ele_val("row_leather")
        # while leather_count < 550:  #  皮革 工坊100 水壶50 双肩包200 皮甲200

        # self.menu.save("04.json")
        sleep(200)
        self.driver.quit()


if __name__ == '__main__':
    Main().go()
