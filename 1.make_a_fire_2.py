#导入webdrvier
from _typeshed import Self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#自行获取弹窗及命令T_T再写入字典
# event = {}
class room:
    def __init__(self,url):
        #指定chromedriver路径
        self.driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        try:
            #访问小黑屋
            url = 'http://adarkroom.doublespeakgames.com/?lang=zh_cn'
            self.driver.get(url)
        except:
            print("访问失败T_T")

        try:
            #查找弹框是否存在
            element = self.driver.find_element_by_id('event')
        except:
            element_existance = False

            return element_existance

    def getelement(self,element_id):
        #选定元素是否可以点击
        element_id = self.driver.find_element_by_id('yes')
        clickable = True

        if self.getelement(element_id):
            try:
                element = self.driver.find_element_by_id(element_id)
                element.click()
            except:
                clickable = False

