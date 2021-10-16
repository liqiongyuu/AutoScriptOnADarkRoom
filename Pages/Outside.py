#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from Common.BasePage import BasePage


class OutsideEle:
    GATHER_WOOD = (By.ID, "gatherButton")
    CHECK_TRAPS = (By.ID, "trapsButton")
    TRAPPER_UP = (By.CSS_SELECTOR, "#workers_row_trapper > .row_val > .upBtn")
    HUNTER_UP10 = (By.CSS_SELECTOR, "#workers_row_hunter > .row_val > .upManyBtn")


class Outside(BasePage):
    def gather_wood(self):
        self.wait_clickable(OutsideEle.GATHER_WOOD)

    def check_traps(self):
        self.wait_clickable(OutsideEle.CHECK_TRAPS)
