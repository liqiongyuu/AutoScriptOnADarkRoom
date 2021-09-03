from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class Room:
    def __init__(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()
        self.driver.get('http://adarkroom.doublespeakgames.com/?lang=zh_cn')
        self.driver.implicitly_wait(3)  # 隐藏等待
        self.sound()
        self.speed()
        self.click_id('lightButton')

    def open_url(self):
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.driver.get(os.path.normpath('file:///{0}/adarkroom/index.html?lang=zh_cn'.format(project_path)))  # 加载到小黑屋
        time.sleep(2)

    def click(self, by, value):
        """
        根据id，元素点击封装
        """
        self.driver.find_element(by, value).click()

    def click_id(self, id):
        """
        根据id定位元素并点击
        """
        self.click(By.ID, id)

    def click_css(self, css):
        """
        根据css定位元素并点击
        """
        self.click(By.CSS_SELECTOR, css)

    def position(self, by, value):
        """
        定位至元素
        """
        self.driver.find_element(by, value)

    def position_css(self, css):
        """
        根据css定位元素
        """
        self.position(By.CSS_SELECTOR, css)

    def get_number(self, css):
        """
        利用css_selector获取对应物资数据，若不存在则返回0
        """
        try:
            number: int = int(self.position_css(css).get_attribute('textContent'))
            return number
        except EOFError as e:
            print("get_number:", e)
            return 0

    def sound(self):
        """
        出现声音弹窗是选择是
        """
        self.click_id('yes')
        time.sleep(1)

    def speed(self):
        """
        通过下面的菜单项选择游戏加速
        """
        self.click_css('.hyper')
        self.click_css('.hyper')
        self.click_id('yes')
        print("已加速")

    def keep(self):
        """
        游戏保存
        """
        self.click_css('div.menu > span:nth-child(8)')  # 定位至保存
        self.click_id('export')  # 子弹窗选择导出游戏进度
        # 获取游戏进度文本
        text = self.position_css('#description > textarea').get_attribute('value')
        # 打开空文本文本并赋予读写
        with open("RoomKeep.txt", 'w') as f:
            f.write(text)
        print(text)
        self.click_id('done')  # 完成

    def input(self):
        """
        游戏导入
        """
        try:
            # 读取文本
            with open("RoomKeep.txt") as f:
                text = f.read()
            self.click_css('body > div.menu > span:nth-child(8)')  # 定位至保存
            self.click_id('import')  # 子弹窗选择导入游戏进度
            self.click_id('yes')  # 确定导入
            # 写入游戏进度文本
            self.position_css('#description > textarea').send_keys(text)
            self.click_id('okay')  # 完成
            # time.sleep(1)
        except FileNotFoundError:
            print("RoomKeep.txt not found!")


if __name__ == '__main__':
    room = Room()

    room.driver.quit()
