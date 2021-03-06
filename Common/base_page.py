#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Pages.event import Event


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.event = Event(self.driver)

    def go_file_url(self, url):
        """ 相对路径转为绝对路径，并拼接成 url 格式 """
        self.driver.get("file:///{0}".format(os.path.abspath(url)))

    def click(self, loc):
        """点击对应元素
        :param loc:
        """
        try:
            self.driver.find_element(*loc).click()
        except NoSuchElementException:
            print("{0} = {1} element not found!".format(*loc))
        except ElementClickInterceptedException:
            self.event.handling_events()
            self.driver.find_element(*loc).click()
        except ElementNotInteractableException:
            print("{0} = {1} element not interactable!".format(*loc))

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

    def wait_clickable(self, loc):
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

    def get_ele_val(self, resource_id):
        """ 获取id对应值
        :param resource_id: 材料对应的id值
        :return: 材料数的整数类型
        """
        try:
            val = self.driver.find_element_by_css_selector("#{0} > .row_val".format(resource_id)).get_attribute(
                "textContent")
            return int(val)
        except NoSuchElementException:  # 找不到说明对应按钮还没出现即为0
            return 0

    def move_click(self, loc):
        """ 移动到地方再点击，可以避免按钮下方出现小提示导致下方按钮无法点击的情况 """
        try:
            self.driver.find_element_by_id("event")
            self.event.handling_events()
            ele = self.driver.find_element(*loc)
            ActionChains(self.driver).move_to_element(ele).click().perform()
        except NoSuchElementException:
            ele = self.driver.find_element(*loc)
            ActionChains(self.driver).move_to_element(ele).click().perform()
