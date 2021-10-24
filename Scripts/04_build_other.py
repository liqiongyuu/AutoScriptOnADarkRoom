#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Pages.room import RoomEle

from Common.init_script import InitScript


class BuildOther(InitScript):
    def go(self):
        self.run("03.json")
        self.click(RoomEle.TRADING_POST)  # 建造贸易站
        self.click(RoomEle.TANNERY)  # 建造制革房
        self.click(RoomEle.SMOKE_HOUSE)  # 建造熏肉房
        self.menu.switch_to_outside()
        self.outside.clear_worker()
        self.outside.add_worker_count("workers_row_tanner", 50)  # 皮革师50
        self.outside.add_worker_count("workers_row_charcutier", 25)  # 熏肉师25
        self.hoard_resource("row_leather", 550)  # 积累皮革550 工坊100 水壶50 双肩包200 皮甲200
        self.outside.clear_worker()
        self.outside.add_worker_count("workers_row_hunter", 50)
        self.menu.switch_to_room()
        self.click(RoomEle.WORKSHOP)
        self.room.build_torch(self.get_ele_val("row_cloth"))  # 将布料全造成火把
        self.move_click(RoomEle.WATER_SKIN)  # 造水壶
        self.room.build_bone_spear(2)  # 造两根骨枪
        self.move_click(RoomEle.RUCKSACK)  # 造双肩包
        self.move_click(RoomEle.L_ARMOUR)  # 造皮甲
        self.click(RoomEle.COMPASS)  # 购买罗盘
        self.menu.save("04.json")
        self.driver.quit()


if __name__ == '__main__':
    BuildOther().go()
