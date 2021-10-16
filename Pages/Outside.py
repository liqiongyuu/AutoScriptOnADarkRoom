#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from Common.BasePage import BasePage


class OutsideEle:
    GATHER_WOOD = (By.ID, "gatherButton")
    CHECK_TRAPS = (By.ID, "trapsButton")


class Outside(BasePage):
    def gather_wood(self):
        self.wait_click(OutsideEle.GATHER_WOOD)

    def check_traps(self):
        self.wait_click(OutsideEle.CHECK_TRAPS)
