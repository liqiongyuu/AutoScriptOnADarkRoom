# import time
# from selenium import webdriver

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# #指定chromedriver路径并访问小黑屋
# driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')   
# url = 'http://adarkroom.doublespeakgames.com/?lang=zh_cn'
# driver.get(url)

# #定位到生火按钮
# fire = driver.find_element_by_id('lightButton')
# # stoke = driver.find_element_by_class_name('button').get_attribute('textContent')
# sound = '//*[@id="yes"]'
# #循环点击生火
# for i in range(12):
#     # if stoke == "enable audio":
#     #     time.sleep(10)
#     #     fire.click()   
#     # else:
#     #     fire.click()
#     fire.click()
#     time.sleep(10)
#     WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.ID,sound)))
#     driver.find_element_by_xpath(sound).click()
a = 313
b = int((a - (a % 100))/100)
print(type(b),b)
