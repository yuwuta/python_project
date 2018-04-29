from selenium import webdriver
from time import *
driver =webdriver.Firefox()
driver.get("http://www.youdao.com")

driver.find_element_by_id('translateContent').clear()
driver.find_element_by_id('translateContent').send_keys('hello')
#提交输入框内容
driver.find_element_by_id('translateContent').submit()
sleep(1)
driver.quit()