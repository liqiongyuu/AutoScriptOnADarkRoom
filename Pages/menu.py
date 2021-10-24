#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from time import sleep

from selenium.webdriver.common.by import By

from Common.base_page import BasePage
from Pages.event import EventEle


class MenuEle:
    HYPER = (By.CSS_SELECTOR, ".hyper")
    LOCATION_ROOM = (By.ID, "location_room")
    LOCATION_OUTSIDE = (By.ID, "location_outside")
    LOCATION_PATH = (By.ID, "location_path")
    SAVE = (By.CSS_SELECTOR, ".menu > span:nth-child(8)")


class Menu(BasePage):
    def pick_up_speed(self):
        """ 开启加速 """
        self.click(MenuEle.HYPER)
        self.event.click(EventEle.YES)

    def switch_to_room(self):
        self.click(MenuEle.LOCATION_ROOM)
        sleep(1)

    def switch_to_outside(self):
        self.click(MenuEle.LOCATION_OUTSIDE)
        sleep(1)

    def switch_to_path(self):
        self.click(MenuEle.LOCATION_PATH)
        sleep(1)

    def save(self, file_name):
        """ 导出数据，在脚本所在目录下创建或者覆盖
        :param file_name: 文件名
        """
        self.click(MenuEle.SAVE)
        self.event.export_action(file_name)

    def import_data(self, file_name):
        """ 导入游戏数据 """
        try:
            with open("../Data/" + file_name, "rb") as f:
                data = f.readline()
            data64 = base64.b64encode(data).decode("utf-8")
            self.click(MenuEle.SAVE)
            self.event.import_data_action(data64)
        except FileNotFoundError:
            print(file_name + " not found!")
