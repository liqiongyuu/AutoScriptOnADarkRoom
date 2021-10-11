# 导入webdrvier
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os


class Roomdram(object):

    def __init__(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()
        # self.driver.get('http://adarkroom.doublespeakgames.com/?lang=zh_cn')
        # 隐藏等待
        self.driver.implicitly_wait(3)
        # 设置浏览器最大化
        # self.driver.maximize_window()  

    def open_url(self):
        # 请求指定站点
        # self.driver.get(url)
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.driver.get(os.path.normpath('file:///{0}/adarkroom/index.html?lang=zh_cn'.format(project_path)))  # 加载到小黑屋
        time.sleep(2)

    # 游戏设置
    def sound(self):
        # 定位声音
        self.driver.find_element_by_id('yes').click()  # 声音选择
        time.sleep(1)

    def speed(self):
        # 加速
        self.driver.find_element_by_css_selector('body > div.menu > span.hyper.menuBtn').click()  # 定位加速
        self.driver.find_element_by_css_selector('body > div.menu > span.hyper.menuBtn').click()  # 加速
        self.driver.find_element_by_id('yes').click()  # 子弹窗同意加速
        print("已加速")

    def keep(self):
        # 游戏保存
        self.driver.find_element_by_css_selector('body > div.menu > span:nth-child(8)').click()  # 定位至保存
        self.driver.find_element_by_id('export').click()  # 子弹窗选择导出游戏进度
        # 获取游戏进度文本
        text = self.driver.find_element_by_css_selector('#description > textarea').get_attribute('value')
        # 打开空文本文本并赋予读写
        with open("Data/roomkeep.txt", 'w') as f:
            f.write(text)
        print(text)
        self.driver.find_element_by_id('done').click()  # 完成
        # time.sleep(1)

    def input(self):
        # 游戏导入
        try:
            # 读取文本
            with open("Data/roomkeep.txt") as f:
                text = f.read()
            self.driver.find_element_by_css_selector('body > div.menu > span:nth-child(8)').click()  # 定位至保存
            self.driver.find_element_by_id('import').click()  # 子弹窗选择导入游戏进度
            self.driver.find_element_by_id('yes').click()  # 确定导入
            # 写入游戏进度文本
            self.driver.find_element_by_css_selector('#description > textarea').send_keys(text)
            self.driver.find_element_by_id('okay').click()  # 完成
            # time.sleep(1)
        except FileNotFoundError:
            print("RoomKeep.txt not found!")

    
    # 通过css_selector获取对应物资数据
    def store(self, css):
        number: int = int(self.driver.find_element_by_css_selector(css).get_attribute('textContent'))
        return number


    if __name__ == '__main__':
    room = Roomdram()
    room.open_url()
    room.sound()  # 设置声音
    room.speed()  # 设置速度
    room.action_click('lightButton')  # 生火/即开始游戏
    # 循环烧柴
    for i in range(4):
        room.action_click('stokeButton')  # 烧柴
        time.sleep(5)
    # 循环烧柴伐木
    for i in range(6):
        room.action_click('stokeButton')  # 烧柴
        room.address('location_outside')  # 静谧森林
        room.action_click('gatherButton')  # 伐木
        time.sleep(30)
        room.address('location_room')  # 生火间

    get_wood = room.store('#row_wood > div.row_val')
    # 建卡车
    if get_wood > 30:
        room.address('location_room')  # 生火间
        room.building('build_cart')
    else:
        print('false')
    # room.driver.quit()