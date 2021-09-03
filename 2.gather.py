from selenium import webdriver
import time

#指定chromedriver路径
driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')   
#访问小黑屋
url = 'http://adarkroom.doublespeakgames.com/?lang=zh_cn'
driver.get(url)
time.sleep(10)

#持续工作
# fire = driver.find_element_by_id('lightButton').click()
# logging = driver.find_element_by_id('gatherButton').click()
# trap = driver.find_element_by_id('trapsButton').click()

stores = driver.find_element_by_id('stores').click()


#获取仓库数值
wood = driver.find_element_by_id('//*[@id="row_wood"]/div[2]').get_attribute('textContent')
row_fur = driver.find_element_by_class_name('row_fur').get_attribute('textContent')
row_key = driver.find_element_by_class_name('row_key').get_attribute('textContent')
row_val = driver.find_element_by_class_name('row_val').get_attribute('textContent')
for i in 10:
    build_hut = driver.find_element_by_id('build_hut').click()
    build_trap = driver.find_element_by_id('build_trap').click()

