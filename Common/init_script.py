#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from Common.base_page import BasePage
from Pages.event import EventEle
from Pages.menu import Menu
from Pages.outside import Outside, OutsideEle
from Pages.room import Room


class InitScript(BasePage):
    """ 此类导入将会开启一个新的浏览器实例，并实例化常用的几个页面，在BasePage实例化将会导致循环导入"""
    def __init__(self):
        self._chrome_options = webdriver.ChromeOptions()
        # 关掉Chrome正受到自动测试软件的控制的提示
        self._chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=self._chrome_options)
        super(InitScript, self).__init__(self.driver)
        self.room = Room(self.driver)
        self.menu = Menu(self.driver)
        self.outside = Outside(self.driver)

    def run(self, file_name):
        """ 导航到对应页并导入游戏数据
        :param file_name:游戏数据文件名
        """
        self.go_file_url("../ADarkRoom/index.html?lang=zh_cn")
        self.wait(EventEle.NO)  # 等待必出的弹窗
        self.click(EventEle.NO)
        sleep(1)  # 必须等待一秒，等待弹窗消失再点保存，否则会报错
        self.menu.import_data(file_name)
        self.menu.pick_up_speed()  # 设置加速
        sleep(1)

    def hoard_resource(self, resource_id, expect_resource_val):
        """ 不停伐木查看陷阱直到达到预期资源值才停止
        :param resource_id: 资源的id
        :param expect_resource_val: 资源的预期的数量
        """
        resource_val = self.get_ele_val(resource_id)  # 获取资源数量
        while resource_val < expect_resource_val:
            wood_count = self.get_ele_val("row_wood")
            hut_count = self.get_ele_val("building_row_hut")
            # 所有陷阱包括上饵陷阱和陷阱
            all_trap = self.get_ele_val("building_row_trap") + self.get_ele_val("building_row_baited-trap")
            if all_trap < 10 and wood_count >= (10 + all_trap * 10):
                self.menu.switch_to_room()
                while all_trap < 10 and wood_count >= (10 + all_trap * 10):  # 陷阱会因为野兽多个同时毁坏，需要及时补充
                    self.room.build_trap()  # 查看陷阱
                    sleep(0.5)  # 等待一小会，防止数据未刷新导致建造失败
                    wood_count = self.get_ele_val("row_wood")
                    all_trap = self.get_ele_val("building_row_trap") + self.get_ele_val("building_row_baited-trap")
                self.menu.switch_to_outside()
            if hut_count < 20 and wood_count >= (100 + (hut_count * 50)):  # 小屋会因为火灾而减少
                self.menu.switch_to_room()
                self.room.build_hut()  # 建小屋
                self.menu.switch_to_outside()
            if self.is_clicked(OutsideEle.GATHER_WOOD):  # 伐木
                self.outside.gather_wood()
            if self.is_clicked(OutsideEle.CHECK_TRAPS):  # 查看陷阱
                self.outside.check_traps()
            resource_val = self.get_ele_val(resource_id)  # 更新资源数量
            sleep(0.7)
