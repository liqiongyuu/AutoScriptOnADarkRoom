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
    WORKSHOP = (By.ID, "build_workshop")  # 工坊
    TORCH = (By.ID, "build_torch")  # 火把
    WATER_SKIN = (By.ID, "build_waterskin")  # 水壶
    CASK = (By.ID, "build_cask")  # 水桶
    BONE_SPEAR = (By.ID, "build_bone spear")  # 骨枪
    RUCKSACK = (By.ID, "build_rucksack")  # 双肩包
    L_ARMOUR = (By.ID, "build_l armour")  # 皮甲


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

    def build_trap(self):
        self.click(RoomEle.TRAP)

    def build_hut(self):
        self.click(RoomEle.HUT)

    def build_workshop(self):
        self.click(RoomEle.WORKSHOP)

    def build_torch(self, count=1):
        for _ in range(count):
            self.click(RoomEle.TORCH)

    def build_bone_spear(self, count=1):
        for _ in range(count):
            self.move_click(RoomEle.BONE_SPEAR)
