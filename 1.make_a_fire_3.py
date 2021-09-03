# 导入webdrvier
from typing import List
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# 指定chromedriver路径
driver = webdriver.Chrome()
# 访问小黑屋
url = 'http://adarkroom.doublespeakgames.com/?lang=zh_cn'
driver.get(url)
time.sleep(5)

#定位声音
sound = driver.find_element_by_id('event')
sound_no = driver.find_element_by_id('yes').click()  #声音选择
time.sleep(1)
print("开启声音")

#加速
list = driver.find_element_by_class_name('menu')    #定位选项列
speed = driver.find_element_by_css_selector('body > div.menu > span.hyper.menuBtn').click() #定位加速
speed = driver.find_element_by_css_selector('body > div.menu > span.hyper.menuBtn').click() #加速
speed_event = driver.find_element_by_id('event')
speed_yes = driver.find_element_by_id('yes').click()    #同意加速
print("已加速")


# #获取提示词
notifications = driver.find_element_by_id('notifications')
notification = driver.find_element_by_xpath('//*[@id="notifications"]/div[1]').get_attribute('textContent')
print("提示词：" + notification)

# 生火并检测是否可以砍柴
fire = driver.find_element_by_id('lightButton') #定位生火
fire.click()
print("生火")
time.sleep(10)
print("等待")
fire_2 = driver.find_element_by_id('stokeButton').click() #定位添柴
fire_2.click()
print("添柴")
header = driver.find_element_by_id('header')    #上拉框
print("定位置上拉框")
location_outside = driver.find_element_by_id('location_outside') .click()   #静谧森林
print("深林")
location_outside = driver.find_element_by_id('location_outside') .click()   #静谧森林
print("深林")
gatherButton = driver.find_element_by_id('gatherButton').click()
print("伐木")
for i in range (60):
    try:
        fire.click() or fire_2.click()
        time.sleep(8)
        print(i)
    except BaseException as e:
        try:
            header = driver.find_element_by_id('header')    #上拉框
            print("定位置上拉框")
            location_outside = driver.find_element_by_id('location_outside') .click()   #静谧森林
            print("深林")
            location_outside = driver.find_element_by_id('location_outside') .click()   #静谧森林
            gatherButton = driver.find_element_by_id('gatherButton').click() 
            gatherButton = driver.find_element_by_id('gatherButton').click()
            print("伐木")   
        except:
            even = driver.find_element_by_id('event')
            prnrose_ignore = driver.find_element_by_id('ignore').click() 
    time.sleep(10)



location_outside = driver.find_element_by_id('location_outside') .click()   #静谧森林
gatherButton = driver.find_element_by_id('gatherButton').click()   
for i in (10):
    try:
        fire = driver.find_element_by_id('lightButton').click()   #生火
        time.sleep(8)
    except BaseException as e:
        even = driver.find_element_by_id('event')
        even_ignore = driver.find_element_by_id('ignore').click()   #忽略所有

#获取物质数据
wood = driver.find_element_by_xpath('//*[@id="row_wood"]/div[2]').get_attribute('textContent')
hut_need = driver.find_element_by_class_name('build_hut')
get_hut = driver.find_element_by_xpath('//*[@id="build_hut"]/div[2]/div[2]').get_attribute('textContent')
print(wood)

# if wood > 40:
#     cart = driver.find_element_by_id('build_cart').click()
# else:
#     try:
#         location_outside = driver.find_element_by_id('location_outside') .click()   #继续砍柴
#         for i in (10):
#         gatherButton = driver.find_element_by_id('gatherButton').click()
#     except:
#         even = driver.find_element_by_id('event')
#         even_ignore = driver.find_element_by_id('ignore').click()   #忽略所有

# hut = driver.find_element_by_id('build_hut')    #间屋子
# for i in (120):
#     get_hut = int(get_hut)
#     if wood > get_hut:
#         hut.click()
#     else:
#         location_outside = driver.find_element_by_id('location_outside') .click()   #继续砍柴
#         # try:
#         #     gatherButton = driver.find_element_by_id('gatherButton').click()
#         # except:


        
