from selenium import webdriver
driver = webdriver.Firefox()
#访问百度首页
first_url= 'http://www.baidu.com'
print("now access %s"%(first_url))
#访问新闻页面
second_url= 'http://news.baidu.com'
print("now access %s"%(second_url))
#返回到百度首页
print("back to %s"%(first_url))
driver.back()
#前进到新闻页
print("forward to %s"%(second_url))
driver.forward()
driver.back()