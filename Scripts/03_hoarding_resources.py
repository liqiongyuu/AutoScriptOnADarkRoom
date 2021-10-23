#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver

from Common.BasePage import BasePage
from Pages.Event import Event, EventEle
from Pages.Menu import Menu
from Pages.Outside import Outside, OutsideEle
from Pages.Room import Room


class Main(BasePage):
    def __init__(self):
        self._chrome_options = webdriver.ChromeOptions()
        # 取消 “Chrome正受到自动测试软件的控制。”的提示
        self._chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=self._chrome_options)
        super(Main, self).__init__(self.driver)
        self.room = Room(self.driver)
        self.menu = Menu(self.driver)
        self.event = Event(self.driver)
        self.outside = Outside(self.driver)

    def go(self):
        self.go_file_url("../ADarkRoom/index.html?lang=zh_cn")
        self.wait(EventEle.NO)  # 等待必出的弹窗
        self.click(EventEle.NO)
        sleep(1)  # 必须等待一秒，等待弹窗消失再点保存，否则会报错
        self.menu.import_data("02.json")
        self.menu.pick_up_speed()  # 设置加速
        sleep(1)
        self.menu.switch_to_outside()
        wood_count = self.get_ele_val("row_wood")
        trap_count = self.get_ele_val("building_row_trap")
        self.menu.switch_to_room()
        while trap_count < 10 and wood_count >= (10 + trap_count * 10):
            self.room.build_trap()
            sleep(0.5)  # 等待一小会，防止数据未刷新导致建造失败
            wood_count = self.get_ele_val("row_wood")
            trap_count = self.get_ele_val("building_row_trap")
        self.menu.switch_to_outside()
        while trap_count < 10 or wood_count < 400:
            wood_count = self.get_ele_val("row_wood")
            trap_count = self.get_ele_val("building_row_trap")
            if trap_count < 10 and wood_count >= (10 + trap_count * 10):
                self.menu.switch_to_room()
                self.room.build_trap()
                self.menu.switch_to_outside()
            if self.is_clicked(OutsideEle.GATHER_WOOD):
                self.outside.gather_wood()
            if self.is_clicked(OutsideEle.CHECK_TRAPS):
                self.outside.check_traps()
        self.menu.switch_to_room()
        self.room.build_lodge()
        self.menu.switch_to_outside()
        self.click(OutsideEle.TRAPPER_UP)
        self.click(OutsideEle.TRAPPER_UP)
        self.click(OutsideEle.HUNTER_UP10)
        self.click(OutsideEle.HUNTER_UP10)
        while wood_count <= 20000:
            hut_count = self.get_ele_val("building_row_hut")
            wood_count = self.get_ele_val("row_wood")
            trap_count = self.get_ele_val("building_row_trap")
            baited_trap_count = self.get_ele_val("building_row_baited-trap")
            if (trap_count + baited_trap_count) < 10 and wood_count >= (10 + (trap_count + baited_trap_count) * 10):
                self.menu.switch_to_room()
                while (trap_count + baited_trap_count) < 10 and wood_count >= (10 + (trap_count + baited_trap_count) * 10):
                    self.room.build_trap()
                    sleep(0.5)  # 等待一小会，防止数据未刷新导致建造失败
                    wood_count = self.get_ele_val("row_wood")
                    trap_count = self.get_ele_val("building_row_trap")
                    baited_trap_count = self.get_ele_val("building_row_baited-trap")
                self.menu.switch_to_outside()
            if hut_count < 20 and wood_count >= (100 + (hut_count * 50)):
                self.menu.switch_to_room()
                self.room.build_hut()
                self.menu.switch_to_outside()
            if self.is_clicked(OutsideEle.GATHER_WOOD):
                self.outside.gather_wood()
            if self.is_clicked(OutsideEle.CHECK_TRAPS):
                self.outside.check_traps()
            sleep(0.7)
        self.menu.save("03.json")
        self.driver.quit()


if __name__ == '__main__':
    Main().go()
