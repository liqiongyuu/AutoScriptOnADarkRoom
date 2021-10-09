#!/bin/python3.7
# coding:utf-8
from time import sleep

from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class ADarkRoom:
    def __init__(self):
        self.driver = webdriver.Chrome()  # 实例化一个浏览器对象
        # project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # self.driver.get(os.path.normpath('file:///{0}/adarkroom/index.html?lang=zh_cn'.format(project_path)))  # 加载到小黑屋
        # self.driver.get("http://adarkroom.doublespeakgames.com/?lang=zh_cn")  # 加载到小黑屋
        WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((By.ID, "event")))  # 等待第一个事件出现
        self.click_button("lightButton")  # 生火-游戏开始
        self.click_ele(By.CSS_SELECTOR, ".hyper")  # 加速
        self.click_ele(By.CSS_SELECTOR, ".hyper")  # 二次点击 一次点击会失效 可能是由于需要先聚焦

    def click_button(self, button_id):
        """
        点击按钮，用id定位
        :param button_id: 按钮的id名称
        """
        try:
            print(button_id)  # 打印id方便观察程序运行到哪一步
            self.handling_events()  # 处理各种事件
            self.click_page(button_id)  # 点击到对应页面
            if self.is_exist(By.CSS_SELECTOR, "#{0} > .tooltip".format(button_id)):  # 判断该按钮是否需要材料
                resource_id = self.not_enough(button_id)  # 获取那些材料不够
                if resource_id is None:  # 判断材料是否足够
                    self.click_button_id(button_id)  # 点击按钮
            else:
                self.click_button_id(button_id)  # 点击按钮
        except ElementClickInterceptedException:  # 防止点击过程中出现新事件
            self.handling_events()
            self.click_button_id(button_id)

    def click_button_id(self, button_id):
        """
        点击id属性的按钮, 有等待,                  这步逻辑有问题，等待点击 应该要先进行事件处理，二者 有耦合
        这步要改！！！
        :param button_id: 按钮的id名称
        """
        WebDriverWait(self.driver, 45).until(lambda x: self.is_clicked(x, button_id))  # 开了加速最多等待45秒，陷阱原速90秒
        self.click_ele(By.ID, button_id)

    def click_ele(self, by, value):
        """
        移动到对应元素并点击
        :param by: By.ID By.CLASS_NAME
        :param value: 对应值
        """
        try:
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, value))
        except NoSuchElementException:
            print("{0} = {1} element not found!".format(by, value))

    def click_ele_id(self, ele_id):
        """
        点击元素 无等待
        :param ele_id: 元素id
        """
        self.click_ele(By.ID, ele_id)

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
            if button_class == "button disabled" or button_class == "button free disabled":  # 按钮的class值有disable就无法点击
                return False
            else:
                return button
        except NoSuchElementException:  # 找不到按钮报错
            print(button_id + " not found！")

    def handling_events(self):
        if self.is_exist(By.CLASS_NAME, "eventTitle"):
            title = self.driver.find_element_by_class_name("eventTitle").text  # 获取事件标题
            print(title)
            if title == "Sound Available!":
                self.click_ele_id("no")
            elif title == "Penrose":
                self.click_ele_id("give in")
                windows = self.driver.window_handles  # 获取当前所有页面句柄
                self.driver.switch_to.window(windows[1])  # 切换当新页面
                self.driver.close()  # 关闭
                self.driver.switch_to.window(windows[0])  # 切换指定页面
            elif title == "噪声":
                self.click_ele_id("investigate")
                if self.is_exist(By.ID, "leave"):
                    self.click_ele_id("leave")
                else:
                    self.click_ele_id("backinside")
            elif title == "损毁的陷阱":  # 有问题
                self.click_ele_id("track")
                self.click_ele_id("end")
            elif title in ["神秘流浪者", "乞丐"]:
                self.click_ele_id("deny")
            elif title == "火灾":
                self.click_ele_id("mourn")
            elif title == "患病男子":
                self.click_ele_id("ignore")
            elif title == "要加速么？":
                self.click_ele_id("yes")
            elif title == "野兽来袭":
                self.click_ele_id("end")
            else:
                print("Accident {0}".format(title))

    def is_exist(self, by, value):
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

    def not_enough(self, button_id):
        """
        判断现有材料数够不都需求数
        :param button_id: 按钮id
        :return: 所有材料都不够返回对应的id
        """
        resource_name_id = {  # 资源表还不完善
            "木头": "row_wood",
            "毛皮": "row_fur"
        }
        demand = self.get_button_tip(button_id)
        for key, value in demand.items():
            resource_val = self.get_resource_val(resource_name_id[key])
            if value > resource_val:  # 现有材料数是否小于需求值
                return resource_name_id[key]  # 返回不足的id并停止循环节省时间开销

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
        if not self.driver.find_element_by_id(button_page[button_id]).is_selected():
            self.driver.find_element_by_id(button_page[button_id]).click()
            sleep(1)  # 需要等待动画结束

    def find_ele(self, by, value):
        """
        显示等待，定位元素
        :param by: By.ID
        :param value: "location_room"
        :return: WebElement 页面元素
        """
        return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(by, value))

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
            return 5  # 前期未找到是因为没有显示出来，设置为5不影响前期点击按钮

    def get_button_tip(self, button_id):
        """
        获取按钮提示对应需求的材料名和材料数
        :param button_id: 按钮id
        :return: 字典 例如：{"木头": 200, "毛皮": 10, "肉": 5}
        """
        tips_key = self.driver.find_elements_by_css_selector(
            "#{0} > .tooltip.bottom.right > .row_key".format(button_id))
        tips_val = self.driver.find_elements_by_css_selector(
            "#{0} > .tooltip.bottom.right > .row_val".format(button_id))
        keys = []
        values = []
        for key in tips_key:
            keys.append(key.get_attribute("textContent"))
        for val in tips_val:
            values.append(int(val.get_attribute("textContent")))

        return dict(zip(keys, values))

    def export_data(self):
        """
        导出数据，在脚本所在目录下创建或者覆盖ExportData.txt
        """
        self.click_ele(By.CSS_SELECTOR, ".menu > span:nth-child(8)")
        self.click_ele_id("export")
        data = self.find_ele(By.CSS_SELECTOR, "#description > textarea").get_attribute("value")
        self.click_ele_id("done")
        with open("ExportData.txt", "w") as f:
            f.write(data)
        return data

    def import_data(self):
        """
        导入ExportData.txt的游戏数据
        :return:
        """
        try:
            with open("ExportData.txt") as f:
                data = f.readline()
            self.click_ele(By.CSS_SELECTOR, ".menu > span:nth-child(8)")
            self.click_ele_id("import")
            self.click_ele_id("yes")
            self.find_ele(By.CSS_SELECTOR, "#description > textarea").send_key(data)
            self.click_ele_id("okay")
        except FileNotFoundError:
            print("ExportData.txt not found!")

    def go(self):
        while not self.is_exist(By.ID, "location_outside"):  # 等待静谧森林出现
            self.click_button("stokeButton")
        while not self.is_exist(By.ID, "build_cart"):  # 等待货车出现
            self.click_button("gatherButton")
            self.click_button("stokeButton")  # 在生火间里才会出建造货车的事件
        while self.get_resource_val("row_wood") < 30:
            self.click_button("gatherButton")
        self.click_button("build_cart")
        self.click_button("gatherButton")
        self.click_button("build_trap")
        while self.is_clicked(self.driver, "build_hut"):
            if not self.is_exist(By.ID, "building_row_trap"):
                self.click_button("build_trap")
                self.click_button("trapsButton")
            else:
                self.click_button("trapsButton")
            if self.not_enough("build_hut") is None:  # 判断材料是否足够
                self.click_button_id("build_hut")
            else:
                self.click_button("gatherButton")
        sleep(20)

        self.driver.quit()
        # self.click_button("trapsButton")
        # self.click_button("build_hut")
        # self.driver.find_element(by, value).click()
        # ActionChains(self.driver).click_and_hold(self.driver.find_element(by, value)).release().perform()
        # ActionChains(self.driver).release(self.driver.find_element(by, value)).perform()
        # if self.driver.find_element_by_id(button_id).get_attribute("buildthing"):
        #     print(self.driver.find_element_by_id(button_id).get_attribute("buildthing"))
        #     self.click_ele(By.ID, button_id)
        #     self.click_ele(By.ID, button_id)
        # else:
        # while self.get_resource_val("row_wood") < self.get_resource_val("building_row_trap") * 10:


if __name__ == '__main__':
    ADarkRoom().go()
