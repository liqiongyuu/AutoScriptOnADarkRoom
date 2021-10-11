#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from Common.BasePage import BasePage
from Pages.Menu import MenuEle


class RoomEle:
    LIGHT_FIRE = (By.ID, "lightButton")
    STOKE_FIRE = (By.ID, "stokeButton")
    CART = (By.ID, "build_cart")
    TRAP = (By.ID, "build_trap")


class Room(BasePage):
    def wait_outside(self):
        self.wait(MenuEle.LOCATION_OUTSIDE)

    def light_fire(self):
        self.wait_click(RoomEle.LIGHT_FIRE)

    def stoke_fire(self):
        self.wait_click(RoomEle.STOKE_FIRE)

    def build_cart(self):
        self.click(RoomEle.CART)

    def get_stores_val(self, resource_id):
        """ 获取右侧库存id对应材料的材料数
        :param resource_id: 材料对应的id值
        :return: 材料数的整数类型
        """
        return int(self.driver.find_element_by_css_selector(resource_id + " > .row_val").get_attribute("textContent"))

    def build_trap(self):
        self.click(RoomEle.TRAP)