#导入webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#创建浏览器
#指定chromedriver路径
driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')

#访问第一章网页
# https://www.xarsd.com/text/51/51472/2093257.html
url = 'https://www.xarsd.com/text/51/51472/2093387_2.html'
driver.get(url)
time.sleep(2)

#打开空文本文本并赋予读写
wtite_chapter = open('G:\\python\\python_learn\\python_two\\story.txt',mode='a+',encoding='utf-8')
# print("《text"+"\n",file = wtite_chapter)

#循环点击下一页
for i in range(480):
    # #获取标题及章节内容，输出在文本中
    # chapter = driver.find_element_by_class_name('title').get_attribute('textContent')
    # # num = str(i+859)
    # print("第" + chapter,file = wtite_chapter)
    # print('\n',file = wtite_chapter)
    try:
        chapter = driver.find_element_by_id('content').get_attribute('textContent')
        print(chapter,file = wtite_chapter)
        # time.sleep(1)
        # print('\n' + '\n',file = wtite_chapter)
        #通过text属性对应的值定位到下一页/写一页
        el_next = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[1]/a[3]')
        get_next = el_next.get_attribute('textContent')
        if get_next == "下一页":
            el_next.click()
        else:
            #点击翻页
            el_next.click()
            time.sleep(2)
            #获取标题及章节内容，输出在文本中
            chapter = driver.find_element_by_class_name('title').get_attribute('textContent')
            # num = str(i+859)
            print("第" + chapter,file = wtite_chapter)
            print('\n',file = wtite_chapter)
            time.sleep(2)
    except BaseException as e:
        time.sleep(1)
        action = ActionChains(driver)
        action.key_down(Keys.F5).perform()
        time.sleep(2)
print("end")
#关闭文件和网页
# wtite_chapter.close()
# time.sleep(1)
# driver.close()
