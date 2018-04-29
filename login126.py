from selenium import webdriver
from time import *
#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("http://www.126.com")
sleep(3)

driver.switch_to_frame("x-URS-iframe")
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("yuwuta")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("LOVE849182000")

driver.find_element_by_id("dologin").click()
sleep(3)
#driver.find_elements_by_xpath(".//*[@id='cnt-box2']/div/div[2]/div[2]/a[1]").click()
driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/a[1]").click()

#driver.quit()