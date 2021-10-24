#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 建小屋，攒人口，人口是第一生产力
from time import sleep

from Pages.outside import OutsideEle

from Common.init_script import InitScript


class BuildHut(InitScript):
    def go(self):
        self.run("01.json")
        self.menu.switch_to_outside()
        hut_count = self.get_ele_val("building_row_hut")
        while hut_count < 20:
            wood_count = self.get_ele_val("row_wood")
            trap_count = self.get_ele_val("building_row_trap")
            if self.is_clicked(OutsideEle.GATHER_WOOD):  # 伐木
                self.outside.gather_wood()
            if self.is_clicked(OutsideEle.CHECK_TRAPS):  # 查看陷阱
                self.outside.check_traps()
            if trap_count < 1 and wood_count >= 10:  # 陷阱会坏，一个陷阱可以触发特殊事件加快资源积累，前期用木头建大量的陷阱性价比比较低
                self.menu.switch_to_room()
                self.room.build_trap()
                self.menu.switch_to_outside()
            if wood_count >= (100 + (hut_count * 50)):  # 建小屋，攒人口，人口是第一生产力
                self.menu.switch_to_room()
                self.room.build_hut()
                hut_count += 1
                self.menu.switch_to_outside()
            sleep(0.7)  # 太快会多占用系统资源，太慢有停滞感， 0.7 比较舒适
        self.menu.save("02.json")  # 保存游戏进度
        self.driver.quit()


if __name__ == '__main__':
    BuildHut().go()
