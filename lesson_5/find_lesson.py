import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.freeconferencecall.com/login')

time.sleep(5)

# print(driver.find_element(By.ID, 'loginformsubmit'))
# print(driver.find_element("id", 'loginformsubmit'))

driver.find_element("id", 'loginformsubmit').click()

time.sleep(3)