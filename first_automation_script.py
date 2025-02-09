# writing first automation script
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://selenium.dev/')
driver.maximize_window()
title=driver.title
print(title)
time.sleep(20)
driver.quit()