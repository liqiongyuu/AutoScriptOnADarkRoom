#!/bin/python3.7
# coding:utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ADarkRoom:
    def __init__(self):
        self.driver = webdriver.Chrome()  # 实例化一个浏览器对象
        self.driver.get("http://adarkroom.doublespeakgames.com/?lang=zh_cn")  # 加载到小黑屋
        WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((By.ID, "event")))  # 等待第一个事件出现
        self.click_button("lightButton")  # 生火-游戏开始
        self.driver.find_element_by_css_selector(".hyper").click()  # 加速
        self.driver.find_element_by_css_selector(".hyper").click()  # 二次点击 一次点击会失效 可能是由于需要先聚焦

    def click_button(self, button_id):
        """
        点击按钮，用id定位
        :param button_id: 按钮的id名称
        """
        print(button_id)  # 打印id方便观察程序运行到哪一步
        self.handling_events()  # 处理各种事件
        self.click_page(button_id)  # 点击到对应页面
        self.click_button_id(button_id)  # 点击按钮

    def click_button_id(self, button_id):
        """
        点击id属性的按钮
        :param button_id: 按钮的id名称
        """
        WebDriverWait(self.driver, 40).until(lambda x: self.is_clicked(x, button_id)).click()

    @staticmethod
    def is_clicked(driver, button_id):
        """
        判断按钮是否可点击
        :param driver: 浏览器实例
        :param button_id: 按钮id
        :return: 按钮可点击就返回按钮，不能就返回False
        """
        try:
            button = driver.find_element_by_id(button_id)  # 获取按钮定位
            button_class = button.get_attribute("class")
            if button_class == "button disable" or button_class == "button free disabled":  # 按钮的class值有disable就无法点击
                return False
            else:
                return button
        except NoSuchElementException:  # 找不到按钮报错
            print("Button not found！")

    def handling_events(self):
        if self.is_exist(By.CLASS_NAME, "eventTitle"):
            title = self.driver.find_element_by_class_name("eventTitle").text  # 获取事件标题
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
            elif title == "要加速么？":
                self.click_button_id("yes")
            else:
                print("Accident！")

    def is_exist(self, by, value=None):
        """
        判断元素是否存在
        is_exist(By.CLASS_NAME, "eventTitle")
        :param by: By.ID By.CLASS_NAME
        :param value: 对应的值
        :return: 存在返回True 不存在返回False
        """
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:  # 没找到按钮就返回False
            return False

    def click_page(self, button_id):
        """
        点击按钮时切换到对应的页面
        :param button_id: 按钮id
        """
        button_page = {
            "lightButton": "location_room",
            "stokeButton": "location_room",
            "build_cart": "location_room",
            "build_trap": "location_room",
            "build_hut": "location_room",
            "gatherButton": "location_outside",
            "trapsButton": "location_outside"
        }
        if self.driver.find_element_by_id(button_page[button_id]).is_selected():
            pass
        else:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(button_page[button_id])).click()
            sleep(3)  # 需要等待动画结束

    def find_ele(self, by, value):
        """
        显示等待，定位元素
        :param by: By.ID
        :param value: "location_room"
        :return: WebElement 页面元素
        """
        return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(by, value))

    def go(self):
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("gatherButton")
        # self.click_button("build_trap")
        # self.click_button("build_cart")
        # self.click_button("trapsButton")
        # self.click_button("build_hut")


if __name__ == '__main__':
    room = ADarkRoom()
    room.go()
