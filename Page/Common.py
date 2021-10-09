#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Common:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by, value):
        """
        移动到对应元素并点击
        :param by: By.ID By.CLASS_NAME
        :param value: 对应值
        """
        try:
            # self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, value))
            self.driver.find_element(by, value).click()
        except NoSuchElementException:
            print("{0} = {1} element not found!".format(by, value))

    def accelerate(self):
        self.click(By.CSS_SELECTOR, ".hyper")
        self.click(By.CSS_SELECTOR, ".hyper")
        self.click(By.ID, "yes")

    def is_exist(self, by, value):
        """
        判断元素是否存在
        is_exist(By.CLASS_NAME, "eventTitle")
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
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((by, value)))