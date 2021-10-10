#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from Common.BasePage import BasePage
from Pages.Header import HeaderEle, Header


class RoomEle:
    LIGHT_FIRE = (By.ID, "lightButton")
    STOKE_FIRE = (By.ID, "stokeButton")


class Room(BasePage):
    def __init__(self, driver):
        super(Room, self).__init__(driver)

    def _select_room(self):
        if "selected" not in self.get_class(HeaderEle.LOCATION_ROOM):
            Header(self.driver).switch_to_room()
            sleep(1)

    def light_fire(self):
        self.wait_click(RoomEle.LIGHT_FIRE)

    def stoke_fire(self):
        self.wait_click(RoomEle.STOKE_FIRE)
