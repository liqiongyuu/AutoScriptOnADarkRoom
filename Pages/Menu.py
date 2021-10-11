#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from Common.BasePage import BasePage
from Pages.Event import EventEle


class MenuEle:
    HYPER = (By.CSS_SELECTOR, ".hyper")
    LOCATION_ROOM = (By.ID, "location_room")
    LOCATION_OUTSIDE = (By.ID, "location_outside")


class Menu(BasePage):
    def pick_up_speed(self):
        """开启加速
        """
        self.click(MenuEle.HYPER)
        self.click(MenuEle.HYPER)
        self.click(EventEle.YES)

    def switch_to_room(self):
        self.click(MenuEle.LOCATION_ROOM)
        sleep(1)

    def switch_to_outside(self):
        self.click(MenuEle.LOCATION_OUTSIDE)
        sleep(1)
