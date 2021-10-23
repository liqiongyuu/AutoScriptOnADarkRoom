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
        self.menu.import_data("01.json")
        self.menu.pick_up_speed()  # 设置加速
        self.menu.switch_to_outside()
        hut_count = 0
        while hut_count < 20:
            hut_count = self.get_ele_val("building_row_hut")
            wood_count = self.get_ele_val("row_wood")
            trap_count = self.get_ele_val("building_row_trap")
            if self.is_clicked(OutsideEle.GATHER_WOOD):
                self.outside.gather_wood()
            if self.is_clicked(OutsideEle.CHECK_TRAPS):
                self.outside.check_traps()
            if wood_count >= (100 + (hut_count * 50)):  # 建小屋，攒人口，人口是第一生产力
                self.menu.switch_to_room()
                self.room.build_hut()
                self.menu.switch_to_outside()
            if trap_count < 1 and wood_count >= 10:  # 陷阱会坏，一个陷阱可以触发特殊事件加快资源积累，前期用木头建大量的陷阱性价比比较低
                self.menu.switch_to_room()
                self.room.build_trap()
                self.menu.switch_to_outside()
            sleep(0.7)  # 太快会多占用系统资源，太慢有停滞感， 0.7 比较舒适
        self.menu.save("02.json")
        self.driver.quit()


if __name__ == '__main__':
    Main().go()
