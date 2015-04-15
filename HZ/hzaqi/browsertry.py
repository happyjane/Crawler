#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")

#登陆快播私有云
driver.find_element_by_id("user_name").send_keys("happyjane1314")
driver.find_element_by_id("user_pwd").send_keys("12586asd")
q=driver.find_element_by_id("dl_an_submit").click()
ActionChains(driver).click(q).perform()
time.sleep(3)

#定位到要右击的元素
qqq =driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[2]")
#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(qqq).perform()


'''
#你也可以使用三行的写法，但我觉得上面两行写法更容易理解
chain = ActionChains(driver)
implement = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[2]")
chain.context_click(implement).perform()
'''

time.sleep(3) #休眠3秒
driver.close()