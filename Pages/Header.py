#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from Common.BasePage import BasePage


class HeaderEle:
    LOCATION_ROOM = (By.ID, "location_room")
    LOCATION_OUTSIDE = (By.ID, "location_outside")


class Header(BasePage):
    def __init__(self, driver):
        super(Header, self).__init__(driver)

    def switch_to_room(self):
        self.click(HeaderEle.LOCATION_ROOM)
        sleep(1)

    def switch_to_outside(self):
        self.click(HeaderEle.LOCATION_OUTSIDE)
        sleep(1)
