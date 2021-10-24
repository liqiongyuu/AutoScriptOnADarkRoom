### 简介
[小黑屋](https://github.com/doublespeakgames/adarkroom)  (A Dark Room) 是一款开源的基于文本的角色扮演游戏。
游戏过程中有较多重复性高的点击操作，也有随机性很高的事件弹窗，本项目旨在使用脚本自动通关整个游戏，采用 Page Object 模式加上 Selenium 框架进行开发。

### 游戏入口
[【点击开始游戏】](http://adarkroom.doublespeakgames.com/?lang=zh_cn)

### 技术基础
小黑屋的源代码由 HTML + CSS + JavaScript 组成，自动化脚本编写需要修改很少的 JavaScript 源代码，方便提高项目的调试效率

小黑屋自动化脚本需要部署 Selenium + Python + 浏览器的开发环境

### 缩写说明

- ele -> element
- val -> value
- loc -> location

### 目录
- ADarkRoom 存放游戏源码
- Common 存放公有方法
- Data 存放每阶段的测试数据
- Doc 存放文档信息
- Page 存放各个页面的定位和操作
- Script 存放主要脚本的运行方法