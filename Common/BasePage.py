#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Pages.Event import Event


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.event = Event(self.driver)

    def go_file_url(self, url):
        """ 相对路径转为绝对路径，并拼接成 url 格式 """
        self.driver.get("file:///{0}".format(os.path.abspath(url)))

    def click(self, loc):
        """移动到对应元素并点击
        :param loc:
        """
        try:
            # self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, value))
            self.driver.find_element(*loc).click()
        except NoSuchElementException:
            print("{0} = {1} element not found!".format(*loc))
        except ElementClickInterceptedException:
            self.event.handling_events()
            self.driver.find_element(*loc).click()

    def is_exist(self, loc):
        """判断元素是否存在 is_exist((By.CLASS_NAME, "eventTitle"))
        :param loc:
        :return: 存在返回True 不存在返回False
        """
        try:
            self.driver.find_elements(*loc)
            return True
        except NoSuchElementException:  # 没找到按钮就返回False
            return False

    def wait(self, loc):
        """等待元素出现
        :param loc:
        """
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc))

    @staticmethod
    def clickable(driver, by, value):
        """判断按钮是否可点击，用于判断
        :param driver: 浏览器实例
        :param value:
        :param by:
        :return: 按钮可点击就返回按钮，不能就返回False
        """
        try:
            button = driver.find_element(by, value)  # 获取按钮定位
            if "disabled" in button.get_attribute("class"):  # 按钮的class值有disable就无法点击
                return False
            else:
                return button
        except NoSuchElementException:  # 找不到按钮报错
            print(by + " = " + value + " not found！")

    def wait_click(self, loc):
        """等待元素可点击
        :param loc:
        """
        try:
            WebDriverWait(self.driver, 60, 0.2).until(lambda x: self.clickable(x, *loc)).click()
        except ElementClickInterceptedException:
            self.event.handling_events()
            self.driver.find_element(*loc).click()

    def is_clicked(self, loc):
        """ 判断是否可点击
        :param loc:
        :return: Ture or False
        """
        return "disable" not in self.driver.find_element(*loc).get_attribute("class")

    def get_resource_val(self, resource_id):
        """
        获取右侧库存id对应材料的材料数
        :param resource_id: 材料对应的id值
        :return: 材料数的整数类型
        """
        try:
            val = self.driver.find_element_by_css_selector("#{0} > .row_val".format(resource_id)).get_attribute(
                "textContent")
            return int(val)
        except NoSuchElementException:
            return 0

