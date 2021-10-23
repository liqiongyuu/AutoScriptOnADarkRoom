#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Common.BasePage import BasePage


class OutsideEle:
    GATHER_WOOD = (By.ID, "gatherButton")
    CHECK_TRAPS = (By.ID, "trapsButton")
    TRAPPER_UP = (By.CSS_SELECTOR, "#workers_row_trapper > .row_val > .upBtn")
    HUNTER_UP10 = (By.CSS_SELECTOR, "#workers_row_hunter > .row_val > .upManyBtn")  # 猎人加10
    TANNER_UP10 = (By.CSS_SELECTOR, "#workers_row_tanner > .row_val > .upManyBtn")  # 皮革师加10
    CHARCUTIER_UP10 = (By.CSS_SELECTOR, "#workers_row_charcutier > .row_val > .upManyBtn")  # 熏肉师加10


class Outside(BasePage):
    def gather_wood(self):
        self.wait_clickable(OutsideEle.GATHER_WOOD)

    def check_traps(self):
        self.wait_clickable(OutsideEle.CHECK_TRAPS)

    def move_click(self, loc):
        """ 移动到地方再点击，可以避免按钮下方出现小提示导致下方按钮无法点击的情况"""
        try:
            ele = self.driver.find_element(*loc)
            ActionChains(self.driver).move_to_element(ele).click().perform()
        except ElementClickInterceptedException:
            self.event.handling_events()
            ele = self.driver.find_element(*loc)
            ActionChains(self.driver).move_to_element(ele).click().perform()

    def clear_worker(self):
        """ 将除伐木者的其他劳动者归零 """
        worker_ele_list = self.driver.find_elements(By.CLASS_NAME, "workerRow")
        del worker_ele_list[0]  # 排除第一个元素 伐木者
        for worker_ele in worker_ele_list:
            worker_id = worker_ele.get_attribute("id")  # 获取劳动者的id
            worker_count = self.get_ele_val(worker_id)  # 获取劳动者个数
            while worker_count > 0:
                self.move_click((By.CSS_SELECTOR, "#{0} > .row_val > .dnManyBtn".format(worker_id)))  # 点击少10个
                worker_count = self.get_ele_val(worker_id)

    def add_worker_count(self, worker_id, count):
        """ 增加劳动者个数
        :param worker_id: 劳动者id
        :param count: 需增加的个数
        """
        for _ in range(count // 10):
            self.move_click((By.CSS_SELECTOR, "#{0} > .row_val > .upManyBtn".format(worker_id)))
        for _ in range(count % 10):
            self.move_click((By.CSS_SELECTOR, "#{0} > .row_val > .upBtn".format(worker_id)))
