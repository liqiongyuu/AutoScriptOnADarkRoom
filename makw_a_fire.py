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
        time.sleep(3)

    # 游戏设置
    def set(self):
        # 定位声音
        self.driver.find_element_by_id('yes').click()  # 声音选择
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

    # 事件点击
    def action_click(self, action_id):
        try:
            self.driver.find_element_by_id(action_id).click()
        except:
            room.event()
            self.driver.find_element_by_id(action_id).click()

    # 转换地址并动作
    def address_action(self, id, action):
        try:
            room.address(id)
            room.action_click(action)
        except:
            pass

    # 建筑/购买点击
    def event_pass(self, building_id):
        try:
            self.driver.find_element_by_id(building_id).click()
        except EOFError as e:
            pass
            return e

    # 游牧民族事件
    def buy(self):
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

    # 地点跳转
    def address(self, address_id):
        """
        :param address_id: 跳转的地址id
        """
        try:
            self.driver.find_element_by_id(address_id).click()
            time.sleep(1)
        except EOFError as e:
            room.event()
            print('def address' + e)
            self.driver.find_element_by_id(address_id).click()

    # 通过css_selector获取对应物资数据
    def get_number(self, css):
        try:
            number: int = int(self.driver.find_element_by_css_selector(css).get_attribute('textContent'))
            return number
        except EOFError as e:
            # room.event()
            return 0

    def store_compare(self, get, need):
        get = room.get_number(get)  # 拥有的物资
        need = int(room.get_number(need))  # 需要的物资
        if get >= need:
            return True
        else:
            return False

    # 添加关注人数
    def work_add(self, css):
        self.driver.find_element_by_css_selector(css)

    # 循环动作
    def loop_action(self):
        for i in range(5):
            room.address_action('location_room', 'stokeButton')  # 生活间烧柴
            room.address_action('location_outside', 'gatherButton')  # 静谧森林伐木
            room.address_action('location_outside', 'trapsButton')  # 静谧森林看陷阱

    # 是否建设建筑物
    def is_building(self, need_wood, need_fur, need_meat, building_id):
        get_wood = room.get_number('#row_wood > div.row_val')  # 我的木头
        get_fur = room.get_number('#row_fur > div.row_val')  # 我的皮毛
        get_meat = room.get_number('#row_meat > div.row_val')  # 我的肉
        if (get_wood >= need_wood) and (get_fur >= need_fur) and (get_meat >= need_meat):
            room.address('location_room')  # 屋子
            room.event_pass(building_id)
        else:
            pass

    def event(self):
        # 判断意外弹窗
        time.sleep(1)
        title = self.driver.find_element_by_class_name('eventTitle').get_attribute('textContent')
        print(title)
        if title == 'Penrose':
            self.driver.find_element_by_id('give in').click()
            time.sleep(3)
            handles = self.driver.window_handles  # 获取当前打开的所有窗口的句柄
            self.driver.switch_to.window(handles[1])
            self.driver.close()  # 关闭新窗口
            self.driver.switch_to.window(handles[0])
        elif title == '噪声':
            self.driver.find_element_by_id('investigate').click()
            try:
                self.driver.find_element_by_id('backinside').click()
            except:
                self.driver.find_element_by_id('leave').click()
        elif title == '神秘流浪者' or '乞丐':
            try:
                self.driver.find_element_by_id('deny').click()
            except:
                try:
                    self.driver.find_element_by_id('leave').click()
                except:
                    self.driver.find_element_by_id('end').click()

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
            room.buy()
            # room.event_pass('buyCompass')
            # room.event_pass('buyScales')
            # room.event_pass('buyTeeth')
        elif title == '损毁的陷阱':
            # self.driver.find_element_by_link_text('追踪').click()
            # self.driver.find_element_by_link_text('追踪').click()
            # time.sleep(1)
            # self.driver.find_element_by_link_text('返回').click()
            self.driver.find_element_by_id('event')
            try:
                self.driver.find_element_by_id('track').click()
                time.sleep(1)
                self.driver.find_element_by_id('end').click()
            except:
                self.driver.find_element_by_id('ignore').click()
        elif title == '患病男子':
            try:
                self.driver.find_element_by_id('help').click()
                time.sleep(1)
                self.driver.find_element_by_id('bye').click()
            except:
                self.driver.find_element_by_id('ignore').click()
        elif title() == '宗师':
            room.event_pass('force')
            room.event_pass('exitButtons')
            room.event_pass('precision')
            room.event_pass('nothing')
        elif title == '瘟疫':
            room.event_pass('learn')
            for i in range(10):
                room.event_pass('buyMap')
            self.driver.find_element_by_id('leave').click()
        elif title == '小偷':
            self.driver.find_element_by_id('spare').click()
            time.sleep(1)
            self.driver.find_element_by_id('leave').click()
        pass


if __name__ == '__main__':
    room = Room()
    room.open_url()
    room.set()  # 设置
    room.action_click('lightButton')  # 生火/即开始游戏
    # 循环烧柴
    for i in range(4):
        room.action_click('stokeButton')  # 烧柴
        time.sleep(5)
    # 循环烧柴伐木
    for i in range(10):
        room.loop_action()
        # 建卡车
        get_wood = room.get_number('#row_wood > div.row_val')
        if get_wood > 30:
            room.address('location_room')  # 生火间
            room.event_pass('build_cart')
            print('cart')
            break
        else:
            print('false')
    # #保存进度
    room.keep()

    # 建建筑
    # 建造数目赋值
    for i in range(520):
        room.is_building(100, 0, 0, 'build_hut')
        room.is_building(10, 0, 0, 'build_trap')
        room.is_building(200, 10, 5, 'build_lodge')
        room.is_building(400, 100, 0, 'build_trading post')
        room.is_building(600, 50, 0, 'build_smokehouse')
        room.is_building(500, 50, 0, 'location_outside')
        room.loop_action()

    # 保存进度
    room.keep()

    # room.driver.quit()
