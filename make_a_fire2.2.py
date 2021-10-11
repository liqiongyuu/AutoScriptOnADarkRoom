# 导入webdrvier
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os


class Room(object):

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

    def id_click(self, element_id):
        # 利用id元素定位并点击
        try:
            self.driver.find_element_by_id(element_id).click()
        except EOFError as e:
            print('id_click:', e)
            self.driver.find_element_by_id(element_id).click()

    # 通过css_selector获取对应物资数据
    def get_number(self, css):
        try:
            number: int = int(self.driver.find_element_by_css_selector(css).get_attribute('textContent'))
            return number
        except EOFError as e:
            print('get_number:', e)
            room.event()
            return 0

    # 循环动作
    def loop_action(self, id, action):
        for _ in range(5):
            room.address_action('location_room', 'stokeButton')  # 生活间烧柴
            room.address_action('location_outside', 'gatherButton')  # 静谧森林伐木
            room.address_action('location_outside', 'trapsButton')  # 静谧森林看陷阱

    # 转换地址并动作
    def address_action(self, id, action):
        try:
            room.id_click(id)
            room.id_click(action)
        except EOFError as e:
            print('loop_action', e)
            room.event()

    # 判断意外弹窗事件
    def event(self):
        # 获取弹窗标题用于判断事件选择
        title = self.driver.find_element_by_class_name('eventTitle').get_attribute('textContent')
        print(title)
        if title == 'Penrose':
            room.event_Penrose()
        elif title == '噪声':
            room.event_noise()
        elif title == '神秘流浪者' or '乞丐':
            room.event_rover_and_rover()
        elif title == '野兽来袭':
            self.driver.find_element_by_id('end').click()
        elif title == '火灾':
            self.driver.find_element_by_id('mourn').click()
        elif title == '可疑的建造者':
            need_wood = room.get_number('#build_hut > div.tooltip.bottom.right > div.row_val')
            if (room.store('#row_wood > div.row_val') > 300) and (need_wood > 300):
                self.driver.find_element_by_id('build').click()
                time.sleep(1)
                self.driver.find_element_by_id('end').click()
            else:
                self.driver.find_element_by_id('leave').click()
        elif title() == '游牧部落':
            room.event_buy()
        elif title == '损毁的陷阱':
            self.driver.find_element_by_link_text('追踪').click()
            self.driver.find_element_by_link_text('追踪').click()
        elif title == '患病男子':
            try:
                self.driver.find_element_by_id('help').click()
                time.sleep(1)
                self.driver.find_element_by_id('bye').click()
            except EOFError as e:
                print('title', e)
                self.driver.find_element_by_id('ignore').click()
        elif title() == '宗师':
            self.driver.find_element_by_id('force').click()
            self.driver.find_element_by_id('exitButtons').click()
            self.driver.find_element_by_id('precision').click()
            self.driver.find_element_by_id('nothing').click()
        elif title == '瘟疫':
            room.event_pass('learn')
            for _ in range(10):
                self.driver.find_element_by_id('buyMap')
            self.driver.find_element_by_id('leave').click()
        elif title == '小偷':
            self.driver.find_element_by_id('spare').click()
            time.sleep(1)
            self.driver.find_element_by_id('leave').click()
        pass

    def event_Penrose(self):
        self.driver.find_element_by_id('give in').click()
        time.sleep(3)
        handles = self.driver.window_handles  # 获取当前打开的所有窗口的句柄
        self.driver.switch_to.window(handles[1])
        self.driver.close()  # 关闭新窗口
        self.driver.switch_to.window(handles[0])

    # 噪音
    def event_noise(self):
        self.driver.find_element_by_id('investigate').click()
        try:
            self.driver.find_element_by_id('backinside').click()
        except Exception as e:
            print('title', e)
            self.driver.find_element_by_id('leave').click()

    # 神秘流浪者 or乞丐
    def event_rover_and_rover(self):
        try:
            self.driver.find_element_by_id('deny').click()
        except EOFError as e:
            print('title', e)
            try:
                self.driver.find_element_by_id('leave').click()
            except EOFError as e:
                print('title', e)
                self.driver.find_element_by_id('end').click()

    # 游牧民族事件
    def event_buy(self):
        # room.get_number('')
        buyCompass_fur = room.store_compare('#row_fur > div.row_val',
                                            '#buyCompass > div.tooltip.bottom.right > div:nth-child(2)')
        buyCompass_scales = room.store_compare('#row_scales > div.row_val',
                                               '#buyCompass > div.tooltip.bottom.right > div:nth-child(4)')
        buyCompass_teeth = room.store_compare('#row_teeth > div.row_val',
                                              '#buyCompass > div.tooltip.bottom.right > div:nth-child(6)')
        if buyCompass_fur and buyCompass_scales and buyCompass_teeth == True:
            try:
                room.building('buyCompass')  # 购买罗盘
                print('购买罗盘')
            except:
                pass
        buyScales_fur = room.store_compare('#row_fur > div.row_val',
                                           '#buyScales > div.tooltip.bottom.right > div.row_val')
        if buyScales_fur == True:
            room.building('buyScales')  # 购买鳞片
            print('购买鳞片')
        buyTeeth_fur = room.store_compare('#row_fur > div.row_val',
                                          '#buyTeeth > div.tooltip.bottom.right > div.row_val')
        if buyTeeth_fur == True:
            room.building('buyTeeth')  # 购买牙齿
            print('购买牙齿')
        room.driver.find_element_by_id('goodbye')


if __name__ == '__main__':
    room = Room()# 实例化一个类
    room.open_url()
    room.sound()  # 设置声音
    room.speed()  # 设置速度
    room.id_click('lightButton')  # 生火/即开始游戏
    for i in range(5):
        # room.id_click('stokeButton')
        # time.sleep(5)
        room.loop_action()

    # 保存进度
    room.keep()

    room.driver.quit()
