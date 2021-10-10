#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Common:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by, value):
        """移动到对应元素并点击
        :param by: By.ID By.CLASS_NAME
        :param value: 对应值
        """
        try:
            # self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, value))
            self.driver.find_element(by, value).click()
        except NoSuchElementException:
            print("{0} = {1} element not found!".format(by, value))

    def pick_up_speed(self):
        """开启加速
        """
        self.click(By.CSS_SELECTOR, ".hyper")
        self.click(By.CSS_SELECTOR, ".hyper")
        self.click(By.ID, "yes")

    def is_exist(self, by, value):
        """判断元素是否存在 is_exist(By.CLASS_NAME, "eventTitle")
        :param by: By.ID By.CLASS_NAME
        :param value: 对应的值
        :return: 存在返回True 不存在返回False
        """
        try:
            self.driver.find_elements(by, value)
            return True
        except NoSuchElementException:  # 没找到按钮就返回False
            return False

    def wait(self, by, value):
        """等待元素出现
        :param by:
        :param value:
        """
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((by, value)))

    @staticmethod
    def clickable(driver, button_id):
        """判断按钮是否可点击，ec判断可点击函数不适用
        :param driver: 浏览器实例
        :param button_id: 按钮id
        :return: 按钮可点击就返回按钮，不能就返回False
        """
        try:
            button = driver.find_element_by_id(button_id)  # 获取按钮定位
            if "disabled" in button.get_attribute("class"):  # 按钮的class值有disable就无法点击
                return False
            else:
                return button
        except NoSuchElementException:  # 找不到按钮报错
            print(button_id + " not found！")

    def wait_click(self, button_id):
        """等待元素可点击
        :param button_id: 元素 id
        """
        WebDriverWait(self.driver, 60, 0.2).until(lambda x: self.clickable(x, button_id)).click()

    def switch_page(self, page_id):
        self.click(By.ID, page_id)
        sleep(1)
