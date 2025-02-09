# viewports
from selenium import webdriver
import time
driver=webdriver.Chrome()

driver.get('https://www.google.com/')
viewports=[(1024,768),(768,1024),(375,883),(333,256)]
try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(4)
finally:
    driver.close()
time.sleep(4)
driver.quit()