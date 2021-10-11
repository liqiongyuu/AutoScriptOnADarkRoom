#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from Common.BasePage import BasePage
from Pages.Menu import MenuEle


class RoomEle:
    LIGHT_FIRE = (By.ID, "lightButton")
    STOKE_FIRE = (By.ID, "stokeButton")


class Room(BasePage):
    def wait_room(self):
        self.wait(MenuEle.LOCATION_OUTSIDE)

    def light_fire(self):
        self.wait_click(RoomEle.LIGHT_FIRE)

    def stoke_fire(self):
        self.wait_click(RoomEle.STOKE_FIRE)
