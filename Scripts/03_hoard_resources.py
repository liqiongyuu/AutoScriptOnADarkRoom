#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 积累各种资源为后续探索做准备
from time import sleep

from Pages.outside import OutsideEle

from Common.init_script import InitScript


class HoardResource(InitScript):
    def go(self):
        self.run("02.json")
        self.menu.switch_to_outside()
        wood_count = self.get_ele_val("row_wood")
        trap_count = self.get_ele_val("building_row_trap")
        self.menu.switch_to_room()
        while trap_count < 10 and wood_count >= (10 + trap_count * 10):  # 建造陷阱
            self.room.build_trap()
            sleep(0.5)  # 等待一小会，防止数据未刷新导致建造失败
            wood_count = self.get_ele_val("row_wood")
            trap_count = self.get_ele_val("building_row_trap")
        self.menu.switch_to_outside()
        while trap_count < 10 or wood_count < 400:  # 准备建造狩猎小屋
            wood_count = self.get_ele_val("row_wood")
            trap_count = self.get_ele_val("building_row_trap")
            if trap_count < 10 and wood_count >= (10 + trap_count * 10):
                self.menu.switch_to_room()
                self.room.build_trap()
                self.menu.switch_to_outside()
            if self.is_clicked(OutsideEle.GATHER_WOOD):
                self.outside.gather_wood()
            if self.is_clicked(OutsideEle.CHECK_TRAPS):
                self.outside.check_traps()
        self.menu.switch_to_room()
        self.room.build_lodge()  # 建造狩猎小屋
        self.menu.switch_to_outside()
        self.outside.add_worker_count("workers_row_trapper", 2)  # 2个陷阱师
        self.outside.add_worker_count("workers_row_hunter", 20)  # 20个猎人，其余为伐木者
        # self.hoard_resource("row_wood", 20000)  # 不停伐木和查看陷阱直到达到木材达到20000才停止
        # 皮毛 皮革2750 罗盘400 贸易站100 制革屋50
        self.hoard_resource("row_fur", 3300)  # 不停伐木和查看陷阱直到达到皮毛达到3300才停止
        self.menu.save("03.json")
        self.driver.quit()


if __name__ == '__main__':
    HoardResource().go()
