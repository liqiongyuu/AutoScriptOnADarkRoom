#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from Pages.room import RoomEle

from Common.init_script import InitScript


class Main(InitScript):
    def go(self):
        self.run("03.json")
        self.click(RoomEle.TRADING_POST)  # 建造贸易站
        self.click(RoomEle.COMPASS)  # 购买罗盘
        self.click(RoomEle.TANNERY)  # 建造制革房
        self.click(RoomEle.SMOKE_HOUSE)  # 建造熏肉房
        self.menu.switch_to_outside()
        self.outside.clear_worker()
        # self.outside.add_worker_count("workers_row_trapper", 1)
        self.outside.add_worker_count("workers_row_hunter", 20)
        self.outside.add_worker_count("workers_row_tanner", 50)
        self.hoard_resource("row_leather", 550)  # 皮革 工坊100 水壶50 双肩包200 皮甲200
        # self.menu.save("04.json")
        sleep(200)
        self.driver.quit()


if __name__ == '__main__':
    Main().go()
