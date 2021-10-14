#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class EventEle:
    YES = (By.ID, "yes")
    NO = (By.ID, "no")
    EXPORT = (By.ID, "export")
    SAVE_TEXT = (By.CSS_SELECTOR, "#description > textarea")
    GOT_IT = (By.ID, "done")
    GIVE_IN = (By.ID, "give in")
    INVESTIGATE = (By.ID, "investigate")
    LEAVE = (By.ID, "leave")
    BACK_INSIDE = (By.ID, "backinside")
    TRACK = (By.ID, "track")
    END = (By.ID, "end")
    DENY = (By.ID, "deny")
    MOURN = (By.ID, "mourn")
    IGNORE = (By.ID, "ignore")
    IMPORT_ELE = (By.ID, "import")
    OKAY = (By.ID, "okay")


class Event:
    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        """ 会跟 BasePage 页中的 click 函数耦合，无法直接导入"""
        self.driver.find_element(*loc).click()

    def click_no(self):
        self.click(EventEle.NO)

    def click_export(self):
        self.click(EventEle.EXPORT)

    def click_got_it(self):
        self.click(EventEle.GOT_IT)

    def get_save_text(self):
        data = self.driver.find_element(*EventEle.SAVE_TEXT).get_attribute("value")
        return base64.b64decode(data)

    def handling_events(self):
        """ 处理各种事件 """
        try:
            title = self.driver.find_element_by_class_name("eventTitle").text  # 获取事件标题
            print(title)
            if title == "Sound Available!":
                self.click(EventEle.NO)
            elif title == "Penrose":
                self.click(EventEle.GIVE_IN)
                windows = self.driver.window_handles  # 获取当前所有页面句柄
                self.driver.switch_to.window(windows[1])  # 切换当新页面
                self.driver.close()  # 关闭
                self.driver.switch_to.window(windows[0])  # 切换指定页面
            elif title == "噪声":
                self.click(EventEle.INVESTIGATE)
                try:
                    self.driver.find_element(*EventEle.LEAVE)
                    self.click(EventEle.LEAVE)
                except NoSuchElementException:
                    self.click(EventEle.BACK_INSIDE)
            elif title == "损毁的陷阱":
                self.click(EventEle.TRACK)
                self.click(EventEle.END)
            elif title in ["神秘流浪者", "乞丐"]:
                self.click(EventEle.DENY)
            elif title == "火灾":
                self.click(EventEle.MOURN)
            elif title == "患病男子":
                self.click(EventEle.IGNORE)
            elif title == "要加速么？":
                self.click(EventEle.YES)
            elif title == "野兽来袭":
                self.click(EventEle.END)
            else:
                print("Accident event: " + title)
        except NoSuchElementException:
            print("Event title not found!")
