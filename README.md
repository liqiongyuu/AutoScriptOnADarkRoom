### 简介
[小黑屋](https://github.com/doublespeakgames/adarkroom)  (A Dark Room) 是一款开源的基于文本的角色扮演游戏，玩家在收集资源、建立村庄后有探索世界的能力。
游戏过程中有大量在浏览器的点击操作，重复率比较高，本项目旨在使用 Selenium 脚本自动通关整个游戏。

### 游戏入口
[【点击开始游戏】](http://adarkroom.doublespeakgames.com/?lang=zh_cn)

### 技术基础
小黑屋的源代码由 HTML + CSS + JavaScript 组成，自动化脚本编写需要修改很少的 JavaScript 源代码，方便提高项目的调试效率

小黑屋自动化脚本需要有部署 Selenium + Python + 浏览器开发环境的能力

### 缩写说明

- ele -> element

### 目录
- adrakroom 存放游戏源码
- Common 存放公有方法
- Page 存放各个页面的定位和操作
- Script 存放主要的运行方法