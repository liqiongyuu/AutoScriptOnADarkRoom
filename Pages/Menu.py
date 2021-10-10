#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from Common.BasePage import BasePage
from Pages.Event import EventEle


class MenuEle:
    HYPER = (By.CSS_SELECTOR, ".hyper")


class Menu(BasePage):
    def pick_up_speed(self):
        """开启加速
        """
        self.click(MenuEle.HYPER)
        self.click(MenuEle.HYPER)
        self.click(EventEle.YES)
