from selenium import webdriver
from time import *
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(1)
driver.refresh() #刷新前页面