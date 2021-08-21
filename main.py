#!/bin/python3.7
# coding:utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class ADarkRoom:
    def __init__(self):
        self.driver = webdriver.Chrome()  # 实例化一个浏览器对象
        # self.driver.get("http://adarkroom.doublespeakgames.com/?lang=zh_cn")  # 加载到小黑屋
        self.driver.get('file:///D:/MyDatabase/Code/JavaScript/adarkroom/index.html?lang=zh_cn')  # 加载到小黑屋
        WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((By.ID, "event")))  # 等待第一个事件出现
        self.click_button("lightButton")  # 生火-游戏开始
        self.click_ele(By.CSS_SELECTOR, ".hyper")  # 加速
        self.click_ele(By.CSS_SELECTOR, ".hyper")  # 二次点击 一次点击会失效 可能是由于需要先聚焦

    def click_button_id(self, ele_id):
        """
        点击id属性的按钮
        :param ele_id: 按钮的id名称
        """
        WebDriverWait(self.driver, 70).until(ec.visibility_of_element_located((By.ID, ele_id))).click()

    def click_button(self, ele_id):
        """
        点击按钮，用id定位
        :param ele_id: 按钮的id名称
        """
        try:
            title = self.get_event_title()
            print(title)
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
            elif title == "火灾":
                self.click_button_id("mourn")
            elif title == "患病男子":
                self.click_button_id("ignore")
        except:
            pass

        self.click_button_id(ele_id)

    def go(self):
        self.click_button("lightButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("gatherButton")
        self.click_button("build_trap")
        self.click_button("build_cart")
        self.click_button("trapsButton")
        self.click_button("build_hut")


if __name__ == '__main__':
    room = ADarkRoom()
    room.go()
