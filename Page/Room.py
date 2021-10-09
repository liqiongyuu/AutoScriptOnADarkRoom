#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from Page.Common import Common


class Room(Common):
    def __init__(self, driver):
        Common.__init__(self, driver)
        self.driver = driver

    def fire(self):
        self.click(By.ID, "stokeButton")
