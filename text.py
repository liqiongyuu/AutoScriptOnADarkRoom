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
driver.find_element_by_id('yes').click()  #声音选择
time.sleep(1)

#加速
driver.find_element_by_css_selector('body > div.menu > span.hyper.menuBtn').click() #定位加速
driver.find_element_by_css_selector('body > div.menu > span.hyper.menuBtn').click() #加速
driver.find_element_by_id('yes').click()    #同意加速
print("已加速")

#生火烧柴
fire = driver.find_element_by_id('lightButton') #定位生火
chai = driver.find_element_by_id('stokeButton') #定位烧柴
fire.click()
print("生火")
time.sleep(6)
print("等待")
for i in range(4):
    try:
        chai.click()
        print("烧柴")
        time.sleep(5)
    except:
        driver.find_element_by_id('ignore').click()   #忽略所有
    
# get_number = int(input())   #自定义循环次数
for i in range(7):
    try:
        driver.find_element_by_id('location_outside') .click()   #静谧森林
        time.sleep(1)
        driver.find_element_by_id('gatherButton').click()
        driver.find_element_by_id('location_room') .click()   #生火间
        time.sleep(1)
        chai.click()
        time.sleep(28)
    except:
        #获取弹窗标题
        title = driver.find_element_by_class_name('eventTitle').get_attribute('textContent')
        print(title)
        if title == '噪声':
            driver.find_element_by_id('investigate').click()
            time.sleep(1)
            driver.find_element_by_id('backinside').click()
        elif title == 'Penrose':
            driver.find_element_by_id('give in').click()
            time.sleep(3)
            handles = driver.window_handles  # 获取当前打开的所有窗口的句柄
            driver.switch_to.window(handles[1])
            driver.close()  # 关闭新窗口
            driver.switch_to.window(handles[0])
            # driver.find_element_by_id('ignore').click()
        elif title == '神秘流浪者':
            driver.find_element_by_id('leave').click()
        elif title == '乞丐':
            #查看物质
            # stores = driver.find_element_by_id('stores')
            # furs = driver.find_elements_by_css_selector('#row_fur > div.row_val')
            # if furs > 500:
            #     investigate = driver.find_element_by_id('500furs').click()
            #     time.sleep(1)
            #     leave = driver.find_element_by_id('leave').click()
            # elif furs > 100:
            #     investigate = driver.find_element_by_id('100furs').click()
            #     time.sleep(1)
            #     leave = driver.find_element_by_id('leave').click()
            deny = driver.find_element_by_id('deny').click()
        
        # prnrose_ignore = driver.find_element_by_id('ignore').click()  

#所拥有的物资数据
wood = driver.find_element_by_css_selector('#row_wood > div.row_val').get_attribute('textContent')

# # 建造所需要的的物资数据
# hut_need = driver.find_element_by_class_name('build_hut')
# get_hut = driver.find_element_by_xpath('//*[@id="build_hut"]/div[2]/div[2]').get_attribute('textContent')
# print(wood)
#定位建筑
buildBtns = driver.find_element_by_id('buildBtns')
if int(wood) > 30:
    cart = driver.find_element_by_css_selector('#build_cart').click()

for i in range(7):
    try:
        driver.find_element_by_id('location_outside') .click()   #静谧森林
        time.sleep(1)
        driver.find_element_by_id('gatherButton').click()
        driver.find_element_by_id('location_room') .click()   #生火间
        time.sleep(1)
        chai.click()
        time.sleep(28)
    except:
        #获取弹窗标题
        title = driver.find_element_by_class_name('eventTitle').get_attribute('textContent')
        print(title)
        if title == '噪声':
            driver.find_element_by_id('investigate').click()
            time.sleep(1)
            driver.find_element_by_id('backinside').click()
        elif title == 'Penrose':
            driver.find_element_by_id('give in').click()
            time.sleep(3)
            handles = driver.window_handles  # 获取当前打开的所有窗口的句柄
            driver.switch_to.window(handles[1])
            driver.close()  # 关闭新窗口
            driver.switch_to.window(handles[0])
            # driver.find_element_by_id('ignore').click()
        elif title == '神秘流浪者':
            driver.find_element_by_id('leave').click()
        elif title == '乞丐':
            #查看物质
            # stores = driver.find_element_by_id('stores')
            # furs = driver.find_elements_by_css_selector('#row_fur > div.row_val')
            # if furs > 500:
            #     investigate = driver.find_element_by_id('500furs').click()
            #     time.sleep(1)
            #     leave = driver.find_element_by_id('leave').click()
            # elif furs > 100:
            #     investigate = driver.find_element_by_id('100furs').click()
            #     time.sleep(1)
            #     leave = driver.find_element_by_id('leave').click()
            deny = driver.find_element_by_id('deny').click()