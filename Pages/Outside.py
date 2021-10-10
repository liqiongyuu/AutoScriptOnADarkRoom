#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from Common.BasePage import BasePage
from Pages.Header import HeaderEle, Header


class OutsideEle:
    GATHER_WOOD = (By.ID, "gatherButton")


class Outside(BasePage):
    def __init__(self, driver):
        super(Outside, self).__init__(driver)

    def _select_outside(self):
        if "selected" not in self.get_class(HeaderEle.LOCATION_OUTSIDE):
            Header(self.driver).switch_to_outside()
            sleep(1)

    def gather_wood(self):
        self.wait_click(OutsideEle.GATHER_WOOD)

