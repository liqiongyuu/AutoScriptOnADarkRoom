#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        with open("../Data/{0}.json".format(file_name), "wb") as f:
            f.write(event.get_save_text())
        event.click_got_it()
