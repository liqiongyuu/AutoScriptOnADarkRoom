#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 建造货车增加伐木量
from time import sleep

from Common.init_script import InitScript
from Pages.menu import MenuEle


class BuildCat(InitScript):
    def go(self):
        self.go_file_url("../ADarkRoom/index.html?lang=zh_cn")
        self.room.light_fire()
        self.click(MenuEle.HYPER)
        self.menu.pick_up_speed()  # 设置加速
        sleep(3)
        self.event.click_no()
        self.room.stoke_fire(3)
        self.room.wait_outside()
        for _ in range(2):
            self.menu.switch_to_outside()
            self.outside.gather_wood()  # 伐木
            self.menu.switch_to_room()
            self.room.stoke_fire(2)  # 等待建造者苏醒
            self.menu.switch_to_outside()  # 切换室内室外以触发建造货车事件
            sleep(2)
            self.menu.switch_to_room()
            self.room.stoke_fire(2)  # 等待建造者苏醒
        self.menu.switch_to_outside()
        self.outside.gather_wood()
        self.menu.switch_to_room()
        self.room.build_cart()  # 建造货车增加伐木量
        self.room.stoke_fire()
        self.menu.switch_to_outside()
        self.outside.gather_wood()
        self.menu.switch_to_room()
        self.room.build_trap()  # 建造陷阱，前期一个陷阱能触发事件就够，多个会拖慢游戏进度
        self.menu.save("01.json")  # 保存游戏进度
        self.driver.quit()


if __name__ == '__main__':
    BuildCat().go()
