# browser commands
# using website : https://opensource-demo.orangehrmlive.com/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
time.sleep(5)
# driver.minimize_window() 
# driver.fullscreen_window()
forget_pass=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
forget_pass.click()
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

driver.refresh()
time.sleep(5)

driver.close()

