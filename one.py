#!/bin/python3.7
# coding:utf-8
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class ADarkRoom:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://adarkroom.doublespeakgames.com/?lang=zh_cn")

    def get_event_title(self):
        """
        获取事件标题
        :return: 事件标题文本
        """
        return self.driver.find_element_by_class_name("eventTitle").text

    def click_button_id(self, id_name):
        """
        点击id属性的按钮
        :param id_name: 按钮的id名称
        """
        self.driver.find_element_by_id(id_name).click()

    def click_button(self, id_name):
        """
        点击按钮，用id定位
        :param id_name: 按钮的id名称
        """
        if self.driver.find_element_by_id("event"):
            title = self.get_event_title()
            if title == "Sound Available!":
                self.click_button_id("no")
            elif title == "Penrose":
                self.click_button_id("give in")
                self.driver.close()
            elif title == "噪声":
                self.click_button_id("investigate")
                self.click_button_id("backinside")
            elif title == "损毁的陷阱":
                self.click_button_id("track")
                self.click_button_id("end")
            elif title == "神秘流浪者":
                self.click_button_id("deny")
        if id_name == "gatherButton" :

        # self.click_button_id(id_name)

    def go(self):
        for _ in range(10):
            self.click_button("lightButton")
        self.click_button("stokeButton")
        sleep(10)
        self.click_button("gatherButton")
        sleep(10)
        self.click_button("build_trap")
        self.click_button("build_cart")
        self.click_button("trapsButton")
        self.click_button("build_hut")


if __name__ == '__main__':
    room = ADarkRoom()
    room.go()