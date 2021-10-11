#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64

from selenium.webdriver.common.by import By

from Common.BasePage import BasePage


class EventEle:
    YES = (By.ID, "yes")
    NO = (By.ID, "no")
    EXPORT = (By.ID, "export")
    SAVE_TEXT = (By.CSS_SELECTOR, "#description > textarea")
    GOT_IT = (By.ID, "done")


class Event(BasePage):
    def click_yes(self):
        self.click(EventEle.YES)

    def click_no(self):
        self.click(EventEle.NO)

    def click_export(self):
        self.click(EventEle.EXPORT)

    def click_got_it(self):
        self.click(EventEle.GOT_IT)

    def get_save_text(self):
        data = self.driver.find_element(*EventEle.SAVE_TEXT).get_attribute("value")
        return base64.b64decode(data)
