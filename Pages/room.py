#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from Common.base_page import BasePage
from Pages.menu import MenuEle


class RoomEle:
    LIGHT_FIRE = (By.ID, "lightButton")
    STOKE_FIRE = (By.ID, "stokeButton")
    CART = (By.ID, "build_cart")
    TRAP = (By.ID, "build_trap")
    HUT = (By.ID, "build_hut")
    LODGE = (By.ID, "build_lodge")
    TRADING_POST = (By.ID, "build_trading post")
    COMPASS = (By.ID, "build_compass")  # 罗盘
    TANNERY = (By.ID, "build_tannery")  # 制革屋
    SMOKE_HOUSE = (By.ID, "build_smokehouse")  # 熏肉房


class Room(BasePage):
    def wait_outside(self):
        self.wait(MenuEle.LOCATION_OUTSIDE)

    def light_fire(self):
        self.wait_clickable(RoomEle.LIGHT_FIRE)

    def stoke_fire(self, count=1):
        for _ in range(count):
            self.wait_clickable(RoomEle.STOKE_FIRE)

    def build_cart(self):
        self.click(RoomEle.CART)

    def build_lodge(self):
        self.click(RoomEle.LODGE)

    def get_stores_val(self, resource_id):
        """ 获取右侧库存id对应材料的材料数
        :param resource_id: 材料对应的id值
        :return: 材料数的整数类型
        """
        return int(self.driver.find_element_by_css_selector(resource_id + " > .row_val").get_attribute("textContent"))

    def build_trap(self):
        self.click(RoomEle.TRAP)

    def build_hut(self):
        self.click(RoomEle.HUT)
