#!/usr/bin/python
#-*- coding:utf-8 -*-
# @Author: xiaopingzi 
# ide: pycharm      
# @Time: 2020-05-13 10:14
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
import time

from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTestbaidu():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testbaidu(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.set_window_size(1440, 900)
        self.driver.find_element(By.ID, "kw").send_keys("huogewozi")
        self.driver.find_element(By.ID, "su").click()

# class TestJavascript():
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()
#
#     def update_date(self):
#         self.driver.get('https://www.12306.cn/index/')
#         date_element = self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
#         self.driver.execute_script("document.getElementById('train_date').value = '2020-12-18'")
#         time.sleep(3)

    # def test_js(self):
    #     self.driver.get('https://www.baidu.com/')
    #     self.driver.find_element_by_id('kw').send_keys('selenium 测试')
    #     element = self.driver.execute_script(" return document.getElementById('su')")
    #     element.click()
    #     time.sleep(3)
    #     self.driver.execute_script('document.documentElement.scrollTop=10000')
    #     self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
    #     time.sleep(3)












# class TestFrame():
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()
#
#     def test_frame(self):
#         self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#         self.driver.switch_to.frame('iframeResult')
#         #不建议下面的写法
#         #self.driver.switch_to_frame('iframeResult')
#         print(self.driver.find_element_by_id('draggable').text)
#         #切换回父级frame
#         self.driver.switch_to.parent_frame()
#         #切换回默认的frame
#         # self.driver.switch_to.default_content()
#         print(self.driver.find_element_by_id('submitBTN').text)













# class Testmultwindow():
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()
#
#     def test_multwindow(self):
#         self.driver.get("https://www.baidu.com/")
#         self.driver.find_element_by_xpath('//*[@id="u1"]/a[2]').click()
#         #打印当前窗口id
#         print(self.driver.current_window_handle)
#         #打印所有窗口id
#         print(self.driver.window_handles)
#         self.driver.find_element_by_link_text('立即注册').click()
#         print(self.driver.current_window_handle)
#         print(self.driver.window_handles)
#         windows = self.driver.window_handles
#         #切换至另外一个窗口
#         self.driver.switch_to.window(windows[-1])
#         time.sleep(3)
#         self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').click()
#         self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys('username')
#         self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').click()
#         self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys('13112345678')
#         time.sleep(3)
#         self.driver.switch_to.window(windows[0])
#         self.driver.find_element_by_css_selector('#TANGRAM__PSP_11__footerULoginBtn').click()
#         time.sleep(3)






# class TestForm():
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()
#
#     def test_form(self):
#         self.driver.get("https://ceshiren.com/latest")
#         self.driver.find_element_by_xpath('//*[@id="ember6"]/header/div/div/div[2]/span/button[2]/span').click()
#         self.driver.find_element_by_id('login-account-name').send_keys('Megranate')
#         self.driver.find_element_by_id('login-account-password').send_keys('Sc@831143')
#         #self.driver.find_element_by_id('user_remeber_me').click()
#         self.driver.find_element_by_xpath('//*[@id="login-button"]/span').click()
#         time.sleep(3)








# class TestAction():
#     def setup(self):
#         option = webdriver.ChromeOptions()
#         option.add_experimental_option('w3c',False)
#         self.driver = webdriver.Chrome(options = option)
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()
    # #搜索"selenium测试"并滑动到最底部
    # def test_touchaction_scrollbottom(self):
    #     self.driver.get("https://www.baidu.com/")
    #     element = self.driver.find_element_by_id('kw')
    #     element.send_keys("selenium测试")
    #     element_search = self.driver.find_element_by_id('su')
    #     action = TouchActions(self.driver)
    #     #tap点击元素
    #     action.tap(element_search).perform()
    #     time.sleep(3)
    #     action.scroll_from_element(element,0,10000).perform()
    #     time.sleep(3)


# class TestActionChains():
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()


    # def test_case_click(self):
    #     self.driver.get("http://sahitest.com/demo/clicks.htm")
    #     #寻找到单击的元素
    #     element_click = self.driver.find_element_by_xpath('/html/body/form/input[3]')
    #     #寻找到双击的元素
    #     element_doubleclick = self.driver.find_element_by_xpath('/html/body/form/input[2]')
    #     #寻找到右键的元素
    #     element_rightclick = self.driver.find_element_by_xpath('/html/body/form/input[4]')
    #
    #     action = ActionChains(self.driver)
    #     action.click(element_click)
    #     action.double_click(element_doubleclick)
    #     action.context_click(element_rightclick)
    #     action.perform()
    #     time.sleep(5)
    # #将光标移动到某一个元素上
    # def test_move_to(self):
    #     self.driver.get("https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6")
    #     element_move = self.driver.find_element_by_xpath('//*[@id="u"]/a[2]')
    #     action = ActionChains(self.driver)
    #     action.move_to_element(element_move)
    #     action.perform()
    #     time.sleep(5)
    # #将第一个元素拖拽到第二个元素上
    # def test_drag(self):
    #     self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
    #     element_drag = self.driver.find_element_by_xpath('//*[@id="dragger"]')
    #     element_drop = self.driver.find_element_by_xpath('/html/body/div[2]')
    #     action =ActionChains(self.driver)
    #     #action.drag_and_drop(element_drag,element_drop).perform()
    #     #第二种表达，release方法传入一个元素的话，就会移动到这个元素上；如果传入参数为空，就执行鼠标抬起的操作
    #     action.click_and_hold(element_drag).release(element_drop).perform()
    #     #第三种表达
    #     action.click_and_hold(element_drag).move_to_element(element_drop).release().perform()
    #     #action.perform()
    #     time.sleep(3)
    # def test_keys(self):
    #     self.driver.get('http://sahitest.com/demo/label.htm')
    #     element = self.driver.find_element(By.XPATH,'/html/body/label[1]/input')
    #     element.click()
    #     action =ActionChains(self.driver)
    #     #action.click(element)
    #     action.send_keys("username")
    #     # 等待2s
    #     action.pause(2)
    #     action.send_keys(Keys.SPACE).pause(2)
    #     action.send_keys("tom").pause(2)
    #     action.send_keys(Keys.BACK_SPACE).pause(2)
    #     action.perform()
    #     time.sleep(2)


# class TestHogwarts:
#     def setup(self):
#         #启动浏览器
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         #隐式等待
#         #self.driver.implicitly_wait(3)
#     def teardown(self):
#         #进行资源回收
#         self.driver.quit()
#
#     def test_hogwarts(self):
#         #打开被测网址
#         self.driver.get("https://ceshiren.com/")
#         #直接等待
#         # time.sleep(5)
#         # print("hello")
#         self.driver.find_element_by_xpath('//*[@title="所有分类"]').click()
#         # time.sleep(5)
#
#         # def wait(x):
#         #     return len(self.driver.find_elements_by_xpath("//*[@class='default']")) == 1
#         # WebDriverWait(self.driver,10).until(wait)
#         WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@class='default']")))
#         print("selenium")
#         self.driver.find_element_by_xpath('//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()

#
# def test_selenium():
#     browser = webdriver.Chrome()
#     browser.get("http://www.baidu.com")


#
# def func(x):
#     return x + 1
# def test_answer():
#     assert func(3) == 4


