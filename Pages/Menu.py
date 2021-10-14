#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from time import sleep

from selenium.webdriver.common.by import By

from Common.BasePage import BasePage
from Pages.Event import EventEle, Event


class MenuEle:
    HYPER = (By.CSS_SELECTOR, ".hyper")
    LOCATION_ROOM = (By.ID, "location_room")
    LOCATION_OUTSIDE = (By.ID, "location_outside")
    SAVE = (By.CSS_SELECTOR, ".menu > span:nth-child(8)")


class Menu(BasePage):
    def pick_up_speed(self):
        """ 开启加速 """
        self.click(MenuEle.HYPER)
        self.click(MenuEle.HYPER)
        self.click(EventEle.YES)

    def switch_to_room(self):
        self.click(MenuEle.LOCATION_ROOM)
        sleep(1)

    def switch_to_outside(self):
        self.click(MenuEle.LOCATION_OUTSIDE)
        sleep(1)

    def save(self, file_name):
        """ 导出数据，在脚本所在目录下创建或者覆盖
        :param file_name: 文件名
        """
        event = Event(self.driver)
        self.click(MenuEle.SAVE)
        event.click_export()
        with open("../Data/" + file_name, "wb") as f:
            f.write(event.get_save_text())
        event.click_got_it()

    def import_data(self, file_name):
        """ 导入游戏数据 """
        try:
            with open("../Data/" + file_name, "rb") as f:
                data = f.readline()
            data64 = base64.b64encode(data).decode("utf-8")
            self.click(MenuEle.SAVE)
            self.click(EventEle.IMPORT_ELE)
            self.click(EventEle.YES)
            self.driver.find_element(*EventEle.SAVE_TEXT).send_keys(data64)
            self.click(EventEle.OKAY)
        except FileNotFoundError:
            print(file_name + " not found!")
