#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from Common.BasePage import BasePage


class EventEle:
    YES = (By.ID, "yes")
    NO = (By.ID, "no")


class Event(BasePage):
    def click_yes(self):
        self.click(EventEle.YES)

    def click_no(self):
        self.click(EventEle.NO)
